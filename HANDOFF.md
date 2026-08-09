# Dexinode Session Handoff

This is the resumable entry point for a fresh ChatGPT / human session.

Repository: `chlangjou/Dexinode`

Canonical/default branch: `main`.

Snapshot date: 2026-08-10.

## Start here

Read, in order:

1. `AGENTS.md`
2. this file
3. `status/current.md`
4. `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
5. `gates/gate-b-orchestration/README.md`
6. `gates/gate-b-orchestration/task.yaml`
7. `gates/gate-b-orchestration/acceptance.yaml`
8. `gates/gate-b-orchestration/reviews/b1-v1.0.0-human-review.md`

Git is the durable source of truth.

## Current state

Gate A — Specialist Validation: **PASS / CLOSED**.

Active gate: **Gate B — Orchestration Advantage**.

Active bounded stage: **B1R — complete, pending human review**.

Gate B decision: **PENDING**.

No Gate B selected-model execution is authorized.

## B1R completion

Commit artifacts freeze `gate-b-orchestration-v1.1.0` and `router-v2` without
modifying v1.0.0/router-v1. The fresh benchmark has 96 cases (48 Math, 48
Coding), 10/24/14 difficulty counts per domain, a case-by-case structural
freshness audit, and a semantic-task-only router boundary. Exact semantic-task
overlap with Gate A is zero; no selected-model output or per-case result was
used for case selection.

Static validation is complete: Math oracle 48/48 PASS, Coding evaluator 48/48
PASS, adapter 13/13 PASS, router 5/5 PASS with 96/96 routes, and tokenizer
context 96/96 PASS (maximum 124 input tokens; margin 2948). No Gate B selected
model was executed. The next decision is human approval of B1R before B2 or
any model execution; do not push until instructed.

## Why B1 v1.0.0 was not approved

Agent commit:

`7228c973130ed6032226118873a140927c48f17f`

Preserved artifacts:

- `experiments/gate-b/benchmark-v1.0.0/`
- `experiments/gate-b/router-v1/`

Human review:

`gates/gate-b-orchestration/reviews/b1-v1.0.0-human-review.md`

Decision: **CHANGES REQUIRED**.

The static validation itself was strong: Math 48/48 PASS, Coding 48/48 cases and 121/121 reference tests PASS, adapter tests 13/13, router tests 6/6, context fit confirmed, and no Gate B selected model was executed.

Two methodological blockers remain:

1. **Structural freshness** — exact prompt overlap is zero, but multiple Gate B cases are near-isomorphic or semantically identical to Gate A executed cases. Examples include the exact 17-mod-43 modular inverse, the same T_8 tiling recurrence, 90-degree rotation, line-region counting, surjection counting, bounded compositions and Catalan evaluation.
2. **Router information boundary** — router-v1 uses standardized model-output/handoff contract phrases (`python 3.10`, `implementation block`, `integer`, `fraction`, etc.), so its 96/96 result partly classifies benchmark formatting rather than semantic task content.

## Preserved B1R target and evidence

The immutable artifacts are:

- benchmark: `gate-b-orchestration-v1.1.0`
- root: `experiments/gate-b/benchmark-v1.1.0/`
- router: `experiments/gate-b/router-v2/`

Do not patch v1.0.0/router-v1 in place.

The revision must:

- preserve the accepted 96-case balance, difficulty distribution, adapter behavior, numerical acceptance thresholds and execution controls;
- replace positional mirrors, constant/coefficient substitutions and near-isomorphic Gate A case constructions;
- record a case-by-case structural freshness audit against Gate A definitions;
- use Gate A definitions only for structural comparison, never per-case results/raw outputs or the retrospective Coder postmortem to select cases;
- independently recompute all Math oracles and all Coding evaluator expected values;
- expose only semantic task text to the router; model-facing handoff/output instructions are applied after routing and remain invisible to router-v2;
- keep task-family metadata reporting-only and invisible to routing;
- freeze later selected-model execution as one orchestrated sequence with no result review between General evidence collection and specialist-selected evidence collection;
- execute no selected model during B1R;
- stop for human review before B2.

## Gate B hypothesis and unchanged thresholds

Primary policies remain:

1. General-only — General for every task.
2. Skill-routed — Math specialist for validated Mathematics tasks; General for Coding/fallback.

Both logical policies use exactly one model inference per task.

Thresholds remain:

- routed overall ≥ General +10 pp;
- paired-bootstrap 95% CI for overall delta excludes zero;
- routed Math ≥ General Math +10 pp with CI excluding zero;
- Coding degradation no worse than 5 pp;
- routing accuracy ≥95%.

## Minimal B1R Agent instruction

> Read `AGENTS.md`, `HANDOFF.md`, `status/current.md`, `gates/gate-b-orchestration/task.yaml`, `gates/gate-b-orchestration/acceptance.yaml`, and `gates/gate-b-orchestration/reviews/b1-v1.0.0-human-review.md`. Execute only active stage B1R. Preserve v1.0.0/router-v1 unchanged, create v1.1.0/router-v2 with structural freshness and pre-handoff semantic routing boundaries, run complete static validation only, execute no selected model, update durable status, commit, stop for human review, and do not push until instructed.
