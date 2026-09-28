# 0004 — Transition Dexinode to a distributed cognitive execution fabric and authorize the first reference vertical slice

- Status: Accepted
- Date: 2026-09-28
- Deciders: Human project owner
- Decision issue: [#42](https://github.com/chlangjou/Dexinode/issues/42)
- Builds on: [ADR 0003](0003-resource-bounded-verifiable-execution-fabric.md)
- Supersedes: None
- Superseded by: None

## Context

Dexinode began as an investigation into distributed Specialist models and explicit model-to-model routing. Gate A established bounded specialization in one pinned same-family model panel. Gate B then showed that even perfect broad-domain routing did not create material orchestration advantage for the pinned General／Math／Coder configuration.

ADR 0003 responded by moving the architecture away from a fixed small Resident model and toward a trusted control plane plus a replaceable, resource-bounded verifiable execution／search configuration.

Subsequent research and ecosystem signals have converged on a more implementation-relevant boundary:

- useful Agent workloads contain many narrow, high-frequency decisions that need not invoke full deliberate reasoning;
- Agent capabilities are increasingly runtime-composable rather than permanently bound to one Agent identity;
- narrow AI capabilities may be implemented by tiny classifiers, adapters, deterministic operators, complete models, or composite pipelines;
- high-frequency latent／recurrent collaboration is more naturally contained inside a trust-local cognitive island than exposed as a wide-area protocol;
- persistent multi-Agent interaction can increase correlation, memory contamination, and verifier exposure;
- deterministic execution authority should remain separable from probabilistic cognition, including after compromise;
- a remote execution provider should not inherit requester-local filesystem, credentials, browser state, LAN access, durable memory, or other ambient authority.

These observations do not prove a Dexinode network will be useful. They do change which uncertainty now has the highest decision value. The dominant unknown has moved from whether specialization or modular cognition can exist toward whether a capability-oriented, isolated cognitive execution contract can be implemented cleanly enough to support replaceable providers.

## Decision drivers

- Stop treating additional literature as a prerequisite when the remaining uncertainty is mainly engineering and systems integration.
- Preserve ADR 0003 deterministic authority, provenance, verification, stopping, and audit principles.
- Separate the requester trust domain from provider execution.
- Make Agent, model, Skill, and topology replaceable behind a stable external contract.
- Allow a Provider Node to expose multiple Agent-capacity classes and specialized capabilities without making each Agent a network identity.
- Optimize provider competition around verified task results rather than model labels or tokens per second.
- Keep the first implementation narrow enough to falsify the architecture before federation, reputation, payment, or marketplace work.

## Options considered

### Continue research-first and defer implementation

This preserves maximum flexibility but has declining decision value. Many new papers now add supporting examples without resolving the practical contract, isolation, scheduling, lifecycle, and evidence questions that require implementation.

### Implement the existing v0.2 repository-repair architecture directly

This would produce code, but it would preserve an older local-first framing that no longer cleanly reflects the Consumer／Provider separation and cognitive-execution-provider model.

### Build a network-first marketplace or federation layer

This would prematurely commit to discovery, reputation, settlement, and governance before the execution contract and isolation model have demonstrated value.

### Transition to a narrow distributed cognitive execution reference slice

This tests the new boundary directly while preserving model and Agent-runtime replaceability.

## Decision

Adopt the working architecture framing:

> **Dexinode is a Distributed Cognitive Execution Fabric.**

The stable external unit is a task-scoped cognitive execution contract. A Provider Node may internally compose one or more Agents, models, Decision Skills, domain Skills, Operators, Verifiers, deterministic tools, or recurrent／latent processes. Those internals are not the primary network abstraction.

### Consumer trust domain

The Consumer side owns:

- user intent and task state;
- private source material before explicit disclosure;
- credentials and identity;
- local filesystem and browser/session state;
- privacy and disclosure policy;
- provider-selection policy and budget;
- received artifacts and receipts;
- final durable-state acceptance.

The first reference slice requires no local model or GPU.

### Provider execution domain

A Provider Node offers one or more cognitive execution capacities and declares:

- capability contracts;
- Agent or execution slot capacity;
- supported Skill／Operator／Verifier classes;
- resource and runtime constraints;
- latency／cost metadata when known;
- isolation and persistence behavior;
- evidence and receipt support.

Provider-internal cognitive topology remains implementation-specific.

### Mandatory isolation invariant

> **A Dexinode Provider receives no ambient requester authority.**

The Provider may access only data and capabilities explicitly granted by the task bundle and Execution Contract. It does not implicitly inherit requester-local filesystem, credentials, browser/session state, LAN access, local tools, durable memory, or policy authority.

Requester-local AI integration is optional and is not part of Provider execution authority.

### Task-scoped execution

Provider execution is ephemeral by default:

1. receive a bounded Task Bundle and Execution Contract;
2. create an isolated task workspace;
3. load only the declared capability configuration;
4. execute the provider-selected cognitive topology;
5. run required verification;
6. emit Artifact(s) and an Execution Receipt;
7. destroy or quarantine task state according to the declared retention policy.

Cognitive state does not persist across requesters or unrelated tasks by default.

### Authority and side effects

Network, filesystem, tool, credential, and external side-effect access are capabilities, not ambient resources.

The first reference slice uses:

- sandbox-only filesystem access;
- no requester-local mount;
- no requester credential forwarding;
- network deny-by-default;
- no direct mutation of requester durable state.

A later protocol may permit explicit, bounded delegation to requester-local capability gateways, but that is not part of the first slice.

### Optimization target

Provider quality should eventually be evaluated around:

> **time-to-verified-result under task, cost, trust, privacy, and reliability constraints**

rather than raw token throughput or advertised model capability.

## First reference vertical slice

Authorize implementation of the specification:

docs/specifications/distributed-cognitive-execution-reference-v0.3.md

The slice is intentionally narrow:

    Client
      -> static Provider Registry
      -> Provider selection
      -> Execution Contract
      -> isolated ephemeral Provider task sandbox
      -> provider-selected Agent/Skill execution
      -> verification
      -> Artifact + Execution Receipt
      -> Client acceptance

The initial slice validates Dexinode own contract and execution boundary, not underlying model intelligence.

## Consequences

### Required

- Consumer and Provider are separate roles and security domains.
- Provider code must not assume access to requester-local ambient resources.
- Provider internal Agent topology must be swappable without changing the external request／result contract.
- Capability use and execution configuration must be attributable in receipts.
- Deterministic hard failures remain authoritative over model or Agent output.
- Reference implementation work may now begin under the accepted v0.3 slice.

### Preserved

- Gate A remains PASS / CLOSED.
- Gate B remains FAIL / CLOSED.
- FIM／syntax-aware MVSS remains HOLD.
- ADR 0003 deterministic control, provenance, verification, search／stopping, rollback, and audit principles remain valid.
- Cognitive Decomposition, Functional Cognitive Node, Jev-like Decision Plane, latent collaboration, and other research items remain implementation-neutral watch items.

### Changed

- The project is no longer blocked on a new research Gate before implementation.
- Research becomes a watch lane rather than the primary workstream.
- The near-term product boundary is no longer a local-first Resident／Local Decision Configuration experiment.
- The Provider Node is treated as a cognitive execution service that may host multiple Agent capacities and Skills.
- A Local Agent is a possible Consumer, not a required Dexinode runtime component.

### Explicitly deferred

- global or permissionless discovery;
- marketplace and global reputation;
- token, payment, settlement, or dispute systems;
- federation governance;
- cross-provider latent-state exchange;
- provider-to-requester raw shell or filesystem access;
- custom foundation-model training;
- a standing model leaderboard;
- production security certification.

## Validation

ADR 0004 should be reconsidered if the reference implementation shows that:

1. useful Provider execution requires ambient requester authority;
2. Provider-independent contracts cannot express practical Agent workloads;
3. execution receipts cannot preserve enough configuration and evidence identity to compare providers;
4. isolation and lifecycle overhead dominate practical value;
5. the same outcome is materially simpler as an ordinary single-runtime plugin system with no provider boundary;
6. consumers cannot express capability requirements without embedding provider-specific implementation details.

Success of the first slice does not prove open federation or economic viability. It only establishes that the execution abstraction is implementable enough to justify the next stage.
