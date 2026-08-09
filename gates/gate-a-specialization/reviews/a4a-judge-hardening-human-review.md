# A4a Human Review — Docker Judge Hardening v2

- Date: 2026-08-09
- Reviewer role: Human decision owner
- Reviewed commit: `9650229643c251e6243c9c78283b86bbcc912164`
- Stage: A4a — Docker Execution Environment Qualification
- Decision: **APPROVED**
- Gate A decision: **PENDING**

## Approved inference path

The previously approved single-GPU Docker inference path remains valid and does not require rerun because its execution identity did not change:

- host: `ai01`;
- Docker Engine 29.5.3, runtime `runc`;
- selected device: NVIDIA L40, host GPU 0;
- selected UUID: `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- Docker `DeviceRequest` constrains visibility to that UUID;
- the qualification container observed exactly one GPU and the expected UUID;
- existing `ollama` and `open-webui` services remain outside the Gate A execution path and must not be modified or used as the Gate model cache.

The generic CUDA image's default `NVIDIA_VISIBLE_DEVICES=all` environment value is not treated as additional exposure because both the controlling Docker device request and the observed device inventory contain only the selected GPU.

## Approved coding-judge path

The hardened v2 judge satisfies the frozen Gate A v1.1.0 process and isolation requirements.

Accepted evidence:

- `experiments/gate-a/execution/a4-docker-qualification/judge-isolation-preflight-v2.json`
- `experiments/gate-a/execution/a4-docker-qualification/judge_isolation_probe_v2.py`

The approved exact policy includes:

- image `python:3.10-slim` at the recorded repository/image digests;
- CPU-only, no GPU devices or device requests;
- `--network none`;
- no host mounts and no Docker socket;
- read-only root filesystem;
- private `/tmp` tmpfs;
- `--cap-drop=ALL`;
- `--security-opt=no-new-privileges:true`;
- `--pids-limit 1`;
- `--ulimit nproc=1:1`;
- `--memory 256m`;
- `--cpus 0.5`;
- 1 MiB file-size limit;
- bounded log/output configuration;
- mandatory host-side 2-second wall-clock watchdog.

The v2 receipt records 21/21 passing checks. In particular:

- `pids.max=1`;
- `RLIMIT_NPROC=[1,1]`;
- external child creation through `subprocess.run()` failed with `BlockingIOError` / `EAGAIN`;
- the 2-second watchdog triggered after 2008 ms and cleanup succeeded;
- all 19 previously approved network/filesystem/device/capability/resource checks passed again.

## Root-container fallback

The preferred non-root UID `65534:65534` failed closed before Python startup under the mandatory one-process policy. That failed attempt is preserved.

The UID 0 fallback is **approved for this exact judge policy** because UID is not being relied upon as the isolation boundary. The passing container is not privileged, has zero effective/permitted/bounding capabilities, has `NoNewPrivs=1`, exposes no host mount/socket/network/GPU, has a read-only root filesystem, and the one-process cgroup limit empirically denies subprocess creation.

Changing any of those controls, the judge image identity, Docker/runtime identity, or the process/watchdog policy requires renewed qualification before coding scores are accepted.

## A4b authorization

A4a is complete and approved. **A4b — General Baseline Execution is authorized.**

A4b may:

- create a Gate-specific model/cache location independent of Ollama storage;
- download only the pinned general baseline `Qwen/Qwen2.5-7B-Instruct` revision `a09a35458c702b33eeacc393d103063234e8bc28`;
- build/use a dedicated inference container with the frozen BF16/no-quantization/runtime policy;
- execute the general baseline over all 96 frozen v1.1.0 cases;
- score coding responses only through the exact approved judge policy above;
- preserve raw outputs, per-case scores, timing, failures, runtime/image/model identities, and preflight receipts.

A4b must not execute Math or Coder specialist checkpoints and must stop for human review before A5.

The frozen benchmark, scoring rules, prompt template, candidate set, and Gate acceptance criteria remain unchanged.