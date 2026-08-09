# Gate A — Specialist Validation Evidence Report

- Date: 2026-08-09
- Stage: A6 — Evidence Report
- Benchmark: `gate-a-cross-skill-v1.2.2`
- A5R2 reviewed commit: `6168558b74fca06e1ef80f41b86cc997915c41b7`
- A5R2 human review: `gates/gate-a-specialization/reviews/a5r2-v1.2.2-human-review.md`
- Recommendation: **PASS**
- Final Gate decision: **PENDING HUMAN REVIEW**
- Gate B activation: **NOT AUTHORIZED BY THIS REPORT**

## Question

Do existing specialist checkpoints from the same Qwen2.5 7B family exhibit reproducible, measurable skill specialization relative to the closely related general-purpose baseline under one frozen cross-skill protocol?

## Accepted capability matrix

| Model role | Overall | Mathematics | Software coding |
|---|---:|---:|---:|
| General baseline | 68/96 (70.83%) | 30/48 (62.50%) | 38/48 (79.17%) |
| Math specialist | 64/96 (66.67%) | 44/48 (91.67%) | 20/48 (41.67%) |
| Coder specialist | 69/96 (71.88%) | 36/48 (75.00%) | 33/48 (68.75%) |

Overall accuracy is descriptive only. Gate A is primarily concerned with domain-specific specialist advantage and specialization concentration.

## Frozen acceptance criteria check

### Minimum evidence — SATISFIED

The frozen minimum-evidence requirements are met:

- one general baseline;
- two specialist checkpoints;
- two skill domains;
- all three models evaluated on the same frozen 96-case benchmark;
- raw per-case outputs and scores preserved;
- reproducibility metadata preserved;
- failed/invalid preflight attempts preserved.

### Candidate comparability — SATISFIED

A2 previously human-approved the three checkpoints as sufficiently comparable in lineage, architecture, parameter scale, tokenizer assets, artifact identity, license/runtime availability, and prospective controls. A5R2 used the exact frozen revisions, common neutral Qwen role-delimiter template, BF16/no quantization, identical 4096-token envelope, deterministic generation policy, one L40 execution substrate, and the same deterministic semantic adapter/judge policy.

### Performance signal — SATISFIED FOR AT LEAST ONE SPECIALIST

The frozen performance requirement is an absolute improvement of at least 10 percentage points on the claimed primary domain, with the 95% bootstrap improvement interval excluding zero.

Using paired bootstrap resampling of the 48 frozen cases per domain, 20,000 resamples, percentile 95% intervals, seed 0:

| Comparison | Observed delta | 95% bootstrap interval | Criterion |
|---|---:|---:|---|
| Math specialist − General, Mathematics | **+29.17 pp** | **[+16.67, +41.67] pp** | **PASS** |
| Coder specialist − General, Coding | **−10.42 pp** | **[−22.92, +2.08] pp** | FAIL |

The Math specialist therefore independently satisfies the frozen primary-domain performance signal. The Coder specialist does not.

### Specialization signal — SATISFIED

The Math specialist shows a strongly concentrated domain-specific profile:

- Mathematics: **+29.17 pp** versus General, CI wholly above zero;
- Software coding: **−37.50 pp** versus General, 95% CI **[−52.08, −22.92] pp**.

This is not a uniformly stronger model. It is a materially different competency profile with a large gain in the checkpoint's claimed specialization and a large non-primary tradeoff. That directly satisfies the frozen specialization-signal requirement.

The Coder specialist does not provide a second clean specialization signal:

- Coding: −10.42 pp versus General, CI includes zero;
- Mathematics: +12.50 pp versus General, 95% CI [−2.08, +27.08] pp.

Its observed profile does not support the checkpoint label as a coding-specialist advantage on this benchmark. This does not negate the Math-specialist evidence required by the frozen Gate criterion, but it prevents the evidence from meeting the stated strong-pass preference for two specialists in different domains.

### Unresolved material methodological defect — NONE IDENTIFIED

A5R2 human review accepted the execution as comparable:

- General -> Math -> Coder ran in frozen order with no between-row result review;
- all three generated 96/96 responses with zero generation failures;
- benchmark, cases, prompt/template, adapter, scoring contract, candidate revisions, and acceptance criteria did not change after execution began;
- four failed attempts stopped in General preflight before model load/output and were preserved;
- accepted coding rows had zero judge infrastructure failures;
- one General and one Math coding case hit the frozen 2-second judge timeout and were scored as model-case failures according to the pre-existing policy;
- the post-execution scorer edit added only elapsed-time receipt metadata and all rows were deterministically rescored from preserved raw outputs without model reruns.

One non-blocking metadata defect remains: `load_elapsed_seconds` in the inference receipt includes generation time because its timer spans model load through completion of all 96 cases. It must not be interpreted as model-load latency. It does not affect capability scores or model comparability.

## Difficulty profile

The Math specialist's primary-domain improvement is not confined to a single difficulty band:

| Mathematics difficulty | General | Math specialist | Coder specialist |
|---|---:|---:|---:|
| Foundational | 7/10 (70.0%) | 8/10 (80.0%) | 8/10 (80.0%) |
| Intermediate | 16/24 (66.7%) | 23/24 (95.8%) | 20/24 (83.3%) |
| Advanced | 7/14 (50.0%) | 13/14 (92.9%) | 8/14 (57.1%) |

Coding shows the inverse tradeoff for the Math specialist and no primary-domain advantage for the Coder checkpoint:

| Coding difficulty | General | Math specialist | Coder specialist |
|---|---:|---:|---:|
| Foundational | 9/10 (90.0%) | 7/10 (70.0%) | 9/10 (90.0%) |
| Intermediate | 21/24 (87.5%) | 9/24 (37.5%) | 20/24 (83.3%) |
| Advanced | 8/14 (57.1%) | 4/14 (28.6%) | 4/14 (28.6%) |

This strengthens the interpretation that the Math checkpoint exhibits real domain specialization rather than a small cluster of easy-case wins.

## Interface behavior remains a separate finding

Strict output-interface compliance remains dramatically different across checkpoints even after semantic scoring is separated:

- General Math canonical contract: 19/48;
- Math specialist Math canonical contract: 0/48;
- Coder specialist Math canonical contract: 0/48;
- coding single-clean-source-block: 0/48 for all three.

This reinforces the earlier Gate A architectural lesson: a usable Dexinode skill should be modeled closer to **checkpoint + explicit handoff contract/adapter**, not checkpoint identity alone.

## Limitations

- The benchmark is self-authored and contamination absence cannot be established; common mathematical structures and coding algorithms may exist in pretraining data.
- Difficulty labels are authored labels, not externally calibrated psychometric difficulty.
- Only the Math specialist satisfies the frozen positive specialist performance signal. The two-specialist strong-pass preference is not met.
- The Coder checkpoint's lack of coding advantage demonstrates that published specialization labels should not be treated as routing truth without empirical skill registration/validation.
- Gate A establishes specialist competency differentiation; it does not establish that routing/orchestration improves system-level utility. That is the purpose of Gate B.

## Recommendation

Under `gates/gate-a-specialization/acceptance.yaml`, the evidence supports a **PASS recommendation** because:

1. minimum evidence is satisfied;
2. candidate comparability is satisfied;
3. the Math specialist exceeds General by 29.17 pp on its claimed primary domain, above the 10 pp threshold, with a 95% improvement interval excluding zero;
4. the Math specialist's advantage is clearly domain-specific and accompanied by a large non-primary tradeoff, satisfying specialization concentration;
5. no unresolved material methodological defect remains after A5R2 human review.

This is a **single-specialist PASS recommendation, not a strong two-specialist pass**. The strongest practical conclusion is that existing same-family checkpoints can indeed encode materially distinct skill profiles, but specialist identity must be measured rather than trusted by label.

The final Gate A decision remains **PENDING HUMAN REVIEW**. Only the human owner may declare Gate A PASS/FAIL/INCONCLUSIVE and authorize Gate B.