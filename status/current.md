# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A3 — Benchmark Construction and Freeze (complete; pending human review)

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

## A3 — Benchmark Construction and Freeze: complete pending human review

The superseding benchmark is frozen as `gate-a-cross-skill-v1.1.0` in
`experiments/gate-a/benchmark-v1.1.0/`. The prior frozen
`gate-a-cross-skill-v1.0.0` artifacts remain unchanged in
`experiments/gate-a/benchmark/`.

Completed A3 outputs:

- 48 mathematics cases and 48 software-coding cases; every approved model is
  assigned all 96 cases across both primary and non-primary domains;
- 10 foundational, 24 intermediate, and 14 advanced cases per domain:
  20.8%, 50.0%, and 29.2%;
- expanded multi-step mathematics, algorithmic, and edge-sensitive coding
  coverage to materially reduce ceiling-effect risk;
- deterministic exact-integer, reduced-rational, JSON, and Python 3.10
  unit-test scoring with equal case weights and no LLM judge;
- the approved neutral Qwen role-delimiter template preserved byte-for-byte;
- pinned-tokenizer measurements for every rendered case: 56–113 input tokens,
  maximum input plus the 1,024-token generation budget 1,137, within 4,096;
- provenance, contamination risks, difficulty-stratified reporting, and
  freeze validation in the new manifest.

Coding evaluation now has a mandatory fail-closed actual bounded-isolation
preflight and receipt requirement. The A3 boundary-only preflight was run on
the current host and failed because bubblewrap could not establish the network
namespace (`NETLINK_ROUTE: Operation not permitted`); the receipt is preserved
at `experiments/gate-a/benchmark-v1.1.0/execution/preflight-receipt-a3.json`.
No candidate weights, candidate models, candidate-generated source, model
outputs, comparative runs, or benchmark results were executed or inspected.

Gate acceptance criteria and the selected candidate set were not modified.
A3 is complete; stop for human review before A4. A4/A5 coding evaluation is
blocked until a later exact evaluation host passes the required preflight.

## Next human checkpoint

Review `experiments/gate-a/benchmark-v1.1.0/`, its scoring policy,
provenance/contamination treatment, difficulty balance, common prompt/template
policy, and the mandatory coding-isolation preflight. Decide whether to approve
the superseding benchmark and resolve the host isolation blocker; A4 remains
inactive until review is recorded.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
