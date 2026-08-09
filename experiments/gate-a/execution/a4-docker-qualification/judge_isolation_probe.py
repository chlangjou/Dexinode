#!/usr/local/bin/python
"""Non-model isolation probes for the Gate A Docker coding judge.

The script is supplied over stdin to a disposable container. It never imports,
compiles, or executes benchmark cases or model-generated source.
"""

from __future__ import annotations

import glob
import json
import os
import resource
import socket
import stat
from pathlib import Path


EXPECTED_CPU_MAX = os.environ.get("EXPECTED_CPU_MAX", "50000 100000")
EXPECTED_MEMORY_MAX = os.environ.get("EXPECTED_MEMORY_MAX", "268435456")
EXPECTED_PIDS_MAX = os.environ.get("EXPECTED_PIDS_MAX", "32")
EXPECTED_FILE_SIZE = int(os.environ.get("EXPECTED_FILE_SIZE", "1048576"))

checks: dict[str, bool] = {}
details: dict[str, object] = {}


def read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8").strip()


# Docker --network none must leave no usable non-loopback route or connection.
try:
    socket.create_connection(("198.51.100.1", 80), timeout=0.25)
    checks["network_denied"] = False
except OSError as exc:
    checks["network_denied"] = True
    details["network_error"] = type(exc).__name__
route_lines = [line for line in read_text("/proc/net/route").splitlines()[1:] if line.strip()]
checks["network_routes_empty"] = not route_lines
details["network_routes"] = route_lines


# No NVIDIA device nodes or host GPU exposure are allowed in the CPU judge.
gpu_nodes = sorted(glob.glob("/dev/nvidia*") + glob.glob("/dev/dri/*"))
checks["no_gpu_devices"] = not gpu_nodes
details["gpu_nodes"] = gpu_nodes


# No host paths, Docker socket, or existing model/cache paths may be visible.
hidden_paths = {
    "host_worktree": "/home/rd/Dexinode",
    "host_home": "/home/rd",
    "docker_socket": "/var/run/docker.sock",
    "ollama_model_mount": "/data/ollama/ollama",
    "ollama_home": "/root/.ollama",
    "docker_root": "/data/docker/lib/docker",
}
for name, path in hidden_paths.items():
    checks[f"{name}_hidden"] = not os.path.exists(path)
details["hidden_paths"] = hidden_paths


# Root must not be able to write the image filesystem; /tmp must be a private tmpfs.
root_probe = "/gate-a-root-write-probe"
try:
    Path(root_probe).write_text("must fail", encoding="utf-8")
    checks["root_filesystem_read_only"] = False
    Path(root_probe).unlink(missing_ok=True)
except OSError as exc:
    checks["root_filesystem_read_only"] = True
    details["root_write_error"] = type(exc).__name__

tmp_mounts = []
for line in read_text("/proc/mounts").splitlines():
    fields = line.split()
    if len(fields) >= 3 and fields[1] == "/tmp":
        tmp_mounts.append(fields[:4])
checks["private_tmp_available"] = False
tmp_probe = "/tmp/gate-a-private-tmp-probe"
try:
    Path(tmp_probe).write_text("private", encoding="utf-8")
    checks["private_tmp_available"] = Path(tmp_probe).read_text(encoding="utf-8") == "private"
    Path(tmp_probe).unlink(missing_ok=True)
except OSError:
    checks["private_tmp_available"] = False
checks["private_tmp_is_tmpfs"] = any(mount[2] == "tmpfs" for mount in tmp_mounts)
details["tmp_mounts"] = tmp_mounts


def status_value(name: str) -> str:
    for line in read_text("/proc/self/status").splitlines():
        if line.startswith(name + ":"):
            return line.split("\t", 1)[-1].strip()
    return "missing"


cap_eff = status_value("CapEff")
cap_prm = status_value("CapPrm")
cap_bnd = status_value("CapBnd")
checks["capabilities_dropped"] = cap_eff == "0000000000000000" and cap_prm == "0000000000000000" and cap_bnd == "0000000000000000"
details["cap_eff"] = cap_eff
details["cap_prm"] = cap_prm
details["cap_bnd"] = cap_bnd
checks["no_new_privileges_effective"] = status_value("NoNewPrivs") == "1"
details["no_new_privs"] = status_value("NoNewPrivs")


def cgroup_value(name: str) -> str:
    return read_text(f"/sys/fs/cgroup/{name}")


cpu_max = cgroup_value("cpu.max")
memory_max = cgroup_value("memory.max")
pids_max = cgroup_value("pids.max")
checks["cpu_bounded"] = cpu_max == EXPECTED_CPU_MAX and cpu_max != "max"
checks["memory_bounded"] = memory_max == EXPECTED_MEMORY_MAX and memory_max != "max"
checks["pids_bounded"] = pids_max == EXPECTED_PIDS_MAX and pids_max != "max"
details["cpu_max"] = cpu_max
details["memory_max"] = memory_max
details["pids_max"] = pids_max


# Confirm the file-size limit is active by attempting a write above the bound.
soft, hard = resource.getrlimit(resource.RLIMIT_FSIZE)
checks["file_size_bounded"] = soft == EXPECTED_FILE_SIZE and hard == EXPECTED_FILE_SIZE
details["rlimit_fsize"] = [soft, hard]
large_path = "/tmp/gate-a-file-size-probe"
try:
    with open(large_path, "wb") as handle:
        handle.write(b"x" * (EXPECTED_FILE_SIZE + 1))
    checks["file_size_write_bound_enforced"] = os.path.getsize(large_path) <= EXPECTED_FILE_SIZE
    os.unlink(large_path)
except (OSError, ValueError):
    checks["file_size_write_bound_enforced"] = True
    try:
        os.unlink(large_path)
    except FileNotFoundError:
        pass
details["expected_file_size_bytes"] = EXPECTED_FILE_SIZE


details["effective_uid"] = os.geteuid()
details["root_mode"] = oct(stat.S_IMODE(os.stat("/").st_mode))
details["all_checks"] = len(checks)
result = {
    "status": "pass" if all(checks.values()) else "fail_closed",
    "checks": checks,
    "details": details,
}
print(json.dumps(result, sort_keys=True))
raise SystemExit(0 if all(checks.values()) else 1)
