# Candidate architecture

This document records a design space, not a frozen system architecture.

The current research frame is recorded in [ADR 0001](decisions/0001-hybrid-resident-agent-research-frame.md). It does not assert that the architecture is production-viable.

## Current candidate: Hybrid Resident-Agent configuration

The nearest-term system boundary is local-first, not local-only:

`deterministic local software + Local Resident Model + memory/context orchestration + tools/verifiers + optional Local Specialist + Remote Model escalation + human review`

The research unit is the complete configuration. A model score that omits the memory manager, context policy, retries, verifier, fallback, and human review is incomplete evidence.

### Responsibility hypothesis

| Component | Candidate responsibility | Constraint / uncertainty |
|---|---|---|
| Deterministic local software | storage, indexes, versions, credentials, permissions, tool execution, pseudonymization maps, budgets, audit log | engineering feasibility is high, but sensitive-entity detection and policy completeness are not automatic |
| Local Resident Model | clarify intent, interpret task state, propose decomposition/context expansion, select bounded tools, decide clarification/refusal/escalation | MVRC is open; function calling alone does not establish failure recovery or multi-step integration |
| Local Specialist | execute a narrow, explicit, locally verifiable contract | MVSS and structural transfer are task-conditioned; labels and active parameters are not sufficient evidence |
| Remote Model | perform a task-scoped difficult subtask or produce a candidate artifact | receives minimum context; must not own durable memory, credentials, or unverified side effects |
| Human reviewer | approve ambiguity, sensitive mappings, high-impact actions, and research decisions | active human time is part of system cost, not a free verifier |

### Local ownership and trust boundary

The local control plane should retain:

- the original workspace and long-term memory;
- current task state, provenance, and evidence;
- pseudonymization/restoration mappings;
- tool credentials, permissions, and side-effect policy;
- loop budget, stopping conditions, and failure history;
- remote escalation policy and final artifact integration.

A Remote Model should receive only the context packet required for one subtask. If every material step still requires a Remote Model, the Local Resident Model's practical value must be treated as unproven rather than assumed.

### Memory and context lifecycle

1. Store raw source, versions, task state, decisions, test results, and failure records outside model context.
2. Retrieve candidate evidence for the current contract.
3. Reconcile updates, conflicts, stale facts, and provenance.
4. Compile a bounded context packet with goal, constraints, relevant source, interfaces, prior decisions, and verification method.
5. Execute locally or escalate the packet.
6. Verify the returned artifact and write back only confirmed state.

The v0.1 effective-context ranges are working assumptions, not frozen limits:

| Invocation | Target | Provisional handling beyond target |
|---|---:|---|
| Local Specialist | 8K–16K tokens | 32K provisional ceiling |
| Local Resident Model | 16K–32K tokens | 64K+ normally requires retrieval, decomposition, or summarization |
| Repository/history/long-term memory | outside model context | local indexed storage with source/version provenance |

Semantic boundaries—module, API, data structure, test, or workflow state—should drive decomposition. Fixed token slicing alone is not sufficient.

### Local pseudonymization and restoration

This is treated as an engineerable safety component rather than a core model-scale hypothesis:

1. a local model proposes sensitive or equivalent-entity candidates;
2. a human approves the mappings when required;
3. deterministic code applies stable placeholders and keeps the map local;
4. placeholder integrity is checked before restoration;
5. replacement, approval, failure, and restoration are audited.

This can guarantee round-trip behavior for approved mappings. It cannot guarantee complete sensitive-data discovery, immunity to contextual re-identification, or zero semantic loss.

### Candidate execution path

1. Clarify the user outcome, authority, quality floor, and failure cost.
2. Load trusted task/project state from local memory.
3. Compile a bounded context packet with provenance.
4. Select deterministic tooling, Local Resident Model, or a registered Local Specialist.
5. Clarify, refuse, or escalate when the packet or capability evidence is insufficient.
6. Send only a pseudonymized, task-scoped packet to a Remote Model when policy permits.
7. Validate schema, placeholders, tests, invariants, and side effects locally.
8. Integrate accepted artifacts and record evidence; do not persist unverified model summaries as fact.

## Current evidence boundary

- Gate A supports measurable specialization as a bounded existence claim.
- Gate B contradicts broad-domain labels as sufficient routing contracts.
- FIM / syntax-aware MVSS eligibility is `HOLD`.
- MVRC, automatic context compilation, agent-specialized absolute-small capability, and full hybrid user value remain open.
- No runtime prototype, benchmark, or experimental Gate is currently authorized.

## Long-term network interaction

1. A provider publishes a signed skill declaration.
2. A router discovers candidates that satisfy the request policy.
3. The caller proposes a handoff contract.
4. A selected node accepts, rejects, or negotiates the contract.
5. The node executes and returns output plus evidence.
6. One or more verifiers evaluate the result.
7. The caller accepts, retries, selects another node, or escalates.
8. Execution evidence updates local or shared reputation.
9. Optional accounting or settlement occurs after acceptance.

## Logical layers

### 1. Identity and transport

Provides node identity, authentication, secure messaging, endpoint reachability, and replay protection.

Questions remain about decentralized identifiers, conventional PKI, delegated identities, NAT traversal, offline operation, and key recovery.

### 2. Skill description and discovery

Publishes versioned capability declarations and finds candidates. Discovery should separate self-reported metadata from evidence-backed performance.

Possible implementations include local catalogs, signed feeds, federated registries, and peer-to-peer indexes.

### 3. Contract and workflow

Defines request/response schemas, budgets, policies, state transitions, and failure behavior. It should support both single handoffs and multi-step workflows without requiring every node to know the whole plan.

### 4. Execution

Runs a model, tool, agent, data query, or hybrid process inside the provider's boundary. Sandboxing, resource limits, observability, and data lifecycle belong here.

### 5. Evidence and verification

Attaches provenance to outputs and evaluates acceptance criteria. Verification policies may combine:

- schema and invariant checks;
- test execution;
- replicated work;
- cross-model review;
- trusted data or tool attestations;
- challenge tasks;
- human approval.

### 6. Reputation and policy

Turns historical evidence into routing signals. Different consumers may calculate different reputations from the same signed events.

### 7. Accounting and settlement

Measures accepted work and optionally transfers value. This layer should remain replaceable and should not dictate the rest of the protocol.

## Proposed object boundaries

| Object | Owned by | Main responsibility |
|---|---|---|
| Skill declaration | Provider | Describe capability and conditions |
| Task request | Caller | State desired outcome and inputs |
| Handoff contract | Caller + provider | Define acceptance and limits |
| Execution receipt | Provider | Record what ran and when |
| Verification record | Verifier | Record evaluation and evidence |
| Reputation view | Router/consumer | Interpret historical evidence |
| Settlement record | Parties/payment layer | Account for accepted work |

## Decentralization strategy

A realistic path is progressive:

1. **Single trust domain:** several independently packaged local nodes.
2. **Federated domains:** organizations exchange signed declarations and evidence.
3. **Open participation:** unknown operators join under constrained workloads and stronger verification.

The first prototype should avoid blockchain dependencies. Signed content-addressed records and replaceable registries are sufficient to test coordination.

## Data and privacy model

The request should carry a data policy alongside its functional input:

- data classification;
- permitted execution locations;
- retention duration;
- whether training or logging is allowed;
- allowed subprocessors or tools;
- redaction requirements;
- evidence that may leave the trust domain.

Routing must treat privacy as a hard constraint, not just a ranking feature.

## Failure model

The protocol should distinguish at least:

- unreachable node;
- refusal or policy mismatch;
- timeout or resource exhaustion;
- schema-invalid output;
- plausible but incorrect output;
- malicious result or fabricated evidence;
- verifier disagreement;
- caller cancellation;
- partial side effect.

Each state needs an observable transition and a bounded recovery action.

## Anti-concentration mechanisms to investigate

- portable skill declarations and evidence;
- multiple compatible registries;
- consumer-defined reputation views;
- diversity-aware routing;
- capped dependence on one operator or model family;
- open conformance tests;
- transparent protocol evolution;
- no mandatory settlement provider.

## Later network prototype boundary

If the Hybrid Resident-Agent evidence later supports a bounded architecture specification, a network prototype may remain intentionally small:

- three specialist services run by at least two operators or trust boundaries;
- one router;
- JSON-based skill declarations and handoff contracts;
- signed execution receipts;
- one deterministic verifier and one model-assisted verifier;
- a replayable event log;
- no token, blockchain, or global reputation.

This is not the current authorized task. The current target is to determine whether the local control plane, Resident Core, bounded specialists, and remote escalation can be assigned credible responsibilities without hiding all difficult reasoning in a remote large model.
