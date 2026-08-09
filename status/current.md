# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A4a — Docker Execution Environment Qualification (judge hardening required)

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

## Frozen Gate A controls

Approved candidate set:

- general baseline: `Qwen/Qwen2.5-7B-Instruct`
- mathematics specialist: `Qwen/Qwen2.5-Math-7B-Instruct`
- coding specialist: `Qwen/Qwen2.5-Coder-7B-Instruct`

Approved benchmark: `experiments/gate-a/benchmark-v1.1.0/`.

The frozen benchmark, scoring rules, neutral prompt template, model revisions, candidate set, and Gate acceptance criteria remain unchanged. No selected model has been executed yet.

## A4 attempt 1 — preserved fail-closed blocker

Run `a4-general-baseline-20260809T064011Z-ai01` stopped before model execution because host-side bubblewrap could not establish the required network namespace.

Evidence:

- `experiments/gate-a/runs/a4-general-baseline-20260809T064011Z-ai01/environment.json`
- `experiments/gate-a/runs/a4-general-baseline-20260809T064011Z-ai01/preflight-receipt.json`

Human review classified this as an execution-context blocker, not a Gate or benchmark failure:

`gates/gate-a-specialization/reviews/a4-preflight-human-review.md`

## A4a Docker qualification — review result

Agent qualification commit reviewed: `8ad46c50cd15a298b45c46613c676c09e9d6cea9`.

Durable evidence root:

`experiments/gate-a/execution/a4-docker-qualification/`

Human review:

`gates/gate-a-specialization/reviews/a4a-docker-qualification-human-review.md`

### Dedicated inference GPU path — APPROVED

The Docker GPU path on `ai01` is accepted:

- Docker Engine 29.5.3, runtime `runc`;
- exactly one selected NVIDIA L40 is exposed;
- selected host GPU 0 UUID: `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- Docker `DeviceRequest` contains only that UUID;
- the probe container observed exactly one GPU and the UUID matched;
- existing `ollama` and `open-webui` services were not modified;
- no selected Qwen checkpoint or benchmark case was executed.

The generic CUDA image's default `NVIDIA_VISIBLE_DEVICES=all` value is not treated as additional GPU exposure because the controlling device request and observed device inventory both show only the selected UUID.

GPU qualification does not need to be repeated solely for the judge revision. Repeat it if the inference host/image/runtime/selected GPU or relevant NVIDIA container configuration changes.

### CPU coding judge — CHANGES REQUIRED

The current Docker judge demonstrated strong isolation controls, including no network, no GPU, no host/Docker/model-cache mounts, read-only root, private tmpfs, dropped capabilities, `NoNewPrivs=1`, cgroup bounds, file-size enforcement, and a host watchdog.

However, the frozen Gate A v1.1.0 coding-isolation policy requires:

- one process (`process_count: 1`);
- a mandatory `subprocess_denied` probe;
- no subprocess/shell/job-control/external-process capability exposed to model code;
- a 2-second per-test timeout.

The reviewed A4a judge used `--pids-limit 32`, `--ulimit nproc=32:32`, a 3-second watchdog, and did not test subprocess denial. These controls are bounded but weaker than the frozen process policy, so A4a is not yet fully approved.

## Active bounded task

Revise and rerun **only the Docker judge qualification**.

Required revision:

1. target `--pids-limit 1` and `--ulimit nproc=1:1` so the Python judge is the only process;
2. add a `subprocess_denied` probe that attempts to start an external child process and must fail;
3. qualify a 2-second host-side wall-clock watchdog;
4. preserve the 1 MiB file-size limit;
5. retain or strengthen all previously passing network/filesystem/GPU/capability/no-new-privileges/resource checks;
6. preserve invalid/failed attempts;
7. preferably run as a non-root container user if practical, and record the effective UID.

Do not rerun the GPU qualification unless its execution identity changes.

Do not download or execute General, Math, or Coder checkpoints. Do not run benchmark cases. Do not modify/restart/recreate `ollama` or `open-webui`. Do not modify the frozen benchmark or Gate acceptance criteria.

## Next human checkpoint

Review the revised judge receipt against the frozen A3 isolation policy. If accepted, authorize A4b General Baseline execution using the approved single-L40 inference path and exact approved judge policy.

A4b and A5 remain inactive.
