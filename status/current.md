# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A5 — Specialist Cross-Evaluation (completed; pending human review)

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

## Frozen Gate A controls

Approved candidate set:

- general baseline: `Qwen/Qwen2.5-7B-Instruct`
- mathematics specialist: `Qwen/Qwen2.5-Math-7B-Instruct`
- coding specialist: `Qwen/Qwen2.5-Coder-7B-Instruct`

Approved benchmark: `experiments/gate-a/benchmark-v1.1.0/`.

The frozen benchmark, scoring rules, neutral prompt template, candidate revisions, generation policy, and Gate acceptance criteria remain unchanged.

## Approved execution environment

Gate A uses Docker on `ai01`.

Inference path:

- Docker Engine 29.5.3, runtime `runc`;
- exactly one NVIDIA L40;
- selected UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- BF16, no quantization;
- formal comparison runs use 40 GiB container memory and 16 CPUs;
- network disabled during formal inference;
- read-only root, private tmpfs, dropped capabilities, no-new-privileges;
- Gate-specific model caches remain independent of Ollama/Open-WebUI storage.

Coding judge v2:

- pinned `python:3.10-slim` image/digest;
- CPU-only, no network/GPU/host mounts/Docker socket;
- read-only root and private tmpfs;
- `--cap-drop=ALL`, `NoNewPrivs=1`;
- `pids.max=1`, `RLIMIT_NPROC=1:1`;
- 256 MiB / 0.5 CPU bounds;
- 1 MiB file-size bound and bounded logs;
- empirical subprocess denial;
- mandatory 2-second host watchdog.

Execution-environment approvals:

- `gates/gate-a-specialization/reviews/a4a-docker-qualification-human-review.md`
- `gates/gate-a-specialization/reviews/a4a-judge-hardening-human-review.md`

## A4b General baseline — APPROVED

Human review:

`gates/gate-a-specialization/reviews/a4b-general-baseline-human-review.md`

Accepted run:

`experiments/gate-a/runs/a4-general-baseline-20260809T082430Z-ai01-gpu0/`

General results:

- 96/96 cases generated and scored;
- mathematics: 10/48 = 20.8333%;
- software coding: 36/48 = 75.0000%;
- overall: 46/96 = 47.9167%;
- mathematics difficulty: foundational 4/10, intermediate 6/24, advanced 0/14;
- coding difficulty: foundational 9/10, intermediate 19/24, advanced 8/14;
- no infrastructure-invalid cases in the final pass;
- one coding case reached the approved 2-second watchdog and was scored zero under the frozen policy.

The low General mathematics score was sanity-reviewed before A5 authorization. Sampled raw responses show genuine incorrect direct answers, not a parser/scoring defect. The benchmark and direct-answer interface were frozen before model results and must not be changed now.

The accepted General row is the reference row for the later cross-skill competency matrix. It does not by itself establish specialization or decide Gate A.

## Active bounded task: A5 — Specialist Cross-Evaluation

Execute both approved specialists, each across the complete 96-case frozen benchmark:

1. `Qwen/Qwen2.5-Math-7B-Instruct`
   - revision `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`
   - primary domain: mathematics

2. `Qwen/Qwen2.5-Coder-7B-Instruct`
   - revision `c03e6d358207e414f1eca0bb1891e29f1db0e242`
   - primary domain: software coding

Every specialist must run all 48 mathematics and all 48 coding cases. No specialist-only subset or early stopping is allowed.

Comparison controls that must remain identical to A4b:

- same package/runtime versions;
- same selected L40 UUID;
- same formal 40 GiB / 16 CPU inference resource policy;
- same BF16/no-quantization policy;
- same neutral prompt rendering and semantic messages;
- same tokenizer policy and 4,096-token context envelope;
- same deterministic generation settings;
- same deterministic mathematics scorer;
- same coding tests and exact judge-v2 isolation policy.

A5 may duplicate or parameterize A4b tooling only to substitute the authorized model ID, pinned revision, run/cache/output identifiers, and metadata. It must not alter prompt rendering, generation, scoring, tests, package versions, or isolation semantics.

Preserve a complete run directory for each specialist with model artifact identity, environment/image/GPU receipts, raw 96-case responses, per-case scores/reasons/timing, coding judge records, and domain/difficulty metrics.

A5 must NOT:

- modify the frozen benchmark, scoring rules, prompt template, or generation policy;
- use specialist repository-default chat templates;
- modify Gate acceptance criteria or the candidate set;
- use/repermission existing Ollama model storage;
- modify/restart/recreate `ollama` or `open-webui`;
- change GPU/resource/runtime policy after observing specialist results;
- proceed to A6.

### A5 execution — COMPLETE, PENDING HUMAN REVIEW

Both approved specialists completed the complete frozen 96-case benchmark under
the comparable A4b policy. Neither the General baseline nor any other model was
rerun.

Math specialist run:

- run: `experiments/gate-a/runs/a5-math-specialist-20260809T092120Z-ai01-gpu0/`;
- revision: `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`;
- mathematics: 0/48; software coding: 0/48; overall: 0/96;
- difficulty: mathematics 0/10, 0/24, 0/14; coding 0/10, 0/24, 0/14;
- 96/96 generated and 96/96 scored; no infrastructure-invalid case or judge timeout.

Coder specialist run:

- run: `experiments/gate-a/runs/a5-coder-specialist-20260809T092120Z-ai01-gpu0/`;
- revision: `c03e6d358207e414f1eca0bb1891e29f1db0e242`;
- mathematics: 12/48; software coding: 39/48; overall: 51/96;
- difficulty: mathematics 4/10, 6/24, 2/14; coding 9/10, 22/24, 8/14;
- 96/96 generated and 96/96 scored; no infrastructure-invalid case or judge timeout.

The descriptive three-row comparison is preserved in
`experiments/gate-a/runs/a5-specialist-cross-evaluation-summary.md`. Both run
directories preserve exact model revisions, 27-file artifact inventories,
runtime/image/resource/preflight receipts, raw responses, per-case scores and
reasons, coding judge records, timing, and reproducible scripts. No benchmark,
prompt, scorer, judge policy, candidate set, or acceptance criterion changed.

## Next human checkpoint

Review both complete specialist runs and confirm that all three model rows are
comparable. If accepted, authorize A6 to compute the cross-skill competency
matrix, specialist-minus-General deltas, frozen bootstrap uncertainty,
specialization concentration, and a Gate recommendation.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
