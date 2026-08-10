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
- [Hybrid Agent evidence map](docs/research/hybrid-agent-evidence-map.md)
- [Agent-specialized small-model landscape](docs/research/agent-specialized-small-model-landscape.md)
- [Hybrid architecture hypothesis](docs/research/dexinode-hybrid-architecture-hypothesis.md)
- [Bounded repository-repair specification](docs/specifications/bounded-repository-repair-resident-core-v0.1.md)
- [Decision records](docs/decisions/README.md)
- [Current status](status/current.md)

## Current status

- Project name: **Dexinode** (working name)
- Stage: bounded repository-repair Resident Core architecture specification, pending human review
- Repository visibility: public
- License: undecided
- Protocol, economics, governance, and threat model: under exploration
- Gate A — Specialist Validation: **PASS / CLOSED**
- Gate B — Orchestration Advantage: **FAIL / CLOSED**
- FIM / syntax-aware MVSS eligibility: **HOLD**
- Active experiment Gate: **none**

## Near-term objective

Human review selected `PROCEED TO BOUNDED ARCHITECTURE SPEC` after the Hybrid Agent evidence review. The current bounded question is:

> For a recoverable repository-repair workflow whose result can be checked by deterministic tests, what minimum responsibility contract, packet/receipt schema, state transitions, and escalation boundary should a 4B–8B Local Resident Core have so that later evidence can determine whether it works without a Remote Model managing every step?

The [v0.1 specification](docs/specifications/bounded-repository-repair-resident-core-v0.1.md) is a falsifiable hypothesis boundary, not a validated architecture. Current work is human review only; it does not authorize model selection, downloads, inference, implementation, benchmark design, acceptance thresholds, or a new Gate.

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
