# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A2 — Candidate Eligibility complete; pending human review before A3

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

## Completed bounded task: A2 — Candidate Eligibility

Verified the human-approved candidate set in
`experiments/gate-a/candidates.yaml` without changing the selected models or
Gate criteria:

- `Qwen/Qwen2.5-7B-Instruct`
- `Qwen/Qwen2.5-Math-7B-Instruct`
- `Qwen/Qwen2.5-Coder-7B-Instruct`

All three pinned revisions expose exactly 7,615,616,512 BF16 parameters and
the same Qwen2ForCausalLM dimensions. Their tokenizer JSON, vocabulary, merges,
and checked special-token definitions are byte-identical. Their repository chat
templates differ: Math adds a math-specific boxed-answer instruction, so A3
must use one neutral shared template.

The corrected config comparison records Math's 4,096-token position/window
limit versus 32,768 position embeddings for General/Coder, plus the different
RoPE theta. A safe common envelope is 4,096 total rendered input plus generated
tokens. The proposed common policy uses the official BF16 artifacts, no
quantization, one CPU-loaded model at a time, explicit greedy generation, and
the observed Transformers 4.41.1 runtime. Memory is feasible on the 1.0 TiB
host; throughput is unverified because no usable GPU is available.

The evidence includes exact revision IDs, metadata SHA-256 checksums, published
weight-shard SHA-256 values and sizes, licenses, lineage corrections, runtime
versions, and A3 confounders. Small metadata was checked in memory; model
weights were not downloaded, executed, or committed.

No benchmark was constructed, frozen, or run.

## Next bounded action after human review

Human review must approve or reject the A2 eligibility record and decide whether
to activate A3 benchmark construction and freeze. Review should specifically
confirm the 4,096-token common envelope, neutral shared chat template, CPU-only
BF16 feasibility, and no-quantization policy.

Do not construct or freeze the formal benchmark until that review is recorded.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
