# Gate B Orchestration Benchmark v1.0.0

Status: **frozen pending human review**. No Gate B selected checkpoint was
executed during construction.

This B1 artifact tests the bounded question of skill-aware model selection:
whether a deterministic prompt-only router can send Math tasks to the
human-validated Math specialist and Coding tasks to General, improving over a
General-only policy while making exactly one model inference per task. It does
not test recursive delegation, multi-step collaboration, networking,
federation, reputation, settlement, or training.

## Benchmark

The benchmark has 96 self-authored cases in frozen order: 48 Math followed by
48 software-coding cases. Each domain has 10 foundational, 24 intermediate,
and 14 advanced cases. Prompts are exact-string disjoint from Gate A v1.1.0,
v1.2.0, v1.2.1, and v1.2.2 prompts. Broad skill families remain comparable,
but no Gate A per-case output or win/loss was used to select or tune a case.

All Math oracles pass independent exact validation in `oracle-validation.yaml`.
The validation found and corrected one pre-freeze authoring error in `math-27`
(the divisor count of 360 is 24). All Coding evaluator fixtures pass an
independent standard-library reference harness: 48/48 cases and 121/121
tests.

## Router and policies

`../router-v1/router.py` accepts only one task-prompt string and returns one
registered route. It performs deterministic CPU-only lexical classification;
unsupported or ambiguous prompts use General fallback. It has no I/O and no
access to hidden labels, expected answers, evaluator tests, model outputs, or
benchmark metadata. Synthetic and benchmark-wide router tests pass 6/6 and
96/96 respectively.

The General-only policy sends every task to `Qwen/Qwen2.5-7B-Instruct`. The
skill-routed policy sends Math to `Qwen/Qwen2.5-Math-7B-Instruct`, Coding to
General, and fallback to General. Both policies use exactly one call per case,
the same frozen prompts, controls, model revisions, context envelope, and
generation budget. The Coder checkpoint is not treated as a validated coding
route because Gate A did not establish a coding advantage.

The semantic adapter is byte-identical to the accepted Gate A v1.2.2 adapter;
strict interface compliance is secondary to semantic scoring. No LLM judge is
used. Later source execution remains exclusively inside approved judge-v2.

## Controls and validation

The neutral Qwen role-delimiter template, BF16/no quantization, deterministic
generation settings, 4096-token context envelope, `max_new_tokens=1024`,
external-tools-disabled policy, pinned tokenizer, and approved execution
substrate are recorded in `template.yaml`, `protocol.yaml`, and `manifest.yaml`.

The maximum rendered input is 188 tokens; with the generation allowance it is
1212, leaving 2884 tokens of context margin. Exact counts are in
`token_counts.yaml`. Gate B selected-model execution remains unauthorized until
human review freezes this B1 design.

Gate decision: **PENDING HUMAN REVIEW**.
