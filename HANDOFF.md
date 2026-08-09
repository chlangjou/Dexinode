# Dexinode Session Handoff

This is the resumable entry point for a fresh ChatGPT / human session.

Repository: `chlangjou/Dexinode`

Canonical/default branch: `main`.

Snapshot date: 2026-08-09.

## Start here in a new session

The user should be able to say only:

> Read `HANDOFF.md` from the Dexinode repository and continue from the current bounded task.

Then read, in order:

1. `AGENTS.md`
2. this file
3. `status/current.md`
4. `gates/gate-a-specialization/task.yaml`
5. `gates/gate-a-specialization/reviews/a5r1-v1.2.2-human-review.md`
6. `experiments/gate-a/benchmark-v1.2.2/manifest.yaml`

Git is the durable source of truth. Do not reconstruct project state from old chat logs when repository state is available.

## Current state

Active gate: **Gate A — Specialist Validation**.

Gate decision: **PENDING HUMAN REVIEW**.

Active bounded stage: **A5R2 — three-model cross-evaluation**.

A5R1 is complete and human-approved. A6 remains inactive.

Prepared execution branch for the hardware-running Agent:

`agent/gate-a-a5r2-three-model-cross-evaluation`

The execution Agent must fetch current refs and verify that this branch is based on the current approved `main` before touching `ai01`.

## Approved A5R1 freeze

Benchmark:

`gate-a-cross-skill-v1.2.2`

Benchmark root:

`experiments/gate-a/benchmark-v1.2.2/`

Reviewed Agent commit:

`cdd691472aa5f08c3284e881c1048956a7d52987`

Human review:

`gates/gate-a-specialization/reviews/a5r1-v1.2.2-human-review.md`

Decision: **APPROVED**.

Accepted evidence includes:

- all 48 Math oracles independently recomputed: 48/48 PASS;
- `math-23 = 1/3`;
- `math-30 = 240`;
- `math-37 = 9/95` in required reduced form;
- v1.2.1 structural Math set carried forward unchanged;
- accepted Coding set byte-identical;
- semantic adapter/scoring behavior unchanged;
- synthetic adapter tests 13/13 PASS;
- maximum rendered input 187 tokens; 1211 with generation allowance; 2885-token remaining context margin;
- no selected checkpoint executed or inspected during A5R1 remediation.

Prior benchmark versions and runs remain preserved as audit history.

## Active task: A5R2

Run the complete approved benchmark on all three frozen checkpoints, under one unchanged protocol, in this frozen order:

1. General — `Qwen/Qwen2.5-7B-Instruct` @ `a09a35458c702b33eeacc393d103063234e8bc28`
2. Math — `Qwen/Qwen2.5-Math-7B-Instruct` @ `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`
3. Coder — `Qwen/Qwen2.5-Coder-7B-Instruct` @ `c03e6d358207e414f1eca0bb1891e29f1db0e242`

Every model receives all 96 v1.2.2 cases in the same order: Math 01–48, then Coding 01–48.

Do **not** inspect or human-review model results between rows. Do not change benchmark cases, prompts, adapter behavior, scoring, inference settings, or acceptance criteria after seeing results. Do not performance-early-stop. A genuine infrastructure or methodological failure may stop the sequence, but the invalid/partial evidence must be preserved.

After all three comparable rows finish, stop for human review before A6.

## Frozen execution policy

- BF16; no quantization;
- Python 3.10.12;
- PyTorch 2.2.2+cu121;
- Transformers 4.41.1;
- safetensors 0.4.3;
- accelerate 0.30.1;
- tokenizers 0.19.1;
- neutral Qwen role-delimiter template; model-specific chat templates ignored;
- `max_new_tokens=1024`;
- `do_sample=false`;
- `num_beams=1`;
- `repetition_penalty=1.0`;
- seed 0;
- total context envelope 4096;
- external tools disabled.

Approved substrate:

- host `ai01`;
- Docker Engine 29.5.3 / `runc`;
- exactly one NVIDIA L40 UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- formal inference 40 GiB / 16 CPUs;
- approved CPU-only judge-v2 isolation with 2-second watchdog;
- Gate-specific caches independent of Ollama/Open-WebUI.

## A5R2 completion requirements

Preserve enough evidence to reproduce and review every row:

- model identifier and exact revision;
- benchmark Git identity/version;
- hardware/runtime and package versions;
- inference settings;
- raw response for every case;
- adapter/extraction decision;
- semantic and strict-interface score per case;
- coding judge result/reason;
- errors, timeouts, invalid-run reasons;
- aggregate domain/difficulty/overall metrics.

Do not authorize or execute A6. Stop after all three A5R2 rows are complete and committed.

## Minimal execution-Agent instruction

> Read `AGENTS.md`, `HANDOFF.md`, `status/current.md`, `gates/gate-a-specialization/task.yaml`, and the approved v1.2.2 human review. Execute only active stage A5R2 exactly as frozen in Git. Run General, then Math, then Coder on all 96 cases without inspecting results between rows or changing protocol. Preserve all evidence, update durable status, commit, stop for human review, and do not push until instructed.

## More detail

- References and evidence map: `docs/handoff/references.md`
- Condensed research history: `docs/handoff/history.md`
- Live status: `status/current.md`
