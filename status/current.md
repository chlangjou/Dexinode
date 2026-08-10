# Current Research Status

- Updated: 2026-08-10
- Gate A — Specialist Validation: **PASS / CLOSED**
- Gate B — Orchestration Advantage: **FAIL / CLOSED**
- Gate B final decision record: `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
- Session handoff: `HANDOFF.md`
- No new research gate is active yet.

## Gate B final evidence

Executable benchmark: `gate-b-orchestration-v1.1.1`

Execution ID: `gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`

Evidence root:

`experiments/gate-b/runs/gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0/`

Human reviews:

- B1R2 benchmark: **APPROVED** — `gates/gate-b-orchestration/reviews/b1r2-v1.1.1-human-review.md`
- B2 static qualification: **PASS / COMPLETE** — `gates/gate-b-orchestration/reviews/b2-static-qualification.md`
- B3B4 execution: **APPROVED AS VALID COMPARABLE EXECUTION EVIDENCE** — `gates/gate-b-orchestration/reviews/b3b4-v1.1.1-human-review.md`
- B5 evidence report: recommendation **FAIL** — `gates/gate-b-orchestration/evidence-report.md`
- Final human decision: **FAIL** — `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`

## Results

| Policy | Overall | Mathematics | Coding |
|---|---:|---:|---:|
| General-only | 76/96 = 79.17% | 40/48 = 83.33% | 36/48 = 75.00% |
| Skill-routed | 77/96 = 80.21% | 41/48 = 85.42% | 36/48 = 75.00% |

Paired routed-minus-General:

- overall: **+1.04 pp**, paired-bootstrap 95% CI **[0.00, +3.125] pp**;
- Mathematics: **+2.08 pp**, CI **[0.00, +6.25] pp**;
- Coding: **0.00 pp**;
- router accuracy: **96/96 = 100%**.

Only `math-41` changed from General incorrect to Math-specialist correct. There were no reverse Math regressions; the other 47 paired Math correctness outcomes were unchanged.

## Why Gate B is FAIL

The execution was valid and comparable, with no material methodology defect requiring INCONCLUSIVE. However, the frozen acceptance criteria required at least +10 pp overall and +10 pp Mathematics, with both paired-bootstrap intervals excluding zero. Neither required performance signal was met.

The router itself was not the bottleneck: routing accuracy was 100%, and Coding protection was satisfied. The weak point was generalization of the measured specialist advantage onto a structurally fresh Math distribution.

## Architectural interpretation

Gate A and Gate B together imply:

1. specialization can create large capability divergence on a measured distribution;
2. a checkpoint label or broad domain such as `Mathematics` is not a sufficient skill identity;
3. capability registry entries should be finer-grained and carry evidence across multiple structurally independent panels;
4. routing should target expected utility for task subtypes, not assume that a broad specialist is uniformly superior within a domain.

## Post-Gate hypothesis: General meta-capabilities

A plausible but **not yet causally established** explanation for the Gate A / Gate B contrast is that the General checkpoint may retain stronger cross-domain meta-capabilities that become increasingly important on fresh or less templated tasks:

- natural-language task interpretation;
- specification grounding;
- ambiguity resolution;
- selecting the intended answer representation;
- self-checking / consistency review;
- deciding whether a familiar solution pattern actually matches the current problem.

Specialist training may improve domain-specific solution patterns or mathematical representations while not improving — and potentially partially trading off — these general comprehension and review capabilities. A task that requires both mathematical competence and robust interpretation/verification can therefore show much less specialist advantage than a benchmark concentrated on patterns aligned with the specialization distribution.

This hypothesis is consistent with the Coding postmortem as well: many differential failures were not missing algorithm knowledge but failures of input representation, language semantics, edge constraints, or final implementation correctness.

## Candidate next research question

Before any new selected-model experiment, define a bounded gate that separates at least:

- domain solution competence;
- task/specification comprehension;
- derivation or implementation reliability;
- answer verification / self-review;
- generalization across independent task families.

A later efficiency gate can then ask whether a much smaller specialist preserves enough quality relative to a stronger General/MoE model to justify Dexinode on VRAM, latency, energy, concurrency or deployment cost.

## Authorization

**Gate B v1 is closed. No additional Gate B selected-model execution is authorized.**

The next step is research-design work only until a new gate, benchmark and acceptance criteria are explicitly frozen.
