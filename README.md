# Dexinode

> Working name for a decentralized AI skill-weaving network.

Dexinode is an exploratory project about whether a trusted local agent can coordinate resident models, bounded specialists, remote models, tools, and verifiers through explicit handoffs—and whether that architecture can later support independently operated skill nodes without depending on one AI provider.

This repository is currently a **feasibility and architecture notebook**, not a finished protocol or product.

## Why explore this?

Frontier AI is increasingly concentrated in a small number of large models and providers. At the same time, many smaller models and idle compute resources can be highly useful when they are specialized, locally deployed, privacy-preserving, or close to the data.

Dexinode asks whether those resources can cooperate through an open network:

- advertise narrow capabilities rather than claim general intelligence;
- route work to suitable specialists;
- exchange tasks through explicit, machine-readable handoff contracts;
- verify results instead of trusting self-reported capability;
- accumulate reputation based on evidence;
- optionally settle economic value;
- resist capture by a single provider, registry, or scoring authority.

## Working hypothesis

The future role of an agent may be less about wrapping one model and more about owning local state, compiling bounded context, controlling tools, and coordinating models with different capability and trust boundaries. A decentralized specialist network is one possible later extension, not an assumed prerequisite.

This is a hypothesis to test—not a conclusion.

## Repository map

- [Vision](docs/vision.md)
- [Core concepts](docs/core-concepts.md)
- [Architecture](docs/architecture.md)
- [Open questions](docs/open-questions.md)
- [Roadmap](docs/roadmap.md)
- [Current evidence baseline](docs/research/2026-08-10-mvss-routing-evidence-baseline.md)
- [Hybrid Agent Architecture Worker brief](docs/research/hybrid-agent-architecture-worker-brief.md)
- [Decision records](docs/decisions/README.md)
- [Current status](status/current.md)

## Current status

- Project name: **Dexinode** (working name)
- Stage: hybrid resident-agent feasibility research
- Repository visibility: public
- License: undecided
- Protocol, economics, governance, and threat model: under exploration
- Gate A — Specialist Validation: **PASS / CLOSED**
- Gate B — Orchestration Advantage: **FAIL / CLOSED**
- FIM / syntax-aware MVSS eligibility: **HOLD**
- Active experiment Gate: **none**

## Near-term objective

Use primary research, official model metadata, and production evidence to answer one upstream question before specifying another experiment:

> Is there a credible Hybrid Resident-Agent architecture region—local control plane, Local Resident Model, memory/context orchestration, tools/verifiers, optional Local Specialists, and controlled Remote Model escalation—worth turning into a bounded architecture specification?

The current work is literature- and metadata-first. It does not authorize model downloads, inference, a new benchmark, or a new Gate.

## Principles

1. Evidence over capability claims.
2. Explicit contracts over implicit prompt conventions.
3. Replaceable components over provider lock-in.
4. Local-first and privacy-aware execution where useful.
5. Recovery and dispute handling as first-class protocol behavior.
6. Governance and anti-concentration considered from the start.
7. Economics are optional until they prove necessary.

## Contributing to the exploration

For now, record new ideas as hypotheses, alternatives, experiments, or decisions. Avoid turning an attractive design into a fixed architecture before it has survived a prototype and adversarial review.
