# Gate A — A5 v1.1 Interface-Confounder Human Review

- Date: 2026-08-09
- Reviewed commit: `c95da721f0e55e0bda1c55f3dee9f4c95c814034`
- Stage: A5 — Specialist Cross-Evaluation
- Benchmark: `gate-a-cross-skill-v1.1.0`
- Decision: **CAPABILITY CONCLUSION NOT ACCEPTED — INTERFACE CONFOUNDER CONFIRMED**
- Gate A decision: **PENDING**
- A6 authorization: **NO**

## What remains valid evidence

The v1.1 execution records are reproducible strict-interface observations and must remain preserved.

- General: mathematics 10/48, coding 36/48.
- Math specialist: mathematics 0/48, coding 0/48 under the frozen strict output/scoring contract.
- Coder specialist: mathematics 12/48, coding 39/48.
- All three used the intended comparable model/runtime/GPU/generation controls.
- No infrastructure-invalid case explains the Math-specialist zero row.

These numbers describe performance under the exact v1.1 wire/output contract. They are not all accepted as measurements of underlying task competence.

## Confirmed confounder

The Math specialist is not behaviorally equivalent to the General/Coder models at the output interface.

The v1.1 mathematics scorer requires exactly one `ANSWER:` line. In the Math-specialist run, the mathematics records are rejected for `answer_marker_count_not_one`, while raw responses frequently contain correct worked solutions ending in conventional boxed mathematics. Examples reviewed before this decision include:

- `math-01`: derives `x = 6` and ends with `\\boxed{6}`; frozen expected value is 6.
- `math-02`: derives 28 and ends with `\\boxed{28}`; frozen expected value is 28.
- `math-03`: derives 56 and ends with `\\boxed{56}`; frozen expected value is 56.
- `math-04`: derives -40 and ends with `\\boxed{-40}`; frozen expected value is -40.
- `math-05`: derives 24 and ends with `\\boxed{24}`; frozen expected value is 24.

Thus a score of 0 on these cases is caused by output-contract noncompliance, not by lack of mathematical competence.

The coding side shows the same morphology. For example, `code-01` contains a plausible `stable_unique` implementation but also explanation/example blocks, so the strict v1.1 extractor rejects it as `multiple_code_blocks`. Other Math-specialist coding responses similarly contain working-looking source surrounded by additional prose/examples.

## Why the v1.1 capability matrix is not acceptable

Gate A asks whether specialist checkpoints exhibit differentiated skill competence relative to a related General baseline. The v1.1 scoring contract unintentionally conflates two variables:

1. task competence;
2. compliance with a narrow common wire/output format.

A2 already identified the Math checkpoint's chat-template / boxed-answer behavior as a material confounder and prospectively attempted to control it with a common neutral role-delimiter template. A5 now demonstrates that the common template alone did not remove the behavioral interface difference.

Therefore the Math-specialist 0/96 row cannot be used as a capability measurement, and the complete v1.1 three-row matrix cannot support Gate A PASS/FAIL/INCONCLUSIVE yet.

## Prohibited remediation

Do not patch v1.1 scoring in place and do not rescore only the Math specialist with a relaxed rule. That would be result-dependent treatment after observing candidate outputs.

Do not switch only the Math specialist to its repository-default chat template.

Do not change Gate acceptance thresholds.

## Approved remediation direction

Create a new benchmark/protocol version `gate-a-cross-skill-v1.2.0` before any further candidate execution.

The v1.2 design must:

- use fresh self-authored case instances rather than reusing the observed v1.1 prompts;
- retain 48 mathematics + 48 software-coding cases and the same 10/24/14 difficulty distribution per domain;
- retain the same selected model set, revisions, BF16/no-quantization policy, common 4096-token envelope, neutral role-delimiter chat envelope, GPU/runtime policy, and Gate acceptance criteria;
- separate semantic task scoring from strict interface-compliance reporting;
- define one common, model-agnostic tolerant output contract for all three models;
- define deterministic normalization/extraction before any model is run;
- validate the normalizer only against synthetic fixtures during construction;
- freeze v1.2 in Git and stop for human review before executing General, Math, or Coder.

After v1.2 human approval, all three selected models must be executed again on the complete fresh v1.2 benchmark under one frozen protocol. No v1.1 model score may be substituted into the v1.2 capability matrix.

## Interpretation for Dexinode

This is itself useful project evidence: specialist checkpoints may expose different native behavioral interfaces even within the same family/tokenizer lineage. A practical skill network therefore needs an explicit handoff/normalization contract rather than assuming one narrow output surface is neutral for every specialist.

This observation is architectural evidence, not a Gate A specialization PASS.
