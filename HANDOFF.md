# Dexinode Session Handoff

This is the resumable entry point for a fresh ChatGPT / human session.

Repository: `chlangjou/Dexinode`

Canonical/default branch: `main` (the repository does not use a `master` branch).

Snapshot date: 2026-08-09.

## Start here in a new session

The user should be able to say only:

> Read `HANDOFF.md` from the Dexinode repository and continue from the current bounded task.

Then read, in order:

1. `AGENTS.md`
2. this file
3. `status/current.md`
4. `gates/gate-a-specialization/task.yaml`
5. the active human review / benchmark files referenced below

Git is the durable source of truth. Do not reconstruct project state from old chat logs if repository state is available.

## Current state

Active gate: **Gate A — Specialist Validation**.

Gate decision: **PENDING HUMAN REVIEW**.

Active bounded stage: **A5R1 — v1.2.2 oracle correction and complete static validation**.

Prepared Agent-owned branch:

`agent/gate-a-a5r1-v1.2.2-oracle-validation`

At handoff time this branch was created from current `main`; no v1.2.2 Agent result had yet been reported or reviewed.

A5R2 and A6 are **inactive**. No selected model is authorized to execute until v1.2.2 is frozen and human-approved.

## Why we are here

Gate A originally used `gate-a-cross-skill-v1.1.0`. The General and Coder rows ran successfully, but the Math specialist scored 0/96 under the strict interface contract even though raw outputs showed it correctly solved sampled math cases and returned conventional worked reasoning plus `\\boxed{...}` answers. Coding outputs also frequently contained valid implementation blocks plus prose/examples. Human review therefore classified the v1.1 Math zero row as an **output-interface confounder**, not capability zero.

A semantic handoff adapter was then designed to separate:

- primary task-semantic competence; and
- secondary strict interface-compliance metrics.

`v1.2.0` froze that adapter and a fresh benchmark, but its Math set was rejected because many cases were near-isomorphic to already-observed v1.1 problem skeletons.

`v1.2.1` replaced all 48 Math cases with structurally fresh constructions and passed the structural-freshness review, but human oracle sanity checking found two benchmark-definition errors:

- `math-23`: expected `1/4`, verified correct value `1/3`;
- `math-30`: expected `432`, verified correct value `240`.

Therefore v1.2.1 is preserved as frozen-not-approved and must not be patched in place.

## Active task: v1.2.2

Create a new benchmark version at:

`experiments/gate-a/benchmark-v1.2.2/`

The revision is deliberately narrow:

- preserve v1.2.1 structural Math constructions;
- preserve the accepted Coding set byte-identically;
- preserve the accepted semantic adapter/scoring behavior;
- correct `math-23` to `1/3`;
- correct `math-30` to `240`;
- independently recompute and validate **all 48 Math oracles**;
- preserve a durable `oracle-validation.yaml` (or equivalent) showing 48/48 validation;
- rerun static/token/context validation and 13 synthetic adapter tests;
- execute **no General, Math, or Coder checkpoint**;
- stop for human review before A5R2.

The controlling review is:

`gates/gate-a-specialization/reviews/a5r1-v1.2.1-human-review.md`

The controlling task state is:

`gates/gate-a-specialization/task.yaml`

## Frozen decisions — do not reopen without explicit human review

Candidate set and exact revisions:

- General: `Qwen/Qwen2.5-7B-Instruct` @ `a09a35458c702b33eeacc393d103063234e8bc28`
- Math: `Qwen/Qwen2.5-Math-7B-Instruct` @ `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`
- Coder: `Qwen/Qwen2.5-Coder-7B-Instruct` @ `c03e6d358207e414f1eca0bb1891e29f1db0e242`

Common later-run inference policy:

- BF16, no quantization;
- Python 3.10.12;
- PyTorch 2.2.2+cu121;
- Transformers 4.41.1;
- safetensors 0.4.3;
- accelerate 0.30.1;
- tokenizers 0.19.1;
- neutral Qwen role-delimiter template;
- model-specific chat templates ignored;
- `max_new_tokens=1024`, `do_sample=false`, `num_beams=1`, `repetition_penalty=1.0`, seed 0;
- total context envelope 4096;
- external tools disabled.

Approved execution substrate for later A5R2:

- host `ai01`;
- Docker Engine 29.5.3 / `runc`;
- exactly one NVIDIA L40 UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- formal inference 40 GiB memory / 16 CPUs;
- approved CPU-only judge-v2 isolation with 2-second watchdog;
- Gate-specific model caches independent of Ollama/Open-WebUI.

Gate acceptance criteria remain unchanged. Agents may recommend but must not declare Gate PASS/FAIL.

## Expected next checkpoints

1. Agent completes v1.2.2 static/oracle validation and commits on `agent/gate-a-a5r1-v1.2.2-oracle-validation`.
2. Human/ChatGPT reviews the complete 48-oracle record and confirms the revision stayed narrow.
3. If approved, integrate v1.2.2 to `main` and activate A5R2.
4. A5R2 runs **General + Math + Coder**, each on all 96 v1.2.2 cases, with no result-driven protocol changes or human review between model runs except genuine infrastructure/methodological failure.
5. Only after all three comparable rows are accepted may A6 compute bootstrap uncertainty, primary-domain deltas, non-primary tradeoffs, specialization concentration, and a Gate recommendation.

## New-session minimal Agent instruction

Once repository refs are fetched and the intended Agent branch is verified, the human can give the execution Agent this short instruction instead of a long prompt:

> Read `AGENTS.md`, `HANDOFF.md`, `status/current.md`, and `gates/gate-a-specialization/task.yaml`. Execute only the active bounded task exactly as recorded in Git. Preserve all evidence, update durable status, commit, stop for human review, and do not push until instructed.

If the Agent branch has moved or already contains new work, inspect and review that work before issuing another execution instruction.

## More detail

- References and evidence map: `docs/handoff/references.md`
- Condensed research history: `docs/handoff/history.md`
- Live status: `status/current.md`
