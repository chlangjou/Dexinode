# Dexinode Session Handoff

This is the resumable entry point for a fresh ChatGPT / human session.

Repository: `chlangjou/Dexinode`

Canonical/default branch: `main`.

Snapshot date: 2026-08-10.

## Start here in a new session

The user should be able to say only:

> Read `HANDOFF.md` from the Dexinode repository and continue from the current bounded task.

Then read, in order:

1. `AGENTS.md`
2. this file
3. `status/current.md`
4. `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
5. `gates/gate-b-orchestration/README.md`
6. `gates/gate-b-orchestration/task.yaml`
7. `gates/gate-b-orchestration/acceptance.yaml`

Git is the durable source of truth. Do not reconstruct project state from old chat logs when repository state is available.

## Current state

Gate A — Specialist Validation: **PASS / CLOSED**.

Active gate: **Gate B — Orchestration Advantage**.

Active bounded stage: **B1 — protocol, router, benchmark and acceptance freeze design**.

Gate B decision: **PENDING**.

No Gate B selected-model execution is currently authorized.

## Gate A final result

Final human decision:

`gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`

A6 evidence report:

`gates/gate-a-specialization/evidence-report.md`

Accepted key result:

- General Math: 30/48 = 62.50%;
- Math specialist Math: 44/48 = 91.67%;
- Math specialist primary-domain advantage: **+29.17 pp**;
- paired-bootstrap 95% CI: **[+16.67, +41.67] pp**;
- Math specialist Coding tradeoff: **-37.50 pp**;
- Coder checkpoint did not establish a Coding advantage over General.

Interpretation: Gate A is a **single-specialist PASS**. Specialist capability exists, but checkpoint labels are not trusted without empirical validation.

Dexinode skill identity should therefore be treated as approximately:

**checkpoint + explicit handoff contract/adapter + measured capability profile**.

## Gate B bounded question

Gate B does not yet attempt full multi-agent collaboration. It first asks whether skill-aware selection alone creates measurable value.

> On a fresh mixed mathematics/software-coding benchmark, can a frozen deterministic router using only task prompt text and the empirically validated Gate A skill registry outperform a General-only policy while using exactly one model inference per task?

Primary comparison:

1. **General-only** — all cases to `Qwen/Qwen2.5-7B-Instruct`.
2. **Skill-routed** — Math to the validated Math specialist; Coding and fallback to General.

The Gate A Coder checkpoint is not treated as a validated coding specialist in this first routing gate.

## Proposed Gate B acceptance signal

Before model execution, B1 currently proposes freezing:

- fresh benchmark: 96 cases, 48 Math + 48 Coding;
- exact Gate A prompt reuse: 0;
- deterministic CPU-only router;
- router input: task prompt only;
- exactly one model inference per case for both policies;
- same context/generation controls;
- no retries, fallback model calls, voting or ensemble;
- primary signal: routed overall accuracy at least **+10 pp** over General-only;
- paired-bootstrap 95% CI of the overall improvement must exclude zero;
- routed Math advantage at least +10 pp with CI excluding zero;
- routed Coding degradation no worse than 5 pp;
- routing accuracy at least 95% against hidden evaluation labels.

These criteria remain **proposed until B1 human review/freeze**. No Gate B result may be observed before that freeze.

## Active bounded task — B1

Static design only:

1. author a fresh Gate B benchmark under `experiments/gate-b/benchmark-v1.0.0/`;
2. independently validate all Math oracles and Coding evaluators;
3. create a deterministic prompt-only router under `experiments/gate-b/router-v1/`;
4. add synthetic router tests and information-boundary checks;
5. freeze scoring, token/context validation, execution policy and resource parity;
6. execute **no General, Math, or Coder checkpoint**;
7. stop for human review before B2/B3.

Do not broaden B1 into multi-step orchestration, recursive delegation, networking, federation, reputation, settlement, or training.

## Minimal execution-Agent instruction

Once the B1 Agent branch is based on current `main`, the execution Agent can be told:

> Read `AGENTS.md`, `HANDOFF.md`, `status/current.md`, and all files under `gates/gate-b-orchestration/`. Execute only active stage B1 exactly as recorded in Git. Build and statically validate the fresh benchmark/router/protocol, execute no selected model, preserve evidence, update durable status, commit, stop for human review, and do not push until instructed.

## More detail

- Gate A evidence: `gates/gate-a-specialization/evidence-report.md`
- Gate A final decision: `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
- Live status: `status/current.md`
