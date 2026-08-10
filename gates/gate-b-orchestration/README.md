# Gate B — Orchestration Advantage

Gate B asks whether an evidence-based skill router can convert the specialization demonstrated in Gate A into a measurable system-level advantage over a single general model **without increasing model calls per task**.

Gate A final decision: **PASS**.

Gate B is intentionally narrower than full multi-agent collaboration. It does not yet test long chains, recursive delegation, reputation, networking, economic settlement, or distributed execution. Those remain future questions.

## Bounded hypothesis

> On a fresh mixed mathematics/software-coding benchmark, a frozen deterministic router that sees only the task prompt and an empirically validated skill registry can outperform a General-only policy by routing mathematics tasks to the validated Math specialist and coding tasks to General, while using exactly one model inference per task and the same generation budget.

This is a first proof of **skill-aware model selection**, not yet a proof of arbitrary agent collaboration.

## Why the Coder checkpoint is not a routed specialist

Gate A did not validate `Qwen/Qwen2.5-Coder-7B-Instruct` as a coding advantage on the frozen benchmark. Gate B therefore must not trust the checkpoint name and route coding tasks to it merely because it is labeled Coder.

The initial empirical registry is:

- mathematics → `Qwen/Qwen2.5-Math-7B-Instruct`;
- software coding → `Qwen/Qwen2.5-7B-Instruct`;
- unknown/unsupported → General fallback.

This registry may use Gate A's human-approved aggregate capability profile, but Gate B case selection and routing rules must not use Gate A per-case raw outputs or case-specific win/loss patterns.

## Comparison

Primary policies:

1. **General-only baseline** — every fresh Gate B task is sent to the frozen General checkpoint.
2. **Skill-routed policy** — a CPU-only deterministic router selects exactly one registered checkpoint from the task prompt; no LLM router, fallback generation, retries, ensemble, voting, or second model call is allowed.

Both policies receive the same fresh cases and identical model inference controls.

## Fresh benchmark requirement

Gate B must create a new benchmark before any Gate B selected-model execution:

- 96 total tasks;
- 48 mathematics and 48 software-coding tasks;
- frozen order and difficulty labels;
- no exact Gate A prompt reuse;
- no case selected or tuned from selected-model performance;
- durable oracle/evaluator validation;
- router sees prompt text only, never hidden domain labels, expected answers, evaluator tests, or case metadata.

Broad skill families may remain comparable to Gate A, but cases must be new instances rather than case-specific remixes chosen from Gate A successes/failures.

## Resource parity

For the primary policy comparison:

- exactly one model inference per task;
- same total context envelope and `max_new_tokens`;
- BF16, no quantization;
- deterministic generation;
- same execution substrate class;
- external tools disabled;
- CPU-only deterministic routing overhead recorded separately;
- no model-call fallback or result-driven rerouting.

This isolates the value of **selecting the right existing skill** rather than buying accuracy with extra inference calls.

## Current stage

**B1R2 — complete pending human review.**

The corrected frozen design is recorded under
`experiments/gate-b/benchmark-v1.1.1/` and reuses unchanged `router-v2`.
The prior v1.0.0/v1.1.0 artifacts remain preserved and unchanged. Static
validation is complete, but no Gate B model execution is authorized until the
human reviews and approves B1R2. B2 remains inactive.
