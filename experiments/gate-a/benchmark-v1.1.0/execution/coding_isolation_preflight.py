#!/usr/bin/env python3
"""Fail-closed bounded-isolation preflight for the Gate A coding runner.

This probes the runner boundary only. It does not load a model or execute any
benchmark case or model-generated source. A later evaluator must preserve the
JSON output as the coding-run preflight receipt and refuse to score without it.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone


PROBE = r'''
import json
import os
import resource
import socket
import subprocess
import sys

checks = {}

resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))
resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))
resource.setrlimit(resource.RLIMIT_NPROC, (1, 1))
checks["cpu_and_memory_bounds_configured"] = True

try:
    with socket.create_connection(("198.51.100.1", 80), timeout=0.25):
        checks["network_denied"] = False
except OSError:
    checks["network_denied"] = True

host_marker = os.environ.get("DEXINODE_HOST_MARKER", "/home/rd/Dexinode")
checks["host_filesystem_hidden"] = not os.path.exists(host_marker) and not os.path.exists("/home/rd")

try:
    with open("/usr/bin/python3", "ab"):
        pass
    checks["system_paths_read_only"] = False
except OSError:
    checks["system_paths_read_only"] = True

try:
    subprocess.run([sys.executable, "-c", "pass"], check=True, timeout=0.25)
    checks["subprocess_denied"] = False
except (OSError, RuntimeError, subprocess.SubprocessError):
    checks["subprocess_denied"] = True

temp_path = "/tmp/dexinode-preflight-private"
try:
    with open(temp_path, "w", encoding="utf-8") as handle:
        handle.write("private")
    checks["private_temp_only"] = os.path.isfile(temp_path)
except OSError:
    checks["private_temp_only"] = False

print(json.dumps(checks, sort_keys=True))
if not all(checks.values()):
    raise SystemExit(1)
'''

REQUIRED_PROBES = {
    "cpu_and_memory_bounds_configured",
    "network_denied",
    "host_filesystem_hidden",
    "system_paths_read_only",
    "subprocess_denied",
    "private_temp_only",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host-marker",
        default=os.getcwd(),
        help="Path that must be hidden inside the sandbox; normally the evaluation worktree.",
    )
    args = parser.parse_args()

    bwrap = shutil.which("bwrap")
    receipt = {
        "preflight_id": "gate-a-coding-bounded-isolation-v1",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "host_identity": platform.node(),
        "kernel_identity": platform.platform(),
        "python_identity": sys.version,
        "sandbox_identity": bwrap or "missing",
        "command_digest": "bwrap namespaces + read-only runtime + private tmpfs + resource limits",
        "probe_results": {},
        "stdout": "",
        "stderr": "",
        "exit_code": 1,
    }
    if bwrap is None:
        receipt["stderr"] = "Required bwrap executable was not found; refusing to score coding cases."
        print(json.dumps(receipt, indent=2, sort_keys=True))
        return 1

    command = [
        bwrap,
        "--die-with-parent",
        "--new-session",
        "--unshare-pid",
        "--unshare-net",
        "--unshare-ipc",
        "--unshare-uts",
        "--ro-bind",
        "/usr",
        "/usr",
        "--ro-bind",
        "/lib",
        "/lib",
        "--ro-bind",
        "/lib64",
        "/lib64",
        "--ro-bind",
        "/etc",
        "/etc",
        "--proc",
        "/proc",
        "--dev",
        "/dev",
        "--tmpfs",
        "/tmp",
        "--dir",
        "/run",
        "--chdir",
        "/tmp",
        "--clearenv",
        "--setenv",
        "HOME",
        "/nonexistent",
        "--setenv",
        "DEXINODE_HOST_MARKER",
        args.host_marker,
        "/usr/bin/python3",
        "-I",
        "-S",
        "-c",
        PROBE,
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        receipt["stdout"] = result.stdout
        receipt["stderr"] = result.stderr
        receipt["exit_code"] = result.returncode
        if result.stdout.strip():
            try:
                receipt["probe_results"] = json.loads(result.stdout.strip().splitlines()[-1])
            except json.JSONDecodeError:
                receipt["probe_results"] = {"unparseable_probe_output": True}
    except (OSError, subprocess.SubprocessError) as exc:
        receipt["stderr"] = repr(exc)

    print(json.dumps(receipt, indent=2, sort_keys=True))
    probes = receipt["probe_results"]
    passed = REQUIRED_PROBES.issubset(probes) and all(
        probes[name] is True for name in REQUIRED_PROBES
    )
    return 0 if receipt["exit_code"] == 0 and passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
