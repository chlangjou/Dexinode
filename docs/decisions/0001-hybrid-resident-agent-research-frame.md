# 0001 — Use a hybrid resident-agent frame for the next research stage

- Status: Accepted
- Date: 2026-08-10
- Deciders: Human project owner
- Decision issue: [#27](https://github.com/chlangjou/Dexinode/issues/27)
- Supersedes: None
- Superseded by: None

## Context

Gate A established that specialization can exist on a measured distribution. Gate B showed that a broad `Mathematics -> specialist` route did not transfer into material held-out orchestration advantage. The subsequent MVSS/routing synthesis found bounded specialist and routing value, while the edge-decentralization thesis and full-stack small-model economics remain open.

The first FIM / syntax-aware code-completion eligibility audit is `HOLD`. Its artifact, licensing, verifier-distribution, lineage, and runtime questions are not being closed in the current stage.

The project now has two coupled scale questions:

- **MVRC — Minimum Viable Resident Core:** the smallest local model-plus-agent configuration that can reliably own state, tools, context assembly, failure recovery, and escalation.
- **MVSS — Minimum Viable Specialist Scale:** the smallest complete specialist service that remains useful at a required task quality and full-stack resource envelope.

Small models also cannot be assumed to consume an entire repository or long project history directly. The relevant system question is whether a local agent can compile the workspace into a bounded, reliable working set.

## Decision drivers

- The local system must retain the workspace, long-term state, trust boundary, credentials, and audit trail.
- Model context-window claims do not establish reliable use of long contexts.
- Small agent-specialized capabilities appear most credible under bounded contracts, while large active-small MoE models must not be mislabeled as absolute-small.
- Remote models can provide important capability without owning the whole workspace or durable memory.
- Memory managers, harnesses, judges, and verifiers can hide dependence on large remote models and must be audited as part of the configuration.

## Options considered

### Continue isolated MVSS/FIM work immediately

This keeps one bounded candidate but leaves the Local Agent, Resident Core, context compilation, memory, and remote fallback assumptions unspecified. FIM remains useful evidence, but its eligibility is already `HOLD` and it is not the highest upstream question.

### Treat Dexinode as a cloud-agent router

This can exploit production routing economics, but it weakens the local trust, privacy, offline, and distributed-participation thesis before those benefits have been evaluated.

### Study a hybrid resident-agent configuration

This keeps local ownership of state and trust while allowing Local Specialists and Remote Models to contribute only through bounded task contracts. It makes the hidden costs and model dependencies of memory, context, harness, verification, and fallback directly auditable.

## Decision

Use the following as the next research unit:

`deterministic local software + Local Resident Model + memory/context orchestration + tools/verifiers + optional Local Specialist + Remote Model escalation + human review`

The trusted local control plane owns:

- workspace and durable memory;
- current task state and provenance;
- context selection and packet compilation;
- local pseudonymization/restoration mappings;
- credentials, permissions, tool execution, and side-effect policy;
- loop budget, stopping conditions, recovery, and audit logging;
- remote escalation, returned-artifact verification, and final integration.

Remote models receive only task-scoped context. Correct refusal, clarification, or escalation is a valid path rather than an automatic failure.

The following context ranges are **v0.1 research assumptions, not acceptance criteria**:

| Working set | Target | Provisional boundary |
|---|---:|---:|
| Specialist task packet | 8K–16K tokens | 32K ceiling |
| Resident Core invocation | 16K–32K tokens | 64K+ normally requires retrieval, decomposition, or summarization |
| Repository, history, long-term memory | outside model context | retrieved and versioned locally |

Local pseudonymization/restoration is classified as a likely engineerable component: models may propose sensitive-entity candidates, humans approve mappings, and deterministic code performs stable replacement, validation, restoration, and audit. Completeness of sensitive-data detection and semantic preservation remain limitations.

This is an accepted **research frame**, not an accepted production architecture.

## Consequences

- The next Worker is literature-, official-metadata-, and production-evidence-only.
- It studies Agent memory/context, loop/harness/workflow design, agent-specialized small models, and hybrid local/remote responsibility boundaries together.
- The unit of comparison is the complete agent configuration, not a standalone model or leaderboard score.
- Gate A and Gate B stay closed and their evidence remains immutable.
- FIM eligibility stays `HOLD`; DELULU closure work is not continued in this stage.
- No model download, inference/GPU run, benchmark creation/freeze, acceptance threshold, routing-economics Gate, or new experimental Gate is authorized.
- The long-term distributed specialist network remains a possible extension. It is not assumed to be the source of the nearest-term value.

## Validation and revisit

The decision is revisited after the Hybrid Agent Architecture Worker returns four auditable deliverables and one of these outcomes:

- `PROCEED TO BOUNDED ARCHITECTURE SPEC`
- `HOLD`
- `PIVOT TO LOCAL CONTROL PLANE`
- `STOP / NEGATIVE`

The working context ranges and provisional responsibility split expire when stronger evidence or a human-approved bounded architecture specification supersedes them.
