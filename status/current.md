# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A4 — General Baseline

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

The immediate purpose is to establish whether distinct competency surfaces exist strongly enough to justify a later orchestration/routing experiment.

## Approved candidate set

- general baseline: `Qwen/Qwen2.5-7B-Instruct`
- mathematics specialist: `Qwen/Qwen2.5-Math-7B-Instruct`
- coding specialist: `Qwen/Qwen2.5-Coder-7B-Instruct`

A2 eligibility is approved. The durable record is:

`gates/gate-a-specialization/reviews/a2-human-review.md`

## A3 benchmark history

### v1.0.0 — preserved, not approved for execution

`gate-a-cross-skill-v1.0.0` was frozen before model execution, then human-reviewed as **CHANGES REQUIRED** because of limited per-domain sample size, ceiling-effect risk, and the need for actual bounded coding isolation.

The frozen v1.0.0 artifacts remain unchanged in:

`experiments/gate-a/benchmark/`

The durable review is:

`gates/gate-a-specialization/reviews/a3-human-review-v1.md`

### v1.1.0 — APPROVED

The superseding benchmark is frozen in:

`experiments/gate-a/benchmark-v1.1.0/`

Human review approves v1.1.0 for A4 subject to execution preflight. The durable review is:

`gates/gate-a-specialization/reviews/a3-human-review-v1.1.md`

Approved benchmark properties:

- 48 mathematics + 48 software-coding cases, 96 total;
- every selected model must eventually run all 96 cases;
- 10 foundational, 24 intermediate, and 14 advanced cases per domain;
- deterministic scoring, equal case weights, no LLM judge;
- neutral shared Qwen role-delimiter template with identical semantic messages;
- `rendered_input_tokens + max_new_tokens <= 4096` for every case;
- BF16, no quantization, no external tools;
- explicit provenance, contamination limitations, and difficulty-stratified reporting;
- Gate acceptance criteria and candidate set remain unchanged.

No selected model output was used to construct either benchmark version.

## Execution blocker discovered during A3

Coding evaluation is fail-closed behind the bounded-isolation preflight defined in:

`experiments/gate-a/benchmark-v1.1.0/execution/coding_isolation_preflight.yaml`

The A3 preflight on host `ai01` failed because bubblewrap could not establish the required network namespace (`NETLINK_ROUTE: Operation not permitted`). The failed receipt is preserved at:

`experiments/gate-a/benchmark-v1.1.0/execution/preflight-receipt-a3.json`

This is an execution-host blocker, not a benchmark-definition failure.

## Active bounded task: A4 — General Baseline

Execute only the pinned general baseline:

- model: `Qwen/Qwen2.5-7B-Instruct`
- revision: `a09a35458c702b33eeacc393d103063234e8bc28`
- benchmark: `gate-a-cross-skill-v1.1.0`

Required order:

1. record the exact execution host, runtime, device, and environment;
2. run the frozen coding-isolation preflight on that exact environment;
3. if preflight fails, stop without executing the baseline and report the blocker;
4. if preflight passes, execute the general baseline over all 96 frozen cases using the approved common inference policy;
5. preserve the passing preflight receipt, raw per-case responses, per-case scores/reasons, timing, failures, and reproducibility metadata;
6. stop for human review before A5.

A4 must NOT:

- modify the frozen v1.1.0 benchmark, scoring, or template;
- modify Gate acceptance criteria;
- change the candidate set;
- execute Math or Coder specialist checkpoints;
- proceed to A5.

## Next human checkpoint

Review the A4 execution environment/preflight and, if baseline execution occurs, the complete general-model run evidence. A5 remains inactive until that review is recorded.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
