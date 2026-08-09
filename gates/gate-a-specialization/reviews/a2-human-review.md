# Gate A — A2 Human Review

- Date: 2026-08-09
- Stage reviewed: A2 — Candidate Eligibility
- Decision: APPROVED
- Selected candidate set: `qwen2.5-7b-instruct-math-coder`
- Next active stage: A3 — Benchmark Construction and Freeze

## Approved controls

1. Keep the selected model set unchanged:
   - `Qwen/Qwen2.5-7B-Instruct`
   - `Qwen/Qwen2.5-Math-7B-Instruct`
   - `Qwen/Qwen2.5-Coder-7B-Instruct`
2. Use a common total context envelope of 4096 tokens. A3 must enforce `rendered_input_tokens + max_new_tokens <= 4096` for every case.
3. Freeze one neutral Qwen role-delimiter chat template for all three models, with identical semantic system/user content. Do not use the Math checkpoint's additional default boxed-answer/system instruction as a benchmark advantage.
4. Use official BF16 checkpoints with no quantization for the initial policy.
5. CPU-only execution is not a permanent Gate constraint. Before A4, the execution host may be changed by human approval provided all compared models use the same execution environment and inference policy and the change is recorded before results are observed.
6. External tools are disabled for Gate A comparative inference unless a later human decision explicitly changes that policy before benchmark execution.

## Interpretation

A2 established sufficient lineage, architecture, parameter-scale, tokenizer, license, artifact identity, and runtime comparability to proceed. The Math checkpoint's shorter context window and chat-template difference are material confounders, but both can be controlled prospectively in A3.

This approval does not approve any benchmark cases or scoring rules. A3 must define and freeze those before any model is executed.

Gate decision remains: PENDING HUMAN REVIEW.
