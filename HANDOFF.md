# Dexinode Session Handoff

Repository: `chlangjou/Dexinode`
Canonical/default branch: `main`
Snapshot date: 2026-08-10

## Start here

Read, in order:

1. `AGENTS.md`
2. this file
3. `status/current.md`
4. `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
5. `gates/gate-b-orchestration/task.yaml`
6. `gates/gate-b-orchestration/acceptance.yaml`
7. `gates/gate-b-orchestration/reviews/b1-v1.0.0-human-review.md`
8. `gates/gate-b-orchestration/reviews/b1r-v1.1.0-human-review.md`

Git is the durable source of truth.

## Current state

Gate A — Specialist Validation: **PASS / CLOSED**.

Active gate: **Gate B — Orchestration Advantage**.

Active bounded stage: **B1R2 — oracle and semantic-contract remediation**.

Gate B decision: **PENDING**.

**No Gate B selected-model execution is authorized.**

## B1R2 completion

Commit artifacts freeze `gate-b-orchestration-v1.1.1` under
`experiments/gate-b/benchmark-v1.1.1/`. v1.0.0, v1.1.0, and router-v2 remain
unchanged. The two Math oracle corrections are recorded as `math-14 = 136` and
`math-37 = 161/36`; all 48 Math cases pass independent recomputation.

All 48 Coding semantic tasks pass the prompt-to-evaluator audit. The five
reviewed specification defects were clarified, with evaluator behavior and
structural constructions preserved. Static validation passes for Coding
evaluators (48/48), adapter (13/13), router-v2 (5/5; target routes 96/96), and
token/context (96/96; max input 124; margin 2948).

No selected model was executed or inspected. Human approval is required before
B2 or any Gate B model execution. Do not push until instructed.

## Preserved history

### B1 v1.0.0

- commit: `7228c973130ed6032226118873a140927c48f17f`;
- benchmark: `experiments/gate-b/benchmark-v1.0.0/`;
- router: `experiments/gate-b/router-v1/`;
- review: `gates/gate-b-orchestration/reviews/b1-v1.0.0-human-review.md`;
- decision: **CHANGES REQUIRED** for structural freshness and handoff-contract routing leakage.

### B1R v1.1.0

- commit: `48d768799bba4d5f3862359eddeb44cf134a962e`;
- benchmark: `experiments/gate-b/benchmark-v1.1.0/`;
- router: `experiments/gate-b/router-v2/`;
- review: `gates/gate-b-orchestration/reviews/b1r-v1.1.0-human-review.md`;
- decision: **CHANGES REQUIRED** for oracle/specification defects.

The v1.1.0 structural freshness remediation and router information boundary are accepted. Preserve v1.1.0/router-v2 unchanged as frozen-not-approved audit history.

## Accepted v1.1.0 controls

- 96 cases: 48 Math + 48 Coding; 10/24/14 difficulty split per domain;
- case-by-case structural freshness audit accepted;
- exact semantic-task overlap with Gate A = 0;
- router sees `semantic_task` only, before handoff/output contract append;
- Gate A adapter byte-identical; 13/13 tests PASS;
- router-v2 tests 5/5 and current benchmark routes 96/96;
- max input 124; max with 1024 generation 1148; context margin 2948;
- route decisions freeze before model output;
- later execution: General all 96 once, then Math specialist only on frozen Math routes, no between-phase result review;
- acceptance thresholds unchanged;
- no selected model executed during B1R.

Router-v2's 96/96 accuracy is only a qualification for this minimal benchmark. Because Coding tasks consistently begin with `Implement`, do not interpret it as evidence of a general-purpose router.

## Why v1.1.0 is not executable

Independent human review found:

1. `math-14`: frozen 64, correct **136**.
2. `math-37`: frozen `41/9`, correct **161/36**.
3. Coding semantic-task/evaluator contract defects, including at least `code-02`, `code-09`, `code-21`, `code-38`, and `code-42`.

All 48 Coding cases require a prompt-to-evaluator semantic-contract audit before any model output is observed.

## Preserved B1R2 target and evidence

The immutable revision is:

- benchmark: `gate-b-orchestration-v1.1.1`;
- root: `experiments/gate-b/benchmark-v1.1.1/`.

Required work:

- preserve v1.0.0 and v1.1.0 artifacts unchanged;
- correct the two Math oracles;
- recompute all 48 Math oracles independently;
- audit all 48 Coding task specifications against their evaluator behavior and make wording unambiguous;
- re-run Coding reference validation;
- retain accepted structural freshness and router boundary unless a correction materially changes a case, in which case re-audit it;
- re-run adapter/router/token/context/static validation and refresh hashes;
- keep numerical acceptance thresholds unchanged;
- execute **no selected model**;
- stop for human review before B2.

## Minimal B1R2 Agent instruction

> Read `AGENTS.md`, `HANDOFF.md`, `status/current.md`, `gates/gate-b-orchestration/task.yaml`, `gates/gate-b-orchestration/acceptance.yaml`, and `gates/gate-b-orchestration/reviews/b1r-v1.1.0-human-review.md`. Execute only active stage B1R2. Preserve prior benchmark/router revisions unchanged, create `gate-b-orchestration-v1.1.1` with the required oracle and 48/48 Coding semantic-contract remediation, run complete static validation only, execute no selected model, update durable status, commit, stop for human review, and do not push until instructed.
