# Gate A Cross-Skill Benchmark v1.2.2

This is the narrow oracle-correction and complete-static-validation revision
of `gate-a-cross-skill-v1.2.1`. The v1.2.0 and v1.2.1 benchmarks remain frozen
and unchanged as audit artifacts; this directory is a new version and the
future Gate A measurement target after human review.

The benchmark contains 96 cases in frozen order: 48 mathematics cases followed
by the accepted software-coding set copied unchanged. Mathematics has 10
foundational, 24 intermediate, and 14 advanced cases. The structurally fresh
v1.2.1 Math constructions and frozen order are carried forward unchanged.
The machine-readable/manual review is preserved in `freshness-audit.yaml`.

## Reused v1.2.0 components

The accepted v1.2 semantic adapter, deterministic semantic scoring contract,
secondary strict-interface metrics, neutral Qwen role-delimiter template,
pinned tokenizer policy, selected candidates and revisions, BF16/no-quantization
controls, 1024-token generation budget, 4096-token context envelope,
deterministic generation settings, and judge-v2 coding policy are reused. No
adapter or scoring behavior changed. Only the two required v1.2.1 Math oracle
values and the additional reduced-fraction correction for math-37 changed;
version identifiers and benchmark metadata were refreshed where needed.

The coding case file is byte-identical to both v1.2.0 and v1.2.1. The adapter
implementation and its 13 synthetic tests are reused without behavioral
changes. Complete Math oracle validation is recorded in
`oracle-validation.yaml` and passes 48/48.

## Provenance and contamination

The remediation design was informed by the observed v1.1 interface confounder.
No selected-model raw response is used as an adapter fixture; no expected value
is used to choose a generated candidate; no v1.2.2 case, oracle, or difficulty
label is selected or tuned using selected-model performance on that case; and
no selected model is executed during v1.2.2 construction.

The cases are self-authored and no external dataset or public answer key was
copied. Absence of contamination is not claimed: common mathematical
structures and standard algorithms can occur in pretraining or educational
material. Difficulty labels are author labels, not model-calibrated results.

## Validation state

All 96 rendered inputs use the pinned byte-identical Qwen2 tokenizer and
satisfy `rendered_input_tokens + 1024 <= 4096`; the maximum input is 187 tokens,
the maximum total is 1211, and the remaining context margin is 2885 tokens.
Synthetic adapter validation passes 13/13. Raw model outputs and benchmark
results are absent by construction. Gate acceptance thresholds remain
unchanged. This benchmark is frozen pending human review; A5R2 and A6 remain
inactive.

Gate decision: PENDING HUMAN REVIEW.
