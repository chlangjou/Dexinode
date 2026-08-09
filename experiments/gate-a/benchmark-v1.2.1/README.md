# Gate A Cross-Skill Benchmark v1.2.1

This is the structural-freshness revision of
`gate-a-cross-skill-v1.2.0`. The v1.2.0 benchmark remains frozen and unchanged
under `experiments/gate-a/benchmark-v1.2.0/`; this directory is a new version.

The benchmark contains 96 cases in frozen order: 48 mathematics cases followed
by the accepted v1.2.0 software-coding set copied unchanged. Mathematics has
10 foundational, 24 intermediate, and 14 advanced cases. The replacement Math
cases use changed constructions and compositions rather than coefficient or
constant substitutions or one-to-one positional mirroring of v1.1. The
machine-readable/manual review is in `freshness-audit.yaml`.

## Reused v1.2.0 components

The v1.2.0 semantic adapter, deterministic semantic scoring contract,
secondary strict-interface metrics, neutral Qwen role-delimiter template,
pinned tokenizer policy, selected candidates and revisions, BF16/no-quantization
controls, 1024-token generation budget, 4096-token context envelope,
deterministic generation settings, and judge-v2 coding policy are reused. No
genuine implementation bug was found. Only version identifiers and benchmark
metadata were changed where needed.

The coding case file is byte-identical to v1.2.0. The adapter implementation
and its 13 synthetic tests are reused without behavioral changes. No selected
model is executed during this revision.

## Provenance and contamination

The remediation design was informed by the observed v1.1 interface confounder.
No selected-model raw response is used as an adapter fixture; no expected value
is used to choose a generated candidate; and no v1.2.1 case, oracle, or
difficulty label is selected or tuned using selected-model performance on that
case. No selected model is executed during v1.2.1 construction.

The cases are self-authored and no external dataset or public answer key was
copied. Absence of contamination is not claimed: common mathematical
structures and standard algorithms can occur in pretraining or educational
material. Difficulty labels are author labels, not model-calibrated results.

## Validation state

All 96 rendered inputs use the pinned byte-identical Qwen2 tokenizer and must
satisfy `rendered_input_tokens + 1024 <= 4096`. Raw model outputs and benchmark
results are absent by construction. Gate acceptance thresholds remain
unchanged. This benchmark is frozen pending human review; A5R2 and A6 remain
inactive.

Gate decision: PENDING HUMAN REVIEW.
