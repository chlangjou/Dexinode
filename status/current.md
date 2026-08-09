# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A1 — Candidate Scout

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

## Active task

Execute **A1 — Candidate Scout** only.

Find one or more candidate model sets containing:

- at least one general-purpose baseline checkpoint;
- at least two specialist checkpoints representing at least two distinguishable skill domains;
- sufficient common lineage and parameter comparability for a fair specialization test.

Record findings in `experiments/gate-a/candidates.yaml`.

Do not construct the formal benchmark or run comparative evaluation until candidate eligibility has been reviewed.

## Required A1 evidence

For every candidate record:

- public model identifier and source;
- base family and generation;
- parameter count;
- base checkpoint / lineage when known;
- claimed specialization;
- license;
- runtime feasibility;
- evidence source for the specialization claim;
- comparability concerns;
- confidence in lineage information.

## Stop conditions for A1

Stop and request human review when either:

1. at least one credible candidate set satisfying the A1 requirements has been identified; or
2. reasonable search has not found a fair candidate set and further progress would require weakening the Gate constraints.

## Next human decision

Review the candidate set and choose one of:

- approve candidate set and activate A2/A3;
- request more candidate research;
- revise Gate A assumptions;
- mark Gate A candidate discovery INCONCLUSIVE.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
