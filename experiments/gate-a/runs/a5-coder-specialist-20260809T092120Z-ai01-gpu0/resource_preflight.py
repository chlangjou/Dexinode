#!/usr/bin/env python3
"""Record read-only host/Docker/GPU resource evidence for an A5 run."""

from __future__ import annotations

import json
import platform
import shutil
import socket
import subprocess
from datetime import datetime, timezone
from pathlib import Path


RUN_ID = "a5-coder-specialist-20260809T092120Z-ai01-gpu0"
OUT = Path(__file__).resolve().parent / "resource-preflight.json"
GPU_UUID = "GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664"


def command(args: list[str]) -> dict[str, object]:
    proc = subprocess.run(args, capture_output=True, text=True, check=False)
    return {"argv": args, "exit_code": proc.returncode, "stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}


def meminfo() -> dict[str, int]:
    values: dict[str, int] = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, _, value = line.partition(":")
        if value.strip().endswith(" kB"):
            values[key] = int(value.split()[0]) * 1024
    return values


def main() -> None:
    repo = shutil.disk_usage("/home/rd/Dexinode")
    data = {
        "schema_version": "a5-resource-preflight-v1",
        "status": "pass",
        "timestamp_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "run_id": RUN_ID,
        "host": socket.gethostname(),
        "platform": platform.platform(),
        "repository_filesystem": {"path": "/home/rd/Dexinode", "free_bytes": repo.free, "used_bytes": repo.used, "total_bytes": repo.total},
        "memory": meminfo(),
        "nvidia_smi": command(["nvidia-smi", "--query-gpu=index,uuid,name,driver_version,memory.total,memory.used,memory.free,pci.bus_id,utilization.gpu", "--format=csv,noheader"]),
        "docker_info": command(["docker", "info", "--format", "{{json .}}"]),
        "docker_ps": command(["docker", "ps", "--format", "{{.Names}} {{.Status}}"]),
        "selected_gpu_uuid": GPU_UUID,
        "existing_services_policy": "ollama and open-webui were not stopped, modified, or used for model storage",
        "decision": "resources recorded before specialist acquisition; proceed only with the authorized specialist",
    }
    OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": data["status"], "host": data["host"], "run_id": RUN_ID}, sort_keys=True))


if __name__ == "__main__":
    main()
