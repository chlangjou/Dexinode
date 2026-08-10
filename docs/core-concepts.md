# Core concepts

These definitions are provisional. They exist to keep discussion precise and will change as experiments reveal better boundaries.

## Node

An independently operated runtime that can receive, execute, or forward work. A node may host one or more models, tools, data sources, agents, or verifiers.

A node is an operational and trust boundary—not necessarily one physical machine.

## Skill

A versioned, addressable capability offered by a node.

A useful skill declaration should eventually describe:

- purpose and scope;
- input and output schemas;
- constraints and side effects;
- privacy and data-retention policy;
- resource, latency, and price expectations;
- model/tool/runtime provenance where disclosure is possible;
- supported verification methods;
- failure and cancellation behavior;
- compatibility and versioning rules.

## Model

A learned inference component used by a skill. A skill may use no model, one model, or several models. Dexinode should route by demonstrated capability, not model brand alone.

## Agent

A component that plans, selects skills, manages state, evaluates results, and decides whether to continue, retry, verify, or escalate.

An agent can also expose a skill. The distinction is functional:

- a **skill** is the contract visible to callers;
- an **agent** manages a process;
- a **model** supplies learned inference;
- a **node** operates the runtime.

## Agent configuration

The complete system evaluated for a task:

`model + memory + context policy + harness/loop + tools + verifier + fallback + human review`

Dexinode should not attribute a result to a model when a large memory backbone, judge, retry budget, or remote fallback supplied material capability.

## Local control plane

Trusted deterministic software and policy that owns the workspace, durable memory, provenance, credentials, tool authority, privacy mappings, budgets, audit log, escalation, and final integration.

It may use learned models, but its durable state and security decisions must not exist only inside a model context.

## Resident Core

The local configuration that remains available to manage a workflow:

`Local general model + memory + context orchestrator + tools/verifiers + task state`

The **Minimum Viable Resident Core (MVRC)** is the smallest such complete configuration that remains reliable enough for a specified workflow and resource envelope. It is not merely the parameter count of the local model.

## Specialist

A model or complete service optimized for a bounded task contract. A specialist may run locally or remotely; its identity comes from measured capability, interface, verifier, runtime, and version—not a checkpoint label.

The **Minimum Viable Specialist Scale (MVSS)** is task-conditioned: the smallest complete specialist service that meets a stated quality floor after context, runtime, verification, and lifecycle costs are included.

## Context packet

A bounded, task-scoped working set compiled from a larger workspace. It should include the goal, constraints, relevant source material, interfaces/dependencies, prior decisions, provenance, and validation method.

It is not a fixed-token chunk or an untraceable summary.

## Effective context envelope

The range in which a particular model/configuration can reliably use supplied context without unacceptable quality, latency, memory, or omission cost. It differs from the model's advertised maximum context window.

Current 8K–32K ranges are research assumptions documented in ADR 0001, not protocol constants.

## Remote escalation

A controlled handoff from the local control plane to a stronger or differently specialized remote capability. Escalation should be task-scoped, privacy-constrained, budgeted, auditable, and locally verified.

Correct clarification, refusal, or escalation can satisfy a specialist contract; standalone replacement is not required.

## Pseudonymization / restoration

A reversible local mapping between sensitive identifiers and stable placeholders. The mapping remains local, replacement/restoration is deterministic, and integrity failures should fail closed.

Pseudonymization is not full anonymization: unrecognized sensitive information, contextual re-identification, and semantic loss remain possible.

## Handoff contract

A machine-readable agreement for one delegation step. It binds a request to acceptance criteria and operational limits.

Candidate fields include:

- task and skill identifiers;
- input schema and content references;
- expected output and evidence;
- time, compute, privacy, and cost limits;
- permitted tools and side effects;
- verification policy;
- retry, timeout, cancellation, and dispute rules;
- provenance chain and cryptographic signatures.

The contract should make failure explicit instead of relying on conversational implication.

## Capability claim

A node's assertion that it can perform a skill under stated conditions. A claim is discoverable metadata, not proof.

## Evidence

An artifact that supports a result or capability claim: deterministic test output, signed execution record, source reference, reproducible trace, benchmark result, verifier judgment, or human approval.

Evidence strength is task-dependent.

## Verifier

A party or mechanism that evaluates a result against the handoff contract. It may be local, remote, deterministic, model-based, replicated, or human.

Verifiers can also be wrong or collude, so their judgments need provenance and reputation.

## Reputation

A contextual summary of historical evidence. Reputation should be scoped by skill, version, workload, verifier set, and time—not reduced prematurely to one global score.

## Router

A component that selects candidate skills or nodes based on capability, evidence, policy, availability, latency, cost, privacy, and diversity.

Routing is a policy choice. The network should allow competing routers.

## Registry

A discovery mechanism for publishing and finding skill declarations and endpoints. A registry may be centralized, federated, peer-to-peer, or local. It should not become the sole authority on truth.

## Settlement

An optional mechanism for accounting or payment between parties. Settlement is deliberately separate from core task execution so the network can first prove technical value.

## Workflow

A graph of handoffs with shared state, budgets, recovery paths, and final acceptance criteria.

## Trust domain

A set of nodes governed by a common organization, policy, or identity authority. Dexinode should work inside one trust domain before attempting open, permissionless federation.
