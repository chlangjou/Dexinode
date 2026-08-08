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
