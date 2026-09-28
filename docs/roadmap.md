# Feasibility roadmap

The roadmap is organized around reducing uncertainty, not maximizing feature count or tracking every model release.

## Completed evidence and architecture stages

### Gate A — Specialist Validation

Result: **PASS / CLOSED**.

Bounded specialization exists, but checkpoint names are not reliable capability identities.

### Gate B — Orchestration Advantage

Result: **FAIL / CLOSED**.

Perfect broad-domain routing did not create material held-out advantage. Broad labels such as `Math` and `Coding` are not sufficient task-success contracts.

### Literature-first MVSS and routing synthesis

Result:

- bounded specialization is established as an existence claim;
- routing has conditional production value;
- structural transfer and per-task model-success prediction remain partial;
- full-stack absolute-small economics and edge decentralization remain open;
- FIM / syntax-aware candidate eligibility is `HOLD`.

### Hybrid Resident-Agent evidence review

Result: **`PROCEED TO BOUNDED ARCHITECTURE SPEC`** by human decision.

Completed outputs:

- memory／context and loop／harness evidence map;
- non-exhaustive agent-specialized small-model landscape;
- responsibility-based Hybrid Resident-Agent hypothesis;
- Worker `HOLD` recommendation and separate human review;
- ADR 0002 decision to specify one recoverable repository-repair workflow.

The decision established enough component evidence for a falsifiable specification. It did not validate MVRC, any model, deployment economics, or user value.

### Strategic reorientation review

Result: **continue with a revised foundation** by human decision in ADR 0003.

Rapid changes in local models, inference hardware, automated research, and recurrent／latent reasoning made a fixed 4B–8B single-Resident premise too volatile.

The durable near-term candidate became:

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

Specification v0.1 remains preserved as provenance. Model landscapes became dated evidence snapshots rather than roadmap anchors.

### Bounded repository-repair verifiable execution specification

Result: [human review](research/2026-08-14-verifiable-execution-v0.2-human-review.md) accepted the [v0.2 specification](specifications/bounded-repository-repair-verifiable-execution-v0.2.md) as the current architecture boundary for one recoverable repository-repair workflow with relevant deterministic checks.

The specification defines:

- deterministic local authority and reversible sandbox boundary;
- a replaceable Local Decision Configuration rather than one mandatory model;
- complete configuration identity across models, runtime, hardware, memory, harness, tools, search, verifier, fallback, and human policy;
- six local semantic responsibility types with actual component ownership;
- separate generator, selector, verifier, policy, Remote, and human roles;
- run state plus per-attempt state and candidate lineage;
- verifier coverage, independence, exposure, baseline, and false-accept risks;
- complete attempt-set and selection receipts;
- explicit Remote and human substitution attribution;
- observability, falsifiers, unsupported tasks, and deferred decisions.

Human acceptance authorized no experiment. There is no active Gate or implementation task.

### DMoE evidence review

Result: **material external evidence / no durable state change**.

DMoE established modular, independently updatable parametric knowledge in its evaluated setting. It did not establish procedural Skill injection, safe composition, an open provider ecosystem, or general superiority to retrieval. The evidence weakened `Skill = standalone model` and separated capability ownership from distributed inference.

### J-Space／J-CoT evidence review

Result: **material external evidence / no experimental authorization**.

J-Space supplied causal evidence for a privileged deliberative workspace in evaluated Claude models while routine language processing remained largely automatic. J-CoT reported a recurrent J-Space interface on a reasoning-adapted Qwen3-8B backbone and scaling evidence from 7B to 405B. These results do not prove that J-Space is the whole reasoning engine or that an 8B core is sufficient.

### Cognitive Decomposition Hypothesis and route review

Result: **provisional long-horizon hypothesis adopted; selected routes closed as primary**.

The current provisional model is:

> **Trusted Local Control Plane + resource-bounded Cognitive Core + external Knowledge／Memory Plane + heterogeneous Operator／Capability Plane + Verification Plane.**

The Cognitive Core includes semantic grounding, automatic foundation capabilities, and deliberate／recurrent integration. Knowledge–reasoning decoupling is expected to be partial, not absolute. J-Space and DMoE are evidence examples rather than selected components.

The [route review](research/2026-08-17-cognitive-decomposition-hypothesis-route-review.md) did not supersede ADR 0003 or specification v0.2 and did not authorize execution.

## Current phase — Specification Convergence and Reference Implementation

[ADR 0004](decisions/0004-distributed-cognitive-execution-reference-slice.md) formally transitions Dexinode from research-first exploration to implementation-driven validation.

The active sequence is:

    Specification Convergence
        ->
    Reference Implementation
        ->
    Implementation Validation
        ->
    later protocol / adoption decision

Research remains a watch lane and no longer blocks implementation unless it changes a core contract, isolation invariant, verification assumption, or Provider boundary.

### Priority 1 — Freeze protocol objects in working code

Implement and validate:

- TaskIntent;
- TaskBundle;
- ProviderDescriptor;
- ExecutionContract;
- Artifact;
- VerificationRecord;
- ExecutionReceipt.

The code must preserve provider-internal implementation freedom.

### Priority 2 — Prove Consumer / Provider isolation

Demonstrate:

- no ambient requester filesystem access;
- no Consumer credentials;
- no requester-home-directory mount;
- network disabled for the reference task;
- per-task ephemeral workspace;
- no cross-task workspace leakage;
- output returned only as protocol Artifact(s).

### Priority 3 — Complete the end-to-end lifecycle with a mock backend

Build:

- Consumer CLI;
- static Provider Registry;
- deterministic hard-constraint matcher;
- Provider Runtime;
- sandbox lifecycle;
- deterministic verifier;
- Artifact / Receipt validation;
- explicit failure states and cleanup receipts.

### Priority 4 — Swap in one real Agent backend

Use an existing Agent runtime or model API behind the same Provider adapter.

Do not change the Consumer contract to accommodate backend-specific details.

### Priority 5 — Produce reproducible implementation evidence

Record:

- successful reference run;
- unsupported capability rejection;
- execution failure;
- verifier failure;
- cleanup failure or quarantine path;
- isolation sentinel test;
- two consecutive tasks showing no workspace leakage.

### Implementation completion question

The v0.3 slice is successful only if the same external contract can support both a deterministic/mock backend and a real Agent backend while preserving the required isolation and evidence semantics.

No benchmark leaderboard or new model-selection Gate is required.

## Routes closed as primary project directions

The following are no longer the default roadmap. “Closed” does not mean scientifically impossible.

- **One Skill = one standalone model:** closed as a foundation.
- **One Skill = one node:** closed as a foundation.
- **Broad-domain router selects one Specialist to replace General:** closed as the default architecture.
- **Fixed 4B–8B Resident or reasoning scale:** closed by ADR 0003 and reaffirmed.
- **Distributed whole-model inference／idle compute as a necessary decentralization thesis:** closed as a requirement.
- **Continuous small-model catalog or leaderboard:** closed as a standing phase; use event-triggered refresh.
- **Parametric procedural Skill or J-Space ABI as the immediate next Gate:** closed as an immediate route; retain as watch items.
- **Re-running Gate A／B because a newer model exists:** closed without a materially different falsifiable system question.
- **Network-first federation, marketplace, token, reputation, settlement, or governance:** closed for the current stage.

## Preserved but dormant routes

- FIM / syntax-aware MVSS eligibility remains `HOLD`; do not resume DELULU work without a separate reason and authorization.
- Whole-model Specialists remain valid capability implementations where measured, but are not the universal Skill unit.
- Distributed compute remains a possible resource provider, but not the defining decentralization mechanism.
- Independent nodes remain long-term possibilities after local composition and verification show measurable value.

## Archived original phases

The following preserve the project's original progression for provenance. They are **not** the current sequence.

### Original Phase 0 — Frame the claim

Goal: identify the narrowest valuable hypothesis, baseline, measurable success criteria, and trust assumptions.

### Original Phase 1 — Local multi-specialist experiment

Original goal: test explicit model specialization and handoffs before networking complexity.

Current disposition: archived. Any future local experiment must use the cognitive-decomposition framing and cannot assume whole-model Specialists or broad-domain routing.

### Original Phase 2 — Independent nodes and verification

Original goal: cross a real trust and operational boundary with signed identities, transport, receipts, verification, and an unreliable participant.

Current disposition: deferred until local composition supplies measurable value.

### Original Phase 3 — Federation and portable evidence

Original goal: portable discovery and evidence across registries.

Current disposition: deferred.

### Original Phase 4 — Operational pilot

Original goal: compare a federated workflow under a real workload.

Current disposition: deferred until one trust-domain configuration is validated.

### Original Phase 5 — Economics and open participation

Original goal: accounting, payments, disputes, Sybil resistance, liability, and governance.

Current disposition: deferred; blockchain or token remains neither prerequisite nor default.

## Immediate next actions

1. Implement v0.3 data models and schema validation.
2. Implement the static Provider Registry and deterministic matcher.
3. Implement the Provider sandbox lifecycle with network disabled.
4. Complete a mock end-to-end path that produces Artifact + ExecutionReceipt.
5. Add deterministic verification and failure-path tests.
6. Connect one real Agent backend behind the same adapter.
7. Run the v0.3 acceptance suite and record reproducibility evidence.
8. Stop for human review before adding a second Provider, controlled network access, capability-artifact distribution, failover, or federation.

Do not add marketplace, reputation, payment, token, settlement, permissionless discovery, or cross-provider latent communication during v0.3.