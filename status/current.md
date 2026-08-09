# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Session handoff: `HANDOFF.md`
- Active execution stage: A5R2 — three-model cross-evaluation

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

## Frozen candidate set

- General: `Qwen/Qwen2.5-7B-Instruct` @ `a09a35458c702b33eeacc393d103063234e8bc28`
- Math specialist: `Qwen/Qwen2.5-Math-7B-Instruct` @ `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`
- Coder specialist: `Qwen/Qwen2.5-Coder-7B-Instruct` @ `c03e6d358207e414f1eca0bb1891e29f1db0e242`

Gate acceptance criteria remain unchanged.

## A5R1 complete and approved

Approved benchmark: `gate-a-cross-skill-v1.2.2`

Benchmark root:

`experiments/gate-a/benchmark-v1.2.2/`

Reviewed Agent commit:

`cdd691472aa5f08c3284e881c1048956a7d52987`

Human review:

`gates/gate-a-specialization/reviews/a5r1-v1.2.2-human-review.md`

Decision: **APPROVED**.

Accepted validation evidence:

- Math oracle validation: **48/48 PASS**;
- corrected `math-23` to `1/3`;
- corrected `math-30` to `240`;
- corrected inherited non-reduced `math-37` to canonical `9/95`;
- v1.2.1 Math structures/order/difficulty carried forward;
- coding set byte-identical to v1.2.0/v1.2.1;
- semantic adapter behavior unchanged;
- scoring/template behavior unchanged apart from version metadata;
- synthetic adapter tests: **13/13 PASS**;
- max rendered input 187 tokens; max with generation allowance 1211; context margin 2885;
- no selected model executed or inspected during A5R1 construction/review.

v1.1, v1.2.0, v1.2.1, and all historical run evidence remain preserved.

## Active bounded task — A5R2

Execute all three frozen checkpoints on the complete approved v1.2.2 benchmark.

Frozen order:

1. General baseline
2. Math specialist
3. Coder specialist

Each model receives the same 96 cases in the same order: `math-01..48`, then `code-01..48`.

Execution constraints:

- one unchanged benchmark, template, adapter, scoring contract, inference policy, and judge policy for all three rows;
- no result-driven protocol or benchmark changes;
- no human/model-result review between rows;
- no performance-based early stopping;
- preserve raw outputs, adapter decisions, per-case scores, metadata, failures, and invalid runs;
- only a genuine infrastructure or methodological failure may stop the sequence before all three comparable rows complete;
- A6 remains inactive until all three rows are completed and accepted.

## Approved execution substrate

- host `ai01`;
- Docker Engine 29.5.3 / `runc`;
- exactly one NVIDIA L40 UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- formal inference: 40 GiB / 16 CPUs;
- BF16, no quantization;
- Python 3.10.12 / PyTorch 2.2.2+cu121 / Transformers 4.41.1;
- deterministic generation: `max_new_tokens=1024`, `do_sample=false`, `num_beams=1`, `repetition_penalty=1.0`, seed 0;
- approved CPU-only judge-v2 isolation with 2-second watchdog;
- Gate-specific model caches independent of Ollama/Open-WebUI.

## Next human checkpoint

After General + Math + Coder have each completed all 96 v1.2.2 cases under the same frozen protocol, review the complete three-row evidence before authorizing A6.

Gate B remains inactive until Gate A receives a human PASS decision.
