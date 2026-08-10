# Dexinode Session Handoff

Repository: `chlangjou/Dexinode`
Canonical/default branch: `main`
Snapshot date: 2026-08-10

## Start here

Read, in order:

1. `AGENTS.md`
2. this file
3. `status/current.md`
4. `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
5. `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`
6. `gates/gate-b-orchestration/evidence-report.md`
7. `gates/gate-b-orchestration/task.yaml`
8. `gates/gate-b-orchestration/acceptance.yaml`

Git is the durable source of truth.

## Current state

Gate A — Specialist Validation: **PASS / CLOSED**.

Gate B — Orchestration Advantage: **FAIL / CLOSED**.

Final Gate B decision:

`gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`

Post-closure retrospective / errata:

`gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

No new research gate is active. No additional Gate B selected-model execution is authorized.

## Gate B frozen evidence

Benchmark: `gate-b-orchestration-v1.1.1`

Execution: `gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`

Evidence root:

`experiments/gate-b/runs/gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0/`

Frozen scores:

- General-only: 76/96 = 79.17%; Math 40/48 = 83.33%; Coding 36/48 = 75.00%.
- Skill-routed: 77/96 = 80.21%; Math 41/48 = 85.42%; Coding 36/48 = 75.00%.
- overall delta: **+1.04 pp**, 95% CI **[0.00, +3.125] pp**;
- Math delta: **+2.08 pp**, 95% CI **[0.00, +6.25] pp**;
- Coding delta: **0.00 pp**;
- router accuracy: **100%**.

The frozen +10 pp overall and +10 pp Math thresholds were not met. The human owner assigned final **FAIL**.

## Post-closure Mathematics retrospective

After closure, inspection of preserved raw outputs found benchmark/scoring issues that are important to future methodology but do not improve the routed-vs-General paired signal:

- `math-23` frozen oracle `19/48` is wrong; exact posterior is **95/242 ~= 0.392562**. Both models independently calculated approximately 0.392 but the frozen rational extractor rejected both decimal-form answers.
- `math-11`, `math-12`, and `math-17` were mathematically correct for both models but rejected because final structured representations did not satisfy the frozen parser.
- `math-41`, the **only** frozen paired Math improvement, was mathematically correct for both models: General returned `0.75`, Math specialist returned `3/4`; only the exact rational representation was accepted.
- `math-16` and `math-32` are genuine shared arithmetic/self-check failures after both models selected an appropriate method.
- `math-36` uses interpretation-sensitive wording (`fair trials`) and both models returned the same general `(1-p)^3 p` form instead of assuming `p=1/2`.

Under a human mathematical-content reading of these cases, the observed specialist Math advantage collapses rather than grows: the checkpoints have the same content-level correctness classification across the inspected Gate B Math panel.

Protocol-purity caveat: the frozen acceptance document listed a benchmark oracle defect as an INCONCLUSIVE condition. The post-closure `math-23` defect therefore deserves explicit disclosure. It is nevertheless non-differential for the paired conclusion and cannot rescue the failed +10 pp thresholds; the final human Gate B label remains FAIL unless the human owner explicitly revises it.

## Combined Gate A / Gate B interpretation

Gate A proved that specialization can exist strongly on a measured distribution. Gate B showed that the same broad specialist identity did not generalize into a material orchestration advantage on a structurally fresh panel.

Do not register a skill solely as a checkpoint label or broad domain such as `Mathematics` or `Coding`. Future capability registry entries should become finer-grained and include evidence across multiple structurally independent panels.

## Post-Gate hypothesis to investigate

A plausible but unproven explanation for the Gate A / Gate B contrast is that the General model retains stronger cross-domain meta-capabilities such as:

- natural-language comprehension;
- specification grounding;
- ambiguity resolution;
- answer-format/intention selection;
- self-checking and consistency review;
- recognizing when a familiar domain pattern does not actually fit the present task.

Specialist training may increase domain solution competence without preserving the same level of comprehension/review capability. Tasks requiring both could therefore erase much of the apparent specialist advantage.

Current Gate B raw evidence does **not** yet prove General is better at review: both checkpoints share arithmetic verification failures, and many frozen zero scores are common-mode answer-contract effects. Treat this as a research hypothesis, not a causal conclusion.

## Candidate next bounded research design

Before any new GPU/model run, design a gate that separates at least:

1. task/specification comprehension;
2. domain-method selection;
3. derivation/computation or implementation correctness;
4. final verification/self-review;
5. answer representation / handoff-contract compliance;
6. generalization across independent task families.

A later or parallel efficiency gate should test the economic Dexinode thesis directly: whether a substantially smaller specialist can retain near-General quality on a validated narrow skill while materially reducing VRAM, latency, energy or deployment cost.

## Next action

Research-design only. Freeze a new hypothesis, benchmark and acceptance criteria before any selected-model experiment.
