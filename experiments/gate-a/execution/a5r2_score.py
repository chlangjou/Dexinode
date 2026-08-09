#!/usr/bin/env python3
"""Score one completed Gate A v1.2.2 A5R2 row with the frozen adapter/judge."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]
BENCHMARK = REPO_ROOT / "experiments/gate-a/benchmark-v1.2.2"
ADAPTER_DIR = BENCHMARK / "adapter"
import sys

sys.path.insert(0, str(ADAPTER_DIR))
from semantic_adapter import (  # noqa: E402
    extract_python_source,
    math_semantic_score,
    normalize_math_response,
    strict_coding_interface_compliance,
    strict_math_interface_compliance,
)


JUDGE_IMAGE = "python:3.10-slim@sha256:63669fd2563fa90b0442fa7b568e66e3667755636cda086d7bcaaa895f66fe39"
JUDGE_POLICY = {
    "image": JUDGE_IMAGE,
    "user": "0:0",
    "network": "none",
    "gpu_devices": "none",
    "host_mounts": "none",
    "docker_socket": "none",
    "read_only_root": True,
    "tmpfs": "/tmp:rw,noexec,nosuid,nodev,size=16m",
    "cap_drop": ["ALL"],
    "no_new_privileges": True,
    "pids_limit": 1,
    "nproc": "1:1",
    "memory": "256m",
    "cpus": "0.5",
    "file_size_bytes": 1048576,
    "log_max_size": "64k",
    "log_max_file": 1,
    "watchdog_seconds": 2,
    "watchdog_kill_after_seconds": 1,
}


JUDGE_EXECUTOR = r'''import builtins, contextlib, io, json, sys

class OutputLimit(Exception):
    pass

class BoundedOutput(io.TextIOBase):
    def __init__(self, limit=65536):
        self.limit = limit
        self.data = []
        self.size = 0
    def write(self, text):
        text = str(text)
        self.size += len(text.encode("utf-8", "replace"))
        if self.size > self.limit:
            raise OutputLimit("judge output limit exceeded")
        self.data.append(text)
        return len(text)
    def flush(self):
        return None
    def isatty(self):
        return False

BLOCKED = {"os", "pathlib", "shutil", "subprocess", "socket", "ssl", "tempfile", "urllib", "http", "ftplib"}
real_import = builtins.__import__
def restricted_import(name, globals=None, locals=None, fromlist=(), level=0):
    root = name.split(".", 1)[0]
    if root in BLOCKED:
        raise RuntimeError("forbidden module import: " + root)
    return real_import(name, globals, locals, fromlist, level)

def forbidden(*args, **kwargs):
    raise RuntimeError("forbidden filesystem or process operation")

safe_builtins = dict(vars(builtins))
safe_builtins["__import__"] = restricted_import
safe_builtins["open"] = forbidden
safe_builtins["breakpoint"] = forbidden

def exact_equal(actual, expected):
    if type(actual) is not type(expected):
        return False
    if isinstance(expected, dict):
        return set(actual) == set(expected) and all(exact_equal(actual[k], expected[k]) for k in expected)
    if isinstance(expected, list):
        return len(actual) == len(expected) and all(exact_equal(a, e) for a, e in zip(actual, expected))
    return actual == expected

def emit(value):
    sys.__stdout__.write(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n")
    sys.__stdout__.flush()

try:
    payload = json.load(sys.stdin)
    source = payload["source"]
    entrypoint = payload["entrypoint"]
    tests = payload["tests"]
    namespace = {"__builtins__": safe_builtins, "__name__": "__judge__"}
    out = BoundedOutput()
    err = BoundedOutput()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        exec(compile(source, "<candidate>", "exec"), namespace, namespace)
    fn = namespace.get(entrypoint)
    if not callable(fn):
        emit({"status": "fail", "reason": "missing_or_non_callable_entrypoint"})
        raise SystemExit(0)
    for index, test in enumerate(tests):
        try:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                actual = fn(*test["args"])
        except BaseException as exc:
            emit({"status": "fail", "reason": "test_exception", "test_index": index, "exception": type(exc).__name__})
            raise SystemExit(0)
        if not exact_equal(actual, test["expected"]):
            emit({"status": "fail", "reason": "wrong_value", "test_index": index})
            raise SystemExit(0)
    emit({"status": "pass", "passed_tests": len(tests), "output_bytes": out.size + err.size})
except SystemExit:
    raise
except OutputLimit:
    emit({"status": "fail", "reason": "output_limit_exceeded"})
except BaseException as exc:
    emit({"status": "fail", "reason": "source_or_judge_exception", "exception": type(exc).__name__})
'''


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def load_cases() -> list[dict]:
    math_cases = yaml.safe_load((BENCHMARK / "cases/math.yaml").read_text(encoding="utf-8"))["cases"]
    code_cases = yaml.safe_load((BENCHMARK / "cases/coding.yaml").read_text(encoding="utf-8"))["cases"]
    cases = list(math_cases) + list(code_cases)
    expected = [f"math-{index:02d}" for index in range(1, 49)] + [f"code-{index:02d}" for index in range(1, 49)]
    if [str(case["id"]) for case in cases] != expected:
        raise RuntimeError("frozen case order mismatch")
    return cases


def load_raw(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def docker_json(args: list[str]) -> tuple[int, str, str]:
    process = subprocess.run(args, capture_output=True, check=False)
    return process.returncode, process.stdout.decode("utf-8", "replace"), process.stderr.decode("utf-8", "replace")


def judge_code(case: dict, source: str, ordinal: int, role: str, judge_records) -> tuple[int, str, bool]:
    name = f"dexinode-gate-a5r2-judge-{role}-{ordinal:03d}"
    create_args = [
        "docker", "create", "-i", "--name", name,
        "--user", "0:0", "--network", "none", "--ipc", "private",
        "--read-only", "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=16m",
        "--cap-drop=ALL", "--security-opt=no-new-privileges:true",
        "--pids-limit", "1", "--ulimit", "nproc=1:1",
        "--ulimit", "fsize=1048576:1048576", "--memory", "256m", "--cpus", "0.5",
        "--stop-timeout", "2", "--log-driver", "json-file", "--log-opt", "max-size=64k",
        "--log-opt", "max-file=1", JUDGE_IMAGE, "python3", "-c", JUDGE_EXECUTOR,
    ]
    create_started = time.monotonic()
    create_code, create_stdout, create_stderr = docker_json(create_args)
    base_record = {
        "case_id": case["id"], "ordinal": ordinal, "container_name": name,
        "image": JUDGE_IMAGE, "policy": JUDGE_POLICY,
    }
    if create_code != 0:
        judge_records.write(json.dumps({
            **base_record, "judge_status": "infrastructure_failure", "create_exit_code": create_code,
            "create_stdout": create_stdout, "create_stderr": create_stderr,
        }, sort_keys=True) + "\n")
        return 0, "judge_container_create_failed", False
    container_id = create_stdout.strip().splitlines()[-1] if create_stdout.strip() else None
    payload = json.dumps({
        "source": source, "entrypoint": case["evaluator"]["entrypoint"], "tests": case["evaluator"]["tests"],
    }, sort_keys=True, separators=(",", ":")).encode("utf-8")
    start_args = ["timeout", "--foreground", "--kill-after=1s", "2s", "docker", "start", "-ai", name]
    started_at = now()
    started = time.monotonic()
    try:
        process = subprocess.Popen(start_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=payload, timeout=6)
        start_code = process.returncode
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        start_code = 124
        stderr += b"\nwatchdog host communication timeout\n"
    elapsed = time.monotonic() - started
    timed_out = start_code == 124
    if timed_out:
        docker_json(["docker", "kill", name])
    inspect_code, inspect_stdout, inspect_stderr = docker_json(["docker", "inspect", name])
    inspect_data = None
    if inspect_code == 0:
        try:
            inspect_data = json.loads(inspect_stdout)[0]
        except (json.JSONDecodeError, IndexError):
            inspect_data = None
    cleanup_code, cleanup_stdout, cleanup_stderr = docker_json(["docker", "rm", "-f", name])
    stdout_text = stdout.decode("utf-8", "replace")
    stderr_text = stderr.decode("utf-8", "replace")
    judge_result = None
    if not timed_out:
        lines = [line for line in stdout_text.splitlines() if line.strip()]
        if lines:
            try:
                judge_result = json.loads(lines[-1])
            except json.JSONDecodeError:
                judge_result = None
    if timed_out:
        score, reason, complete = 0, "judge_timeout_2_seconds", True
    elif start_code != 0:
        score, reason, complete = 0, "judge_runtime_failure", True
    elif not isinstance(judge_result, dict):
        score, reason, complete = 0, "judge_protocol_error", True
    elif judge_result.get("status") == "pass":
        score, reason, complete = 1, "all_unit_tests_passed", True
    else:
        score, reason, complete = 0, str(judge_result.get("reason", "judge_rejected_source")), True
    judge_records.write(json.dumps({
        **base_record, "container_id": container_id, "started_at": started_at,
        "elapsed_seconds": elapsed, "create_elapsed_seconds": time.monotonic() - create_started,
        "create_exit_code": create_code, "start_exit_code": start_code, "timed_out": timed_out,
        "stdout": stdout_text, "stderr": stderr_text, "judge_result": judge_result,
        "inspect_exit_code": inspect_code,
        "container_exit_code": inspect_data.get("State", {}).get("ExitCode") if inspect_data else None,
        "container_oom_killed": inspect_data.get("State", {}).get("OOMKilled") if inspect_data else None,
        "cleanup_exit_code": cleanup_code, "cleanup_stdout": cleanup_stdout, "cleanup_stderr": cleanup_stderr,
    }, sort_keys=True) + "\n")
    return score, reason, complete


def aggregate(records: list[dict]) -> dict:
    def group(domain=None, difficulty=None):
        selected = [
            record for record in records
            if (domain is None or record["domain"] == domain)
            and (difficulty is None or record["difficulty"] == difficulty)
        ]
        correct = sum(int(record["score"]) for record in selected)
        return {"correct": correct, "total": len(selected), "accuracy": correct / len(selected) if selected else None}

    return {
        "overall": group(),
        "mathematics": group("mathematics"),
        "software_coding": group("software_coding"),
        "difficulty": {
            domain: {difficulty: group(domain, difficulty) for difficulty in ("foundational", "intermediate", "advanced")}
            for domain in ("mathematics", "software_coding")
        },
        "case_count": len(records),
        "scored_case_count": sum(record["status"] == "scored" for record in records),
        "strict_interface": {
            "math_canonical_answer_contract": sum(record.get("strict_interface_compliant", False) for record in records if record["domain"] == "mathematics"),
            "math_total": sum(record["domain"] == "mathematics" for record in records),
            "coding_single_clean_source_block": sum(record.get("strict_interface_compliant", False) for record in records if record["domain"] == "software_coding"),
            "coding_total": sum(record["domain"] == "software_coding" for record in records),
        },
        "failed_or_invalid_cases": [record["case_id"] for record in records if record["score"] == 0],
    }


def score_run(run_dir: Path, role: str, model_id: str, revision: str) -> int:
    scoring_started = time.monotonic()
    cases = load_cases()
    raw_path = run_dir / "raw-responses.jsonl"
    raw = load_raw(raw_path)
    if len(raw) != 96 or [row.get("case_id") for row in raw] != [case["id"] for case in cases]:
        raise RuntimeError(f"raw response order/count mismatch for {run_dir}")
    records: list[dict] = []
    coding_complete = True
    with (run_dir / "per-case-results.jsonl").open("w", encoding="utf-8") as case_output, (run_dir / "coding-judge-records.jsonl").open("w", encoding="utf-8") as judge_output:
        for ordinal, (case, row) in enumerate(zip(cases, raw), start=1):
            response = str(row.get("response_for_scoring", ""))
            base = {
                "ordinal": ordinal, "case_id": case["id"], "domain": case["domain"], "difficulty": case["difficulty"],
                "response_status": row.get("status"), "input_tokens": row.get("input_tokens"),
                "output_tokens": row.get("output_tokens"), "generation_elapsed_seconds": row.get("elapsed_seconds"),
            }
            if row.get("status") != "generated":
                result = {**base, "status": "scored", "score": 0, "reason": "generation_failure", "strict_interface_compliant": False}
            elif case["domain"] == "mathematics":
                normalization = normalize_math_response(response, case["expected"])
                result = {
                    **base, "status": "scored", "score": math_semantic_score(normalization, case["expected"]),
                    "reason": normalization.reason or ("accepted_candidate" if normalization.status == "accepted" else normalization.status),
                    "normalization_status": normalization.status, "candidate_kind": normalization.candidate_kind,
                    "candidate_count": normalization.candidate_count, "normalized": normalization.normalized,
                    "strict_interface_compliant": strict_math_interface_compliance(response, case["expected"]),
                }
            else:
                extraction = extract_python_source(response, case["evaluator"]["entrypoint"])
                strict = strict_coding_interface_compliance(response, case["evaluator"]["entrypoint"])
                result = {
                    **base, "status": "scored", "score": 0, "reason": extraction.reason,
                    "extraction_status": extraction.status, "extraction_reason": extraction.reason,
                    "block_index": extraction.block_index, "block_language": extraction.block_language,
                    "strict_interface_compliant": strict,
                }
                if extraction.status == "accepted" and extraction.source is not None:
                    source_bytes = extraction.source.encode("utf-8")
                    result.update({"source_bytes": len(source_bytes), "source_sha256": hashlib.sha256(source_bytes).hexdigest()})
                    if len(source_bytes) > 12000:
                        result["reason"] = "source_exceeds_12000_bytes"
                    else:
                        score, reason, coding_complete = judge_code(case, extraction.source, ordinal, role, judge_output)
                        result.update({"score": score, "reason": reason})
                if not coding_complete:
                    result["status"] = "not_scored"
            records.append(result)
            case_output.write(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")
            case_output.flush()
            if not coding_complete:
                for remaining_ordinal, remaining in enumerate(cases[ordinal:], start=ordinal + 1):
                    result = {
                        "ordinal": remaining_ordinal, "case_id": remaining["id"], "domain": remaining["domain"],
                        "difficulty": remaining["difficulty"], "status": "not_scored", "score": 0,
                        "reason": "coding_judge_infrastructure_failure", "strict_interface_compliant": False,
                    }
                    records.append(result)
                    case_output.write(json.dumps(result, sort_keys=True) + "\n")
                break
    metrics = aggregate(records)
    metrics.update({
        "model_id": model_id, "model_role": role, "model_revision": revision,
        "benchmark_id": "gate-a-cross-skill-v1.2.2", "scoring_policy": "experiments/gate-a/benchmark-v1.2.2/scoring.yaml",
        "adapter": "experiments/gate-a/benchmark-v1.2.2/adapter/semantic_adapter.py",
        "coding_judge_policy": JUDGE_POLICY, "scoring_elapsed_seconds": time.monotonic() - scoring_started,
    })
    write_json(run_dir / "metrics.json", metrics)
    write_json(run_dir / "scoring-summary.json", {
        "schema_version": 1, "status": "complete" if coding_complete and len(records) == 96 else "incomplete",
        "timestamp_utc": now(), "benchmark_id": "gate-a-cross-skill-v1.2.2", "model_id": model_id,
        "model_role": role, "model_revision": revision, "raw_responses": "raw-responses.jsonl",
        "per_case_results": "per-case-results.jsonl", "coding_judge_records": "coding-judge-records.jsonl",
        "metrics": "metrics.json", "metrics_inline": metrics,
    })
    print(json.dumps({"run_id": run_dir.name, "status": "complete" if coding_complete else "incomplete", "overall": metrics["overall"]}, sort_keys=True))
    return 0 if coding_complete and len(records) == 96 else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--revision", required=True)
    args = parser.parse_args()
    return score_run(Path(args.run_dir), args.role, args.model_id, args.revision)


if __name__ == "__main__":
    raise SystemExit(main())
