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

### CPU coding judge — HARDENING COMPLETE; PENDING HUMAN REVIEW

The revised Docker judge now passes the frozen one-process policy: all 19 previous isolation checks remain true, `pids.max=1`, `RLIMIT_NPROC=[1,1]`, and the mandatory `subprocess_denied` probe failed child creation with `BlockingIOError`/errno 11. The 2-second host watchdog killed a harmless long-sleep workload after 2008 ms and cleanup succeeded.

The preferred non-root attempt (`65534:65534`) failed closed before Python startup under `nproc=1`; its failed metadata is preserved. The passing exact policy uses effective UID 0 inside the container, with `--cap-drop=ALL`, `no-new-privileges`, no mounts/devices/socket, and all previously approved controls retained. Non-root was not used because it was incompatible with executable Python under the frozen one-process bound on this runtime.

New durable evidence:

- `experiments/gate-a/execution/a4-docker-qualification/judge-isolation-preflight-v2.json`
- `experiments/gate-a/execution/a4-docker-qualification/judge_isolation_probe_v2.py`

The prior v1 judge receipt remains unchanged.

## Active bounded task

The Docker judge hardening revision is complete; stop for human review. No GPU qualification was rerun because its approved execution identity was unchanged.

Completed requirements:

1. `--pids-limit 1` and `--ulimit nproc=1:1` are enforced;
2. `subprocess_denied` is mandatory and passes;
3. the 2-second host-side wall-clock watchdog passes;
4. the 1 MiB file-size limit and all prior isolation checks pass;
5. failed/invalid attempts and the prior receipt are preserved;
6. effective UID is recorded, with the non-root startup failure documented.

Do not rerun the GPU qualification unless its execution identity changes.

Do not download or execute General, Math, or Coder checkpoints. Do not run benchmark cases. Do not modify/restart/recreate `ollama` or `open-webui`. Do not modify the frozen benchmark or Gate acceptance criteria.

## Next human checkpoint

Review `judge-isolation-preflight-v2.json` against the frozen A3 isolation policy, especially the root fallback, `pids/nproc=1`, subprocess denial, and 2-second watchdog. If accepted, authorize A4b General Baseline execution using the approved single-L40 inference path and exact approved judge policy.

A4b and A5 remain inactive.
