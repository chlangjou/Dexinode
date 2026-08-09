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

Active bounded stage: **B1 — complete pending human review**.

Gate B decision: **PENDING HUMAN REVIEW**.

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

## Frozen pending-human-review Gate B acceptance signal

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

These criteria are frozen for human review; thresholds were not changed during B1. No Gate B result may be observed before human approval.

## B1 completion — pending human review

The static design is complete under:

1. fresh benchmark: 96 cases, 48 Math + 48 Coding;
2. exact prompt overlap with Gate A v1.1.0/v1.2.0/v1.2.1/v1.2.2: zero;
3. Math oracle validation: 48/48 PASS;
4. Coding evaluator validation: 48/48 cases and 121/121 tests PASS;
5. deterministic prompt-only router: 6/6 tests and 96/96 benchmark routes;
6. copied accepted semantic adapter tests: 13/13 PASS;
7. maximum rendered input 188; maximum with generation allowance 1212; context margin 2884;
8. no General, Math, or Coder checkpoint executed during B1.

One authoring defect found during static validation (`math-27`, divisor count
of 360) was corrected from 18 to 24 and recorded in the oracle-validation
record. No model result informed the correction.

Review the B1 artifacts before authorizing B2. B3 and B4 remain inactive.

Do not broaden B1 into multi-step orchestration, recursive delegation, networking, federation, reputation, settlement, or training.

## Minimal next-session instruction

For the next session, the B1 execution Agent should be told:

> Read `AGENTS.md`, `HANDOFF.md`, `status/current.md`, and all files under `gates/gate-b-orchestration/`. Review the completed B1 benchmark/router/protocol evidence and await human direction. Do not authorize or execute B2/B3, and do not push until instructed.

## More detail

- Gate A evidence: `gates/gate-a-specialization/evidence-report.md`
- Gate A final decision: `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
- Live status: `status/current.md`
