# Cognitive Decomposition Hypothesis and Research Route Review

- Date: 2026-08-17
- Scope: strategic research framing and route disposition
- Human direction: accepted in project discussion as the current provisional long-horizon hypothesis and research-priority update
- Related decision: [ADR 0003](../decisions/0003-resource-bounded-verifiable-execution-fabric.md)
- Current bounded specification: [Repository-Repair Verifiable Execution Fabric Specification v0.2](../specifications/bounded-repository-repair-verifiable-execution-v0.2.md)
- DMoE evidence: [2026-08-16 material evidence review](2026-08-16-dmoe-parametric-knowledge-injection-evidence-review.md)
- J-Space／J-CoT evidence: [2026-08-17 material evidence review](2026-08-17-j-space-j-cot-material-evidence-review.md)
- Evidence cutoff: 2026-08-17
- Disposition: **ADOPT PROVISIONAL COGNITIVE-DECOMPOSITION HYPOTHESIS / CLOSE SELECTED ROUTES AS PRIMARY / NO EXPERIMENTAL AUTHORIZATION**

This review does not claim that a composable cognitive architecture has been validated. It updates which questions have durable decision value after Gate A, Gate B, the Hybrid Agent review, ADR 0003, DMoE, J-Space, and J-CoT.

## Executive conclusion

Dexinode should no longer organize its long-term research around a network of standalone small Specialist models that each receive a broadly classified task and return a final answer. That was a useful early concrete hypothesis, but it is too narrow and increasingly inconsistent with the available evidence.

The more durable provisional hypothesis is:

> **Useful intelligence may be partially decomposable into a trusted deterministic control plane; a resource-bounded but broadly pretrained cognitive core containing semantic grounding, automatic foundation capabilities, and deliberative／recurrent integration; externalized knowledge and memory; heterogeneous operator capabilities; and independent verification.**
>
> The cognitive core integrates typed evidence and intermediate artifacts from the other planes. A J-Space-like workspace is one possible internal mechanism for deliberative integration, and DMoE-like experts are one possible knowledge substrate. Neither technology is required by the hypothesis.

This is **partial** decoupling. The core cannot be assumed to operate in a knowledge vacuum. Language, broadly reusable concepts, world priors, automatic routines, and the neural operators that read and write a workspace may remain deeply entangled and require joint pretraining.

The strategic question therefore changes from:

> Can a small standalone Specialist beat a General model on a domain?

into:

> What is the minimum complete cognitive core, and which knowledge, memory, operators, and verification functions can be externalized without losing reliable integration on structurally new tasks?

## 1. Provisional architecture hypothesis

### 1.1 Trusted Local Control Plane

Deterministic software remains responsible for:

- canonical task and project state;
- credentials, permissions, disclosure policy, and privacy mappings;
- context and evidence provenance;
- typed tools, sandboxes, reversible side effects, and rollback;
- attempt, candidate, selection, verifier, Remote, and human receipts;
- budgets, stopping, quarantine, recovery, and audit.

No model, workspace representation, Adapter, Specialist, or Remote capability becomes authoritative merely because it supplies a plausible result.

### 1.2 Resource-bounded Cognitive Core

The Cognitive Core is the minimum local learned／procedural substrate that can provide, as one complete configuration:

- natural-language and semantic grounding;
- broadly reusable concepts and world priors;
- automatic foundation capabilities learned through pretraining;
- deliberate reasoning, planning, clarification, abstention, and escalation;
- a mechanism for maintaining and reusing task-relevant intermediate state;
- integration of external knowledge, memory, tools, operator outputs, and verifier feedback.

The core may be one model, several tightly coupled local components, or a recurrent／latent configuration. It is not defined by a fixed parameter count.

A J-Space-like workspace is a candidate internal mechanism. It is not synonymous with the Cognitive Core: the full reasoning process still depends on the surrounding attention, MLP, semantic, automatic, and read／write machinery.

### 1.3 Knowledge and Memory Plane

The externalizable knowledge plane may include:

- current and time-sensitive facts;
- private enterprise or repository knowledge;
- long-tail domain material;
- episodic project and task history;
- structured databases and indexes;
- retrieved documents;
- parameterized knowledge artifacts such as DMoE-like experts.

The plane must preserve provenance, version, conflict, revocation, trust, and validity. Supplying correct information does not guarantee that the Cognitive Core will reconcile or use it correctly.

### 1.4 Operator／Capability Plane

Operators perform bounded transformations or analyses that are not best represented as factual retrieval alone. Possible implementations include:

- deterministic algorithms;
- compilers, static analyzers, databases, formal solvers, and simulators;
- learned adapters or specialist circuits;
- complete local or remote models;
- task-specific agents or services;
- human expertise.

An operator should return a typed artifact or integration packet containing relevant claims, bindings, constraints, uncertainty, evidence, and unresolved questions. It should not be assumed to replace the Cognitive Core for the complete task.

### 1.5 Verification Plane

Verification remains independent of whether capability comes from a monolithic model, knowledge module, operator, recurrent workspace, Remote service, or human. It may combine deterministic checks, replication, model-assisted criticism, attestations, and human review, while recording scope, revision, coverage, independence, feedback exposure, and false-accept risk.

### 1.6 Optional Network／Distribution Plane

The long-term network may distribute any of the following:

- knowledge sources and knowledge artifacts;
- operator capabilities and tools;
- verifiers and attestations;
- memory or indexing services;
- compute providers;
- complete cognitive configurations where justified.

Distributed whole-model inference is one option, not the foundation. Decentralization may instead occur in capability production, ownership, evidence, and provider choice while a local core performs integration.

## 2. Evidence calibration

| Claim | Current state | Basis and limit |
|---|---|---|
| Bounded whole-model specialization exists | `ESTABLISHED / PINNED` | Gate A only |
| Broad-domain whole-model routing creates material advantage | `CONTRADICTED / PINNED` | Gate B; not a universal statement about all routing |
| Tiny independently updatable modules can encode knowledge | `ESTABLISHED IN DMoE PAPER SCOPE` | knowledge injection, not procedural skill |
| Claude-family models use a privileged workspace for flexible reasoning | `ESTABLISHED IN J-SPACE PAPER SCOPE` | causal interventions in evaluated models |
| Much routine language processing can proceed outside that workspace | `PARTIALLY ESTABLISHED` | task- and model-dependent |
| A workspace-like recurrent interface can help 7B–8B models | `PARTIALLY SUPPORTED` | J-CoT reported results; work in progress; no independent replication |
| An 8B Cognitive Core is sufficient for Dexinode | `OPEN` | not established by J-CoT or J-Space |
| Long-tail knowledge and deliberate reasoning can be partially separated | `HIGH-PLAUSIBILITY / OPEN` | combined architectural inference |
| Foundational semantics, language, world priors, and automatic skills can be fully externalized | `NOT SUPPORTED` | likely deeply entangled with the core |
| Skill is a model, Adapter, node, or workspace location | `REJECT AS FOUNDATION` | Skill remains a capability contract |
| Trusted Local Control Plane has measurable end-to-end value | `PARTIALLY SUPPORTED / UNVALIDATED` | current architectural hypothesis |
| Open decentralized capability supply is viable | `OPEN / LONG TERM` | no network experiment authorized |

## 3. Routes to continue

### C1 — Minimum viable Cognitive Core and decomposition boundary

Continue asking:

- What semantic grounding, automatic capabilities, world priors, planning, integration, and recurrence must remain inside the core?
- Which failure modes persist even when complete and correct external knowledge is supplied?
- How do model size, recurrence depth, context policy, tools, and verifier support trade off as one complete configuration?
- Can a resource-bounded core clarify, integrate, stop, and escalate without a hidden Remote or human decision owner?

This replaces a fixed 4B–8B Resident premise and the earlier focus on Minimum Viable Specialist Scale as the project-defining question.

### C2 — Knowledge／memory externalization and reader integration

Continue work on:

- external factual, private, current, and episodic knowledge;
- retrieval, structured memory, parametric memory, and hybrid approaches;
- provenance, conflict, freshness, revocation, poisoning, and recovery;
- whether the reader can reconcile correct evidence rather than merely retrieve it;
- the boundary between foundational semantic knowledge and externalizable long-tail knowledge.

DMoE is one evidence point in this route, not the selected implementation.

### C3 — Operator capabilities and typed integration packets

Continue exploring how tools, solvers, learned operators, Specialists, and Remote services should contribute bounded intermediate artifacts rather than being assumed to own the full task.

The key questions are:

- What output structure lets the core recombine an operator result on a new requirement?
- Which relations, bindings, constraints, uncertainty, and evidence must be preserved?
- When is a direct final artifact appropriate, and when is an intermediate claim safer?
- How is actual contribution attributed when several operators, the core, Remote, or a human cooperate?

### C4 — Deliberative workspace and recurrent／latent reasoning as evidence-triggered architecture research

Continue monitoring and synthesizing:

- workspace-like structures across open models and scales;
- recurrent, latent, token, and hybrid reasoning interfaces;
- binding, relational structure, capacity, observability, and failure modes;
- whether additional inference depth lowers the minimum viable core size;
- whether gains survive compute-, parameter-, memory-, and task-matched comparisons.

Do not bind Dexinode to J-Space or require hidden-chain-of-thought access.

### C5 — Trusted control, verification, and full-system attribution

Continue treating control and verification as the stable project layer:

- authority and side-effect boundaries;
- complete configuration identity;
- candidate lineage, verifier exposure, false acceptance, and stopping;
- privacy, provenance, rollback, and audit;
- Remote and human substitution;
- total workflow quality, latency, resource, disclosure, and active-human-time cost.

This route remains relevant whether future cores are monolithic, recurrent, modular, local, remote, or hybrid.

### C6 — One bounded recoverable workflow as the eventual falsification surface

Repository repair remains a useful candidate workflow because it offers immutable bases, reversible sandboxes, typed artifacts, deterministic checks, and observable human substitution. Specification v0.2 remains the accepted architecture boundary.

Any later experiment must distinguish at least:

1. missing or incorrect external knowledge;
2. missing operator capability;
3. cognitive-core comprehension／integration failure;
4. verifier or selection failure;
5. Remote or human substitution.

## 4. Routes closed as primary project directions

“Closed” below means the route is no longer a default foundation or near-term research program. It does not claim scientific impossibility and does not erase historical evidence.

### X1 — `One Skill = one standalone model`

**Disposition:** `CLOSED AS FOUNDATION`.

A Skill is an externally observable capability contract. Its substrate may be a model, tool, algorithm, knowledge artifact, verifier, agent, service, or composed configuration.

### X2 — Broad-domain router selects one Specialist to replace General

**Disposition:** `CLOSED AS DEFAULT ARCHITECTURE`.

Gate B already showed that perfect Math／Coding classification did not create material held-out advantage in the pinned setup. Future routing should select knowledge, operators, tools, or configurations based on task-conditioned expected utility, and the Cognitive Core may remain the integration owner.

### X3 — Fixed parameter range as the Resident or reasoning definition

**Disposition:** `CLOSED BY ADR 0003; REAFFIRMED`.

Parameter count remains metadata. The evaluated unit is the full configuration, including reasoning mode, runtime, hardware, context, tools, verifier, fallback, and human policy.

### X4 — Distributed inference／idle compute as a required decentralization thesis

**Disposition:** `CLOSED AS NECESSARY FOUNDATION`.

It remains a possible resource source. Dexinode can still have anti-concentration and decentralization value through independent knowledge, operators, verifiers, evidence, provider choice, and locally owned integration.

### X5 — Continuous standalone-small-model landscape and leaderboard work

**Disposition:** `CLOSED AS STANDING PHASE`.

Refresh model, reasoning, runtime, and hardware evidence only when a material event changes the minimum-core or full-system question. Do not maintain an exhaustive catalog.

### X6 — Parametric procedural Skill or J-Space ABI as the immediate next Gate

**Disposition:** `CLOSED AS IMMEDIATE ROUTE / RETAIN AS WATCH ITEM`.

The DMoE record's procedural-skill question remains scientifically interesting, but it is now one operator／knowledge-substrate possibility inside a broader decomposition problem. J-Space is an internal mechanism candidate, not a portable cross-model interface.

### X7 — Re-run Gate A／B or repeat `Specialist versus General` ranking without a new hypothesis

**Disposition:** `CLOSED`.

A new model release alone is insufficient. Any later experiment must answer a different bounded system question and preserve the original Gate evidence.

### X8 — Network-first federation, marketplace, token, reputation, or settlement design

**Disposition:** `CLOSED FOR THE CURRENT STAGE`.

These topics remain conditional long-term backlog. They should not proceed before one trust domain demonstrates measurable value for the local cognitive／capability composition and verification contract.

## 5. Routes preserved but dormant

### FIM／syntax-aware MVSS eligibility

FIM remains **`HOLD`**. It may later fit the operator plane, but this review does not complete DELULU artifact, licensing, verifier, comparability, or runtime closure. Do not resume it merely because the cognitive taxonomy changed.

### Long-term independent nodes

Independent capability providers remain part of the long-term vision, but the provider need not host a complete Specialist model. No federation prototype is authorized.

### Whole-model Specialists

Whole-model Specialists remain valid capability implementations where measured. They are no longer the assumed universal Skill unit or primary architecture.

## 6. Highest-decision-value unresolved question

Before opening an experimental Gate, Dexinode should determine whether one bounded workflow can cleanly expose the decomposition boundary:

> **Can failures be attributed separately to missing external knowledge, missing operator capability, inadequate Cognitive Core integration, and inadequate verification／selection—well enough that a resource-bounded configuration can be compared fairly with a strong monolithic or Remote baseline?**

A possible later experimental question, still **not authorized**, is:

> Given a fixed resource-bounded Cognitive Core and one recoverable workflow, do complete external knowledge and typed operator outputs improve independently verified completion on structurally fresh tasks relative to core-only and strong monolithic baselines, without unacceptable false acceptance, integration loss, Remote substitution, or human repair?

No benchmark, task sample, model, dataset, threshold, statistical method, implementation, or run is frozen by this review.

## 7. Consequences for project interpretation

The long-term Dexinode contribution is now better framed as a **composable capability and evidence fabric** around a replaceable local cognitive core, rather than a protocol that assumes work must hop among small model nodes.

The current near-term architecture remains:

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

The new cognitive-decomposition hypothesis sits underneath the replaceable Local Decision Configuration as a research model. It does not supersede ADR 0003 or specification v0.2.

## 8. Preserved durable state and authorization boundary

This review does **not**:

- change Gate A `PASS / CLOSED` or Gate B `FAIL / CLOSED`;
- change any frozen result, oracle record, retrospective, or acceptance criterion;
- resolve FIM `HOLD`;
- supersede ADR 0003;
- revise specification v0.2;
- select a Cognitive Core, model, J-Space method, DMoE implementation, RAG system, operator, verifier, runtime, or hardware;
- authorize model download, training, inference, quantization, GPU work, implementation, benchmark creation, task sampling, statistics, thresholds, or a new Gate;
- authorize federation, marketplace, token, reputation, settlement, or governance work.

## 9. Stop point

Adopt the Cognitive Decomposition Hypothesis as the provisional long-horizon research framing. Continue literature／design work only where it sharpens the decomposition boundary or the eventual falsifiable system question. Close the listed model-node, broad-routing, fixed-scale, continuous-landscape, and network-first routes as primary directions.

Stop before experimental execution.