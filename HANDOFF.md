# Dexinode Session Handoff

Repository: `chlangjou/Dexinode`

Canonical branch: `main`

Canonical merged base: `e72499506c4ada56a3782a427c210f564f694fff`

Current integration branch: `agent/cognitive-decomposition-attribution-feasibility`

Current decision issue: [#31](https://github.com/chlangjou/Dexinode/issues/31)

Snapshot: 2026-08-17

Git is the durable source of truth. This file is intentionally compact for a fresh session.

## Start here

Read in this order:

1. `AGENTS.md`
2. `HANDOFF.md`
3. `status/current.md`
4. `docs/research/2026-08-17-cognitive-decomposition-attribution-feasibility-review.md`
5. `docs/research/2026-08-17-cognitive-decomposition-hypothesis-route-review.md`
6. `docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md`
7. `docs/specifications/bounded-repository-repair-verifiable-execution-v0.2.md`
8. `docs/research/2026-08-17-j-space-j-cot-material-evidence-review.md`
9. `docs/research/2026-08-16-dmoe-parametric-knowledge-injection-evidence-review.md`

Read Gate closure records only when their evidence is needed:

- `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

Do not reopen Gate A／B execution unless a new human decision explicitly requires it.

## Durable empirical state

### Gate A — Specialist Validation

**PASS / CLOSED.**

Same-family Qwen2.5-7B evidence established capability divergence on one pinned distribution. Durable lesson: a model or domain label is not a capability identity.

### Gate B — Orchestration Advantage

**FAIL / CLOSED.**

Frozen result:

- General-only: 76/96 = 79.17%;
- Skill-routed: 77/96 = 80.21%;
- overall delta: +1.04 pp, 95% CI [0, +3.125] pp;
- Router domain accuracy: 100%.

Post-closure content review found no paired Mathematics content advantage. Durable lesson: broad-domain classification is not per-task success prediction, and choosing one whole-model Specialist is not a sufficient integration architecture.

Gate conclusions remain scoped to their pinned models, benchmark, runtime, and date.

## Preserved decisions

- FIM／syntax-aware MVSS eligibility remains **`HOLD`**.
- ADR 0002 and specification v0.1 remain accepted history and unchanged provenance.
- ADR 0003 remains the current architecture decision.
- Specification v0.2 remains the accepted architecture boundary for one recoverable repository-repair workflow.
- No experimental Gate, implementation, benchmark, model run, or execution plan is active.

## Accepted near-term architecture boundary

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

The evaluated unit is the complete Local Decision Configuration:

`model(s) + memory/context policy + harness/loop + tools + verifier(s) + search/stopping policy + fallback/human policy + runtime/hardware`

The deterministic Local Control Plane retains canonical state, credentials, policy, provenance, typed tool authority, reversible effects, receipts, Verifier invocation, budgets, stopping, rollback, quarantine, recovery, and audit.

## Provisional long-horizon framing

The Cognitive Decomposition Hypothesis treats useful intelligence as potentially partially decomposable into:

- trusted deterministic local authority;
- a resource-bounded Cognitive Core with language／semantic grounding, automatic foundation capabilities, and deliberate／recurrent integration;
- external Knowledge／Memory;
- heterogeneous Operator／Capability providers;
- independent Verification.

Knowledge–reasoning decoupling is partial, not absolute. J-Space is one candidate internal workspace rather than a protocol. DMoE is one possible Knowledge substrate rather than procedural-Skill proof. Skill remains a substrate-neutral externally observable capability contract.

## Current bounded review

Issue #31 authorized one literature-first, design-only attribution-feasibility review:

> Can controlled interventions and observable receipts distinguish failures caused by Knowledge, Operator capability, Cognitive Core integration, Verification／Selection, and hidden Remote／human substitution without relying on private chain-of-thought?

The completed review recommends:

> **`PIVOT TO COARSER ATTRIBUTION`**

### Why

A targeted correction and prefix／state-preserving replay can establish that an intervention was sufficient to change a pinned outcome. It does not generally establish a unique, minimal, or earliest root cause. Real runs may contain multiple sufficient causes, propagation, detection failures, recovery failures, and terminal-acceptance failures.

The original five categories also mix causal levels. Knowledge, Operator, Core, and Verification／Selection are possible component loci. Hidden Remote／human substitution is mainly a provenance-integrity axis; a disclosed contribution is not automatically a semantic failure.

### Proposed attribution dimensions

1. **Component family**
   - `K` Knowledge;
   - `O` Operator;
   - `C` Cognitive Core;
   - `V` Verification／Selection.
2. **Provenance integrity**
   - `P` Remote／human contribution, disclosure, attribution, and authority.
3. **Causal role**
   - initiating;
   - enabling;
   - propagating;
   - detection;
   - recovery;
   - terminal acceptance.
4. **Evidence grade**
   - narrative;
   - observational;
   - controlled intervention without outcome flip;
   - sufficiency-supported outcome flip;
   - limited minimality／necessity within a predeclared intervention set.

Attribution should be set-valued and preserve unresolved alternatives. Do not claim one unique root cause by default.

### Core-failure guardrail

`Cognitive Core failure` must never be a residual catch-all. It requires positive evidence that:

- the task contract is complete;
- the Knowledge packet is oracle-sufficient and delivered exactly;
- required Operator outputs are independently valid;
- authority, environment, and tools are fixed;
- the Core still fails to interpret, integrate, plan, stop, or escalate;
- and a targeted observable correction or controlled alternative configuration enables verified continuation.

This supports a configuration-conditional integration locus, not an internal neural-mechanism claim.

## Candidate workflow family

If a later human decision authorizes experiment design, the best first family is a **synthetic or repository-local versioned API／configuration migration**.

Reasons:

- old, stale, conflicting, absent, and correct Knowledge can be controlled;
- compiler／schema validation can provide deterministic Operators and acceptance evidence;
- the Core must integrate bounded changes across files and constraints;
- Verifier coverage can be varied;
- Remote／human contribution lineage can be injected and audited.

Configuration repair is useful for calibration. Dependency constraints and schema migrations are possible later. Concurrency-invariant repair and arbitrary real repository issues are not recommended first because attribution and oracles are too entangled.

No task set, benchmark, model, threshold, or statistical method is selected.

## Current stop point

Stop for human review of:

- the `PIVOT TO COARSER ATTRIBUTION` recommendation;
- the component／role／evidence ontology;
- the positive Core-failure criteria;
- the candidate workflow family;
- whether a separate later decision should authorize one bounded experiment-design specification.

Review completion does not automatically authorize an experiment.

## Hard stop conditions

Do not:

- select or download a checkpoint;
- run inference, training, quantization, GPU, J-lens, J-CoT, DMoE, custom-hardware, or deployment work;
- implement an attribution harness, runtime, or Verifier;
- create or freeze a benchmark, task set, oracle set, baseline, statistical method, threshold, or Gate;
- modify Gate A／B evidence or conclusions;
- resolve FIM HOLD or continue DELULU work;
- design or implement federation, marketplace, token, reputation, settlement, or governance.
