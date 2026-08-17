# Dexinode Session Handoff

Repository: `chlangjou/Dexinode`

Canonical branch: `main`

Canonical merged base: `174b235fed6ac69a20c285c4a0cb2829d09d28a9`

Current integration branch: `agent/intervention-supported-attribution-experiment-design`

Current decision issue: [#33](https://github.com/chlangjou/Dexinode/issues/33)

Snapshot: 2026-08-17

Git is the durable source of truth. This file is intentionally compact for a fresh session.

## Start here

Read in this order:

1. `AGENTS.md`
2. `HANDOFF.md`
3. `status/current.md`
4. `docs/research/2026-08-17-intervention-supported-attribution-experiment-design.md`
5. `docs/research/2026-08-17-cognitive-decomposition-attribution-feasibility-review.md`
6. `docs/research/2026-08-17-cognitive-decomposition-hypothesis-route-review.md`
7. `docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md`
8. `docs/specifications/bounded-repository-repair-verifiable-execution-v0.2.md`
9. `docs/research/2026-08-17-j-space-j-cot-material-evidence-review.md`
10. `docs/research/2026-08-16-dmoe-parametric-knowledge-injection-evidence-review.md`

Read Gate closure records only when their evidence is needed:

- `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

Do not reopen Gate A／B unless a new human decision explicitly requires it.

## Durable empirical state

### Gate A — Specialist Validation

**PASS / CLOSED.**

Same-family Qwen2.5-7B evidence established capability divergence on one pinned distribution. Durable lesson: a model or domain label is not a capability identity.

### Gate B — Orchestration Advantage

**FAIL / CLOSED.**

- General-only: 76/96 = 79.17%;
- Skill-routed: 77/96 = 80.21%;
- overall delta: +1.04 pp, 95% CI [0, +3.125] pp;
- Router domain accuracy: 100%.

Post-closure content review found no paired Mathematics content advantage. Durable lesson: broad-domain classification is not per-task success prediction, and selecting one whole-model Specialist is not a sufficient integration architecture.

Gate conclusions remain scoped to their pinned models, benchmark, runtime, and date.

## Preserved decisions

- FIM／syntax-aware MVSS eligibility remains **`HOLD`**.
- ADR 0002 and specification v0.1 remain accepted history and unchanged provenance.
- ADR 0003 remains the current architecture decision.
- Specification v0.2 remains the accepted architecture boundary for one recoverable repository-repair workflow.
- No experimental Gate, implementation, benchmark, selected model, or execution plan is active.

## Accepted architecture and long-horizon framing

Near-term:

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

The evaluated unit is a complete Local Decision Configuration:

`model(s) + memory/context policy + harness/loop + tools + verifier(s) + search/stopping policy + fallback/human policy + runtime/hardware`

Long-horizon:

> Useful intelligence may be partially decomposable into a trusted deterministic control plane; a resource-bounded Cognitive Core with language／semantic grounding, automatic foundation capabilities, and deliberate／recurrent integration; external Knowledge／Memory and Operator／Capability planes; and independent Verification.

Knowledge–reasoning decoupling is partial. J-Space is one possible internal workspace, not a protocol. DMoE is one possible Knowledge substrate, not proof of procedural Skill injection. Skill remains a substrate-neutral capability contract.

## Accepted attribution-feasibility result

PR #32 was human-approved and merged into `main@174b235fed6ac69a20c285c4a0cb2829d09d28a9`.

Accepted recommendation:

> **`PIVOT TO COARSER ATTRIBUTION`**

Do not force one unique root-cause label. Use intervention-supported, set-valued attribution across:

1. component family — `K` Knowledge, `O` Operator, `C` Cognitive Core, `V` Verification／Selection;
2. orthogonal provenance integrity — `P` Remote／human contribution, disclosure, attribution, and authority;
3. causal role — initiating, enabling, propagating, detection, recovery, terminal acceptance;
4. evidence grade — `E0` narrative, `E1` observational, `E2` controlled-no-flip, `E3` sufficiency-supported, and limited `E4` minimality／necessity;
5. run disposition — detected, recovered, masked, escaped, false accepted／rejected, or unresolved.

A disclosed authorized Remote／human contribution is not automatically a failure. `Cognitive Core failure` requires positive upstream sufficiency evidence and must never be residual.

## Current bounded experiment design

Issue #33 authorized one design-only specification. The completed design recommends:

> **`PROCEED TO GATE SPECIFICATION`**

This is not an active Gate and does not authorize implementation or execution.

### Critical stage split

The next candidate Gate should test **Attribution Contract Calibration**, not autonomous AI root-cause diagnosis.

Candidate question:

> Can one synthetic repository-local migration workflow provide faithful receipts, controlled fault boundaries, prefix／state-preserving replay, independent oracles, and negative controls sufficient for correct `E3` set-valued attribution records for predeclared `K`／`O`／`C`／`V` faults and `P` provenance conditions?

Only after that contract is validated should a later decision consider an **Automatic Attribution Policy Evaluation** where a learned or rule-based system proposes hypotheses and interventions without seeing the fault manifest.

### Candidate workflow

Use a fictional repository-local Relay API v1 → v2 plus configuration migration.

Conceptually:

```text
publish(topic, payload)
```

becomes:

```text
publish(PublishRequest { channel, body, tenant, codec })
```

The repository-local v2 contract requires preserved channel／body behavior, config-derived tenant and codec, error propagation, and removal of v1 usage.

The scenario is selected because Knowledge revisions, deterministic Operator outputs, Core integration, Verifier coverage, Selector decisions, Remote／human provenance, and reversible effects can be controlled.

No language, fixture, case, file count, model, or benchmark is frozen.

### Candidate conditions

The design proposes:

- clean reference;
- missing, stale, conflicting, or packet-omitted Knowledge;
- unavailable, schema-invalid, or semantically wrong Operator outputs;
- controlled Core-plan／integration／stop-or-escalate faults with valid upstream inputs;
- complete, partial, false-positive, or false-negative workflow Verifiers;
- Selector failure on a closed candidate set;
- authorized disclosed and hidden／misattributed Remote or human contributions;
- no-op interventions and negative controls;
- only a small predeclared set of two-fault cascades.

### Replay contract

Snapshots are required before Knowledge delivery, Operator output, Core decision, candidate closure, Verifier record, and Selector disposition.

Only a prefix／state-preserving replay that changes the hidden-oracle outcome is eligible for `E3` sufficiency language. Independent stochastic reruns remain observational unless the targeted state is preserved.

No-op replay stability is a hard prerequisite.

### Oracle separation

Keep separate:

- Operator oracle;
- exposed workflow Verifier;
- hidden final acceptance oracle;
- fault manifest.

The hidden oracle and fault manifest must not be exposed to generation, repair, or selection.

### Candidate metrics

A later Gate specification must freeze numerical criteria for:

- attribution coverage and abstention;
- supported precision／recall;
- set-valued truth containment and ambiguity;
- overclaim and negative-control false attribution;
- residual-Core guardrail violations;
- provenance detection and false accusation;
- false acceptance／rejection, recovery, stopping, and rollback;
- replay fidelity;
- full instrumentation, replay, Verifier, Remote, and active-human cost.

## Current stop point

Stop for human review of:

1. the split between attribution-contract calibration and later automatic-attribution evaluation;
2. the Relay API／configuration migration scenario family;
3. single-fault calibration before limited two-fault cascades;
4. replay fidelity and evidence-grade requirements;
5. the recommendation to proceed only to a formal Gate specification.

Acceptance of the design does not create or activate a Gate. A separate decision must authorize and human-approve a formal Gate specification before implementation or execution.

## Hard stop conditions

Do not:

- create or activate a Gate;
- freeze benchmark cases, fixtures, model baselines, statistical methods, thresholds, or acceptance criteria;
- select or download a checkpoint;
- run inference, training, quantization, GPU, J-lens, J-CoT, DMoE, Remote execution, custom-hardware, or deployment work;
- implement the synthetic repository, attribution harness, receipt schema, replay system, Operator, Verifier, Selector, or runtime;
- modify Gate A／B evidence or conclusions;
- revise ADR 0003 or specification v0.2;
- resolve FIM HOLD or continue DELULU work;
- design or implement federation, marketplace, reputation, token, settlement, or governance.
