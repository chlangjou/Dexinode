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
5. `gates/gate-b-orchestration/evidence-report.md`
6. `gates/gate-b-orchestration/task.yaml`
7. `gates/gate-b-orchestration/acceptance.yaml`

Git is the durable source of truth.

## Current state

Gate A — Specialist Validation: **PASS / CLOSED**.

Gate B — Orchestration Advantage: **FAIL / CLOSED**.

Final Gate B decision:

`gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`

No new research gate is active. No additional Gate B selected-model execution is authorized.

## Gate B final evidence

Benchmark: `gate-b-orchestration-v1.1.1`

Execution: `gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`

Evidence root:

`experiments/gate-b/runs/gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0/`

Results:

- General-only: 76/96 = 79.17%; Math 40/48 = 83.33%; Coding 36/48 = 75.00%.
- Skill-routed: 77/96 = 80.21%; Math 41/48 = 85.42%; Coding 36/48 = 75.00%.
- overall delta: **+1.04 pp**, 95% CI **[0.00, +3.125] pp**;
- Math delta: **+2.08 pp**, 95% CI **[0.00, +6.25] pp**;
- Coding delta: **0.00 pp**;
- router accuracy: **100%**.

Only `math-41` changed from General incorrect to Math-specialist correct; the other 47 Math paired correctness outcomes were identical.

The execution is human-approved as valid comparable evidence. The frozen +10 pp overall and +10 pp Math thresholds were not met, and both improvement intervals include zero. No material methodology defect requires INCONCLUSIVE. Gate B is therefore final **FAIL**.

## Combined Gate A / Gate B interpretation

Gate A proved that specialization can exist strongly on a measured distribution. Gate B proved that the same broad specialist identity did not generalize into a material orchestration advantage on a structurally fresh panel.

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

This hypothesis is consistent with the earlier Coding retrospective, where many differential errors were implementation-contract, representation, edge-condition or language-semantic failures rather than absence of the underlying algorithm.

Treat this as a **research hypothesis**, not a causal conclusion from Gate B.

## Candidate next bounded research design

Before any new GPU/model run, design a gate that separates at least:

1. domain solution competence;
2. task/specification comprehension;
3. derivation or implementation reliability;
4. answer verification / self-review;
5. generalization across independent task families.

A later or parallel efficiency gate should test the economic Dexinode thesis directly: whether a substantially smaller specialist can retain near-General quality on a validated narrow skill while materially reducing VRAM, latency, energy or deployment cost.

## Next action

Research-design only. Freeze a new hypothesis, benchmark and acceptance criteria before any selected-model experiment.
