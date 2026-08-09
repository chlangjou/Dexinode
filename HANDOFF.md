# Dexinode Session Handoff

This is the resumable entry point for a fresh ChatGPT / human session.

Repository: `chlangjou/Dexinode`

Canonical/default branch: `main`.

Snapshot date: 2026-08-09.

## Start here in a new session

The user should be able to say only:

> Read `HANDOFF.md` from the Dexinode repository and continue from the current bounded task.

Then read, in order:

1. `AGENTS.md`
2. this file
3. `status/current.md`
4. `gates/gate-a-specialization/task.yaml`
5. `gates/gate-a-specialization/reviews/a5r2-v1.2.2-human-review.md`
6. `gates/gate-a-specialization/evidence-report.md`
7. `experiments/gate-a/a6-evidence-summary.yaml`

Git is the durable source of truth. Do not reconstruct project state from old chat logs when repository state is available.

## Current state

Active gate: **Gate A — Specialist Validation**.

Active bounded stage: **A6 — evidence report complete pending final human decision**.

Gate decision: **PENDING HUMAN REVIEW**.

Gate B remains inactive.

No additional model execution is required for the current Gate A evidence set.

## Frozen benchmark and candidates

Approved benchmark:

`gate-a-cross-skill-v1.2.2`

Benchmark root:

`experiments/gate-a/benchmark-v1.2.2/`

Candidates:

- General: `Qwen/Qwen2.5-7B-Instruct` @ `a09a35458c702b33eeacc393d103063234e8bc28`
- Math: `Qwen/Qwen2.5-Math-7B-Instruct` @ `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`
- Coder: `Qwen/Qwen2.5-Coder-7B-Instruct` @ `c03e6d358207e414f1eca0bb1891e29f1db0e242`

A5R1 human review:

`gates/gate-a-specialization/reviews/a5r1-v1.2.2-human-review.md`

## A5R2 — human approved

Reviewed commit:

`6168558b74fca06e1ef80f41b86cc997915c41b7`

Human review:

`gates/gate-a-specialization/reviews/a5r2-v1.2.2-human-review.md`

Decision: **APPROVED**. A6 was authorized.

Accepted capability matrix:

| Role | Overall | Math | Coding |
|---|---:|---:|---:|
| General baseline | 68/96 (70.83%) | 30/48 (62.50%) | 38/48 (79.17%) |
| Math specialist | 64/96 (66.67%) | 44/48 (91.67%) | 20/48 (41.67%) |
| Coder specialist | 69/96 (71.88%) | 36/48 (75.00%) | 33/48 (68.75%) |

All three models generated all 96 cases under the same frozen protocol in order General → Math → Coder, with no between-row result review. Four earlier failures stopped during General preflight before model load/output and remain preserved.

One non-blocking receipt issue is recorded: `load_elapsed_seconds` includes generation and is not a model-load-latency measurement. It does not affect scoring or comparability.

## A6 — complete

Evidence report:

`gates/gate-a-specialization/evidence-report.md`

Machine-readable summary:

`experiments/gate-a/a6-evidence-summary.yaml`

Recommendation: **PASS**.

The recommendation is based on the frozen acceptance criteria:

- minimum evidence satisfied;
- candidate comparability satisfied;
- Math specialist primary-domain improvement = **+29.17 pp**, paired-bootstrap 95% CI **[+16.67, +41.67] pp**;
- Math specialist non-primary coding change = **−37.50 pp**, CI **[−52.08, −22.92] pp**, demonstrating a concentrated specialization/tradeoff profile;
- Coder specialist does **not** demonstrate a coding advantage: **−10.42 pp**, CI **[−22.92, +2.08] pp**;
- no unresolved material methodological defect remains after A5R2 human review.

Therefore the frozen criteria support a **single-specialist PASS recommendation**. The strong preference for two specialists in different domains is **not satisfied**.

Architectural implication retained from Gate A: specialist identity should be empirically registered/validated, and a Dexinode skill should be treated closer to **checkpoint + explicit handoff contract/adapter**, rather than trusting checkpoint labels alone.

## Current bounded human action

The human owner must assign the final Gate A decision:

- PASS;
- FAIL; or
- INCONCLUSIVE.

A6 may recommend but cannot assign that final result.

If the human records **PASS**, the next repository action is to close Gate A, activate Gate B — Orchestration Advantage, and define Gate B's bounded hypothesis/acceptance protocol **before** running any orchestration experiment.

Do not activate Gate B until the final Gate A decision is explicitly recorded.

## More detail

- References and evidence map: `docs/handoff/references.md`
- Condensed research history: `docs/handoff/history.md`
- Live status: `status/current.md`
