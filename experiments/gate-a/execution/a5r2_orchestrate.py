#!/usr/bin/env python3
"""Run the authorized A5R2 rows in frozen order without inspecting results."""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def run_command(command: list[str], log_path: Path) -> int:
    with log_path.open("w", encoding="utf-8") as log:
        log.write("COMMAND " + shlex.join(command) + "\n")
        log.flush()
        process = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, check=False)
    return process.returncode


def docker_command(
    *,
    mode: str,
    row: dict,
    config: dict,
    root: Path,
    run_root: Path,
    receipt_name: str,
    raw_name: str | None,
) -> list[str]:
    benchmark = root / config["benchmark_root"]
    runner = root / config["runner"]
    run_dir = root / "experiments/gate-a/runs" / row["run_id"]
    command = [
        "docker", "run", "--rm",
        "--name", f"dexinode-gate-a5r2-{mode}-{row['ordinal']}",
        "--gpus", f"device={config['selected_gpu_uuid']}",
        "--network", "none",
        "--ipc", "private",
        "--read-only",
        "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=64m",
        "--cap-drop", "ALL",
        "--security-opt", "no-new-privileges:true",
        "--memory", config["formal_resources"]["memory"],
        "--cpus", str(config["formal_resources"]["cpus"]),
        "--log-driver", "json-file",
        "--log-opt", "max-size=64k",
        "--log-opt", "max-file=1",
        "--mount", f"type=volume,source={row['cache_volume']},target=/gate-cache,readonly",
        "--mount", f"type=bind,source={benchmark},target=/benchmark,readonly",
        "--mount", f"type=bind,source={runner},target=/opt/gate-a/a5r2_runner.py,readonly",
        "--mount", f"type=volume,source={row['output_volume']},target=/run",
        "--entrypoint", "python3",
        config["runner_image"],
        "/opt/gate-a/a5r2_runner.py", mode,
        "--model-id", row["model_id"],
        "--model-role", row["role"],
        "--model-revision", row["revision"],
        "--model-dir", row["model_dir"],
        "--benchmark-root", "/benchmark",
        "--receipt", f"/run/{receipt_name}",
    ]
    if raw_name is not None:
        command.extend(["--raw-output", f"/run/{raw_name}"])
    return command


def collect_output_volume(row: dict, config: dict, root: Path, run_dir: Path) -> tuple[int, str]:
    collector = f"dexinode-gate-a5r2-collector-{row['ordinal']}"
    create = [
        "docker", "create", "--name", collector,
        "--mount", f"type=volume,source={row['output_volume']},target=/src,readonly",
        config["runner_image"],
    ]
    created = subprocess.run(create, capture_output=True, check=False, text=True)
    if created.returncode != 0:
        return created.returncode, created.stderr.strip()
    copied = subprocess.run(
        ["docker", "cp", f"{collector}:/src/.", str(run_dir)],
        capture_output=True, check=False, text=True,
    )
    removed = subprocess.run(["docker", "rm", "-f", collector], capture_output=True, check=False, text=True)
    if copied.returncode != 0:
        return copied.returncode, copied.stderr.strip()
    if removed.returncode != 0:
        return removed.returncode, removed.stderr.strip()
    return 0, ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="experiments/gate-a/execution/a5r2-execution.yaml")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    config_path = root / args.config
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    rows = list(config["run_order"])
    if [row["ordinal"] for row in rows] != [1, 2, 3]:
        raise SystemExit("run order is not exactly General, Math, Coder")
    if not config["controls"]["inspect_results_between_rows"]:
        pass
    run_root = root / "experiments/gate-a/runs"
    for row in rows:
        (run_root / row["run_id"]).mkdir(parents=True, exist_ok=True)
    orchestration_path = run_root / f"a5r2-orchestration-{rows[0]['run_id']}.json"
    plan = {
        "schema_version": 1,
        "execution_id": config["execution_id"],
        "status": "planned",
        "started_utc": now(),
        "benchmark_id": config["benchmark_id"],
        "config": str(config_path.relative_to(root)),
        "runner_sha256": __import__("hashlib").sha256((root / config["runner"]).read_bytes()).hexdigest(),
        "runner_image": config["runner_image"],
        "run_order": rows,
        "rows": [],
        "result_inspection_between_rows": False,
    }
    orchestration_path.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    # Preflight all rows before any formal generation. No model outputs exist at this phase.
    for row in rows:
        run_dir = run_root / row["run_id"]
        command = docker_command(
            mode="preflight", row=row, config=config, root=root, run_root=run_root,
            receipt_name="preflight.json", raw_name=None,
        )
        started = time.monotonic()
        code = run_command(command, run_dir / "container-preflight.log")
        result = {
            "ordinal": row["ordinal"], "role": row["role"], "model_id": row["model_id"],
            "phase": "preflight", "exit_code": code, "elapsed_seconds": time.monotonic() - started,
            "log": str((run_dir / "container-preflight.log").relative_to(root)),
        }
        plan["rows"].append(result)
        orchestration_path.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        if code != 0:
            plan["status"] = "stopped_preflight_failure"
            plan["finished_utc"] = now()
            orchestration_path.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            return code

    # Formal rows are launched in order. This process never reads raw output files.
    for row in rows:
        run_dir = run_root / row["run_id"]
        command = docker_command(
            mode="run", row=row, config=config, root=root, run_root=run_root,
            receipt_name="inference-receipt.json", raw_name="raw-responses.jsonl",
        )
        started = time.monotonic()
        code = run_command(command, run_dir / "container-inference.log")
        result = {
            "ordinal": row["ordinal"], "role": row["role"], "model_id": row["model_id"],
            "phase": "formal_inference", "exit_code": code, "elapsed_seconds": time.monotonic() - started,
            "log": str((run_dir / "container-inference.log").relative_to(root)),
            "raw_output": str((run_dir / "raw-responses.jsonl").relative_to(root)),
            "result_inspected_by_orchestrator": False,
        }
        plan["rows"].append(result)
        orchestration_path.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        if code != 0:
            plan["status"] = "stopped_formal_infrastructure_failure"
            plan["finished_utc"] = now()
            orchestration_path.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            return code

    for row in rows:
        run_dir = run_root / row["run_id"]
        code, error = collect_output_volume(row, config, root, run_dir)
        plan["rows"].append({
            "ordinal": row["ordinal"], "role": row["role"], "phase": "output_collection",
            "exit_code": code, "error": error, "result_inspected_by_orchestrator": False,
            "output_volume": row["output_volume"],
        })
        orchestration_path.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        if code != 0:
            plan["status"] = "stopped_output_collection_failure"
            plan["finished_utc"] = now()
            orchestration_path.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            return code

    plan["status"] = "formal_inference_complete_pending_scoring"
    plan["finished_utc"] = now()
    orchestration_path.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("A5R2_FORMAL_INFERENCE_COMPLETE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
