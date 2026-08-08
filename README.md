# Dexinode

> Working name for a decentralized AI skill-weaving network.

Dexinode is an exploratory project about enabling specialized models, agents, and compute nodes to discover one another, negotiate explicit handoffs, perform verifiable work, and build portable reputation without depending on a single AI provider.

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

The future role of an agent may be less about wrapping one model and more about coordinating multiple specialized models and agents. If specialization reduces drift and repeated dead ends, the coordination layer becomes a protocol for discovery, delegation, verification, recovery, and accountability.

This is a hypothesis to test—not a conclusion.

## Repository map

- [Vision](docs/vision.md)
- [Core concepts](docs/core-concepts.md)
- [Architecture](docs/architecture.md)
- [Open questions](docs/open-questions.md)
- [Roadmap](docs/roadmap.md)
- [Decision records](docs/decisions/README.md)

## Current status

- Project name: **Dexinode** (working name)
- Stage: problem framing and feasibility research
- Repository visibility: private
- License: undecided
- Protocol, economics, governance, and threat model: under exploration

## Near-term objective

Define the smallest falsifiable prototype that can answer one question:

> Can independently operated specialist nodes complete a multi-step task more reliably or efficiently than a single general model, while keeping handoffs observable and verifiable?

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
