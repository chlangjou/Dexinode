# 0003 — Reframe the Resident Core as a resource-bounded verifiable execution fabric

- Status: Accepted
- Date: 2026-08-14
- Deciders: Human project owner
- Decision issue: [#30](https://github.com/chlangjou/Dexinode/issues/30)
- Evidence review: [2026-08-14 strategic reorientation review](../research/2026-08-14-strategic-reorientation-review.md)
- Supersedes: ADR 0002 only where it fixes a single 4B–8B Local Resident Model as the mandatory candidate boundary
- Superseded by: None

## Context

[ADR 0002](0002-proceed-to-bounded-repository-repair-spec.md) correctly chose to specify one recoverable, deterministically checked repository-repair workflow before implementation or experimentation. Its v0.1 question used a 4B–8B Local Resident Model to make the responsibility boundary concrete.

Subsequent developments materially increased uncertainty in that model-specific premise:

- locally deployable and distilled agentic models continue to improve;
- model-specific inference hardware can alter attempt cost and latency discontinuously;
- automated propose／execute／evaluate loops are receiving significant research and commercial investment;
- recurrent-depth and latent-reasoning methods may trade inference compute for capability without scaling parameter count or visible reasoning tokens;
- very cheap attempts can move the bottleneck from generation to trustworthy selection.

None of these developments proves that a small local configuration is sufficient, that AI self-research is complete, or that latent reasoning will dominate. Together they make a fixed parameter range and one reasoning architecture too volatile to serve as Dexinode's foundation.

## Decision drivers

- Preserve project value when model capability, inference hardware, and reasoning architecture change.
- Retain a bounded, recoverable workflow and falsifiable responsibility boundary.
- Prevent high-throughput candidate search from hiding verifier gaming, false acceptance, or human／Remote substitution.
- Attribute results to complete configurations rather than parameter count or model brand.
- Reduce expiring model-landscape research and increase work on stable contracts, verification, provenance, and replaceability.
- Preserve Gate A, Gate B, FIM, and v0.1 as auditable history.

## Options considered

### Keep the fixed 4B–8B Resident Core

This preserves a simple actor but makes the architecture depend on a fast-moving capability boundary. It also handles multi-model local configurations, latent recurrence, and high-throughput search poorly.

### Stop Dexinode because its small-model premise is unstable

This would treat a parameter range as the whole project and discard the still-open need for local state, policy, privacy, verification, recovery, provider independence, and portable evidence.

### Return to broad model-landscape research

This improves current awareness but produces rapidly expiring output and delays the stable interfaces required under every model outcome.

### Reframe around a trusted local execution／search fabric

This keeps models and reasoning strategies replaceable while making authority, attempts, candidates, verification, stopping, disclosure, and fallback explicit.

## Decision

Choose:

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

Replace the mandatory single 4B–8B Local Resident Model with a **Local Decision Configuration**:

`model(s) + memory／context policy + harness／loop + tools + verifier(s) + search／stopping policy + fallback／human policy + runtime／hardware`

The Local Decision Configuration is the task-level learned and procedural configuration inside the local trust boundary. It may contain one model, multiple local models, deterministic algorithms, or recurrent／latent inference. It does not receive canonical state, credential, policy-override, or direct side-effect authority.

The Deterministic Local Control Plane remains the only authority for:

- canonical repository and task state;
- credentials, disclosure policy, and tool permissions;
- sandbox application and side effects;
- immutable receipts and configuration identity;
- verifier invocation and coverage records;
- budgets, stopping enforcement, rollback, quarantine, and audit.

For the bounded repository-repair workflow, specification v0.2 must:

1. preserve reversible sandbox execution and a locally verified candidate as the strongest automatic output;
2. separate logical generator, selector, verifier, policy, and human roles even when one component fills several roles;
3. record every attempt and candidate lineage, not only the selected result;
4. record verifier visibility, repeated exposure, revision, coverage, and independence;
5. prohibit a deterministic hard failure from being overridden by search volume or model judgment;
6. expose Remote and human substitution at the responsibility level;
7. bind evidence to the complete capability configuration;
8. leave model size, reasoning mode, hardware, attempt count, benchmark, and thresholds unfrozen.

## Consequences

### Preserved

- Gate A remains `PASS / CLOSED` and Gate B remains `FAIL / CLOSED` for their pinned evidence.
- FIM／syntax-aware MVSS eligibility remains `HOLD`.
- ADR 0002 remains the accepted historical authorization to write one bounded, falsifiable specification.
- Specification v0.1 remains immutable provenance.
- Repository repair remains the only current workflow boundary.
- The long-term decentralized skill-node possibility remains, but is not current implementation scope.

### Changed

- Specification v0.2 becomes the current candidate for human review.
- A fixed 4B–8B model is no longer required to own all six semantic decisions.
- Local responsibility is measured at the Local Decision Configuration level, with the actual component for each decision still recorded.
- “Broad standalone dense 1–7B replacement: `CONTRADICTED`” is explicitly scoped to the pinned prior configurations and date; it is not a universal claim about future models.
- Model landscapes become dated evidence snapshots rather than registries or roadmap anchors.
- Candidate throughput is evaluated together with selector quality, verifier false acceptance, correlation, exposure, and full workflow cost.

### Required capability identity

Any later claim about a capability or run must identify, when applicable:

- model identifier and exact revision;
- quantization and inference／reasoning mode;
- runtime and hardware;
- prompts, harness, loop or recurrence policy;
- memory and context-compilation policy;
- available tools and permissions;
- search, attempt, stopping, and selection policy;
- verifier set and revisions;
- Local Specialist／Remote fallback;
- human clarification, review, edit, takeover, and approval boundary.

Missing identity or telemetry remains missing. It must not be inferred from a model score.

## Non-decisions and restrictions

This ADR does not:

- validate any Meta, Taalas, Discovery Loop, recurrent, or latent-reasoning claim for Dexinode;
- select or download a model;
- authorize inference, quantization, GPU, hardware, or deployment work;
- authorize implementation of the control plane or execution fabric;
- create a benchmark, task set, baseline, statistical method, threshold, or Gate;
- modify Gate A／B evidence or decisions;
- resolve FIM HOLD or resume DELULU work;
- reopen routing economics;
- authorize network federation, reputation, token, settlement, marketplace, or governance design.

## Validation and revisit

Human review should first determine whether specification v0.2:

1. remains one bounded and recoverable workflow;
2. preserves clear deterministic authority;
3. attributes each semantic decision, attempt, candidate, verification, selection, Remote contribution, and human action;
4. controls or exposes verifier reuse and false-accept risk;
5. permits model／reasoning／hardware replacement without changing the trust contract;
6. freezes no model, performance threshold, benchmark, or execution plan.

Revisit this decision if verifier independence proves infeasible, the local control plane supplies no measurable value, stable latent runtimes require different observability, or evidence independent of model size justifies a networked skill-node experiment.

Any experimental question still requires a separate human decision.
