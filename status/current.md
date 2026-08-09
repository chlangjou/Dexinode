# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Session handoff: `HANDOFF.md`
- Active execution stage: A5R2 — complete pending human review

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

## A5R2 complete — pending human review

All three authorized checkpoints completed all 96 frozen v1.2.2 cases in order (General → Math → Coder) under one unchanged protocol. No result review occurred between rows, no performance early stop occurred, and A6 remains inactive.

Evidence summary: `experiments/gate-a/a5r2-v1.2.2-cross-evaluation.md`
Machine-readable index: `experiments/gate-a/a5r2-v1.2.2-cross-evaluation.yaml`

| Role | Overall | Math | Coding |
|---|---:|---:|---:|
| General baseline | 68/96 (0.7083) | 30/48 (0.6250) | 38/48 (0.7917) |
| Math specialist | 64/96 (0.6667) | 44/48 (0.9167) | 20/48 (0.4167) |
| Coder specialist | 69/96 (0.7188) | 36/48 (0.7500) | 33/48 (0.6875) |

Validation and preservation:

- all three rows: 96/96 generated, frozen order, zero generation failures;
- maximum rendered input 187 tokens; maximum with generation allowance 1211; context margin 2885;
- coding judge infrastructure failures: 0; timeouts: General 1, Math 1, Coder 0;
- four preflight failures are preserved with logs in `experiments/gate-a/runs/a5r2-attempts-20260809T142953Z.yaml`; no failed attempt loaded a model or created candidate output;
- raw responses, inference receipts, adapter/per-case results, judge records, and metrics are preserved under the three retry4 run directories.

The benchmark, prompt/template, adapter, scoring contract, inference controls, candidate revisions, and acceptance criteria were not changed after execution began. A scorer receipt-field fix was applied only after all three formal rows completed; the rows were rescored from preserved raw outputs without model reruns.

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

Review the complete A5R2 three-row evidence and decide whether to authorize A6. The Gate decision remains **PENDING HUMAN REVIEW**; this agent does not declare PASS or FAIL.

Gate B remains inactive until Gate A receives a human PASS decision.
