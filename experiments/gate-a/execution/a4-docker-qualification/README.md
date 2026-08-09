# Gate A A4a Docker execution qualification

Status: GPU path approved; Docker judge hardening v2 passed and is pending human review. This directory records the Docker substrate only. No selected Qwen checkpoint was downloaded or executed, and no frozen Gate A benchmark case was run.

## Environment

The exact host, Docker Engine, NVIDIA Container Toolkit, GPU inventory, image IDs/digests, and read-only snapshots of `ollama` and `open-webui` are in [environment.json](environment.json). The existing services remained running and unchanged. Their bind mounts were recorded as out of scope and were not accessed, repermissioned, or used as a Gate A cache.

Qualification images are generic infrastructure images only:

- GPU probe: `nvidia/cuda:12.4.1-base-ubuntu22.04`, image ID `sha256:ca14dc8401b66a20e1ca678268250834c5c66ac3f458dd570088bb681444ffc0`, repository digest `sha256:0f6bfcbf267e65123bcc2287e2153dedfc0f24772fb5ce84afe16ac4b2fada95`.
- Judge probe: `python:3.10-slim`, image ID `sha256:a28dc131a2de35d6475377050de1b5a71d0ee3118d7fdf3ce65be660d9feb6cf`, repository digest `sha256:63669fd2563fa90b0442fa7b568e66e3667755636cda086d7bcaaa895f66fe39`.

## Dedicated GPU inference qualification

Result: **PASS**.

The selected device is host GPU 0, UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`, an NVIDIA L40 at PCI address `00000000:26:00.0`. The host has two L40s; the probe saw exactly one GPU, with the selected UUID, driver `550.107.02`, CUDA image version `12.4.1`, and compute capability `8.9`.

The successful disposable launch was:

```bash
docker run --name dexinode-gate-a-a4a-gpu-qual-20260809-final \
  --gpus '"device=GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664"' \
  --network none --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=16m \
  --cap-drop=ALL --security-opt=no-new-privileges:true \
  --pids-limit 64 --memory 512m --cpus 1 --ulimit nproc=64:64 \
  nvidia/cuda:12.4.1-base-ubuntu22.04 bash -lc 'set -eu; nvidia-smi -L; nvidia-smi --query-gpu=index,uuid,name,driver_version,memory.total,compute_cap --format=csv,noheader; test "$(nvidia-smi --query-gpu=count --format=csv,noheader | tr -d "[:space:]")" = 1; test "$(nvidia-smi --query-gpu=uuid --format=csv,noheader)" = GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664; test "$(nvidia-smi --query-gpu=name --format=csv,noheader)" = "NVIDIA L40"; echo QUALIFICATION_GPU_VISIBILITY_PASS'
```

The recorded container ID is `e81ec2fdf0846dc6ad89aeefd5cdafaa71077262c3d0e953b71ea687055fedc2`; it exited 0 and was removed after inspection. Docker recorded runtime `runc`, no mounts, `privileged=false`, and one `DeviceRequest` containing only the selected UUID. The full receipt is [inference-gpu-preflight.json](inference-gpu-preflight.json).

The CUDA image has a default `NVIDIA_VISIBLE_DEVICES=all` image environment value, but the Docker device request constrained actual device visibility; `nvidia-smi` reported only the selected UUID. A separate attempt to reassert the UUID with an explicit `--env NVIDIA_VISIBLE_DEVICES=...` stopped at its environment assertion before `nvidia-smi` and exited 1. That nonfinal failure and metadata are retained in the receipt; it was not concealed or used to weaken the device-request qualification.

## CPU-only coding judge qualification — A4a v1 historical receipt

Result: **PASS**. The final probe produced 19/19 true checks. The probe is standard-library-only and is supplied over stdin; it does not import, compile, or execute benchmark or model-generated code.

The exact successful isolation launch was:

```bash
docker run -i --name dexinode-gate-a-a4a-judge-qual-receipt \
  --user 0:0 --network none --ipc private --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=16m \
  --cap-drop=ALL --security-opt=no-new-privileges:true \
  --pids-limit 32 --memory 256m --cpus 0.5 \
  --ulimit nproc=32:32 --ulimit fsize=1048576:1048576 \
  --stop-timeout 2 \
  --log-driver=json-file --log-opt max-size=64k --log-opt max-file=1 \
  python:3.10-slim python3 - \
  < experiments/gate-a/execution/a4-docker-qualification/judge_isolation_probe.py
```

The probe container had no mounts, no devices, no device requests, and `privileged=false`. It demonstrated network denial and empty routes; no GPU nodes; hidden host worktree, host home, Docker socket, Docker root, Ollama home, and Ollama model mount; read-only root; private writable `/tmp` tmpfs; zero effective/permitted/bounding capabilities; effective `NoNewPrivs=1`; cgroup CPU/memory/PID limits; and a 1 MiB file-size limit enforced on write. The receipt is [judge-isolation-preflight.json](judge-isolation-preflight.json), and the probe source is [judge_isolation_probe.py](judge_isolation_probe.py).

Wall-clock enforcement in v1 used a non-model 60-second sleep and a 3-second host-side runner. This is historical evidence only; it is superseded for later coding evaluation by the v2 receipt below.

## CPU-only coding judge hardening — A4a v2 revision

Result: **PASS pending human review**. The new receipt is [judge-isolation-preflight-v2.json](judge-isolation-preflight-v2.json); the v1 receipt remains unchanged. The revised probe produced 21/21 true checks: all 19 previous checks, explicit `nproc_bounded`, and mandatory `subprocess_denied`.

The exact hardened judge launch was:

```bash
docker run -i --name dexinode-gate-a-a4a-judge-qual-v2-root \
  --user 0:0 --network none --ipc private --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=16m \
  --cap-drop=ALL --security-opt=no-new-privileges:true \
  --pids-limit 1 --memory 256m --cpus 0.5 \
  --ulimit nproc=1:1 --ulimit fsize=1048576:1048576 \
  --stop-timeout 2 \
  --log-driver=json-file --log-opt max-size=64k --log-opt max-file=1 \
  python:3.10-slim python3 - \
  < experiments/gate-a/execution/a4-docker-qualification/judge_isolation_probe_v2.py
```

The successful container exited 0 with effective UID 0, GID 0, no mounts/devices/device requests, and `privileged=false`. The probe observed `pids.max=1`, `RLIMIT_NPROC=[1,1]`, zero effective/permitted/bounding capabilities, `NoNewPrivs=1`, and all previous network, filesystem, GPU, tmpfs, resource, file-size, and output-limit checks passing.

The mandatory subprocess probe called `subprocess.run([sys.executable, "-c", "pass"])`. Child creation failed with `BlockingIOError`, errno 11 (`EAGAIN`), and the receipt recorded `subprocess_denied=true`.

The preferred non-root attempt used UID `65534:65534` with the same mandatory policy. It failed closed before Python startup with `resource temporarily unavailable`; that failed container metadata is preserved in the v2 receipt. The passing fallback uses root only inside the container, while retaining `--cap-drop=ALL` and `no-new-privileges`; no privileged mode or host capability was added.

The v2 wall-clock qualification used the same hardened policy and a harmless 60-second sleep:

```bash
timeout --foreground --kill-after=1s 2s docker wait dexinode-gate-a-a4a-judge-wallclock-v2
```

The watchdog returned exit 124 after 2008 ms while the container was still running, then cleanup returned kill exit 0 and remove exit 0. The 2-second bound is now the required per-test wall-clock policy; Docker's host-side watchdog remains mandatory because the container launch has no native per-process wall-clock limit.

## Attempt and failure accounting

The receipts retain nonfinal failures rather than treating them as passes: the explicit GPU environment reassertion failed before visibility probing; an early judge invocation used unsupported `--pid private`; two noninteractive stdin invocations did not execute the v1 probe; and the v2 non-root attempt failed before Python startup under `nproc=1`. The v1 judge receipt was not overwritten. The final v2 receipt uses only the successful, correctly invoked hardened probe. No privileged container, Docker socket, host mount, existing Ollama cache, model artifact, or benchmark case was used.

## Human checkpoint

Human review is required to approve the v2 judge receipt, exact image digest, one-process policy, subprocess denial, root fallback, and 2-second host-side watchdog before A4b General Baseline execution. A4b remains inactive until that approval. The frozen benchmark, scoring rules, neutral template, candidate set, and Gate acceptance criteria are unchanged.
