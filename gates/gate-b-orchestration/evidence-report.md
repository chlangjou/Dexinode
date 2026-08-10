# Gate B — Orchestration Advantage Evidence Report

Status: **B5 COMPLETE / GATE B CLOSED**

Recommendation: **FAIL**

Final human Gate B decision: **FAIL**

Final decision record: `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`

Post-closure retrospective: `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

Benchmark: `gate-b-orchestration-v1.1.1`

Execution: `gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`

## Bounded hypothesis

Gate B v1 asked whether a frozen evidence-based semantic-task router, using the Gate A empirical registry and exactly one logical model inference per task, could improve a structurally fresh 48-Math/48-Coding workload over General-only by at least 10 absolute percentage points overall with a paired-bootstrap 95% confidence interval excluding zero.

The routed policy used the validated Qwen2.5 Math checkpoint for frozen Mathematics routes and the General checkpoint for Coding/fallback. The Coder checkpoint was excluded because Gate A did not validate it as a Coding specialist.

## Frozen execution validity

The final v1.1.1 benchmark was human-approved before selected-model execution after structural-freshness, oracle, evaluator, and semantic-contract remediation. B3B4 persisted all 96 route decisions before output, executed General on all 96 cases, executed the Math specialist only on 48 frozen specialist routes, and delayed composition/scoring until both evidence phases completed. There was no between-phase result inspection, result-driven rerouting, retry, ensemble, Coder execution, or performance early stop.

The preserved failed attempt stopped in General preflight on a token-manifest field-name mismatch before formal inference and created no selected-model output.

## Frozen primary results

| Policy | Overall | Mathematics | Coding |
|---|---:|---:|---:|
| General-only | 76/96 = 79.17% | 40/48 = 83.33% | 36/48 = 75.00% |
| Skill-routed | 77/96 = 80.21% | 41/48 = 85.42% | 36/48 = 75.00% |

| Signal | Observed delta | 95% paired-bootstrap CI | Frozen requirement | Result |
|---|---:|---:|---:|---|
| Overall | +1.04 pp | [0.00, +3.125] pp | >= +10 pp and CI excludes 0 | **NOT MET** |
| Mathematics | +2.08 pp | [0.00, +6.25] pp | >= +10 pp and CI excludes 0 | **NOT MET** |
| Coding | 0.00 pp | [0.00, 0.00] pp | degradation <= 5 pp | **MET** |
| Router accuracy | 100% | n/a | >=95% | **MET** |

At frozen scoring time only `math-41` improved relative to General; no Math case regressed.

## Frozen acceptance outcome

Satisfied: minimum evidence, freshness/leakage controls, router information boundary, resource/execution parity, frozen execution sequence, router quality, and Coding protection.

Not satisfied: the +10 pp overall signal, overall CI excluding zero, +10 pp Mathematics signal, and Mathematics CI excluding zero.

The human owner accepted the B5 recommendation and assigned final **FAIL**.

## Post-closure Mathematics retrospective and errata

After closure, preserved raw responses were inspected without rerunning a model or altering frozen evidence.

### `math-23` oracle defect

The frozen Bayes posterior `19/48` is wrong. For prevalence 2%, sensitivity 95%, and false-positive rate 3%, the exact posterior is:

`(.02*.95) / ((.02*.95)+(.98*.03)) = 95/242 ~= 0.392562`.

Both General and Math specialist independently computed approximately 0.392, but the frozen exact-rational extractor rejected both decimal answers. Thus the oracle defect is real but **non-differential for the frozen paired score vector**.

### Common-mode answer-contract false negatives

Human mathematical-content inspection found both checkpoints correct on `math-11`, `math-12`, and `math-17`, while the structured-output parser rejected their final representations.

### Sole frozen Math improvement is representation-only

On `math-41`, General correctly computed `0.75` and Math specialist correctly computed `3/4`. The exact-rational extractor accepted only `3/4`. Therefore the sole +1/48 frozen specialist improvement is answer representation, not mathematical-content competence.

### Genuine shared verification failures

On `math-16` and `math-32`, both checkpoints selected an appropriate mathematical method and then made simple arithmetic aggregation errors. These are consistent with weak final verification/self-review rather than missing method knowledge.

### Interpretation-sensitive case

On `math-36`, both checkpoints returned the correct general geometric formula `(1-p)^3 p`. The prompt's phrase `fair trials` was intended to imply `p=1/2`, but that assumption was not stated explicitly.

### Content-level retrospective result

Under the human content classification of these cases, the specialist's sole frozen +1 Mathematics advantage disappears. The inspected paired mathematical-content classifications are the same for General and Math specialist.

This retrospective is diagnostic only; it does not replace the immutable frozen score files.

## Protocol-purity caveat

The frozen acceptance definition listed a benchmark oracle defect as an INCONCLUSIVE condition. The post-closure `math-23` defect therefore creates a legitimate literal-protocol caveat and is disclosed in the final decision and acceptance record.

However, the defect cannot rescue the specialist performance signal: it is common-mode, and the broader content retrospective reduces the specialist advantage from one frozen case to zero content-level cases. The final human decision remains **FAIL / CLOSED** unless explicitly revised.

## Interpretation for Dexinode

Gate B does not show that routing is harmful. It shows that the Gate A Math advantage did not transfer as a stable held-out content advantage under a coarse `Mathematics -> Math specialist` registry entry.

The combined Gate A/B evidence supports:

1. capability registries need generalization evidence across structurally independent panels;
2. skill granularity should be finer than broad domains;
3. routing should estimate expected utility by task subtype rather than domain identity alone;
4. end-to-end exact-answer accuracy should be decomposed into comprehension, method selection, derivation/computation, self-review, and handoff-contract compliance;
5. Gate A remains valid as evidence that specialization can exist, but not that the broad specialist label guarantees transferable advantage.

## Post-Gate causal hypothesis

A plausible explanation for the Gate A / Gate B contrast is that the General checkpoint may retain stronger cross-domain meta-capabilities such as language comprehension, specification grounding, ambiguity resolution, answer selection, and self-checking, while specialist training mainly improves domain solution patterns.

Current Gate B data does **not** prove that General is better at self-review: both checkpoints share arithmetic verification failures. This should be tested causally in a new bounded study that separately scores task comprehension, domain-method selection, derivation/computation, verification, and answer representation.

## Final decision

The human owner accepted FAIL on 2026-08-10.

**Final Gate B = FAIL / CLOSED, with the disclosed post-closure protocol-purity caveat.**

No additional Gate B selected-model execution is authorized for the current v1 evidence set. A new hypothesis, benchmark, and acceptance criteria must be frozen before any new selected-model experiment.
