# Dexinode Session Handoff

Repository: `chlangjou/Dexinode`

Canonical branch: `main`

Integration surface: Draft PR [#28](https://github.com/chlangjou/Dexinode/pull/28)

Snapshot: 2026-08-11

Git is the durable source of truth. This file is intentionally compact for a fresh session.

## Start here

Read in this order:

1. `AGENTS.md`
2. `HANDOFF.md`
3. `status/current.md`
4. `docs/decisions/0002-proceed-to-bounded-repository-repair-spec.md`
5. `docs/specifications/bounded-repository-repair-resident-core-v0.1.md`
6. `docs/research/2026-08-11-hybrid-agent-human-review.md`
7. `docs/research/dexinode-hybrid-architecture-hypothesis.md`

Read the evidence map and model landscape when their claims are needed:

- `docs/research/hybrid-agent-evidence-map.md`
- `docs/research/agent-specialized-small-model-landscape.md`

Read Gate closure records only when their evidence is needed:

- `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

Do not reopen Gate A/B execution unless a new, human-approved question explicitly requires it.

## Durable empirical state

### Gate A — Specialist Validation

**PASS / CLOSED.**

Same-family Qwen2.5-7B evidence established strong capability divergence on one measured distribution. The Math checkpoint showed a large Mathematics advantage; the Coder checkpoint did not validate as a Coding specialist.

Durable lesson: capability identity is `checkpoint + interface/contract + measured profile`, not a model label.

### Gate B — Orchestration Advantage

**FAIL / CLOSED.**

Frozen execution: `gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`.

- General-only: 76/96 = 79.17%.
- Skill-routed: 77/96 = 80.21%.
- Overall delta: +1.04 pp, 95% CI [0, +3.125] pp.
- Router domain accuracy: 100%.

The frozen +10 pp thresholds were not met. Post-closure review found that the sole frozen Mathematics improvement was answer representation, not content competence. Gate B remains `FAIL / CLOSED` with its recorded oracle/protocol caveat.

Durable lesson: broad-domain classification is not per-task model-success prediction.

## Preserved FIM eligibility decision

FIM / syntax-aware code completion remains **`HOLD`**.

The current task does not resolve this HOLD, continue DELULU work, select a model, or run inference.

## Completed Hybrid Agent evidence stage

[ADR 0001](docs/decisions/0001-hybrid-resident-agent-research-frame.md) framed the complete configuration:

`deterministic local software + Local Resident Model + memory/context orchestration + tools/verifiers + optional Local Specialist + Remote Model escalation + human review`

The Worker completed the evidence map, non-exhaustive small-model landscape, architecture hypothesis, and a `HOLD` recommendation. Human review accepted the evidence but rejected the decision mapping.

[ADR 0002](docs/decisions/0002-proceed-to-bounded-repository-repair-spec.md), issue [#29](https://github.com/chlangjou/Dexinode/issues/29), records the accepted decision:

**`PROCEED TO BOUNDED ARCHITECTURE SPEC`**

This means the component evidence is sufficient to specify a falsifiable boundary. It does not validate a Resident Core, model, context envelope, deployment, or user value.

Corrections already incorporated:

- long-term state outside context is a `PARTIALLY SUPPORTED` Dexinode design constraint, not a universal necessity;
- the SERA-8B 80GB card recommendation is not independently corroborated by the paper hardware section, which describes SERA-32B;
- the model landscape is not a registry;
- 8K–32K, 70%, -30%, and -50% remain non-frozen.

## Current bounded artifact

`docs/specifications/bounded-repository-repair-resident-core-v0.1.md`

Question:

> For a recoverable repository-repair workflow whose result can be checked by deterministic tests, what minimum responsibility contract, packet/receipt schema, state transitions, and escalation boundary should a 4B–8B Local Resident Core have so that later evidence can determine whether it works without a Remote Model managing every step?

The specification limits automatic work to one repository, an immutable base, reversible sandbox writes, and a relevant deterministic verifier. It stops at a locally verified candidate; publication, PR, merge, deployment, and production mutation are outside scope.

The Local Resident owns six semantic decisions:

1. intent contract;
2. task decomposition;
3. semantic context request;
4. verifier-failure interpretation;
5. final integration judgment;
6. bounded escalation decision.

Deterministic software owns canonical state, packet compilation, policy, tools, sandbox, verification, rollback, and audit. Specialist and Remote outputs are untrusted proposals.

Remote dependence is classified as:

- `none`;
- `bounded_artifact`;
- `core_advice`;
- `core_substitution`.

A `core_substitution` workflow may be useful, but it is not positive Resident Core evidence.

## Current bounded task

Human-review specification v0.1 only.

Check that:

1. the workflow boundary is singular, recoverable, and deterministically verifiable;
2. every semantic decision and side effect has an attributable packet／receipt path;
3. Remote replacement cannot be hidden;
4. security, rollback, human review, unsupported tasks, and falsifiers are explicit;
5. no model, benchmark, performance threshold, or execution plan is frozen.

Stop after review. A later experiment or Gate requires a new decision issue.

## Hard stop conditions

Do not:

- select or download a checkpoint;
- run inference, quantization, GPU, or deployment work;
- implement the runtime;
- create or freeze a benchmark, task set, baseline, statistical method, or acceptance threshold;
- add or activate a Gate;
- modify Gate A/B evidence or conclusions;
- resolve FIM HOLD or continue DELULU closure work;
- reopen routing economics;
- design token economics, reputation, settlement, governance, or a decentralized marketplace.

## Next human decision

Accept the v0.1 specification boundary or request a focused revision. Do not infer authorization for an experiment from specification acceptance.
