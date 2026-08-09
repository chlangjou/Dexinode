# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A1 — Candidate Scout complete; pending human review

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

## Completed bounded task: A1 — Candidate Scout

Recorded one credible candidate set in `experiments/gate-a/candidates.yaml`:

- general baseline: `Qwen/Qwen2.5-7B-Instruct`;
- mathematics specialist: `Qwen/Qwen2.5-Math-7B-Instruct`;
- coding specialist: `Qwen/Qwen2.5-Coder-7B-Instruct`.

The set has traceable Qwen/Qwen2.5-7B lineage, comparable nominal 7.61B
parameter scale, public immutable revisions, Apache-2.0 licenses, and official
specialization evidence. Runtime feasibility is conditional: the current host
has 1.0 TiB RAM but no usable CUDA GPU, so CPU/offload execution is possible in
principle but throughput is unverified.

The principal unresolved confounder is that the Math checkpoint's published
config has a 4K context window while the general and Coder checkpoints expose
131K. Tokenizer/chat-template equivalence, exact artifact checksums, and actual
runtime feasibility remain A2 work.

No benchmark was constructed, frozen, or executed. No model weights were
downloaded or modified.

## Next bounded action after human review

Human review must choose one of:

- approve this candidate set and activate A2/A3;
- request more candidate research;
- revise Gate A assumptions;
- mark Gate A candidate discovery INCONCLUSIVE.

Until that decision is recorded, do not construct the formal benchmark or run
comparative evaluation.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
