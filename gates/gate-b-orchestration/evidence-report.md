# Gate B — Orchestration Advantage Evidence Report

Status: **B5 COMPLETE / GATE B CLOSED**

Recommendation: **FAIL**

Final human Gate B decision: **FAIL**

Final decision record: `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`

Benchmark: `gate-b-orchestration-v1.1.1`

Execution: `gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`

B3B4 human review: `gates/gate-b-orchestration/reviews/b3b4-v1.1.1-human-review.md`

## Bounded hypothesis

Gate B v1 asked whether a frozen evidence-based semantic-task router, using the Gate A empirical registry and exactly one logical model inference per task, could improve a structurally fresh 48-Math/48-Coding workload over General-only by at least 10 absolute percentage points overall with a paired-bootstrap 95% confidence interval excluding zero.

The routed policy used the validated Qwen2.5 Math checkpoint for frozen Mathematics routes and the General checkpoint for Coding/fallback. The Coder checkpoint was excluded because Gate A did not validate it as a Coding specialist.

## Evidence validity

The final v1.1.1 benchmark was human-approved before selected-model execution after structural-freshness, oracle, evaluator, and semantic-contract remediation. The B3B4 execution then preserved all 96 route decisions before output, executed General on all 96 cases, executed the Math specialist only on the 48 frozen specialist routes, and delayed composition/scoring until both evidence phases were complete. There was no between-phase result inspection, result-driven rerouting, retry, ensemble, Coder execution, or performance early stop.

The preflight-only failed attempt stopped on a runner token-manifest field-name mismatch before formal inference and created no selected-model output. It is preserved as invalid/preflight history and does not contaminate the successful run.

Therefore the Gate B v1 result is interpretable as a valid test of the frozen bounded hypothesis rather than an inconclusive methodology failure.

## Primary results

| Policy | Overall | Mathematics | Coding |
|---|---:|---:|---:|
| General-only | 76/96 = 79.17% | 40/48 = 83.33% | 36/48 = 75.00% |
| Skill-routed | 77/96 = 80.21% | 41/48 = 85.42% | 36/48 = 75.00% |

Paired routed-minus-General results:

| Signal | Observed delta | 95% paired-bootstrap CI | Frozen requirement | Result |
|---|---:|---:|---:|---|
| Overall | +1.04 pp | [0.00, +3.125] pp | >= +10 pp and CI excludes 0 | **NOT MET** |
| Mathematics | +2.08 pp | [0.00, +6.25] pp | >= +10 pp and CI excludes 0 | **NOT MET** |
| Coding | 0.00 pp | [0.00, 0.00] pp | degradation <= 5 pp | **MET** |
| Router accuracy | 100% | n/a | >=95% | **MET** |

Only one routed Math case improved relative to General (`math-41`); no Math case regressed. The other 47 Math paired correctness outcomes were unchanged.

## Frozen acceptance criteria

- minimum evidence: **SATISFIED**;
- freshness and leakage controls: **SATISFIED**;
- router information boundary: **SATISFIED**;
- resource/execution parity: **SATISFIED**;
- execution freeze: **SATISFIED**;
- router quality: **SATISFIED**;
- non-target Coding protection: **SATISFIED**;
- primary overall orchestration signal: **NOT SATISFIED**;
- validated Mathematics skill signal on the fresh Gate B distribution: **NOT SATISFIED**;
- unresolved material methodological defect: **NONE IDENTIFIED**.

The acceptance definition specifies FAIL when a valid fresh benchmark exists, both policies complete comparably, and the predefined primary orchestration threshold is not met. Those conditions are satisfied here. The evidence supports **FAIL**, not INCONCLUSIVE.

## Interpretation

Gate B does **not** show that routing is harmful: the point estimate is positive and there were no routed regressions. It shows that the validated Gate A Math advantage did **not generalize strongly enough** to this structurally fresh Math distribution to create the required system-level benefit.

This is particularly informative because routing accuracy was 100%. The bottleneck was not router classification. It was the capability profile: on Gate B Math, General reached 83.33% and the Math specialist reached 85.42%, only one case apart.

For comparison, Gate A had shown a much larger Math separation between the same checkpoints. Gate B therefore narrows the architectural conclusion: a coarse registry entry such as `Mathematics -> Math specialist` is not sufficiently stable evidence of transferable advantage. Capability identity should be conditioned on narrower task families and demonstrated across structurally independent held-out panels.

Because the workload is exactly 50% Math and Coding is routed to the identical General output, the overall delta is mathematically one half of the Math delta. Thus the frozen +10 pp overall requirement effectively required approximately +20 pp Math improvement under this workload. Gate A made that target plausible; Gate B showed that the advantage did not persist on the fresh panel.

## Architectural implications for Dexinode

1. **Capability registries need generalization evidence, not one benchmark score.** A specialist should register a capability only after demonstrating repeatable advantage across multiple structurally independent panels or task families.
2. **Skill granularity should be finer than broad domains.** `mathematics` and `coding` are likely too coarse.
3. **Routing should eventually estimate expected utility, not merely domain identity.** A perfect Math/Coding classifier cannot help when the selected specialist is only marginally better on the actual task distribution.
4. **Gate A remains valid but narrower.** It established that specialization can exist in same-size checkpoints; Gate B shows that the observed advantage can be distribution-sensitive.
5. **The broader Dexinode thesis is not rejected.** This Gate rejects the specific v1 hypothesis that this coarse two-domain registry and these same-size Qwen2.5 checkpoints deliver >=10 pp mixed-workload advantage on a fresh panel.

## Post-Gate causal hypothesis to test

A plausible explanation for the Gate A / Gate B contrast is that the General checkpoint may retain stronger cross-domain meta-capabilities such as task-language comprehension, specification grounding, ambiguity resolution, answer selection and self-checking. Specialist training may improve domain-specific solution competence without matching those general interpretation and review capabilities. On tasks requiring both, the two effects can offset each other.

Gate B does **not** establish that causal mechanism; it is a research hypothesis for a future bounded study. The next design should separate domain solution competence from comprehension/grounding, derivation reliability, and verification/self-review.

## Final decision

The human owner accepted the evidence recommendation on 2026-08-10.

**Final Gate B = FAIL / CLOSED.**

No additional Gate B selected-model execution is authorized for the current v1 evidence set. A new benchmark and acceptance criteria must be frozen before any new selected-model experiment.
