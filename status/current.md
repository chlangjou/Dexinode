# Current Project Status

- Updated: 2026-09-28
- Current phase: **Specification Convergence -> Reference Implementation**
- Active implementation: **Distributed Cognitive Execution Reference v0.3**
- Active experimental Gate: **none**
- Gate A — Specialist Validation: **PASS / CLOSED**
- Gate B — Orchestration Advantage: **FAIL / CLOSED**
- FIM / syntax-aware MVSS eligibility: **HOLD**
- Current architecture decision: [ADR 0004](../docs/decisions/0004-distributed-cognitive-execution-reference-slice.md)
- Preserved architecture foundation: [ADR 0003](../docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md)
- Current implementation specification: [Distributed Cognitive Execution Reference v0.3](../docs/specifications/distributed-cognitive-execution-reference-v0.3.md)
- Authorizing decision: [Issue #42](https://github.com/chlangjou/Dexinode/issues/42)
- Integration branch: integration/reference-vertical-slice-v0.3

## Phase transition

Dexinode is no longer blocked on another research Gate before implementation.

The working architecture is now:

> **Distributed Cognitive Execution Fabric**

A Consumer expresses a bounded task-level cognitive execution intent. A Provider Node supplies task-scoped Agent capacity and declared capabilities, chooses its own internal Agent／Skill／Operator／Verifier topology, executes inside an isolated environment, and returns Artifact(s) plus an Execution Receipt.

Research remains active as a watch lane but does not block v0.3 unless new evidence changes a core contract, isolation invariant, verification assumption, or Provider execution boundary.

## Mandatory architecture invariants

### Consumer and Provider are separate security domains

The Consumer owns:

- private source material before explicit disclosure;
- credentials and identity;
- local filesystem and browser/session state;
- local Agent memory;
- privacy and disclosure policy;
- final durable-state acceptance.

The Provider owns its own execution environment and receives only the explicit Task Bundle and Execution Contract.

### No ambient requester authority

> **A Dexinode Provider receives no ambient requester authority.**

Provider execution must not implicitly inherit requester filesystem access, credentials, browser/session state, LAN access, local tools, durable memory, environment variables, or policy authority.

### Provider internal topology is replaceable

A Provider may internally use:

- one Agent;
- multiple exploration Agents plus synthesis;
- Decision Skills;
- domain Skills;
- deterministic Operators;
- Verifiers;
- recurrent／latent mechanisms;
- local or API-backed models.

The Consumer contract must not depend on one specific topology.

### Task execution is ephemeral by default

Provider task state is isolated per request and destroyed or quarantined after completion. Cognitive or workspace state must not silently persist across unrelated tasks or requesters.

## Active reference vertical slice

The first slice is:

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

The reference Consumer requires no local model or GPU.

## Implementation authorization

v0.3 authorizes implementation of:

- protocol data models and schema validation;
- static Provider Registry;
- deterministic hard-constraint provider matching;
- Consumer CLI;
- Provider Runtime;
- task-scoped sandbox lifecycle;
- network-denied reference execution;
- deterministic/mock Agent backend adapter;
- one real external Agent backend adapter;
- Artifact and Execution Receipt generation／validation;
- deterministic verifier adapter;
- isolation, failure-path, cleanup, and reproducibility tests.

Implementation may use existing Agent runtimes or model APIs behind a provider adapter. The project does not need to select or train its own model to complete v0.3.

## Explicitly deferred

Do not implement in v0.3:

- public or permissionless discovery;
- federation governance;
- marketplace or global reputation;
- token, payment, settlement, or disputes;
- cross-provider latent／KV exchange;
- requester-local raw shell or filesystem access;
- credential delegation;
- custom model training;
- a standing model leaderboard;
- production security certification.

## Preserved empirical state

### Gate A

Gate A remains **PASS / CLOSED**. It established measurable specialization on one pinned same-family panel.

Durable lesson: a checkpoint or domain label is not a capability identity.

### Gate B

Gate B remains **FAIL / CLOSED**.

Frozen result:

| Policy | Overall | Mathematics | Coding |
|---|---:|---:|---:|
| General-only | 76/96 = 79.17% | 40/48 = 83.33% | 36/48 = 75.00% |
| Skill-routed | 77/96 = 80.21% | 41/48 = 85.42% | 36/48 = 75.00% |

Durable lesson: broad-domain classification is not per-task success prediction, and selecting one whole-model Specialist is not a sufficient orchestration architecture.

## Preserved research watch

The following remain relevant but are not implementation prerequisites:

- Cognitive Decomposition and minimum-core research;
- DMoE and modular knowledge／capability artifacts;
- J-Space／J-CoT and recurrent reasoning;
- Jev／System-One-like high-frequency Decision Skills;
- Functional Cognitive Nodes;
- latent collaboration and Cognitive ABI questions;
- Agent Swarm coupling, epistemic independence, and memory contamination;
- deterministic post-compromise execution governance.

FIM remains HOLD.

## Current success question

The first implementation is not trying to prove that Dexinode has better AI.

It asks:

> **Can one stable Consumer／Provider contract support isolated, replaceable cognitive execution and produce useful artifacts plus trustworthy execution evidence without granting the Provider ambient requester authority?**

If the answer is no, the architecture must be revised before federation or promotion.
