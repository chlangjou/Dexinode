# Dexinode

> **Distributed Cognitive Execution Fabric — working project**

Dexinode explores an open execution layer in which a Consumer requests a bounded combination of cognitive capabilities, while independent Provider Nodes supply task-scoped Agent capacity, Skills, Operators, and Verification behind a stable execution contract.

The current project phase is no longer research-only. [ADR 0004](docs/decisions/0004-distributed-cognitive-execution-reference-slice.md) authorizes the first reference implementation defined by [Distributed Cognitive Execution Reference v0.3](docs/specifications/distributed-cognitive-execution-reference-v0.3.md).

## Current architecture

The external interaction is intentionally simple:

    Consumer
       |
       | TaskIntent + explicit TaskBundle
       v
    Dexinode selection / contract
       |
       v
    Provider Node
       |
       | isolated task-scoped Agent/Skill execution
       v
    Artifact + Execution Receipt
       |
       v
    Consumer acceptance

A Provider may internally use one Agent, a temporary Swarm, Decision Skills, domain Skills, deterministic Operators, Verifiers, recurrent reasoning, or another implementation. Those details are provider configuration, not the stable network abstraction.

## Core invariant

> **A Dexinode Provider receives no ambient requester authority.**

Consumer and Provider are separate security domains.

The Provider does not implicitly receive access to the Consumer filesystem, credentials, browser/session state, LAN, local Agent memory, tools, or durable state. It receives only the explicit Task Bundle and Execution Contract.

The reference Consumer requires no local model or GPU.

## What Dexinode is trying to provide

Dexinode aims to make cognitive execution describable and replaceable at the Provider boundary:

- task-level capability requirements rather than model names;
- Provider declarations of Agent capacity, Skills, Operators, Verifiers, constraints, and evidence support;
- hard-constraint provider matching;
- task-scoped execution contracts;
- isolated, ephemeral Provider execution;
- artifacts and verifiable execution receipts;
- provider-internal freedom to optimize Agent topology;
- later comparison by time-to-verified-result, cost, trust, privacy, and reliability.

## What a Skill means

A Skill is a versioned capability contract, not a model class.

A Skill may be implemented by:

- deterministic code;
- a tiny classifier or Decision model;
- an Adapter or parameter artifact;
- a complete local or remote model;
- an Agent;
- an Operator;
- a Verifier;
- a composite Provider pipeline.

The external contract and evidence matter more than the substrate.

## First reference vertical slice

The active v0.3 slice is:

    Consumer CLI
      -> static Provider Registry
      -> Provider selection
      -> Execution Contract
      -> isolated ephemeral Provider task sandbox
      -> provider-selected Agent/Skill execution
      -> verification
      -> Artifact + Execution Receipt
      -> Consumer acceptance

The initial task family is bounded repository exploration／analysis.

The first slice deliberately avoids global discovery, reputation, payment, federation, and custom model work. Its purpose is to validate Dexinode's own contract and isolation boundary.

## Why the direction changed

Early work tested whether distributed Specialist models and explicit routing could be the foundation.

- Gate A: **PASS / CLOSED** — bounded specialization exists in the pinned experiment.
- Gate B: **FAIL / CLOSED** — perfect broad-domain routing did not create material orchestration advantage in the pinned General／Math／Coder setup.

Subsequent architecture work moved the project away from one Skill = one model, one Skill = one node, and fixed Resident-model assumptions.

Recent ecosystem and research signals strengthened a capability-oriented interpretation: Agent workloads contain many narrow Decision functions; Agent runtimes increasingly compose Skills dynamically; specialized AI substrates can be much smaller than full models; high-frequency latent collaboration is often local to a cognitive island; Swarms introduce correlation and contamination risks; and deterministic authority remains separable from probabilistic cognition.

These are supporting signals, not proof that Dexinode will succeed. The remaining high-value uncertainty is now implementation-level.

## Repository map

- [Vision](docs/vision.md)
- [Core concepts](docs/core-concepts.md)
- [Architecture](docs/architecture.md)
- [Open questions](docs/open-questions.md)
- [Roadmap](docs/roadmap.md)
- [Current status](status/current.md)
- [ADR 0004 — Distributed Cognitive Execution phase transition](docs/decisions/0004-distributed-cognitive-execution-reference-slice.md)
- [Reference specification v0.3](docs/specifications/distributed-cognitive-execution-reference-v0.3.md)
- [ADR 0003 — Verifiable execution fabric](docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md)
- [Functional Cognitive Node reframing](docs/research/2026-09-16-functional-cognitive-node-reframing.md)
- [Jev / System-One reflex watch](docs/research/2026-09-16-jev-system-one-agent-reflex-watch.md)
- [Latent collaboration watch](docs/research/2026-09-19-latent-collaboration-context-exchange-watch.md)
- [Decision records](docs/decisions/README.md)

## Current status

- Stage: **Reference Implementation authorized**
- Active specification: **v0.3 Distributed Cognitive Execution Reference**
- Active experimental Gate: **none**
- Gate A: **PASS / CLOSED**
- Gate B: **FAIL / CLOSED**
- FIM / syntax-aware MVSS: **HOLD**
- Repository visibility: public
- License: undecided

## Current priorities

1. Freeze the v0.3 protocol objects in working code.
2. Build Consumer -> Provider -> Artifact/Receipt end to end.
3. Demonstrate Provider isolation and task-state cleanup.
4. Complete the same lifecycle with a mock backend and one real Agent backend.
5. Record reproducible implementation evidence.
6. Review whether the abstraction is still simpler and more useful than an ordinary single-runtime plugin system.

## Deferred

The current phase does not implement:

- permissionless discovery or open federation;
- marketplace or global reputation;
- token, payment, settlement, or disputes;
- cross-provider latent-state communication;
- requester-local raw shell or filesystem delegation;
- custom foundation-model training;
- a standing model leaderboard.

## Principles

1. Evidence over capability claims.
2. Explicit contracts over implicit prompt conventions.
3. Consumer and Provider trust domains remain separate.
4. No ambient requester authority for Providers.
5. Provider internals are replaceable behind the external capability contract.
6. Verification is part of execution.
7. Complete configurations and receipts over model-only claims.
8. Task-scoped ephemeral execution by default.
9. Decentralization is justified by measurable resilience, privacy, interoperability, access, competition, or anti-capture value.
10. Research informs implementation but does not indefinitely postpone it.
