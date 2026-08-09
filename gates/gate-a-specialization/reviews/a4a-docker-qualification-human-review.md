# A4a Human Review — Docker Execution Qualification

- Date: 2026-08-09
- Reviewer role: Human decision owner / planning review
- Reviewed commit: `8ad46c50cd15a298b45c46613c676c09e9d6cea9`
- Stage: A4a — Docker Execution Environment Qualification
- Decision: **CHANGES REQUIRED — JUDGE HARDENING ONLY**
- Gate A decision: **PENDING**

## Accepted evidence

### Dedicated inference GPU path — APPROVED

The GPU qualification is accepted for later A4b execution:

- host: `ai01`;
- Docker Engine 29.5.3, runtime `runc`;
- selected device: host GPU 0, NVIDIA L40;
- UUID: `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- Docker `DeviceRequest` specifies only that UUID;
- the disposable probe observed exactly one GPU and the observed UUID matched the selected UUID;
- driver `550.107.02` and CUDA container visibility were recorded;
- no selected Qwen checkpoint or benchmark case was executed;
- existing `ollama` and `open-webui` services were not modified.

The CUDA image's default `NVIDIA_VISIBLE_DEVICES=all` environment value is not treated as evidence that both GPUs were exposed. The controlling Docker device request and the observed `nvidia-smi` inventory both show exactly one visible selected GPU. The preserved failed attempt to reassert `NVIDIA_VISIBLE_DEVICES` explicitly does not invalidate the successful UUID-constrained probe.

The approved GPU receipt is:

`experiments/gate-a/execution/a4-docker-qualification/inference-gpu-preflight.json`

The GPU qualification does not need to be repeated solely because the judge policy requires revision. It must be repeated if the later inference host, image/runtime policy, selected GPU, or relevant NVIDIA container configuration changes.

## Judge isolation — revision required

The Docker judge probe successfully demonstrated many required isolation properties, including no network, no GPU devices, no host mounts or Docker socket, read-only root, private tmpfs, dropped capabilities, `NoNewPrivs=1`, resource bounds, file-size enforcement, and a host-side wall-clock watchdog.

However, it does **not yet satisfy the frozen Gate A v1.1.0 coding-isolation contract**.

The frozen policy at:

`experiments/gate-a/benchmark-v1.1.0/execution/coding_isolation_preflight.yaml`

requires:

- `process_count: 1`;
- a `subprocess_denied` mandatory probe;
- coding evaluator exposure must not provide subprocess, shell, job-control, or external-process capability to model-generated code;
- `per_test_timeout_seconds: 2`.

The reviewed Docker judge instead used `--pids-limit 32`, `--ulimit nproc=32:32`, and a 3-second watchdog, and its 19 checks did not include a subprocess-denial probe. These are bounded controls, but they are weaker than the already frozen process-execution policy and therefore cannot be silently substituted after benchmark freeze.

## Required bounded revision

Revise and rerun only the Docker judge qualification. Do not rerun the GPU probe unless its execution identity changes.

The revised judge policy must, at minimum:

1. enforce a one-process container cgroup/process limit compatible with the Python judge itself, targeting `--pids-limit 1` and `--ulimit nproc=1:1` unless a technically necessary alternative is documented and human-reviewed before use;
2. add a mandatory `subprocess_denied` probe that attempts to create an external child process and verifies that it fails;
3. use a 2-second host-side wall-clock timeout for each later coding case, matching the frozen policy;
4. preserve the existing 1 MiB file-size limit;
5. retain or strengthen all currently passing network/filesystem/GPU/capability/no-new-privileges/resource-isolation checks;
6. preserve invalid or failed attempts rather than replacing them silently;
7. continue to prohibit privileged containers, Docker-socket mounts, host/model-cache mounts, selected-model execution, and benchmark-case execution during qualification.

Defense in depth: if practical without weakening reproducibility, run the judge as a non-root container user and record the effective UID. This is preferred but is not the reason for this CHANGES REQUIRED decision.

The frozen benchmark cases, scoring rules, template, candidate set, model revisions, and Gate acceptance thresholds remain unchanged.

## Human checkpoint

A4a remains active with judge hardening required. A4b General Baseline execution remains inactive.

After the revised judge receipt passes the frozen one-process/subprocess-denial and 2-second timeout controls, stop again for human review before any selected Qwen checkpoint is downloaded or executed.
