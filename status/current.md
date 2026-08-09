# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A3 — Benchmark Construction and Freeze

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

The immediate purpose is to establish whether distinct competency surfaces exist strongly enough to justify a later orchestration/routing experiment.

## Current assumptions

- Prefer the same model family and generation.
- Prefer similar parameter scale and compatible inference architecture.
- Use existing published checkpoints only during Gate A.
- Do not fine-tune or create specialist models during Gate A.
- Do not test multi-agent orchestration during Gate A.
- Capability claims are not evidence; candidates must eventually be cross-evaluated on a frozen benchmark.

## Human decision: A2 approved

A2 — Candidate Eligibility is APPROVED.

Selected candidate set remains:

- `Qwen/Qwen2.5-7B-Instruct`
- `Qwen/Qwen2.5-Math-7B-Instruct`
- `Qwen/Qwen2.5-Coder-7B-Instruct`

The durable review record is `gates/gate-a-specialization/reviews/a2-human-review.md`.

Approved controls for A3:

- enforce `rendered_input_tokens + max_new_tokens <= 4096` for every benchmark case;
- freeze one neutral Qwen role-delimiter chat template with identical semantic system/user content for all three models;
- use official BF16 checkpoints with no quantization for the initial inference policy;
- keep external tools disabled for Gate A comparative inference;
- CPU-only execution is not a permanent Gate constraint. A different execution host may be approved before A4 provided all compared models use the same environment/policy and the change is recorded before results are observed.

A2 verified exact revisions, common 7,615,616,512-parameter scale, shared Qwen2ForCausalLM architecture and Qwen2.5-7B foundation, byte-identical tokenizer assets, Apache-2.0 licensing, artifact identity, and the material Math context/chat-template confounders.

## Active bounded task: A3 — Benchmark Construction and Freeze

Construct and freeze a cross-skill benchmark that fairly measures the approved mathematics and software-coding specialization axes.

A3 must:

- include both mathematics and software-coding domains;
- require every selected model to eventually run the complete benchmark;
- measure primary and non-primary skill performance;
- define benchmark cases and scoring rules before model results are observed;
- use deterministic scoring wherever practical;
- record benchmark provenance and contamination risks;
- obey the approved 4096-token common context envelope;
- freeze the shared neutral chat template and scoring policy in Git;
- produce a versioned benchmark manifest.

A3 must NOT:

- download or execute the candidate models for comparative evaluation;
- run the general baseline or specialist checkpoints;
- inspect model results while constructing or tuning the benchmark;
- modify Gate acceptance criteria;
- change the selected candidate set without human review.

When the benchmark is constructed and frozen, update the durable evidence and stop for human review before A4.

## Next human checkpoint

Review the frozen benchmark, scoring policy, provenance/contamination treatment, and common prompt/template policy. A4 remains inactive until that review is recorded.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
