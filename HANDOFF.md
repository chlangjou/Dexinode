# Dexinode Session Handoff

Repository: chlangjou/Dexinode

Canonical branch: main

Current integration branch: integration/reference-vertical-slice-v0.3

Current decision issue: [#42](https://github.com/chlangjou/Dexinode/issues/42)

Snapshot: 2026-09-28

Git is the durable source of truth.

## Start here

Read in this order:

1. AGENTS.md
2. HANDOFF.md
3. status/current.md
4. docs/decisions/0004-distributed-cognitive-execution-reference-slice.md
5. docs/specifications/distributed-cognitive-execution-reference-v0.3.md
6. docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md
7. docs/research/2026-09-16-functional-cognitive-node-reframing.md
8. docs/research/2026-09-16-jev-system-one-agent-reflex-watch.md
9. docs/research/2026-09-19-latent-collaboration-context-exchange-watch.md

Read Gate closure records only when historical empirical evidence is needed.

## Current phase

The project has formally transitioned from research-first exploration to:

> **Specification Convergence -> Reference Implementation -> Implementation Validation**

The active architecture framing is:

> **Dexinode is a Distributed Cognitive Execution Fabric.**

No new research Gate is required before the first implementation slice.

## Current implementation boundary

The first reference vertical slice is authorized by Issue #42 and ADR 0004:

    Client
      -> static Provider Registry
      -> Provider selection
      -> Execution Contract
      -> isolated ephemeral Provider task sandbox
      -> provider-selected Agent/Skill execution
      -> verification
      -> Artifact + Execution Receipt
      -> Client acceptance

The initial task family is bounded repository exploration／analysis.

The Consumer requires no local AI model or GPU.

## Mandatory invariants

1. **Consumer and Provider are separate security domains.**
2. **A Provider receives no ambient requester authority.**
3. Provider receives only the explicit Task Bundle and Execution Contract.
4. Provider internal Agent topology is replaceable and does not define the protocol.
5. Provider task state is ephemeral by default.
6. Network is deny-by-default for the reference task.
7. Provider cannot directly mutate Consumer durable state.
8. Deterministic hard failures cannot be overridden by Agent output.
9. Artifact and Execution Receipt hashes are validated by the Consumer.
10. Receipt identity binds the actual Provider configuration, capabilities used, verifier results, isolation state, and cleanup result.

## Allowed implementation work

Agents may now implement:

- v0.3 protocol models and schemas;
- Consumer CLI;
- static Provider Registry and deterministic matcher;
- Provider Runtime;
- sandbox lifecycle and isolation tests;
- mock backend adapter;
- one real Agent backend adapter;
- deterministic verifier;
- Artifact／Receipt production and validation;
- end-to-end reference demo and reproducibility evidence.

Use existing Agent runtimes or model APIs behind adapters where useful. Do not turn model selection into a new research program.

## Hard stop conditions

Do not broaden v0.3 into:

- permissionless or federated discovery;
- reputation or marketplace;
- payment, token, settlement, or disputes;
- cross-provider latent-state exchange;
- requester-local raw shell/filesystem access;
- credential delegation;
- custom foundation-model training;
- production security certification.

Gate A and Gate B remain closed. FIM remains HOLD.

## Preserved empirical state

### Gate A — PASS / CLOSED

Bounded same-family specialization exists in the pinned experiment.

### Gate B — FAIL / CLOSED

Perfect broad-domain routing did not produce material held-out orchestration advantage in the pinned configuration.

The durable lesson is that capability identity and routing must be task／configuration conditioned rather than broad model labels.

## Research posture

Research is now a watch lane. Record material developments only when they may change:

- capability contracts;
- Consumer／Provider isolation;
- Provider capacity semantics;
- Agent runtime composition;
- verifier independence;
- provenance and receipts;
- scheduling economics;
- security or authority boundaries.

Research notes do not automatically block or supersede the active v0.3 implementation.

## Completion condition

The reference slice is complete only after both:

- a deterministic/mock backend; and
- at least one real Agent backend

complete the same external lifecycle while satisfying the v0.3 contract, isolation, evidence, failure, and cleanup acceptance criteria.

Completion requires human review before expanding toward a second Provider, failover, capability-artifact distribution, or federation.
