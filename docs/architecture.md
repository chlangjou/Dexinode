# Candidate architecture

This document records a design space, not a frozen production architecture.

[ADR 0003](decisions/0003-resource-bounded-verifiable-execution-fabric.md) makes the current candidate:

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

The current bounded artifact is the [Repository-Repair Verifiable Execution Fabric Specification v0.2](specifications/bounded-repository-repair-verifiable-execution-v0.2.md). It preserves [v0.1](specifications/bounded-repository-repair-resident-core-v0.1.md) as provenance while removing a fixed 4B–8B single-Resident premise.

## Current candidate boundary

The nearest-term boundary is local-first, not local-only:

`deterministic local control + Local Decision Configuration + typed tools/sandboxes + candidate search + verifiers + bounded Remote fallback + human disposition`

The evaluated unit is the complete configuration:

`model(s) + memory/context policy + harness/loop + tools + verifier(s) + search/stopping policy + fallback/human policy + runtime/hardware`

A model score, parameter count, advertised context window, or tokens-per-second figure that omits material configuration is incomplete evidence.

### Responsibility and trust hypothesis

| Component or logical role | Candidate responsibility | Constraint / uncertainty |
|---|---|---|
| Deterministic Local Control Plane | canonical repository/task state, provenance, credentials, permissions, packet compilation, typed tools, sandboxes, budgets, receipts, verifier invocation, stopping enforcement, rollback, audit | must not infer uncovered semantics or treat model statements as execution evidence |
| Local Decision Configuration | local intent, decomposition, context request, failure interpretation, candidate generation/selection, stopping/escalation | may use one or several models, cognitive cores, operators, or reasoning modes; composition and actual decision owner must remain visible |
| Proposal generator | produce one bounded typed hypothesis and artifact | cannot directly mutate canonical state or accept its own work |
| Candidate selector/integrator | compare eligible candidates against contract, evidence, coverage, uncertainty, and cost | cannot override deterministic hard failures; coupling to generator/verifier must be disclosed |
| Local Operator／Specialist | one declared subtask, claim, artifact, score, refusal, or clarification | capability identity is configuration- and task-conditioned, not a label or necessarily a whole model |
| Remote capability | one task-scoped difficult subtask, operator result, or candidate artifact | untrusted; no durable memory, credentials, unrestricted workspace, policy authority, or direct side effects |
| Verifier | scoped reproducible evidence and coverage statement | can be incomplete, exposed, gamed, correlated, wrong, or model-coupled |
| Human reviewer | clarify intent, judge uncovered/high-impact semantics, approve exceptional disclosure and external disposition | human repair, selection, and takeover are system cost and capability contributions |

### Stable local authority

The Local Control Plane retains:

- original workspace, immutable bases, durable task state, and provenance;
- credentials, pseudonymization/restoration mappings, permissions, and disclosure policy;
- typed tool authority and reversible sandbox effects;
- context-packet compilation rules and recipient-specific disclosure;
- attempt, candidate, verifier, selection, and contribution receipts;
- budgets, stopping conditions, rollback, quarantine, and recovery;
- final candidate-set assembly for human disposition.

No Local or Remote model, operator, or latent workspace receives authority merely because it generated a plausible plan or patch.

### Replaceable Local Decision Configuration

The Local Decision Configuration may be:

- a single local general model;
- a Resident Model plus Local Specialists;
- a resource-bounded Cognitive Core using external knowledge and operator capabilities;
- several small models with deterministic routing or selection;
- a model using visible tool/reflection loops;
- a recurrent or latent-reasoning model;
- deterministic logic for some decisions and learned inference for others;
- any of the above with bounded Remote fallback.

Each variant competes as a complete configuration under the same authority and evidence contract. A fixed parameter range is not a role definition.

### Memory and context lifecycle

1. Preserve raw source, versions, task state, decisions, attempts, failures, and receipts outside model context.
2. Retrieve candidate evidence for the bounded contract.
3. Preserve conflicts, stale sources, taint, omissions, and provenance.
4. Compile a role- and recipient-specific packet with goal, constraints, source pointers, interfaces, and verifier context.
5. Execute one or more bounded attempts locally or through explicit escalation.
6. Apply candidates only in isolated sandboxes through typed capabilities.
7. Verify every candidate under recorded coverage and exposure.
8. Select or abstain using the closed attempt set; persist only confirmed state.

Semantic boundaries—module, API, data structure, test, workflow state, knowledge request, or operator contract—should drive decomposition. Token counts remain observations, not architectural constants.

### Candidate-search path

1. Contract the user outcome, authority, non-goals, quality scope, and failure cost.
2. Pin complete configuration, policy, immutable repository base, and verifier plan.
3. Compile bounded local context with provenance.
4. Plan attempts with hypotheses, lineage, diversity claim, verifier visibility, and finite budgets.
5. Generate typed proposals locally or through bounded delegation.
6. Apply each proposal in its own recorded sandbox.
7. Run contracted verifiers; record revision, coverage, independence, exposure, and baseline delta.
8. Close the attempt set for the current policy.
9. Select an eligible candidate, request a materially new attempt, escalate, ask a human, or abstain.
10. Produce a candidate set and complete integration receipt; stop before publication or merge.

More attempts can increase the chance of finding a valid candidate, but only a trustworthy selector and verifier can turn candidate volume into reliability. Correlated failures, repeated test exposure, and false acceptance remain first-class risks.

### Local pseudonymization and restoration

This remains an engineerable safety component rather than a model-scale premise:

1. local learned or deterministic components propose sensitive-entity candidates;
2. a human approves mappings when policy requires it;
3. deterministic code applies stable placeholders and keeps the map local;
4. placeholder integrity is checked before restoration;
5. replacement, disclosure, approval, failure, and restoration are audited.

This can guarantee round-trip behavior only for approved mappings. It cannot guarantee complete sensitive-data discovery, immunity to contextual re-identification, or zero semantic loss.

## Current evidence boundary

- Gate A supports measurable specialization as a bounded, pinned existence result.
- Gate B contradicts broad-domain labels as sufficient routing contracts for its pinned configuration.
- Neither Gate is a universal claim about all later models of the same parameter range.
- FIM / syntax-aware MVSS eligibility remains `HOLD`.
- Rapid model, inference-hardware, automated-research, and latent-reasoning developments justify architecture-level replaceability, not a specific model endorsement.
- DMoE supports modular parametric knowledge in its evaluated setting, not general procedural Skill injection.
- J-Space provides causal evidence for a privileged deliberative workspace in evaluated Claude models; J-CoT reports a usable recurrent J-Space interface on resource-bounded open backbones, but does not prove an 8B core is sufficient.
- The [Cognitive Decomposition route review](research/2026-08-17-cognitive-decomposition-hypothesis-route-review.md) closes standalone model-node specialization and broad-domain replacement routing as primary project directions.
- No runtime prototype, benchmark, model selection, or experimental Gate is currently authorized.

## Provisional long-horizon cognitive decomposition hypothesis

The current candidate architecture remains v0.2. Beneath its replaceable Local Decision Configuration, Dexinode now uses the following provisional research model:

```text
Trusted Local Control Plane
            │
            ▼
Resource-bounded Cognitive Core
  ├─ language and semantic grounding
  ├─ automatic foundation capabilities
  ├─ deliberative／recurrent workspace
  └─ planning, integration, stopping
            │
     capability requests
            │
   ┌────────┴─────────┐
   ▼                  ▼
Knowledge／Memory   Operator／Capability
Plane              Plane
   │                  │
   └────────┬─────────┘
            ▼
       typed claims,
   artifacts and evidence
            │
            ▼
Verification／Selection
```

This hypothesis is intentionally substrate-neutral:

- a J-Space-like workspace is one possible internal reasoning interface, not a Dexinode protocol;
- DMoE-like parameter experts are one possible knowledge substrate, not the definition of a Skill;
- language ability and other automatic capabilities may remain deeply integrated with the core;
- external knowledge may include factual, current, private, domain, and episodic material;
- operators may be deterministic algorithms, tools, solvers, Adapters, models, agents, services, or humans;
- every external contribution remains typed, attributable, policy-constrained, and verified.

The central open question is partial decoupling: which capabilities and knowledge can be externalized while a resource-bounded core still integrates them reliably on structurally new tasks?

The following are closed as current foundations:

- `one Skill = one standalone model`;
- `one Skill = one node`;
- broad-domain routing that replaces the General core with one Specialist by default;
- a fixed Resident parameter range;
- distributed whole-model inference as a required decentralization mechanism;
- direct J-Space or DMoE productization as the immediate next Gate.

Whole-model Specialists and distributed compute remain permissible implementations when evidence supports them. They are not mandatory architecture.

## Long-term network interaction

The local execution fabric can later become one node or trust domain in a wider network. A provider may publish a knowledge source, parameter artifact, operator, tool, verifier, complete Skill service, or compute endpoint under a signed versioned declaration.

A generic interaction remains:

1. a provider publishes a signed versioned capability declaration;
2. a router discovers candidates satisfying hard policy constraints;
3. the caller proposes a handoff or invocation contract;
4. a selected provider accepts, rejects, or negotiates;
5. the provider returns a typed result, artifact, or evidence receipt;
6. the local Cognitive Core or selector integrates eligible contributions;
7. verifiers evaluate the result under disclosed coverage;
8. the caller accepts, retries, selects another provider, escalates, or abstains;
9. execution evidence updates local or shared reputation views;
10. optional accounting or settlement occurs after acceptance.

This remains a long-term possibility. Current work does not implement it.

## Logical network layers

### 1. Identity and transport

Node identity, authentication, secure messaging, endpoint reachability, replay protection, key rotation, and recovery.

### 2. Capability description and discovery

Versioned Skill, knowledge, operator, artifact, verifier, and endpoint declarations, separating self-report from evidence-backed behavior.

### 3. Contract and workflow

Request/response schemas, policies, budgets, state transitions, cancellation, and failure behavior.

### 4. Execution

Models, tools, agents, data queries, knowledge services, operators, or hybrid processes inside provider boundaries with sandboxing, limits, and observability.

### 5. Evidence and verification

Provenance and acceptance evidence, potentially combining deterministic checks, replicated work, model-assisted criticism, attestations, challenge tasks, and human approval.

### 6. Reputation and policy

Consumer-specific interpretations of historical evidence. No single global score is assumed.

### 7. Accounting and settlement

Optional value accounting, kept replaceable and separate from core task execution.

## Proposed object boundaries

| Object | Owned by | Main responsibility |
|---|---|---|
| Capability configuration | Operator / run owner | Bind behavior to model, runtime, harness, search, verifier, fallback, and hardware |
| Skill／capability declaration | Provider | Describe externally observable capability, compatibility, contract, and operating conditions |
| Knowledge artifact declaration | Provider | Describe source, version, validity, compatibility, provenance, and update／revocation behavior |
| Task request | Caller | State desired outcome, inputs, authority, and policy |
| Handoff／invocation contract | Caller + provider | Define acceptance, evidence, disclosure, and limits |
| Attempt / candidate lineage | Control Plane | Preserve all candidate derivations and terminal states |
| Execution receipt | Execution authority | Record what actually ran and changed |
| Verification record | Verifier | Record scope, revision, coverage, exposure, and result |
| Selection／integration record | Selector / Control Plane | Explain eligibility, comparison, contribution, stopping, and uncertainty |
| Reputation view | Router / consumer | Interpret historical evidence contextually |
| Settlement record | Parties / payment layer | Account for accepted work |

## Progressive decentralization

1. **Single trust domain:** replaceable local configurations and explicit receipts.
2. **Federated domains:** organizations exchange signed declarations and evidence.
3. **Open participation:** unknown operators join only under constrained workloads and stronger verification.

The first network prototype, if later authorized, should avoid blockchain dependencies. Signed content-addressed records and replaceable registries are enough to test coordination.

## Failure model

The architecture distinguishes at least:

- unreachable or refused capability;
- policy or disclosure mismatch;
- timeout or resource exhaustion;
- schema-invalid output;
- missing or incorrect knowledge;
- correct knowledge that the Cognitive Core fails to reconcile;
- missing or incorrect operator capability;
- plausible but incorrect candidate;
- verifier false positive, false negative, error, or disagreement;
- correlated candidate failures;
- adaptive overfitting to exposed checks;
- malicious result or fabricated evidence;
- selector or integration failure;
- hidden Remote or human substitution;
- partial side effect and failed rollback;
- caller cancellation or human takeover.

Each state requires an observable transition and bounded recovery action.

## Later network prototype boundary

Only if later evidence supports the local execution fabric and independent-provider value, a small prototype might include:

- three independently provided capabilities across at least two operators or trust domains;
- at least two different capability substrates, such as knowledge plus operator or operator plus verifier;
- one replaceable router／selector;
- JSON-based declarations and invocation contracts;
- signed execution, verification, and selection receipts;
- deterministic and model-assisted verifiers with disclosed independence;
- replayable event and attempt logs;
- no token, blockchain, or global reputation.

This is not the current task. [Human review](research/2026-08-14-verifiable-execution-v0.2-human-review.md) accepted specification v0.2 as the current architecture boundary, and the cognitive-decomposition review changed research priorities without authorizing implementation, an experimental Gate, or a network prototype.