#!/usr/bin/env python3
"""Execute the frozen Gate B B3B4 sequence without between-phase result reads."""

from __future__ import annotations

import argparse
import hashlib
import json
import shlex
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
BENCHMARK = ROOT / "experiments/gate-b/benchmark-v1.1.1"
ROUTER = ROOT / "experiments/gate-b/router-v2/router.py"
RUNNER = ROOT / "experiments/gate-b/execution/b3b4_runner.py"
IMAGE = "sha256:004879ed29152e413822d14c6720e4374ac0d8e88b882a9f471bb492ba3f8f4f"
GPU_UUID = "GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664"
MODEL_ROWS = {
    "general_baseline": {
        "model_id": "Qwen/Qwen2.5-7B-Instruct",
        "revision": "a09a35458c702b33eeacc393d103063234e8bc28",
        "cache_volume": "dexinode-gate-a-general-20260809T082430Z-cache",
        "model_dir": "/gate-cache/models/qwen2.5-7b-instruct",
    },
    "mathematics_specialist": {
        "model_id": "Qwen/Qwen2.5-Math-7B-Instruct",
        "revision": "ef9926d75ab1d54532f6a30dd5e760355eb9aa4d",
        "cache_volume": "dexinode-gate-a5-math-20260809T092120Z-cache",
        "model_dir": "/gate-cache/models/qwen2.5-math-7b-instruct",
    },
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_cases() -> list[dict]:
    math_cases = yaml.safe_load((BENCHMARK / "cases/math.yaml").read_text(encoding="utf-8"))["cases"]
    coding_cases = yaml.safe_load((BENCHMARK / "cases/coding.yaml").read_text(encoding="utf-8"))["cases"]
    cases = list(math_cases) + list(coding_cases)
    expected = [f"math-{index:02d}" for index in range(1, 49)] + [f"code-{index:02d}" for index in range(1, 49)]
    if [str(case["id"]) for case in cases] != expected:
        raise RuntimeError("frozen case order mismatch")
    return cases


def route_cases(cases: list[dict]) -> list[dict]:
    import importlib.util

    spec = importlib.util.spec_from_file_location("gate_b_router_v2", ROUTER)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load router")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    decisions = []
    for ordinal, case in enumerate(cases, start=1):
        semantic_task = str(case["semantic_task"])
        route = module.route_semantic_task(semantic_task)
        decisions.append({
            "ordinal": ordinal,
            "case_id": str(case["id"]),
            "semantic_task": semantic_task,
            "route": route,
            "evaluation_domain": str(case["domain"]),
        })
    return decisions


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.write_text("".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records), encoding="utf-8")


def run_command(command: list[str], log_path: Path) -> tuple[int, float]:
    started = time.monotonic()
    with log_path.open("w", encoding="utf-8") as log:
        log.write("COMMAND " + shlex.join(command) + "\n")
        log.flush()
        process = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, check=False)
    return process.returncode, time.monotonic() - started


def docker_run_command(*, mode: str, role: str, row: dict, output_volume: str, receipt_name: str,
                       raw_name: str | None, selected_path: Path | None) -> list[str]:
    benchmark = str(BENCHMARK)
    command = [
        "docker", "run", "--rm", "--name", f"dexinode-gate-b3b4-{mode}-{role}",
        "--gpus", f"device={GPU_UUID}", "--network", "none", "--ipc", "private", "--read-only",
        "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=64m", "--cap-drop", "ALL",
        "--security-opt", "no-new-privileges:true", "--memory", "40g", "--cpus", "16",
        "--log-driver", "json-file", "--log-opt", "max-size=64k", "--log-opt", "max-file=1",
        "--mount", f"type=volume,source={row['cache_volume']},target=/gate-cache,readonly",
        "--mount", f"type=bind,source={benchmark},target=/benchmark,readonly",
        "--mount", f"type=bind,source={RUNNER},target=/opt/gate-b/b3b4_runner.py,readonly",
        "--mount", f"type=volume,source={output_volume},target=/run",
    ]
    if raw_name is not None:
        raw_argument = ["--raw-output", f"/run/{raw_name}"]
    else:
        raw_argument = []
    if selected_path is not None:
        command.extend(["--mount", f"type=bind,source={selected_path},target=/selection/selected-case-ids.txt,readonly"])
        selected_argument = ["--selected-case-ids-file", "/selection/selected-case-ids.txt"]
    else:
        selected_argument = []
    command.extend([
        "--entrypoint", "python3", IMAGE, "/opt/gate-b/b3b4_runner.py", mode,
        "--model-id", row["model_id"], "--model-role", role, "--model-revision", row["revision"],
        "--model-dir", row["model_dir"], "--benchmark-root", "/benchmark", "--receipt", f"/run/{receipt_name}",
        *raw_argument, *selected_argument,
    ])
    return command


def collect_output_volume(volume: str, run_dir: Path, ordinal: int) -> tuple[int, str]:
    collector = f"dexinode-gate-b3b4-collector-{ordinal}"
    create = ["docker", "create", "--name", collector, "--mount", f"type=volume,source={volume},target=/src", IMAGE]
    created = subprocess.run(create, capture_output=True, check=False, text=True)
    if created.returncode != 0:
        return created.returncode, created.stderr.strip()
    copied = subprocess.run(["docker", "cp", f"{collector}:/src/.", str(run_dir)], capture_output=True, check=False, text=True)
    removed = subprocess.run(["docker", "rm", "-f", collector], capture_output=True, check=False, text=True)
    if copied.returncode != 0:
        return copied.returncode, copied.stderr.strip()
    if removed.returncode != 0:
        return removed.returncode, removed.stderr.strip()
    return 0, ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execution-id", required=True)
    args = parser.parse_args()
    cases = load_cases()
    decisions = route_cases(cases)
    if len(decisions) != 96:
        raise RuntimeError("route decision count mismatch")
    counts = {route: sum(item["route"] == route for item in decisions) for route in ("mathematics_specialist", "general_baseline", "fallback")}
    if counts != {"mathematics_specialist": 48, "general_baseline": 48, "fallback": 0}:
        raise RuntimeError(f"unexpected route counts: {counts}")

    run_root = ROOT / "experiments/gate-b/runs" / args.execution_id
    general_dir = run_root / "general-baseline"
    math_dir = run_root / "mathematics-specialist"
    general_dir.mkdir(parents=True, exist_ok=True)
    math_dir.mkdir(parents=True, exist_ok=True)
    route_path = run_root / "route-decisions.jsonl"
    selected_path = math_dir / "selected-case-ids.txt"
    write_jsonl(route_path, decisions)
    selected_path.write_text("".join(item["case_id"] + "\n" for item in decisions if item["route"] == "mathematics_specialist"), encoding="utf-8")
    route_receipt = {
        "schema_version": 1, "execution_id": args.execution_id, "benchmark_id": "gate-b-orchestration-v1.1.1",
        "router": "experiments/gate-b/router-v2/router.py", "router_sha256": sha256_file(ROUTER),
        "route_decisions": str(route_path.relative_to(ROOT)), "selected_math_case_ids": str(selected_path.relative_to(ROOT)),
        "case_count": 96, "route_counts": counts, "decision_input": "semantic_task_only",
        "decision_before_first_model_output": True, "model_output_visible_to_router": False,
        "expected_value_visible_to_router": False, "evaluation_domain_recorded_after_decision": True,
        "timestamp_utc": now(),
    }
    write_json(run_root / "route-receipt.json", route_receipt)
    plan = {
        "schema_version": 1, "execution_id": args.execution_id, "benchmark_id": "gate-b-orchestration-v1.1.1",
        "status": "route_freeze_complete", "started_utc": now(),
        "benchmark_root": "experiments/gate-b/benchmark-v1.1.1/",
        "benchmark_manifest_sha256": sha256_file(BENCHMARK / "manifest.yaml"),
        "protocol_sha256": sha256_file(BENCHMARK / "protocol.yaml"),
        "scoring_sha256": sha256_file(BENCHMARK / "scoring.yaml"),
        "runner_sha256": sha256_file(RUNNER), "route_receipt": str((run_root / "route-receipt.json").relative_to(ROOT)),
        "run_order": ["general_baseline", "mathematics_specialist"], "result_inspection_between_phases": False,
        "rows": [],
    }
    plan_path = run_root / "orchestration.json"
    write_json(plan_path, plan)

    run_specs = [
        (1, "general_baseline", general_dir, None, 96),
        (2, "mathematics_specialist", math_dir, selected_path, 48),
    ]
    for ordinal, role, run_dir, selected, selected_count in run_specs:
        row = MODEL_ROWS[role]
        output_volume = f"dexinode-gate-b3b4-{args.execution_id}-{role}-output"
        subprocess.run(["docker", "volume", "create", output_volume], capture_output=True, check=True, text=True)
        code, elapsed = run_command(
            docker_run_command(mode="preflight", role=role, row=row, output_volume=output_volume,
                               receipt_name="preflight.json", raw_name=None, selected_path=selected),
            run_dir / "container-preflight.log",
        )
        plan["rows"].append({"ordinal": ordinal, "role": role, "phase": "preflight", "exit_code": code,
                             "elapsed_seconds": elapsed, "selected_case_count": selected_count,
                             "run_dir": str(run_dir.relative_to(ROOT)), "output_volume": output_volume})
        write_json(plan_path, plan)
        if code != 0:
            plan["status"] = "stopped_preflight_failure"
            plan["finished_utc"] = now()
            write_json(plan_path, plan)
            return code

    # Formal rows are launched in order. This process never opens either raw output file.
    for ordinal, role, run_dir, selected, selected_count in run_specs:
        row = MODEL_ROWS[role]
        output_volume = f"dexinode-gate-b3b4-{args.execution_id}-{role}-output"
        code, elapsed = run_command(
            docker_run_command(mode="run", role=role, row=row, output_volume=output_volume,
                               receipt_name="inference-receipt.json", raw_name="raw-responses.jsonl", selected_path=selected),
            run_dir / "container-inference.log",
        )
        plan["rows"].append({"ordinal": ordinal, "role": role, "phase": "formal_inference", "exit_code": code,
                             "elapsed_seconds": elapsed, "selected_case_count": selected_count,
                             "raw_output": str((run_dir / "raw-responses.jsonl").relative_to(ROOT)),
                             "result_inspected_by_orchestrator": False, "output_volume": output_volume})
        write_json(plan_path, plan)
        if code != 0:
            for collect_ordinal, collect_role, collect_dir, _, _ in run_specs[:ordinal]:
                collect_volume = f"dexinode-gate-b3b4-{args.execution_id}-{collect_role}-output"
                collect_output_volume(collect_volume, collect_dir, collect_ordinal)
            plan["status"] = "stopped_formal_infrastructure_failure"
            plan["finished_utc"] = now()
            write_json(plan_path, plan)
            return code

    # Collection is intentionally delayed until both formal phases have finished.
    for ordinal, role, run_dir, _, _ in run_specs:
        output_volume = f"dexinode-gate-b3b4-{args.execution_id}-{role}-output"
        code, error = collect_output_volume(output_volume, run_dir, ordinal)
        plan["rows"].append({"ordinal": ordinal, "role": role, "phase": "output_collection", "exit_code": code,
                             "error": error, "result_inspected_by_orchestrator": False, "output_volume": output_volume})
        write_json(plan_path, plan)
        if code != 0:
            plan["status"] = "stopped_output_collection_failure"
            plan["finished_utc"] = now()
            write_json(plan_path, plan)
            return code
    plan["status"] = "formal_inference_complete_pending_scoring"
    plan["finished_utc"] = now()
    write_json(plan_path, plan)
    print("B3B4_FORMAL_INFERENCE_COMPLETE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
