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
6. `gates/gate-b-orchestration/reviews/b3b4-v1.1.1-human-review.md`
7. `gates/gate-b-orchestration/evidence-report.md`

Git is the durable source of truth.

## Current state

Gate A — Specialist Validation: **PASS / CLOSED**.

Gate B — Orchestration Advantage: **B5 COMPLETE / FINAL HUMAN DECISION PENDING**.

Repository recommendation: **FAIL**.

No additional Gate B selected-model execution is required or authorized for the current v1 evidence set.

## Gate B final evidence

Benchmark:

`gate-b-orchestration-v1.1.1`

Execution:

`gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`

Evidence root:

`experiments/gate-b/runs/gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0/`

B3B4 human review:

`gates/gate-b-orchestration/reviews/b3b4-v1.1.1-human-review.md`

B5 report:

`gates/gate-b-orchestration/evidence-report.md`

## Result

General-only:

- overall 76/96 = 79.17%;
- Math 40/48 = 83.33%;
- Coding 36/48 = 75.00%.

Skill-routed:

- overall 77/96 = 80.21%;
- Math 41/48 = 85.42%;
- Coding 36/48 = 75.00%.

Paired deltas:

- overall **+1.04 pp**, 95% CI **[0.00, +3.125] pp**;
- Math **+2.08 pp**, 95% CI **[0.00, +6.25] pp**;
- Coding **0.00 pp**;
- router accuracy **100%**.

Only `math-41` changed from General incorrect to Math-specialist correct. There were no reverse Math regressions.

## Why recommendation is FAIL rather than INCONCLUSIVE

The execution is valid and comparable:

- route decisions frozen before output;
- General 96/96 and Math specialist 48/48 generated with zero failures;
- no between-phase result inspection;
- no Coder execution;
- no result-driven retry/rerouting or post-output protocol change;
- Coding judge had zero infrastructure failures/timeouts;
- the preserved failed attempt stopped in General preflight on a token-manifest field-name bug before formal inference and created no model output.

The frozen thresholds required at least +10 pp overall and +10 pp Math, with both paired-bootstrap intervals excluding zero. Neither performance signal was met. Router quality and Coding protection were met. No material methodology defect remains.

Therefore the predefined FAIL conditions are satisfied: valid fresh benchmark, comparable completed policies, predefined primary threshold not met.

## Main interpretation

Gate A proved specialization can exist, but Gate B shows that the observed Math advantage was strongly distribution-sensitive. Perfect coarse Math/Coding routing did not create a material system advantage because on the fresh panel the General model scored 40/48 Math and the Math specialist 41/48.

For Dexinode, capability registry entries should therefore become finer-grained and should carry generalization evidence across multiple structurally independent panels. Future routing should target expected utility by task subtype rather than assume a broad `Mathematics -> specialist` mapping.

## Next human action

Choose the final Gate B label: **PASS / FAIL / INCONCLUSIVE**.

The repository evidence recommendation is **FAIL**. If FAIL is accepted, record the human decision, close Gate B, and define the next bounded research question before any new experiment. A strong candidate is capability granularity/generalization, potentially followed by or combined with small-specialist efficiency testing.
