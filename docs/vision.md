# Vision

## Problem statement

AI capability is concentrating around a small number of general-purpose models, cloud providers, and closed orchestration stacks. Meanwhile, specialized models, local data, domain tools, and idle compute remain fragmented and difficult to combine safely.

Dexinode explores whether an open coordination layer can let these independent resources cooperate without requiring one operator to own the entire stack.

## Long-term vision

A task can move through a network of specialized nodes. Each node declares what it can do, what inputs it accepts, what evidence it returns, and under what operational constraints it runs. Agents compose these nodes into workflows, while verification and reputation make unreliable or malicious behavior visible.

A useful Dexinode network would:

- let small, local, or domain-specific models participate;
- keep sensitive work near its data when needed;
- survive the loss or refusal of any single provider;
- support multiple routing, verification, and settlement implementations;
- reward demonstrated capability rather than scale or branding alone;
- make handoffs inspectable, replayable, and contestable.

This remains the long-term possibility. The current research does not assume the network layer is the first or primary source of value. It first asks whether a trusted local control plane can own state, memory, context, tools, and verification while using Local and Remote Models through bounded contracts.

## Intended contribution

The project may contribute at three levels:

1. **Protocol:** interoperable descriptions and handoff contracts for AI skills.
2. **Runtime:** reference tools for discovery, routing, execution, verification, and recovery.
3. **Ecosystem:** portable evidence, reputation, and optional settlement across operators.

The protocol is the most important layer. A successful experiment should still be useful if the reference runtime is replaced.

## Design values

### Decentralization is a means

The goal is not decentralization for its own sake. It should improve resilience, access, privacy, interoperability, or competition. If a decentralized mechanism adds cost without one of those benefits, it should be questioned.

### Specialization should be measurable

A “specialist” is not a label chosen by its operator. It is a capability supported by versioned tests, provenance, operational history, and task-specific evidence.

### Verification is part of execution

A handoff is incomplete until the caller can evaluate whether the returned result satisfies the contract. Verification may be deterministic, model-assisted, replicated, human-reviewed, or combined.

### Diversity is a resilience property

Diversity includes model families, hardware, operators, jurisdictions, data sources, and verification methods. It reduces correlated failure and makes the network harder to disable or capture.

### Local participation should be practical

Idle compute and small models matter only if participation does not require running a full blockchain, exposing private data, or accepting unbounded liability.

## Non-goals for the first phase

- creating a new foundation model;
- promising AGI or autonomous civilization-scale coordination;
- launching a token or speculative market;
- solving universal truth or model alignment;
- fully permissionless execution before basic safety is demonstrated;
- replacing all centralized AI services.

## Success criteria

These are long-term network criteria, not the current research exit condition. The current exit condition is whether evidence supports a bounded Hybrid Resident-Agent architecture specification.

The idea becomes more credible if a prototype demonstrates all of the following:

- a task uses independently operated specialist nodes;
- capability discovery is based on machine-readable declarations;
- handoffs are observable and replayable;
- at least one incorrect or unavailable node is detected and bypassed;
- quality, latency, and cost can be compared with a single-model baseline;
- no central component is indispensable to the demonstration.

## Failure signals

We should be willing to narrow or stop the project if:

- coordination overhead consistently exceeds specialization benefits;
- verification costs approach or exceed execution costs;
- capability claims cannot remain trustworthy without one central authority;
- privacy, abuse prevention, or liability make open participation impractical;
- the same value is better achieved through a conventional local plugin system.
