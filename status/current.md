# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A4a — Docker Execution Environment Qualification (qualified; pending human review)

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

The immediate purpose is to establish whether distinct competency surfaces exist strongly enough to justify a later orchestration/routing experiment.

## Approved candidate set

- general baseline: `Qwen/Qwen2.5-7B-Instruct`
- mathematics specialist: `Qwen/Qwen2.5-Math-7B-Instruct`
- coding specialist: `Qwen/Qwen2.5-Coder-7B-Instruct`

A2 eligibility is approved. The durable record is:

`gates/gate-a-specialization/reviews/a2-human-review.md`

## Approved benchmark

Gate A execution uses the frozen superseding benchmark:

`experiments/gate-a/benchmark-v1.1.0/`

Human approval record:

`gates/gate-a-specialization/reviews/a3-human-review-v1.1.md`

Key frozen controls remain unchanged:

- 48 mathematics + 48 software-coding cases, 96 total;
- every selected model eventually runs all 96 cases;
- deterministic scoring, equal case weights, no LLM judge;
- neutral shared Qwen role-delimiter template;
- `rendered_input_tokens + max_new_tokens <= 4096`;
- BF16, no quantization, no external tools;
- Gate acceptance criteria and candidate set unchanged.

## A4 attempt 1 — valid fail-closed blocker

Run ID: `a4-general-baseline-20260809T064011Z-ai01`

Evidence:

- `experiments/gate-a/runs/a4-general-baseline-20260809T064011Z-ai01/environment.json`
- `experiments/gate-a/runs/a4-general-baseline-20260809T064011Z-ai01/preflight-receipt.json`

The host-side bubblewrap preflight failed before model execution:

`bwrap: loopback: Failed to create NETLINK_ROUTE socket: Operation not permitted`

No General, Math, or Coder model was executed. Human review accepts this as an execution-context blocker, not a Gate or benchmark failure.

Durable review:

`gates/gate-a-specialization/reviews/a4-preflight-human-review.md`

## Human-approved execution direction

Qualify Docker on `ai01` as the Gate A execution substrate before any model download or inference.

Existing `ollama` and `open-webui` containers are out of scope for modification. They may be inspected read-only only as infrastructure evidence. Do not alter their configuration, mounts, permissions, model cache, lifecycle, or network.

The intended topology is:

1. a dedicated Gate A inference container using one explicitly selected NVIDIA L40 GPU;
2. a separate CPU-only coding judge container with fail-closed isolation;
3. a Gate-specific model/cache location independent of existing Ollama storage when model execution is later authorized.

The Docker qualification contract is:

`gates/gate-a-specialization/execution/a4-docker-qualification.yaml`

This is an explicit human-approved execution-policy amendment. It does not modify the frozen benchmark cases, scoring, prompt template, candidate set, or Gate acceptance criteria.

## Active bounded task: A4a — Docker Execution Environment Qualification

Qualification only. Do not download or execute any selected Qwen model and do not run benchmark cases.

Completed on `ai01` with both required paths passing:

- dedicated disposable GPU probe: PASS; exactly one visible GPU, host GPU 0 `NVIDIA L40`, UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- separate CPU-only judge probe: PASS; 19/19 isolation checks true, plus a passing 3-second host watchdog probe;
- no selected model was downloaded or executed, no benchmark case ran, and existing `ollama`/`open-webui` containers were inspected read-only only and remained unchanged.

Durable evidence:

- `experiments/gate-a/execution/a4-docker-qualification/environment.json`
- `experiments/gate-a/execution/a4-docker-qualification/inference-gpu-preflight.json`
- `experiments/gate-a/execution/a4-docker-qualification/judge-isolation-preflight.json`
- `experiments/gate-a/execution/a4-docker-qualification/README.md`
- `experiments/gate-a/execution/a4-docker-qualification/judge_isolation_probe.py`

The receipts preserve nonfinal failed/invalid attempts. A residual policy note is recorded: actual GPU visibility is constrained by Docker's UUID device request even though the generic CUDA image carries a default `NVIDIA_VISIBLE_DEVICES=all`; an explicit environment reassertion attempt failed before the visibility probe and was not substituted for the passing qualification. The later judge runner must retain the recorded host-side 3-second wall-clock watchdog.

Required work:

1. record Docker engine/runtime and host identity;
2. inspect existing `ollama`/`open-webui` read-only only as needed to confirm NVIDIA Docker infrastructure;
3. qualify a dedicated disposable GPU container that sees exactly one selected L40 and record GPU/driver/CUDA/container identity;
4. qualify a separate CPU-only judge container with no network, no GPU, read-only root, private tmpfs, dropped capabilities, `no-new-privileges`, hidden host worktree/home/Docker socket/model cache, and bounded CPU/memory/PIDs/time/output;
5. preserve machine-readable receipts for both qualification paths;
6. stop for human review.

A4a must NOT:

- download or execute General, Math, or Coder checkpoints;
- run benchmark cases;
- modify the frozen benchmark;
- modify Gate acceptance criteria;
- modify/restart/recreate `ollama` or `open-webui`;
- repermission or use the existing Ollama model bind mount;
- use a privileged judge container or mount the Docker socket into it;
- weaken isolation merely to obtain a pass;
- proceed to baseline inference.

## Next human checkpoint

Review and accept or reject the Docker GPU qualification, judge-isolation receipts, image digests, exact launch flags, and host-side watchdog. If accepted, authorize A4b General Baseline execution on this exact policy. A4b remains inactive until that decision.

A5 remains inactive.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
