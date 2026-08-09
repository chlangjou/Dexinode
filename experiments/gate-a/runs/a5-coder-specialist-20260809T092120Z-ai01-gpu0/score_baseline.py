#!/usr/bin/env python3
"""Deterministically score one frozen Gate A coding specialist run.

Mathematics is scored in this host-side script using the frozen exact rules.
Coding source is never compiled or executed here: each case is supplied only
to a disposable CPU-only Docker judge using the approved judge-v2 policy.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent
BENCHMARK = ROOT.parents[1] / "benchmark-v1.1.0"
RAW_PATH = ROOT / "raw-responses.jsonl"
CASE_OUTPUT = ROOT / "per-case-results.jsonl"
JUDGE_OUTPUT = ROOT / "coding-judge-records.jsonl"
METRICS_OUTPUT = ROOT / "metrics.json"
SUMMARY_OUTPUT = ROOT / "scoring-summary.json"
JUDGE_IMAGE = "python:3.10-slim@sha256:63669fd2563fa90b0442fa7b568e66e3667755636cda086d7bcaaa895f66fe39"
JUDGE_PREFIX = "dexinode-gate-a5-coder-judge-20260809T092120Z"
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


def load_cases() -> list[dict]:
    math_cases = yaml.safe_load((BENCHMARK / "cases/math.yaml").read_text())['cases']
    code_cases = yaml.safe_load((BENCHMARK / "cases/coding.yaml").read_text())['cases']
    return math_cases + code_cases


def load_raw() -> list[dict]:
    return [json.loads(line) for line in RAW_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]


def math_score(case: dict, response: str) -> tuple[int, str, object | None]:
    answer_lines = [line.strip() for line in response.splitlines() if line.strip().startswith("ANSWER:")]
    if len(answer_lines) != 1:
        return 0, "answer_marker_count_not_one", None
    answer = answer_lines[0][len("ANSWER:"):].strip()
    expected = case["expected"]
    kind = expected["type"]
    if kind == "integer":
        if not re.fullmatch(r"[+-]?\d+", answer):
            return 0, "invalid_integer_format", None
        parsed = int(answer)
        return (1, "exact_integer_match", parsed) if parsed == expected["value"] else (0, "integer_mismatch", parsed)
    if kind == "rational":
        match = re.fullmatch(r"([+-]?\d+)/([+-]?\d+)", answer)
        if not match:
            return 0, "invalid_rational_format", None
        numerator, denominator = int(match.group(1)), int(match.group(2))
        if denominator == 0:
            return 0, "zero_rational_denominator", None
        divisor = math.gcd(numerator, denominator)
        numerator //= divisor
        denominator //= divisor
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        parsed = f"{numerator}/{denominator}"
        expected_n, expected_d = map(int, expected["value"].split("/"))
        expected_g = math.gcd(expected_n, expected_d)
        expected_n, expected_d = expected_n // expected_g, expected_d // expected_g
        if expected_d < 0:
            expected_n, expected_d = -expected_n, -expected_d
        return (1, "exact_reduced_rational_match", parsed) if (numerator, denominator) == (expected_n, expected_d) else (0, "rational_mismatch", parsed)
    if kind == "json_object":
        try:
            parsed = json.loads(answer)
        except json.JSONDecodeError:
            return 0, "invalid_json_format", None
        if not isinstance(parsed, dict) or set(parsed) != set(expected["value"]):
            return 0, "json_object_keys_mismatch", parsed
        if any(type(value) is not int for value in parsed.values()):
            return 0, "json_object_values_not_integers", parsed
        return (1, "exact_json_object_match", parsed) if parsed == expected["value"] else (0, "json_object_mismatch", parsed)
    return 0, "unknown_math_expected_type", None


def extract_source(response: str) -> tuple[str | None, str]:
    fences = list(re.finditer(r"```([^\n`]*)\n([\s\S]*?)```", response))
    if not fences:
        return response, "full_response_fallback"
    if len(fences) != 1:
        return None, "multiple_code_blocks"
    fence = fences[0]
    language = fence.group(1).strip().lower()
    outside = (response[:fence.start()] + response[fence.end():]).strip()
    if language not in {"python", "py", ""}:
        return None, "non_python_code_fence"
    if outside:
        return None, "prose_outside_code_block"
    return fence.group(2), "first_python_code_block"


def docker_json(args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(args, capture_output=True, check=False)
    return proc.returncode, proc.stdout.decode("utf-8", "replace"), proc.stderr.decode("utf-8", "replace")


def score_code(case: dict, response: str, ordinal: int, judge_records) -> tuple[dict, bool]:
    source, extraction = extract_source(response)
    base = {
        "case_id": case["id"],
        "domain": case["domain"],
        "difficulty": case["difficulty"],
        "score": 0,
        "status": "scored",
        "reason": extraction,
        "extraction": extraction,
    }
    if source is None:
        return base, True
    try:
        source_bytes = source.encode("utf-8")
    except UnicodeEncodeError:
        base["reason"] = "source_not_utf8"
        return base, True
    base["source_bytes"] = len(source_bytes)
    base["source_sha256"] = hashlib.sha256(source_bytes).hexdigest()
    if len(source_bytes) > 12000:
        base["reason"] = "source_exceeds_12000_bytes"
        return base, True

    evaluator = case["evaluator"]
    name = f"{JUDGE_PREFIX}-{ordinal:03d}"
    create_args = [
        "docker", "create", "-i", "--name", name,
        "--user", "0:0", "--network", "none", "--ipc", "private",
        "--read-only", "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=16m",
        "--cap-drop=ALL", "--security-opt=no-new-privileges:true",
        "--pids-limit", "1", "--ulimit", "nproc=1:1",
        "--ulimit", "fsize=1048576:1048576", "--memory", "256m",
        "--cpus", "0.5", "--stop-timeout", "2",
        "--log-driver", "json-file", "--log-opt", "max-size=64k",
        "--log-opt", "max-file=1", JUDGE_IMAGE,
        "python3", "-c", JUDGE_EXECUTOR,
    ]
    create_started = time.monotonic()
    create_code, create_stdout, create_stderr = docker_json(create_args)
    if create_code != 0:
        judge_records.write(json.dumps({
            **base, "container_name": name, "judge_status": "infrastructure_failure",
            "create_exit_code": create_code, "create_stdout": create_stdout,
            "create_stderr": create_stderr, "policy": JUDGE_POLICY,
        }, sort_keys=True) + "\n")
        return {**base, "status": "not_scored", "reason": "judge_container_create_failed"}, False
    container_id = create_stdout.strip().splitlines()[-1] if create_stdout.strip() else None
    payload = json.dumps({
        "source": source,
        "entrypoint": evaluator["entrypoint"],
        "tests": evaluator["tests"],
    }, sort_keys=True, separators=(",", ":")).encode("utf-8")
    start_args = ["timeout", "--foreground", "--kill-after=1s", "2s", "docker", "start", "-ai", name]
    started_at = now()
    start_mono = time.monotonic()
    try:
        proc = subprocess.Popen(start_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate(input=payload, timeout=6)
        start_code = proc.returncode
    except subprocess.TimeoutExpired as exc:
        proc.kill()
        stdout, stderr = proc.communicate()
        start_code = 124
        stderr += b"\nwatchdog host communication timeout\n"
    elapsed = time.monotonic() - start_mono
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
    out_text = stdout.decode("utf-8", "replace")
    err_text = stderr.decode("utf-8", "replace")
    judge_result = None
    if not timed_out:
        lines = [line for line in out_text.splitlines() if line.strip()]
        if lines:
            try:
                judge_result = json.loads(lines[-1])
            except json.JSONDecodeError:
                judge_result = None
    reason = ""
    score = 0
    if timed_out:
        reason = "judge_timeout_2_seconds"
    elif start_code != 0:
        reason = "judge_runtime_failure"
    elif not isinstance(judge_result, dict):
        reason = "judge_protocol_error"
    elif judge_result.get("status") == "pass":
        score = 1
        reason = "all_unit_tests_passed"
    else:
        reason = str(judge_result.get("reason", "judge_rejected_source"))
    base.update({"score": score, "reason": reason, "container_name": name, "container_id": container_id})
    judge_record = {
        "case_id": case["id"],
        "ordinal": ordinal,
        "container_name": name,
        "container_id": container_id,
        "image": JUDGE_IMAGE,
        "policy": JUDGE_POLICY,
        "started_at": started_at,
        "elapsed_seconds": elapsed,
        "create_elapsed_seconds": time.monotonic() - create_started,
        "create_exit_code": create_code,
        "start_exit_code": start_code,
        "timed_out": timed_out,
        "stdout": out_text,
        "stderr": err_text,
        "judge_result": judge_result,
        "inspect_exit_code": inspect_code,
        "container_exit_code": inspect_data.get("State", {}).get("ExitCode") if inspect_data else None,
        "container_oom_killed": inspect_data.get("State", {}).get("OOMKilled") if inspect_data else None,
        "cleanup_exit_code": cleanup_code,
        "cleanup_stdout": cleanup_stdout,
        "cleanup_stderr": cleanup_stderr,
    }
    judge_records.write(json.dumps(judge_record, sort_keys=True) + "\n")
    return base, True


def aggregate(records: list[dict]) -> dict:
    def group(domain=None, difficulty=None):
        selected = [r for r in records if (domain is None or r["domain"] == domain) and (difficulty is None or r["difficulty"] == difficulty)]
        return {"correct": sum(r["score"] for r in selected), "total": len(selected), "accuracy": (sum(r["score"] for r in selected) / len(selected) if selected else None)}
    metrics = {
        "overall": group(),
        "mathematics": group("mathematics"),
        "software_coding": group("software_coding"),
        "difficulty": {
            domain: {difficulty: group(domain, difficulty) for difficulty in ("foundational", "intermediate", "advanced")}
            for domain in ("mathematics", "software_coding")
        },
        "case_count": len(records),
        "scored_case_count": sum(r["status"] == "scored" for r in records),
        "failed_or_invalid_cases": [r["case_id"] for r in records if r["score"] == 0],
    }
    return metrics


def main() -> int:
    started = time.monotonic()
    cases = load_cases()
    raw = load_raw()
    raw_by_id = {row["case_id"]: row for row in raw}
    if len(cases) != 96 or len(raw) != 96 or set(raw_by_id) != {case["id"] for case in cases}:
        raise SystemExit("case/raw response set does not exactly match frozen 96-case benchmark")
    records = []
    coding_complete = True
    with CASE_OUTPUT.open("w", encoding="utf-8") as case_out, JUDGE_OUTPUT.open("w", encoding="utf-8") as judge_out:
        for ordinal, case in enumerate(cases, start=1):
            response = raw_by_id[case["id"]].get("response_for_scoring", "")
            base = {
                "ordinal": ordinal,
                "case_id": case["id"],
                "domain": case["domain"],
                "difficulty": case["difficulty"],
                "response_status": raw_by_id[case["id"]].get("status"),
                "input_tokens": raw_by_id[case["id"]].get("input_tokens"),
                "output_tokens": raw_by_id[case["id"]].get("output_tokens"),
                "generation_elapsed_seconds": raw_by_id[case["id"]].get("elapsed_seconds"),
            }
            if raw_by_id[case["id"]].get("status") != "generated":
                result = {**base, "status": "scored", "score": 0, "reason": "generation_failure"}
            elif case["domain"] == "mathematics":
                score, reason, parsed = math_score(case, response)
                result = {**base, "status": "scored", "score": score, "reason": reason, "parsed_answer": parsed}
            else:
                result, coding_complete = score_code(case, response, ordinal, judge_out)
                result = {**base, **result}
            records.append(result)
            case_out.write(json.dumps(result, sort_keys=True) + "\n")
            case_out.flush()
            if not coding_complete:
                for remaining_ordinal, remaining in enumerate(cases[ordinal:], start=ordinal + 1):
                    result = {"ordinal": remaining_ordinal, "case_id": remaining["id"], "domain": remaining["domain"], "difficulty": remaining["difficulty"], "status": "not_scored", "score": 0, "reason": "coding_judge_infrastructure_failure"}
                    records.append(result)
                    case_out.write(json.dumps(result, sort_keys=True) + "\n")
                break
    metrics = aggregate(records)
    metrics["scoring_elapsed_seconds"] = time.monotonic() - started
    metrics["coding_judge_policy"] = JUDGE_POLICY
    metrics["coding_isolation_preflight_receipt"] = "coding-isolation-preflight.json"
    metrics["scoring_policy"] = "experiments/gate-a/benchmark-v1.1.0/scoring.yaml"
    status = "complete" if coding_complete and len(records) == 96 else "incomplete"
    summary = {
        "schema_version": "a5-specialist-scoring-summary-v1",
        "status": status,
        "timestamp_utc": now(),
        "benchmark_version": "gate-a-cross-skill-v1.1.0",
        "scoring_policy": "experiments/gate-a/benchmark-v1.1.0/scoring.yaml",
        "raw_responses": "raw-responses.jsonl",
        "per_case_results": "per-case-results.jsonl",
        "coding_judge_records": "coding-judge-records.jsonl",
        "metrics": "metrics.json",
        "coding_isolation_preflight": "coding-isolation-preflight.json",
        "metrics_inline": metrics,
    }
    METRICS_OUTPUT.write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY_OUTPUT.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "case_count": len(records), "scoring_elapsed_seconds": metrics["scoring_elapsed_seconds"], "overall": metrics["overall"]}, sort_keys=True))
    return 0 if status == "complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())
