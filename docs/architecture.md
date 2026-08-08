# Candidate architecture

This document records a design space, not a frozen system architecture.

## Minimal interaction

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

## First prototype boundary

Keep the first runtime intentionally small:

- three specialist services run by at least two operators or trust boundaries;
- one router;
- JSON-based skill declarations and handoff contracts;
- signed execution receipts;
- one deterministic verifier and one model-assisted verifier;
- a replayable event log;
- no token, blockchain, or global reputation.

The target is to learn whether explicit handoffs and verification improve outcomes enough to justify a broader protocol.
