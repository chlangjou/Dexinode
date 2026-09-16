# Functional Cognitive Node reframing — from distributed models to distributed capability nodes

- Date: 2026-09-16
- Status: **research framing / no architecture supersession**
- Relation to current architecture: **compatible with ADR 0003; does not modify Gate A, Gate B, FIM HOLD, or the current authorization boundary**
- Trigger: follow-on discussion after the Jev/System-One reflex-layer watch note

## Why this is being retained

Dexinode began with a relatively model-centric intuition:

> distributed specialist models may let Agents obtain useful capability without depending completely on frontier-model APIs.

Recent work has made that unit of distribution look too narrow. A modern Agent or capability provider may increasingly be a composite system containing a Cognitive Core, local reflex／System-One decision mechanisms, Knowledge／Memory, deterministic Operators, Verifiers, policies, and possibly other Agents or remote fallbacks.

The useful distributed object may therefore be better treated as a **functional cognitive node** rather than a model endpoint.

The node is defined by the capability contract it can fulfill and the evidence attached to that capability. Its internal model topology is an implementation detail unless it materially affects trust, cost, latency, provenance, or reproducibility.

## Working reframing

### Earlier model-centric framing

```text
Agent
  |
  +-- frontier model API
  +-- local specialist model
  +-- remote specialist model
  +-- tools
```

The principal distributed object is a model endpoint. Routing primarily selects which model should answer.

### Emerging node-centric framing

```text
Requester / Orchestrator
          |
     Dexinode fabric
          |
  +-------+-------+
  |               |
  v               v
Capability Node A Capability Node B
  |               |
  +-- Core        +-- Core / Agent
  +-- Reflex      +-- Knowledge
  +-- Knowledge   +-- Operators
  +-- Operators   +-- Verifiers
  +-- Verifiers   +-- Policy
```

The principal distributed object is a provider that can fulfill a capability contract. A model is only one possible internal component.

## Functional cognitive node

Working definition:

> A **Functional Cognitive Node** is a bounded provider that can independently accept and fulfill a declared capability contract, while exposing enough identity, provenance, cost, latency, authority, verification, and failure information for another system to compose with it safely.

A node may contain:

- one or more Agents or Cognitive Cores;
- a local high-frequency reflex subsystem such as Jev/System-One-like typed decision primitives;
- shared base models plus adapters／LoRAs or other specialization mechanisms;
- external or local Knowledge／Memory;
- deterministic Operators and tools;
- independent or partially independent Verification;
- routing, search, stopping, fallback, and escalation policy;
- local or remote compute resources.

This is a composition envelope, not a mandatory checklist.

## Agent is common, but is not the node definition

Many useful nodes will likely contain an Agent because the capability requires planning, interpretation, tool use, iteration, or local orchestration.

However, Dexinode should avoid replacing the old assumption:

```text
Skill == Model
```

with another hard binding:

```text
Node == Agent
```

Some valid providers may be mostly deterministic, retrieval-oriented, verification-oriented, or narrowly learned. The stable external abstraction is the capability contract and evidence, not whether the implementation deserves the label "Agent".

## Jev/System-One implication

The Jev discussion strengthens the node-centric view because high-frequency, low-latency reflex decisions are likely to be colocated with the Agent or workflow that uses them rather than exposed individually as network providers.

A plausible node-internal structure is:

```text
Functional Node
  |
  +-- Cognitive Core / Agent
  |
  +-- Reflex Subsystem
  |     +-- shared Jev-like base
  |     +-- optional domain adapters
  |     +-- many typed reflex contracts
  |
  +-- Knowledge
  +-- Operators
  +-- Verifiers
  +-- Policy
```

This remains an implementation hypothesis. Jev's published architecture does not currently establish that its real deployment is a shared base plus LoRA pool.

The durable point is architectural: **small, high-frequency learned control is more naturally an internal node resource than a separate wide-area network hop**.

## Two orchestration scales

The node-centric framing suggests at least two distinct orchestration regimes.

### Intra-node orchestration

Likely characteristics:

- high frequency;
- low latency;
- tightly coupled state;
- local shared memory／cache;
- reflex routing, pruning, stopping, escalation, and tool selection;
- implementation-specific behavior.

### Inter-node orchestration

Likely characteristics:

- coarser capability contracts;
- lower interaction frequency;
- explicit input／output boundaries;
- stronger provenance and trust requirements;
- higher tolerance for network latency;
- provider replaceability.

Therefore retain the hypothesis:

```text
intra-node coupling != inter-node coupling
```

This complements the earlier Jev watch hypothesis:

```text
control-coupling frequency != information-coupling frequency
```

## Frontier independence is broader than local-model substitution

Earlier intuition could be stated as:

```text
frontier independence ~= replace frontier API with local / distributed models
```

The stronger working interpretation is:

> **Frontier independence means avoiding a single mandatory intelligence dependency.**

A Dexinode workflow may still use a frontier model as escalation, fallback, or specialist support while preserving useful local and distributed capability when that frontier provider is unavailable, undesirable, too expensive, or outside policy.

Illustrative structure:

```text
mostly local node execution
       +
distributed capability nodes
       +
optional frontier escalation
```

The objective is not necessarily `zero frontier usage`; it is to make frontier access non-exclusive and replaceable where practical.

## Consequence for provider identity

Provider identity should increasingly describe a complete capability configuration rather than only a checkpoint.

Relevant identity may include:

- declared capability contract;
- Cognitive Core／Agent configuration;
- reflex subsystem and adapter set when material;
- Knowledge versions;
- Operators and tool authority;
- Verifier set and independence properties;
- runtime／hardware;
- search, stopping, fallback, and escalation policy;
- provenance and human／remote contribution boundaries.

This is consistent with ADR 0003's `Local Decision Configuration` framing and with Gate B's durable lesson that broad-domain model selection is not a sufficient composition architecture.

## Possible Dexinode evolution

Retain the following as a useful conceptual progression rather than a committed roadmap:

```text
V0  Distributed Specialist Models
          |
          v
V1  Distributed Skills / Cognitive Components
          |
          v
V2  Distributed Functional Cognitive Nodes
          |
          v
    Composable Intelligence Fabric
```

The emerging research question is correspondingly broader:

> **How can heterogeneous distributed cognitive systems compose safely, economically, and verifiably?**

rather than only:

> Which distributed model should answer this task?

## Implications for future research

Questions worth preserving for later work:

1. What is the minimum useful external capability contract for a functional node?
2. Which internal properties must be disclosed for trust and reproducibility, and which may remain implementation details?
3. How should Dexinode distinguish a node's claimed capability from measured capability evidence?
4. How should node-level Verification compose when each node also has internal Verifiers?
5. When should an internal cognitive component become a separately addressable provider?
6. How should cost／latency／privacy／availability determine local execution, peer-node delegation, and frontier escalation?
7. Can a network of heterogeneous nodes demonstrate measurable composition value beyond the best single provider?
8. How should failure attribution work across nested Agents, reflex subsystems, tools, and peer nodes?

## Non-decisions

This note does **not**:

- supersede ADR 0003;
- define a new protocol or provider API;
- authorize federation, marketplace, reputation, settlement, or governance implementation;
- reopen Gate A or Gate B;
- resolve FIM HOLD;
- select Jev, LoRA, a base model, or any specific node implementation;
- authorize inference, training, deployment, benchmark creation, or a new experimental Gate.

It records a durable research framing so later Dexinode work does not implicitly collapse `capability provider` back into `model endpoint`.