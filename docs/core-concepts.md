# Core concepts

These definitions are provisional. They exist to keep discussion precise and will change as experiments reveal better boundaries.

## Node

An independently operated runtime that can receive, execute, or forward work. A node may host one or more models, tools, data sources, agents, knowledge artifacts, operators, or verifiers.

A node is an operational and trust boundary—not necessarily one physical machine and not necessarily one model.

## Skill

A versioned, addressable capability contract offered by a node or provider.

A Skill is an externally observable promise about behavior under stated conditions. It is **not** a claim that the capability occupies one model, one Adapter, one J-Space location, or one network node. Its implementation may combine models, parameter artifacts, knowledge sources, memory, deterministic algorithms, tools, agents, Remote services, verifiers, and humans.

A useful Skill declaration should eventually describe:

- purpose and scope;
- input and output schemas;
- constraints and side effects;
- privacy and data-retention policy;
- resource, latency, and price expectations;
- model／artifact／tool／runtime provenance where disclosure is possible;
- supported verification methods;
- failure and cancellation behavior;
- compatibility and versioning rules.

## Model

A learned inference component used by a Skill or Local Decision Configuration. A Skill may use no model, one model, or several models. Dexinode should route by demonstrated capability, not model brand alone.

## Agent

A component that plans, selects Skills, manages state, evaluates results, and decides whether to continue, retry, verify, or escalate.

An agent can also expose a Skill. The distinction is functional:

- a **Skill** is the contract visible to callers;
- an **agent** manages a process;
- a **model** supplies learned inference;
- a **node** operates a runtime／trust boundary.

## Agent configuration

The complete system evaluated for a task:

`model(s) + memory + context policy + harness/loop + tools + verifier(s) + search/stopping policy + fallback + human policy + runtime/hardware`

Dexinode should not attribute a result to a model when a large memory backbone, judge, retry budget, operator, or Remote fallback supplied material capability.

Parameter count, active parameters, advertised context, and tokens per second are configuration metadata. None is a complete capability identity.

## Local control plane

Trusted deterministic software and policy that owns the workspace, durable memory, provenance, credentials, tool authority, privacy mappings, budgets, audit log, escalation, and final integration.

It may use learned models, but its durable state and security decisions must not exist only inside a model context or latent workspace.

## Local Decision Configuration

The complete learned and procedural configuration inside the local trust boundary for one task run:

`model(s) + memory/context policy + harness/loop + tools + verifier(s) + search/stopping policy + fallback/human policy + runtime/hardware`

It may use one general model, multiple local models, Specialists, deterministic algorithms, visible token loops, or latent/recurrent inference. Each actual component and role must remain attributable.

The Local Decision Configuration may make bounded semantic decisions, generate or select proposals, and request tools. It does not own canonical state, credentials, policy override, direct side effects, or final external publication authority.

## Cognitive Core

A provisional research term for the minimum broadly pretrained local substrate able to integrate a task rather than merely supply one narrow capability.

A complete Cognitive Core may include:

- language and semantic grounding;
- broadly reusable concepts and world priors;
- automatic foundation capabilities;
- deliberate reasoning, planning, clarification, abstention, and escalation;
- a mechanism for preserving and reusing task-relevant intermediate state;
- integration of external knowledge, memory, operators, tools, and verifier feedback.

A Cognitive Core may be one model or several tightly coupled components. It is one possible organization inside a Local Decision Configuration, not a new authority boundary and not a fixed parameter range.

## Deliberative workspace

A limited internal medium through which a Cognitive Core may hold, transform, and broadcast task-relevant intermediate state for flexible reasoning.

J-Space is one research example of workspace-like representations. Dexinode does not require J-Space, does not treat raw latent vectors as a protocol, and does not assume the workspace is the whole reasoning engine. Automatic capabilities and the circuits that read, write, and operate on workspace state remain part of the complete Cognitive Core.

## Knowledge and memory plane

Sources outside the immediate Cognitive Core that provide factual, current, private, domain, episodic, or project state. Examples include documents, databases, retrieved context, structured memory, indexes, and parameterized knowledge artifacts.

The plane must preserve source, version, validity, conflict, trust, revocation, and provenance. Correct retrieval is not equivalent to correct downstream integration.

## Operator capability

A bounded component that performs a transformation or analysis rather than merely returning facts. It may be a deterministic algorithm, compiler, solver, tool, Adapter, Specialist model, agent, Remote service, or human contribution.

An operator should return a typed artifact or integration packet that preserves relevant claims, relations, constraints, uncertainty, evidence, and unresolved questions. It does not automatically own the complete task or final decision.

## Resident Core

The earlier, narrower candidate in which one Local Resident Model plus deterministic support remains available to manage a workflow:

`Local general model + memory + context orchestrator + tools/verifiers + task state`

The **Minimum Viable Resident Core (MVRC)** remains useful historical terminology. Under ADR 0003, a Resident Core is one possible Local Decision Configuration, not a mandatory single-model architecture. Under the Cognitive Decomposition Hypothesis, the broader research question is the minimum viable complete Cognitive Core and its externalizable boundaries. Any viability claim is task- and resource-conditioned and cannot be reduced to model parameter count.

## Specialist

A model, operator, or complete service optimized for a bounded task contract. A Specialist may run locally or remotely and may return an intermediate claim, typed artifact, score, refusal, clarification, or final result. Its identity comes from measured capability, interface, verifier, runtime, and version—not a checkpoint label.

The **Minimum Viable Specialist Scale (MVSS)** remains task-conditioned historical terminology: the smallest complete Specialist service that meets a stated quality floor after context, runtime, verification, and lifecycle costs are included. It is no longer the project-defining scale question.

## Context packet

A bounded, task-scoped working set compiled from a larger workspace. It should include the goal, constraints, relevant source material, interfaces/dependencies, prior decisions, provenance, and validation method.

It is not a fixed-token chunk or an untraceable summary.

## Effective context envelope

The range in which a particular model/configuration can reliably use supplied context without unacceptable quality, latency, memory, or omission cost. It differs from the model's advertised maximum context window.

Current 8K–32K ranges are research assumptions documented in ADR 0001, not protocol constants.

## Remote escalation

A controlled handoff from the local control plane to a stronger or differently specialized Remote capability. Escalation should be task-scoped, privacy-constrained, budgeted, auditable, and locally verified.

Correct clarification, refusal, or escalation can satisfy a Specialist contract; standalone replacement is not required.

## Pseudonymization / restoration

A reversible local mapping between sensitive identifiers and stable placeholders. The mapping remains local, replacement/restoration is deterministic, and integrity failures should fail closed.

Pseudonymization is not full anonymization: unrecognized sensitive information, contextual re-identification, and semantic loss remain possible.

## Handoff contract

A machine-readable agreement for one delegation step. It binds a request to acceptance criteria and operational limits.

Candidate fields include:

- task and Skill identifiers;
- input schema and content references;
- expected output and evidence;
- time, compute, privacy, and cost limits;
- permitted tools and side effects;
- verification policy;
- retry, timeout, cancellation, and dispute rules;
- provenance chain and cryptographic signatures.

The contract should make failure explicit instead of relying on conversational implication.

## Capability claim

A node's or provider's assertion that it can perform a Skill under stated conditions. A claim is discoverable metadata, not proof.

## Evidence

An artifact that supports a result or capability claim: deterministic test output, signed execution record, source reference, reproducible trace, benchmark result, verifier judgment, or human approval.

Evidence strength is task-dependent.

## Verifier

A party or mechanism that evaluates a result against the handoff contract. It may be local, remote, deterministic, model-based, replicated, or human.

Verifiers can also be wrong or collude, so their judgments need provenance and reputation.

Verifier identity should include revision, environment, scope, coverage limitations, independence from the generator and selector, and what feedback was exposed during candidate search.

## Attempt

One bounded proposal-generation and verification path inside a run. An attempt has a hypothesis, parent lineage, configuration, context packet, budget, verifier exposure, sandbox, receipts, and terminal state.

Failed, invalid, cancelled, and rolled-back attempts are evidence and must not disappear merely because a later attempt succeeds.

## Candidate lineage

The causal graph connecting attempts and artifacts. It records whether a candidate was generated independently, mutated from an earlier proposal, repaired using verifier feedback, or derived from Local, Remote, deterministic, operator, or human work.

Lineage prevents correlated best-of-N results from being represented as independent trials.

## Selector

A fallible component or policy that compares eligible candidates and recommends a disposition using the task contract, verifier receipts, coverage, uncertainty, cost, and policy.

A selector cannot override a deterministic hard failure. When the same model generates and selects candidates, that coupling must be disclosed and is not independent verification.

## Search / stopping policy

The configured rules for how attempts are generated, diversified, repaired, compared, budgeted, and terminated.

More attempts improve the chance of finding a good candidate only when the candidate set, selector, and verifier support that inference. “Try until something passes” is not a valid unbounded policy.

## Reputation

A contextual summary of historical evidence. Reputation should be scoped by Skill, version, workload, verifier set, and time—not reduced prematurely to one global score.

## Router

A component that selects candidate Skills, knowledge sources, operators, configurations, or nodes based on capability, evidence, policy, availability, latency, cost, privacy, and diversity.

Routing is a policy choice. Broad domain classification alone is not a sufficient success predictor, and the network should allow competing routers.

## Registry

A discovery mechanism for publishing and finding Skill declarations, artifacts, evidence, and endpoints. A registry may be centralized, federated, peer-to-peer, or local. It should not become the sole authority on truth.

## Settlement

An optional mechanism for accounting or payment between parties. Settlement is deliberately separate from core task execution so the network can first prove technical value.

## Workflow

A graph of handoffs with shared state, budgets, recovery paths, and final acceptance criteria.

## Trust domain

A set of nodes governed by a common organization, policy, or identity authority. Dexinode should work inside one trust domain before attempting open, permissionless federation.