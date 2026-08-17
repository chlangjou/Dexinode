# Current Research Status

- Updated: 2026-08-17
- Gate A — Specialist Validation: **PASS / CLOSED**
- Gate B — Orchestration Advantage: **FAIL / CLOSED**
- FIM / syntax-aware MVSS eligibility: **HOLD**
- Active experimental Gate: **none**
- Active work type: **intervention-supported attribution experiment design complete / pending human review**
- Canonical base: `main@174b235fed6ac69a20c285c4a0cb2829d09d28a9`
- Current architecture decision: [ADR 0003](../docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md)
- Current bounded architecture: `docs/specifications/bounded-repository-repair-verifiable-execution-v0.2.md`
- Accepted attribution feasibility result: `docs/research/2026-08-17-cognitive-decomposition-attribution-feasibility-review.md`
- Authorizing decision: [Issue #33](https://github.com/chlangjou/Dexinode/issues/33)
- Current design: `docs/research/2026-08-17-intervention-supported-attribution-experiment-design.md`
- Integration branch: `agent/intervention-supported-attribution-experiment-design`

## Closed empirical evidence that must not change

### Gate A

Gate A remains **PASS / CLOSED**. It established bounded specialization on one pinned same-family panel.

Durable lesson: a checkpoint or domain label is not a capability identity.

### Gate B

Gate B remains **FAIL / CLOSED**. A perfect broad-domain router did not create material held-out advantage for the pinned General／Math／Coder configuration.

| Policy | Overall | Mathematics | Coding |
|---|---:|---:|---:|
| General-only | 76/96 = 79.17% | 40/48 = 83.33% | 36/48 = 75.00% |
| Skill-routed | 77/96 = 80.21% | 41/48 = 85.42% | 36/48 = 75.00% |

Routed-minus-General overall was +1.04 pp with 95% CI [0, +3.125] pp. Post-closure content review found no paired Mathematics content advantage.

Durable lesson: broad-domain classification is not per-task success prediction, and selecting one whole-model Specialist is not a sufficient integration architecture.

## Accepted architecture and research framing

The near-term boundary remains:

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

The evaluated unit remains the complete Local Decision Configuration:

`model(s) + memory/context policy + harness/loop + tools + verifier(s) + search/stopping policy + fallback/human policy + runtime/hardware`

The provisional Cognitive Decomposition Hypothesis remains unchanged:

> Useful intelligence may be partially decomposable into a trusted deterministic control plane; a resource-bounded Cognitive Core containing semantic grounding, automatic foundation capabilities, and deliberate／recurrent integration; external Knowledge／Memory and Operator／Capability planes; and independent Verification.

Knowledge–reasoning decoupling remains partial, not absolute.

## Accepted attribution target

The human owner accepted the feasibility review's recommendation:

> **`PIVOT TO COARSER ATTRIBUTION`**

Dexinode should use intervention-supported, set-valued attribution rather than force one unique root-cause label.

The accepted dimensions are:

- component family: `K` Knowledge, `O` Operator, `C` Cognitive Core, `V` Verification／Selection;
- orthogonal provenance-integrity axis: `P` Remote／human contribution, disclosure, attribution, and authority;
- causal role: initiating, enabling, propagating, detection, recovery, terminal acceptance;
- evidence grade: `E0` narrative, `E1` observational, `E2` controlled-no-flip, `E3` sufficiency-supported, and limited `E4` minimality／necessity;
- run disposition: detected, recovered, masked, escaped, false accepted／rejected, or unresolved.

A disclosed and authorized Remote／human contribution is a configuration contribution, not automatically a semantic failure.

`Cognitive Core failure` must not be a residual label. It requires positive evidence that the task contract, Knowledge packet, Operator outputs, authority, environment, and tools were sufficient and fixed.

## Current experiment-design result

Recommendation:

> **`PROCEED TO GATE SPECIFICATION`**

This is a recommendation to write a formal Gate specification only. No Gate is active and no execution is authorized.

### Candidate first Gate boundary

The proposed first Gate should be **Attribution Contract Calibration**, not automatic AI root-cause diagnosis.

Candidate question:

> Can one synthetic, repository-local migration workflow provide sufficiently faithful receipts, controlled fault boundaries, prefix／state-preserving replay, independent oracles, and negative controls to support correct `E3 SUFFICIENCY-SUPPORTED` set-valued attribution records for predeclared `K`／`O`／`C`／`V` faults and `P` provenance conditions?

A positive result would validate the attribution evidence contract only in the pinned synthetic setting. It would not show that a learned Core can autonomously diagnose unknown real-world failures.

### Two-stage research boundary

1. **Attribution Contract Calibration** — known fault manifests, controlled interventions, replay, oracle outcomes, and evidence grades. Recommended as the next Gate specification.
2. **Automatic Attribution Policy Evaluation** — a learned or rule-based policy proposes hypotheses and interventions without access to the fault manifest. Deferred to a later decision and conditional on Stage 1 success.

## Candidate workflow family

The design uses a fictional repository-local **Relay API v1 → v2 plus configuration migration** family.

Conceptual migration:

```text
publish(topic, payload)
```

becomes:

```text
publish(PublishRequest { channel, body, tenant, codec })
```

The repository-local contract requires preserved channel／body semantics, config-derived tenant and codec, error propagation, and removal of deprecated v1 usage.

This family is preferred because:

- Knowledge revisions and packet omissions can be controlled;
- Operator requests and outputs can have deterministic oracles;
- the Core must integrate bounded rules across files;
- workflow Verifier coverage can be complete, partial, false positive, or false negative;
- the Selector can operate on a closed candidate set;
- Remote／human provenance can be disclosed, hidden, misattributed, material, or unused;
- the final artifact remains reversible in a sandbox;
- fictional repository-local semantics reduce public pretraining leakage.

No fixture, language, file count, task set, or benchmark case is frozen.

## Candidate calibration conditions

The design proposes, but does not freeze:

- one clean reference condition;
- single-fault conditions for missing／stale／omitted Knowledge;
- unavailable, schema-invalid, or semantically wrong Operator outputs;
- controlled observable Core-plan／integration／stop-or-escalate faults with oracle-valid upstream inputs;
- incomplete or incorrect workflow Verifiers and a separate Selector fault;
- disclosed versus hidden／misattributed Remote and human contributions;
- negative controls and semantic no-op interventions;
- a small predeclared set of two-fault cascades such as stale Knowledge plus blind Verifier.

Concurrency, arbitrary repository issues, live external services, open-ended architecture changes, and model-internal neural attribution remain excluded from the first design.

## Replay and evidence contract

The design distinguishes logical snapshots before:

1. Knowledge packet delivery;
2. Operator output;
3. Core observable decision;
4. candidate-set closure;
5. workflow-Verifier records;
6. Selector disposition.

Only a replay that preserves the exact prefix／state through the targeted boundary and changes the hidden-oracle outcome is eligible for `E3` sufficiency-supported language.

Independent stochastic reruns may describe variability but are not causal evidence by themselves.

No-op interventions are mandatory. Frequent no-op outcome flips invalidate the replay contract.

The hidden acceptance oracle must remain separate from the exposed workflow Verifier and must not provide repair feedback.

## Measurement plan

A future Gate specification should freeze metrics for:

- attribution coverage and correct abstention;
- `E3` supported precision and recall;
- set-valued truth containment and ambiguity size;
- overclaim and negative-control false-attribution rates;
- residual-Core guardrail violations;
- provenance-integrity detection and false accusation;
- false acceptance／rejection, recovery, stopping, and rollback;
- replay fidelity and invalid replay rate;
- instrumentation, storage, replay, Verifier, Remote, and active-human costs.

No numerical acceptance thresholds or statistical method are frozen by this design.

## Human review required

Human review should confirm or revise:

1. the split between attribution-contract calibration and later automatic-attribution evaluation;
2. the Relay API／configuration migration scenario family;
3. controlled single-fault calibration followed by only limited two-fault cascades;
4. replay-fidelity and `E0`–`E4` evidence-grade requirements;
5. the recommendation to proceed only to a formal Gate specification.

Acceptance of this design would not authorize implementation or execution. A separate human decision must create and approve the Gate specification.

## Preserved but dormant

- FIM remains **`HOLD`** and DELULU work does not resume.
- Whole-model Specialists remain possible implementations, not the universal Skill unit.
- Distributed compute remains an optional resource source, not a necessary foundation.
- DMoE, J-Space, J-CoT, and Parametric Procedural Skill remain evidence／watch items.
- Independent capability providers remain long-term and conditional.

## Authorization boundary

Do not:

- create or activate a Gate;
- freeze benchmark cases, fixtures, model baselines, statistics, or thresholds;
- select or download a checkpoint;
- run inference, training, quantization, GPU, J-lens, J-CoT, DMoE, Remote execution, or custom-hardware work;
- implement the synthetic repository, attribution harness, receipt schema, replay system, Operator, Verifier, Selector, or runtime;
- modify Gate A／B evidence or decisions;
- revise ADR 0003 or specification v0.2;
- resolve FIM HOLD or continue DELULU work;
- design or implement federation, marketplace, reputation, token, settlement, or governance.
