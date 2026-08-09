#!/usr/bin/env python3
"""Run the approved Gate A judge-v2 isolation probe and preserve its receipt."""

from __future__ import annotations

import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path


RUN_ROOT = Path(__file__).resolve().parent
PROBE = Path("experiments/gate-a/execution/a4-docker-qualification/judge_isolation_probe_v2.py")
IMAGE = "python:3.10-slim@sha256:63669fd2563fa90b0442fa7b568e66e3667755636cda086d7bcaaa895f66fe39"
CONTAINER = "dexinode-gate-a4b-judge-preflight-20260809T082430Z"

docker_args = [
    "docker", "run", "-i", "--name", CONTAINER,
    "--user", "0:0",
    "--network", "none",
    "--ipc", "private",
    "--read-only",
    "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=16m",
    "--cap-drop=ALL",
    "--security-opt=no-new-privileges:true",
    "--pids-limit", "1",
    "--ulimit", "nproc=1:1",
    "--ulimit", "fsize=1048576:1048576",
    "--memory", "256m",
    "--cpus", "0.5",
    "--stop-timeout", "2",
    "--log-driver", "json-file",
    "--log-opt", "max-size=64k",
    "--log-opt", "max-file=1",
    IMAGE,
    "python3", "-",
]

started = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
started_mono = time.monotonic()
probe = PROBE.read_bytes()
proc = subprocess.run(
    docker_args,
    input=probe,
    capture_output=True,
    check=False,
)
elapsed = time.monotonic() - started_mono
finished = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

inspect = subprocess.run(
    ["docker", "inspect", CONTAINER],
    capture_output=True,
    check=False,
)
inspect_json = None
if inspect.returncode == 0:
    inspect_json = json.loads(inspect.stdout)

receipt = {
    "receipt_version": "a4b-coding-judge-preflight-v2-run-v1",
    "status": "pass" if proc.returncode == 0 else "fail_closed",
    "started_at": started,
    "finished_at": finished,
    "elapsed_seconds": elapsed,
    "container_name": CONTAINER,
    "image": IMAGE,
    "docker_args": docker_args,
    "probe": str(PROBE),
    "probe_sha256": __import__("hashlib").sha256(probe).hexdigest(),
    "exit_code": proc.returncode,
    "stdout": proc.stdout.decode("utf-8", errors="replace"),
    "stderr": proc.stderr.decode("utf-8", errors="replace"),
    "docker_inspect_exit_code": inspect.returncode,
    "docker_inspect": inspect_json,
}
(RUN_ROOT / "coding-isolation-preflight.json").write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "status": receipt["status"],
    "exit_code": proc.returncode,
    "elapsed_seconds": elapsed,
    "container_name": CONTAINER,
}, sort_keys=True))
raise SystemExit(0 if proc.returncode == 0 else 1)
