# Dexinode Session Handoff

Repository: `chlangjou/Dexinode`

Canonical branch: `main`

Snapshot: 2026-08-10

Git is the durable source of truth. This file is intentionally compact for a fresh session.

## Start here

Read in this order:

1. `AGENTS.md`
2. `HANDOFF.md`
3. `status/current.md`
4. `docs/decisions/0001-hybrid-resident-agent-research-frame.md`
5. `docs/research/2026-08-10-mvss-routing-evidence-baseline.md`
6. `docs/research/hybrid-agent-architecture-worker-brief.md`

Read Gate closure records only when their evidence is needed:

- `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

Do not reopen Gate A/B execution unless a new, human-approved question explicitly requires it.

## Durable empirical state

### Gate A — Specialist Validation

**PASS / CLOSED.**

Same-family Qwen2.5-7B evidence established that specialization can produce strong capability divergence on one measured distribution. The Math checkpoint showed a large Mathematics advantage; the Coder checkpoint did not validate as a Coding specialist.

Durable lesson: capability identity is `checkpoint + interface/contract + measured profile`, not a model label.

### Gate B — Orchestration Advantage

**FAIL / CLOSED.**

Frozen execution: `gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`.

- General-only: 76/96 = 79.17%.
- Skill-routed: 77/96 = 80.21%.
- Overall delta: +1.04 pp, 95% CI [0, +3.125] pp.
- Router domain accuracy: 100%.

The frozen +10 pp thresholds were not met. Post-closure content review found that the sole frozen Mathematics improvement was answer representation (`0.75` versus `3/4`), not content competence. Gate B remains `FAIL / CLOSED`, with its recorded oracle/protocol caveat.

Durable lesson: broad-domain classification is not per-task model-success prediction.

## Post-Gate evidence baseline

Current consolidated classifications:

- bounded specialist existence: `ESTABLISHED`;
- structural transfer: `PARTIALLY SUPPORTED`;
- GCI as more than catastrophic forgetting: `ESTABLISHED` as a required distinction;
- dense 1–7B general standalone replacement: `CONTRADICTED` as a broad claim;
- model complementarity: `ESTABLISHED`;
- robust pre-inference `P(success | task, model)`: `PARTIALLY SUPPORTED`;
- conditional production routing savings: `ESTABLISHED` under bounded assumptions;
- full-stack absolute-small/edge economics: `OPEN`;
- edge/decentralized specialist-network viability: `OPEN`.

Do not infer consumer/idle-compute viability from datacenter routing or a large-total MoE model's active parameter count.

## Preserved FIM eligibility decision

FIM / syntax-aware code completion: **`HOLD`**.

It remains a credible narrow MVSS candidate, but it does not proceed to Gate design because DELULU artifact/licensing/verifier distribution, Qwen scale-lineage/licensing, and common-runtime measurement are incomplete.

The current task does not resolve this HOLD, continue DELULU work, select a model, or run inference.

## Current research frame

Decision: [ADR 0001](docs/decisions/0001-hybrid-resident-agent-research-frame.md), issue [#27](https://github.com/chlangjou/Dexinode/issues/27).

Study a complete Hybrid Resident-Agent configuration:

`deterministic local software + Local Resident Model + memory/context orchestration + tools/verifiers + optional Local Specialist + Remote Model escalation + human review`

The local control plane owns workspace state, durable memory, provenance, context compilation, pseudonymization mappings, credentials/permissions, tool authority, budgets, stopping conditions, audit, escalation, verification, and final integration.

Remote models receive only task-scoped context and do not own durable memory or unverified side effects.

This is a research frame, not an accepted production architecture.

## Two scale questions

- **MVRC — Minimum Viable Resident Core:** smallest local model-plus-agent configuration that can reliably manage intent, task state, context, tools, recovery, and escalation.
- **MVSS — Minimum Viable Specialist Scale:** smallest complete specialist service that remains useful at a specified task quality and full-stack resource envelope.

Both are task-conditioned. Parameter count alone is not the service boundary.

## v0.1 working assumptions

These are not Gate criteria:

- Specialist task packet target: 8K–16K tokens; 32K provisional ceiling.
- Resident Core working set target: 16K–32K tokens.
- 64K+ inputs normally require retrieval, semantic decomposition, or summarization.
- Repository, task history, and long-term memory remain outside model context and retain source/version provenance.
- Correct clarification, refusal, or escalation is a valid path.
- Pseudonymization/restoration is a likely engineerable local component; detection completeness, contextual re-identification, and semantic loss remain limitations.

## Current bounded task

Execute the literature-, official-metadata-, and production-evidence-only Worker brief:

`docs/research/hybrid-agent-architecture-worker-brief.md`

Tracks:

1. Agent memory and context engineering.
2. Loop, harness, workflow, and graph engineering, including simpler/negative baselines.
3. Agent-specialized edge-small, absolute-small, active-small MoE, and remote-reference models.
4. Hybrid local/remote responsibility, trust, verification, and user-value evidence.

Required outputs:

1. `hybrid-agent-evidence-map.md`
2. `agent-specialized-small-model-landscape.md`
3. `dexinode-hybrid-architecture-hypothesis.md`
4. `hybrid-agent-research-decision.md`

The decision file must choose exactly one:

- `PROCEED TO BOUNDED ARCHITECTURE SPEC`
- `HOLD`
- `PIVOT TO LOCAL CONTROL PLANE`
- `STOP / NEGATIVE`

It may name only one next bounded question and must stop for human review.

## Hard stop conditions

The current Worker must not:

- download model weights;
- run inference or GPU experiments;
- create or freeze a benchmark or acceptance threshold;
- add or activate a Gate;
- modify Gate A/B evidence or conclusions;
- resolve FIM HOLD or continue DELULU closure work;
- design a new routing algorithm or reopen routing economics;
- design token economics, reputation, settlement, or governance;
- commit or push as part of the research task unless separately authorized.

## Next human decision

Review the four Worker deliverables. Only after that review decide whether to write a bounded architecture specification, hold, pivot to a local control plane, or stop.
