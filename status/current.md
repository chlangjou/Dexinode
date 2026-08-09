# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A3 — Benchmark Construction and Freeze (revision required)

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

The durable A2 review record is `gates/gate-a-specialization/reviews/a2-human-review.md`.

Approved controls remain:

- enforce `rendered_input_tokens + max_new_tokens <= 4096` for every benchmark case;
- freeze one neutral Qwen role-delimiter chat template with identical semantic system/user content for all three models;
- use official BF16 checkpoints with no quantization for the initial inference policy;
- keep external tools disabled for Gate A comparative inference;
- CPU-only execution is not a permanent Gate constraint. A different execution host may be approved before A4 provided all compared models use the same environment/policy and the change is recorded before results are observed.

## A3 v1.0.0 review: changes required

Agent produced and froze `gate-a-cross-skill-v1.0.0` at commit
`6b8d3c0854cc1770e459ec9454ee7d78afd049ce` without executing any selected model.
The process discipline, deterministic scoring approach, provenance record, common
template, and context controls were acceptable.

Human review did **not** authorize A4. The durable review record is:

`gates/gate-a-specialization/reviews/a3-human-review-v1.md`

The benchmark must be revised before execution because:

1. 16 binary cases per domain provide coarse 6.25-percentage-point granularity and are weakly matched to the predefined >=10 percentage-point signal plus 95% bootstrap interval requirement;
2. the current math and coding sets contain many foundational/intermediate tasks and present a material ceiling-effect risk for capable 7B models;
3. coding-score validity requires actual bounded isolation for generated Python before scored A4/A5 execution.

The frozen v1.0.0 files are historical evidence and must not be edited in place.

## Active bounded task: revise and re-freeze A3 benchmark

Create a new benchmark version that supersedes v1.0.0 for Gate A execution.

Required design constraints:

- at least 48 mathematics cases and 48 software-coding cases (>=96 total), unless a different pre-execution size is analytically justified and returned for human approval;
- preserve both cross-skill domains and require all three models to run the complete benchmark later;
- plan a meaningful difficulty distribution in both domains, approximately 20–25% foundational, 45–55% intermediate, and 25–30% advanced;
- retain deterministic scoring and equal predeclared case weights unless a change is justified before any model output is observed;
- reduce ceiling-effect risk with materially more discriminating intermediate/advanced tasks;
- preserve the approved neutral shared template and 4,096-token total context envelope;
- keep provenance and contamination risks explicit;
- record coding execution isolation as a mandatory execution preflight requirement;
- do not modify Gate acceptance criteria.

Do NOT:

- edit the frozen v1.0.0 artifacts in place;
- execute the General, Math, or Coder checkpoints;
- inspect selected-model outputs while revising cases;
- tune difficulty from selected-model performance;
- proceed to A4.

When the revised benchmark is constructed and frozen, commit it, update durable state, and stop again for human review.

## Next human checkpoint

Review the superseding benchmark version for statistical usefulness, difficulty balance, deterministic scoring, provenance/contamination treatment, context/template compliance, and execution-isolation requirements.

A4 remains inactive.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
