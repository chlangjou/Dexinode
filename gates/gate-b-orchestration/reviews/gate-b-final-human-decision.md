# Gate B Final Human Decision

Date: 2026-08-10
Gate: Gate B — Orchestration Advantage
Final human decision: **FAIL**

## Decision

The human owner accepts the B5 evidence recommendation and assigns Gate B the final result **FAIL**.

Gate B is therefore closed for the current `gate-b-orchestration-v1.1.1` evidence set. No additional selected-model execution is authorized under Gate B v1.

## Basis at time of decision

The frozen and human-approved Gate B protocol completed comparable execution:

- General-only: 76/96 = 79.17% overall; Mathematics 40/48 = 83.33%; Coding 36/48 = 75.00%.
- Skill-routed: 77/96 = 80.21% overall; Mathematics 41/48 = 85.42%; Coding 36/48 = 75.00%.
- Routed minus General overall: +1.04 percentage points, paired-bootstrap 95% CI [0.00, +3.125] pp.
- Routed minus General Mathematics: +2.08 pp, 95% CI [0.00, +6.25] pp.
- Coding delta: 0.00 pp.
- Router accuracy: 96/96.

The frozen acceptance criteria required at least +10 pp overall and +10 pp Mathematics, with both improvement confidence intervals excluding zero. Those required signals were not met.

## Interpretation

Gate A remains valid: specialization can create strong capability divergence on a measured distribution. Gate B adds a distinct negative result: a broad capability registry entry such as `Mathematics -> Math specialist` did not generalize into a material orchestration advantage on the structurally fresh panel.

The current evidence therefore supports the following architectural constraint for Dexinode:

> A specialist checkpoint name or a broad domain label is not a sufficient routing contract. Capability registration needs finer task granularity and evidence of generalization across multiple structurally independent panels.

## Post-Gate research hypothesis

A plausible explanation for the Gate A / Gate B contrast, not established by Gate B itself, is that the General checkpoint may carry stronger cross-domain meta-capabilities such as natural-language task interpretation, specification grounding, ambiguity resolution, answer selection and self-checking. A specialist checkpoint may improve domain-specific representations or solution patterns while failing to match those general reasoning and review capabilities. On benchmark items that require both domain knowledge and robust interpretation/verification, those effects can offset each other.

This hypothesis should be treated as a future research question rather than as a concluded causal explanation.

## Post-closure addendum: Mathematics scoring/oracle retrospective

After the human FAIL decision, preserved raw outputs were inspected without rerunning any model. The resulting retrospective is:

`gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

It found:

- `math-23` frozen oracle `19/48` is incorrect; the exact posterior is `95/242 ~= 0.392562`. Both checkpoints independently computed approximately 0.392 but were rejected by the frozen exact-rational answer contract.
- `math-11`, `math-12`, and `math-17` were mathematically correct for both checkpoints but rejected because their final structured representation did not match the frozen parser.
- `math-41`, the sole frozen paired Mathematics improvement, was mathematically correct for both checkpoints: General returned `0.75`, Math specialist returned `3/4`; only the specialist representation was accepted by the frozen rational extractor.
- `math-16` and `math-32` are genuine arithmetic/self-check failures for both checkpoints.
- `math-36` is interpretation-sensitive (`fair trials`) and produced the same general symbolic answer from both checkpoints.

Under a human mathematical-content reading, the specialist's sole frozen +1 case disappears; the inspected paired content classifications are the same. Thus these post-closure findings do not rescue the failed +10 pp thresholds and, substantively, strengthen the conclusion that the broad Math route did not provide held-out content advantage.

### Protocol-purity caveat

The frozen acceptance document listed a benchmark oracle defect as an INCONCLUSIVE condition. The post-closure `math-23` discovery therefore creates a legitimate protocol-purity caveat and must not be hidden.

The final human Gate B label remains **FAIL** unless the human owner explicitly revises it, because the discovered defect is non-differential for the paired result and the retrospective content-level comparison moves the specialist advantage from +1 case to no content-level advantage rather than toward the PASS threshold.

## Future study dimensions

A suitable next study should separately score at least:

1. task/specification comprehension;
2. domain-method selection;
3. implementation or derivation correctness;
4. answer verification / self-review;
5. answer representation / handoff-contract compliance;
6. capability generalization across independent task families.

## Closure

Gate B status: **FAIL / CLOSED**, with the disclosed post-closure protocol-purity caveat above.

The next research gate has not yet been frozen. Define its bounded hypothesis and acceptance criteria before any new selected-model experiment.
