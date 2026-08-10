# Dexinode Session Handoff

Repository: `chlangjou/Dexinode`
Canonical/default branch: `main`
Snapshot date: 2026-08-10

## Start here

Read, in order:

1. `AGENTS.md`
2. this file
3. `status/current.md`
4. `gates/gate-b-orchestration/task.yaml`
5. `gates/gate-b-orchestration/acceptance.yaml`
6. `gates/gate-b-orchestration/reviews/b1r2-v1.1.1-human-review.md`
7. `gates/gate-b-orchestration/reviews/b2-static-qualification.md`

Git is the durable source of truth.

## Current state

Gate A — Specialist Validation: **PASS / CLOSED**.

Active gate: **Gate B — Orchestration Advantage**.

Gate B final decision: **PENDING HUMAN REVIEW**.

Active bounded stage: **B3B4 — comparable policy execution**.

B1R2 `gate-b-orchestration-v1.1.1` is human-approved. B2 static qualification is PASS/COMPLETE. Selected-model execution is now authorized **only** under the frozen B3B4 protocol.

## Frozen benchmark and registry

Benchmark:

`experiments/gate-b/benchmark-v1.1.1/`

Router:

`experiments/gate-b/router-v2/`

Registry:

- Mathematics → `Qwen/Qwen2.5-Math-7B-Instruct` @ `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`;
- Coding/fallback → `Qwen/Qwen2.5-7B-Instruct` @ `a09a35458c702b33eeacc393d103063234e8bc28`;
- Qwen2.5-Coder must **not** be executed in Gate B v1.

Static acceptance evidence is complete: Math 48/48, Coding evaluator 48/48, Coding semantic-contract audit 48/48, adapter 13/13, router tests 5/5 with 96/96 target routes, max input 124, context margin 2948. Numerical Gate B thresholds are frozen unchanged.

The informational `case_file` strings inside the v1.1.1 case YAML still contain a v1.1.0 label; this is a recorded non-material metadata issue. Do not create a new revision or patch the benchmark for it.

## B3B4 execution sequence

1. Persist all 96 router decisions from semantic task text before the first model output.
2. Run General once on all 96 cases in frozen order and preserve every response/receipt.
3. **Do not inspect, score, summarize, or review General results.**
4. Run the Math specialist only on the frozen `mathematics_specialist` routes and preserve every response/receipt.
5. Reuse the preserved General response for General/fallback routes in the routed-policy row.
6. Only after both evidence phases finish, compose/score General-only and routed rows and compute frozen metrics.
7. No retries, second-model fallback, voting, ensemble, Coder execution, result-driven rerouting, performance early stop, protocol/benchmark/scoring/threshold change, or result-conditioned tuning.
8. Genuine infrastructure/methodological failure may stop the run; preserve partial/invalid evidence and do not patch from observed results.
9. Commit all durable evidence and stop for human review before B5 or a final Gate B decision.

The execution environment remains the approved `ai01` / single NVIDIA L40 / BF16 / no quantization / deterministic-generation substrate recorded in the benchmark manifest and protocol.

## Execution Agent branch

Prepared branch after integration:

`agent/gate-b-b3b4-comparable-policy-execution`

Before touching `ai01`, verify this branch is based on current approved `main` and read the controlling files above.

## Minimal Agent instruction

> Read `AGENTS.md`, `HANDOFF.md`, `status/current.md`, `gates/gate-b-orchestration/task.yaml`, `gates/gate-b-orchestration/acceptance.yaml`, and `gates/gate-b-orchestration/reviews/b2-static-qualification.md`. Execute only active B3B4 exactly as frozen. Persist all routes before model output; run General on all 96, do not inspect results, then run Math specialist only on frozen specialist routes. Preserve all evidence, compose/score only after both phases, update durable status, commit, stop for human review, do not execute Coder, and do not push until instructed.
