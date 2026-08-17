# Cognitive Decomposition Attribution Feasibility Review

- Date: 2026-08-17
- Scope: literature-first, design-only identifiability review
- Authorizing decision: [Issue #31](https://github.com/chlangjou/Dexinode/issues/31)
- Base state: `main@e72499506c4ada56a3782a427c210f564f694fff`
- Related architecture decision: [ADR 0003](../decisions/0003-resource-bounded-verifiable-execution-fabric.md)
- Current bounded specification: [Repository-Repair Verifiable Execution Fabric Specification v0.2](../specifications/bounded-repository-repair-verifiable-execution-v0.2.md)
- Cognitive framing: [2026-08-17 Cognitive Decomposition Hypothesis and route review](2026-08-17-cognitive-decomposition-hypothesis-route-review.md)
- Evidence cutoff: 2026-08-17
- Recommendation: **`PIVOT TO COARSER ATTRIBUTION`**
- Experimental authorization: **none**

This review asks whether one bounded recoverable workflow could distinguish failures caused by external knowledge, operators, the Cognitive Core, verification／selection, and hidden Remote／human substitution without relying on private chain-of-thought.

It does not select a task, model, benchmark, oracle set, statistical method, threshold, implementation, or Gate.

## Executive conclusion

The original five-way question contains a useful architecture decomposition, but it is too strong if interpreted as assigning one unique root-cause label to every failed run.

The literature supports four conclusions.

1. **Static traces and model explanations are not enough.** Reliable attribution needs complete observable inputs, metadata, outputs, dependency information, replay, and targeted intervention.
2. **A successful correction establishes intervention-supported sufficiency, not uniqueness or minimality.** More than one intervention may make the run succeed, and distributed or multi-trial failures may have no defensible single earliest cause.
3. **The five proposed families do not occupy one causal level.** Knowledge, Operator, Core, and Verifier／Selector are possible failure loci or mechanisms. Hidden Remote／human substitution is primarily a provenance-integrity axis and may be a valid disclosed contribution rather than a task failure.
4. **A coarser, multi-axis attribution is feasible and decision-relevant.** A run can record component family, causal role, recovery status, and evidence strength without claiming a unique root cause.

The recommended target is therefore:

> **Intervention-supported, set-valued failure attribution:** identify which component-level interventions are sufficient to change or recover the outcome; record initiating, propagating, detection, recovery, and terminal-acceptance roles separately; keep provenance／substitution orthogonal; and explicitly preserve unresolved causal ambiguity.

This is strong enough to guide whether the system should refresh knowledge, replace an Operator, strengthen or escalate the Cognitive Core, repair a Verifier／Selector, or quarantine an attribution-integrity breach. It is not strong enough to support a universal single-label root-cause classifier.

## 1. Decision question and required precision

### 1.1 The original question

Can a bounded recoverable workflow distinguish failures caused by:

1. missing or incorrect external knowledge;
2. missing or incorrect Operator capability;
3. Cognitive Core comprehension／reasoning／integration failure;
4. Selector or Verifier failure;
5. hidden Remote or human substitution?

### 1.2 Why “root cause” is underspecified

A failed run may contain several different causal roles:

```text
stale knowledge
    ↓
Core chooses an obsolete migration
    ↓
Operator produces an invalid patch
    ↓
Verifier misses the incompatible edge case
    ↓
Selector accepts the patch
```

Calling any one of these the root cause loses information needed for recovery. Structural causal models formalize causes through counterfactual interventions, but actual-cause judgments can depend on contingencies and can admit multiple sufficient causes. Software causal testing likewise relies on minimally different passing and failing executions rather than narrative inspection alone.

The review therefore distinguishes:

- **failure family／locus** — where an invalid condition or decision occurred;
- **causal role** — how it contributed to the terminal outcome;
- **evidence grade** — how strongly the attribution is supported;
- **run disposition** — whether the problem was detected, recovered, masked, or escaped.

### 1.3 Operational target

The feasible target is not:

> assign exactly one of five labels to every failure.

It is:

> produce one or more intervention-supported attribution records, each binding a component family and causal role to observable receipts, a controlled change, and the resulting outcome, while retaining unresolved alternatives.

## 2. Evidence synthesis

### 2.1 Causal evidence requires interventions, not only correlations

Halpern and Pearl define actual cause using structural equations and counterfactuals. The useful Dexinode implication is methodological: a causal claim needs a model of variables and interventions, not merely temporal order or a plausible explanation.

Causal Testing applies this principle to software by generating executions that differ minimally from a failing run but exhibit different behavior. Its empirical coverage is meaningful but incomplete: the method was applicable to 71% of examined Defects4J defects and helped identify a root cause for 77% of the applicable subset. This argues for intervention-friendly workflows and explicit non-identifiable cases rather than assuming universal attribution.

Lineage-driven fault injection supplies a complementary systems lesson: provenance can be used to reason backward from an expected successful outcome and target combinations of faults. Its bounded certificates apply only to the modeled configuration, reinforcing that attribution claims must be configuration-scoped.

**Dexinode inference:** complete receipts and causal structure are prerequisites, but neither guarantees a unique root cause.

### 2.2 Current LLM-agent attribution work supports replay but exposes limits

REFLECT explicitly separates correction from attribution. It proposes four requirements for intervention-supported trace attribution:

- execution grounding;
- prefix-preserving replay;
- targeted intervention rather than independent retry;
- inference-time testing rather than only a trained classifier.

Its attribution record is a targeted intervention at a candidate step plus a controlled replay whose prefix is preserved and whose final outcome flips from incorrect to correct. The authors correctly limit this claim: the intervention is sufficient to change the outcome, but it is not necessarily unique, minimal, or identical to the earliest causal origin; single-step attribution may be ill-posed for distributed or multi-trial failures.

TraceElephant strengthens the observability requirement. In its evaluated multi-agent traces, access to inputs and metadata materially improves attribution, and dynamic replay improves step-level localization. Yet even with ground truth and dynamic analysis, reported average step-level accuracy is 33.3%; the paper's dynamic method validates only a short local continuation rather than global causal sufficiency. Its “ground truth” labels are expert-consensus annotations, not intervention-proven unique causes.

AgenTracer reports that general reasoning models are poor at failure attribution and constructs training data using counterfactual replay and programmed fault injection. A trained localizer may be useful as a hypothesis generator, but its inference-time prediction is still not causal evidence unless the proposed attribution is tested on the current trace.

MAST supplies a useful descriptive taxonomy of recurrent multi-agent failure patterns, but several observed modes can arise from system design, prompt specification, or base-model limitations. A taxonomy of symptoms or design patterns is not automatically a causal ontology.

GraphTracer is excluded as supporting evidence: its arXiv submission was withdrawn because the authors reported a fundamental methodological error affecting the main results. Its proposed information-dependency framing remains a research idea, not evidence for this review.

**Dexinode inference:** a localizer, judge, or taxonomy should propose hypotheses; targeted replay and outcome evidence should determine the attribution grade.

### 2.3 Knowledge failure and Core integration failure are entangled by default

DisentQA identifies the core ambiguity directly: a model may answer from parametric knowledge or supplied contextual knowledge, and ordinary outputs do not reveal which source determined the answer. The paper uses counterfactual data augmentation and specialized training to separate the two in a QA setting.

RAGChecker demonstrates the value of separate retrieval- and generation-side diagnostic metrics. Such metrics can show that retrieval coverage or grounding is weak, but they remain diagnostic correlations unless paired with controlled packet replacement and outcome replay.

For Dexinode, “correct knowledge was retrieved” is not equivalent to “the Cognitive Core received, understood, and used it.” At least four loci must remain distinguishable:

```text
source validity
  → retrieval
  → packet compilation／delivery
  → reader interpretation／integration
```

A Core attribution is defensible only after the upstream packet has been positively established as correct and sufficient under a task-specific oracle. It must never be the residual label assigned after other explanations seem unlikely.

### 2.4 Verifiers and Selectors are themselves fallible and adaptive

LLM judges can show strong aggregate agreement with human preferences, while still exhibiting position, verbosity, self-enhancement, and reasoning biases. Model-based verdicts therefore need calibration, version identity, and independent checks where the task permits them.

Repeated exposure to a verifier also changes the evidentiary meaning of a pass. Adaptive-data-analysis work shows that repeatedly tuning hypotheses against the same holdout can overfit the holdout itself. In an agent loop, a pass obtained after seeing detailed test failures is useful recovery evidence, but it is not equivalent to an untouched holdout pass.

A fixed candidate set is necessary to distinguish Verifier from Selector failure:

- **Verifier failure:** a candidate receives an incorrect validity or quality record relative to an independent oracle.
- **Selector failure:** given the same candidate set and accurate admissible records, the policy chooses an inferior or ineligible disposition.

Conditioning analysis only on accepted candidates can create selection bias: candidate quality and Verifier leniency jointly influence acceptance. The complete attempt set must remain visible.

### 2.5 Model rationales are not causal receipts

Chain-of-thought explanations can systematically rationalize answers without disclosing the feature that actually influenced the result. A model's statement that it failed because documentation was missing is therefore, at most, a hypothesis.

Dexinode should record observable inputs, actions, artifacts, tool results, interventions, and outcomes. It should neither require private chain-of-thought nor treat generated rationales as execution evidence.

## 3. Revised failure ontology

The five original categories should be represented using three orthogonal dimensions.

### 3.1 Dimension A — Component family

| Code | Family | Operational definition | Required positive evidence | Not sufficient by itself |
|---|---|---|---|---|
| `K` | Knowledge supply | Required external information is invalid, stale, missing, not retrieved, corrupted, misbound, or omitted before the Core receives the frozen packet. | Versioned source／packet comparison plus a matched correction or removal intervention that changes a relevant downstream state or outcome. | Model says it lacked knowledge; retrieval score is low; another model knows the answer. |
| `O` | Operator capability | A declared bounded transformation／analysis is unavailable, contract-invalid, execution-invalid, or returns a semantically wrong typed artifact relative to an independent Operator oracle. | Frozen Operator request; exact revision; captured output; independent deterministic or human-approved oracle; replacement with an oracle-valid output. | Final task fails after calling the Operator; Core dislikes the output; learned Operator self-evaluation. |
| `C` | Cognitive Core | With a complete task contract, an oracle-sufficient Knowledge packet, oracle-valid Operator outputs, and fixed authority／tool conditions, the Core misinterprets, fails to integrate, chooses an invalid plan, fails to stop, or fails to escalate. | Positive upstream sufficiency evidence and either a targeted Core-decision correction that enables verified continuation or a controlled alternative Core/configuration that succeeds on the identical frozen bundle. | No other cause was found; the final answer is wrong; the Core's rationale is confused. |
| `V` | Verification／selection | A Verifier assigns an incorrect record relative to an independent acceptance oracle, or a Selector makes an invalid choice from a frozen candidate set and admissible records. | Frozen candidate set, complete Verifier receipts, independent oracle, and isolated replacement of Verifier or Selector policy. | A bad candidate was accepted when the generator, Verifier, and Selector were all changed together. |
| `P` | Provenance／substitution integrity | A Remote or human contribution, edit, selection, or takeover materially affects the result but is omitted, misattributed, or violates the declared authority boundary. | Immutable access／tool／edit／artifact lineage proving contribution and mismatch with the declared record. | The output resembles a frontier model; no receipt exists in a system that did not technically enforce complete mediation. |

`P` is not normally a semantic task-failure family. A fully disclosed human correction may be a legitimate `human_substitution` contribution. The failure occurs when provenance or policy representation is false, incomplete, or unauthorized.

### 3.2 Dimension B — Causal role

A run may assign several roles to different records:

| Role | Meaning |
|---|---|
| `initiating` | Earliest observed invalid condition in the modeled dependency graph. |
| `enabling` | A condition required for another fault to affect the outcome, without independently originating the invalid state. |
| `propagating` | A component accepts, transforms, or amplifies an upstream invalid state. |
| `detection` | A Verifier, monitor, or policy fails to detect an already invalid state. |
| `recovery` | A retry, fallback, rollback, clarification, or escalation policy fails to contain or correct the fault. |
| `terminal_acceptance` | The decision or authority transition that permits the invalid artifact to become the run's accepted output or side effect. |

This prevents an incorrect Verifier from erasing an earlier Knowledge or Core fault, while still recognizing that the Verifier caused the bad artifact to escape.

### 3.3 Dimension C — Evidence grade

| Grade | Evidence | Permitted language |
|---|---|---|
| `E0 NARRATIVE` | Model／human explanation without controlled evidence. | “suspected”, “self-reported”. |
| `E1 OBSERVATIONAL` | Full trace, receipts, dependency relation, temporal contrast, or diagnostic metric. | “consistent with”, “localized candidate”. |
| `E2 CONTROLLED-NO-FLIP` | Targeted matched intervention and replay, but no verified outcome flip. | “intervention did not establish sufficiency”; hypothesis unresolved or weakened. |
| `E3 SUFFICIENCY-SUPPORTED` | Prefix／state-preserving targeted intervention produces a faithful verified outcome flip. | “this intervention was sufficient under the pinned configuration”. |
| `E4 MINIMALITY／NECESSITY-SUPPORTED` | A predeclared contrast set or factorial interventions establish that removing the candidate condition prevents the effect and that a smaller admissible intervention does not suffice. | “minimal／necessary within the modeled intervention set”; never universal uniqueness. |

`E4` will be rare in stochastic agent workflows. No record should claim “the unique root cause” unless uniqueness follows from the explicitly modeled intervention space, which is unlikely for realistic tasks.

### 3.4 Run disposition

Each record should also state whether the fault was:

- `detected`;
- `recovered`;
- `masked` by another component;
- `escaped` into the final candidate;
- `false_accepted`;
- `false_rejected`;
- or remained `unresolved`.

## 4. Observable evidence and receipt matrix

| Observable | Minimum content | Attribution use | Limitation |
|---|---|---|---|
| Task contract | exact goal, non-goals, authority, expected artifact, acceptance boundary | freezes what “correct” means | an ambiguous contract can itself be an upstream specification defect outside the five families |
| Immutable base | repository／environment revision, dependency snapshot, seeds when meaningful | makes replay comparable | external services and nondeterminism may still drift |
| Knowledge manifest | source IDs, revisions, validity interval, trust, retrieval query, selected fragments | distinguishes source, retrieval, and packet stages | cannot prove the Core used the information |
| Frozen context packet | exact bytes／tokens, schema, omissions, provenance, hash | proves delivery to the Core interface | does not reveal internal attention or use |
| Operator receipt | request, schema, revision, runtime, output, refusal／error, independent oracle status | isolates capability availability and output validity | learned Operator semantics may lack a strong oracle |
| Core decision receipt | observable request, structured decision／artifact, tool proposal, abstain／escalate outcome | localizes integration decisions without private reasoning | rationale text is not assumed faithful |
| Attempt／candidate lineage | parent, mutation, exposed feedback, generator, sandbox, terminal state | separates independent attempts from repaired descendants | provenance is incomplete if side effects bypass the Control Plane |
| Verifier receipt | revision, environment, scope, coverage, visibility, feedback exposure, result | measures false positive／negative and adaptivity | verifier may share blind spots with the generator |
| Selector record | closed candidate set, eligibility, records used, policy revision, disposition | isolates selection from generation／verification | a learned selector may remain opaque but its input/output is observable |
| Remote receipt | provider, model／service revision, disclosed packet, output, cost, policy | records explicit substitution | absence is not proof without network／tool mediation |
| Human receipt | clarification, edit, selection, override, approval, timestamps | measures active-human contribution | informal activity outside the instrumented boundary remains unobservable |
| Acceptance oracle | deterministic tests, schema, formal condition, hidden check, or human-owned outcome | defines verified outcome flips | incomplete or adaptive oracles can be gamed |
| Final artifact／effects | diff, state transition, publication／merge status | links semantic result to authority | a valid artifact may still have uncovered harms |

### 4.1 Information that must not be inferred

The system must not infer any of the following from output text alone:

- private chain-of-thought;
- the true internal reason for a model decision;
- knowledge use from citation style or verbal confidence;
- independence of two candidates merely because their wording differs;
- absence of Remote／human work when bypass paths were not technically blocked;
- held-out validity after repeated detailed Verifier exposure;
- unique causation from one successful repair.

## 5. Controlled intervention and counterfactual matrix

### 5.1 Knowledge interventions

Hold the task contract, immutable base, Operator outputs, Core configuration, Verifier, Selector, and budgets fixed while replacing a matched Knowledge packet:

- `K-absent`: required item removed;
- `K-stale`: plausible prior revision supplied;
- `K-incorrect`: controlled counterfactual value supplied;
- `K-correct`: oracle-sufficient current packet supplied;
- `K-conflict`: contextual packet conflicts with likely parametric knowledge.

Packets should be schema- and length-matched where practical so that salience and context pressure do not become hidden treatments. A successful `K-correct` intervention supports Knowledge sufficiency only if the resulting continuation faithfully depends on the corrected item rather than finding an unrelated path.

### 5.2 Operator interventions

Freeze the Core-facing request and compare captured typed results:

- unavailable／refusal;
- contract-invalid output;
- semantically wrong but schema-valid output;
- oracle-valid output;
- equivalent output from an independent implementation.

Deterministic Operators with strong oracles are the cleanest first target. If the Operator is another generative model and no independent oracle exists, Operator and Core attribution may remain inseparable.

### 5.3 Cognitive Core interventions

A positive Core test requires all upstream conditions to be supplied rather than inferred:

1. complete frozen task contract;
2. oracle-sufficient Knowledge packet;
3. oracle-valid Operator output or no Operator requirement;
4. identical tool authority and environment;
5. candidate generation separated from final acceptance;
6. targeted correction of an observable Core decision／intermediate or a controlled alternative Core on the identical bundle.

A correction that changes an invalid plan into a valid plan and enables a verified continuation is `E3` evidence for a configuration-conditional Core integration locus. It does not identify an internal neural mechanism.

### 5.4 Verifier and Selector interventions

First close and freeze the candidate set.

To test the Verifier:

- run a high-coverage independent oracle;
- run a deliberately partial or blind Verifier;
- compare false acceptance and false rejection on the identical candidates;
- record whether detailed feedback was exposed during generation.

To test the Selector:

- provide fixed candidate and Verifier records;
- replace only the selection policy;
- verify whether the chosen candidate satisfies hard eligibility and the independent oracle.

Changing generation, Verifier, and Selector together cannot isolate the failure family.

### 5.5 Provenance／substitution interventions

Inside a future sandboxed study, a known Remote or human contribution could be introduced through the only permitted authority path and then checked under:

- complete correct receipts;
- incomplete attribution metadata;
- an attempted bypass blocked by policy;
- an unauthorized contribution that should trigger quarantine.

The relevant outcome is not task correctness alone. It is whether the contribution, authority, disclosure, and attribution record remain accurate.

### 5.6 Staged intervention design

A defensible future design would proceed in stages:

1. **Single injected fault:** establish that each family can be manipulated and detected under known ground truth.
2. **Two-factor interactions:** test cascades such as wrong Knowledge plus weak Verifier or wrong Operator plus compensating Core.
3. **Recovery loops:** distinguish original fault, detection, and recovery failure under controlled feedback.
4. **Natural failures:** apply the framework only after intervention validity is demonstrated; preserve `unresolved` and multi-label outcomes.

Starting with natural failures would invite post-hoc storytelling before the attribution mechanism is validated.

## 6. Identifiability and confounder analysis

### 6.1 Observational equivalence

The same final artifact can result from different mechanisms:

- missing external documentation;
- correct documentation omitted during packet compilation;
- correct packet ignored by the Core;
- correct plan mistranslated by an Operator;
- valid candidate rejected by a faulty Verifier.

Full traces reduce ambiguity but do not remove it. Controlled replacement at a specific boundary is required.

### 6.2 Multiple sufficient causes

A run may be recoverable by either replacing the Knowledge packet or strengthening the Core. Both interventions can be sufficient. Neither result proves which was “the” unique cause.

The attribution should record both sufficient interventions and their costs, because the engineering choice may depend on whether refreshing Knowledge is cheaper than escalating the Core.

### 6.3 Mediation and propagation

Downstream failures can mediate an upstream fault. An invalid Knowledge item may cause a Core decision that causes a bad patch. Correcting the patch directly may flip the outcome even though the Knowledge remains wrong.

A successful late intervention therefore identifies a sufficient rollback／repair point, not necessarily the earliest origin. Dependency lineage and interventions at several boundaries are needed to distinguish origin from recovery point.

### 6.4 Selection and collider bias

If only accepted candidates are inspected, both candidate quality and Verifier permissiveness influence inclusion. Conditioning on acceptance can make unrelated generator and Verifier properties appear associated.

The complete closed attempt set, rejected candidates, Verifier records, and Selector decisions must remain available.

### 6.5 Parametric-knowledge masking

A Core may already know the required fact. Removing it from external context may not degrade the outcome, while supplying a counterfactual packet may expose whether contextual knowledge actually governs the result.

This means `K-absent` alone is weak evidence. Matched conflict and replacement interventions are more informative, although they can still alter salience and behavior.

### 6.6 Shared-model correlation

If the Core, Operator, Verifier, and Selector reuse one model family, prompt pattern, memory, or training distribution, their failures may be correlated. Logical role separation does not create evidentiary independence.

Complete configuration identity must record shared dependencies. Independent deterministic or differently sourced checks should be preferred where feasible.

### 6.7 Stochastic replay

Prefix-preserving replay can still diverge because of model sampling, tools, clocks, external services, or concurrency. A future design must separate treatment effects from ordinary replay variance, but this review does not choose a statistical method or threshold.

Captured deterministic inputs and outputs should be replayed where isolation is more important than natural end-to-end behavior.

### 6.8 Adaptive feedback

After a generator sees compiler or test failures, later candidates are descendants of the Verifier feedback. They are not independent attempts, and the exposed checks are no longer held out.

Lineage must record feedback exposure, and a separate untouched acceptance oracle may be needed for stronger claims.

### 6.9 Hidden substitution is an observability property

No semantic intervention can reliably detect an undisclosed Remote or human contribution from the artifact alone. Detection depends on authority mediation, access controls, network／tool receipts, sandbox lineage, and auditable human actions.

Therefore `P` should be evaluated as an attribution-integrity property rather than inferred as a cognitive failure.

## 7. What each evidence level can support

| Claim type | Minimum support | Example |
|---|---|---|
| Descriptive | full trace and receipts | “the stale packet preceded the invalid plan” |
| Diagnostic | component-specific metric or oracle | “the Operator output violates the schema” |
| Sufficiency-supported causal | targeted faithful replay and verified outcome flip | “replacing this packet was sufficient to recover this pinned run” |
| Necessity／minimality-supported | predeclared contrast set or factorial interventions | “within these allowed interventions, this condition was necessary” |
| Unique universal root cause | generally unavailable | must not be claimed from one trace or one repair |

The practical unit should be an **attribution set**, not a single label:

```yaml
attributions:
  - family: K
    subtype: stale_source
    role: initiating
    evidence: E3
  - family: C
    subtype: propagated_invalid_constraint
    role: propagating
    evidence: E1
  - family: V
    subtype: false_accept
    role: detection
    evidence: E3
provenance_integrity: pass
unresolved_alternatives:
  - Core could have recovered with a stronger conflict-resolution policy
```

This schema is illustrative only and is not adopted as a protocol specification.

## 8. Candidate workflow assessment

### 8.1 Required workflow properties

An attribution-friendly workflow should provide:

- immutable and replayable base state;
- a clear task contract and artifact boundary;
- externally controllable Knowledge packets;
- replaceable Operators with independent oracles;
- observable Core decisions or typed artifacts without private reasoning;
- deterministic or high-quality acceptance evidence;
- reversible effects;
- complete attempt, feedback, Remote, and human lineage.

### 8.2 Comparison of repository-repair subtypes

| Candidate subtype | Knowledge isolation | Operator oracle | Core integration demand | Verifier strength | First-study suitability |
|---|---:|---:|---:|---:|---|
| Versioned local API／configuration migration | high when the API is synthetic or repository-local | compiler／schema validator／migration checker | medium–high across several files and constraints | high | **best candidate family** |
| Configuration repair against a versioned schema | high | deterministic schema validator | medium; may be too shallow alone | high | good calibration task |
| Dependency-constraint repair | medium | package solver and lockfile checks | medium–high | medium–high | useful second family; ecosystem metadata can drift |
| Database／data-schema migration | medium–high | schema and migration checks | high | medium–high | valuable but data semantics and rollback add confounders |
| Bounded concurrency-invariant repair | low–medium | static analysis and stress tests are incomplete | high and nonlocal | low–medium | **not recommended first** |
| Arbitrary real repository issue | low | highly variable | very high | variable | unsuitable before attribution validity is established |

### 8.3 Provisional workflow recommendation

If a later human decision authorizes experiment design, begin from a **synthetic or repository-local versioned API／configuration migration family**, not an open-ended real bug.

This family can vary old, stale, conflicting, and correct documentation; provide deterministic compilers or schema validators as Operators; require the Core to integrate changes across a bounded artifact; vary Verifier coverage; and preserve exact Remote／human lineage.

This is a candidate family only. No task set, benchmark, or oracle is frozen here.

## 9. Decision value and expected recovery actions

Coarse attribution has direct engineering value because different evidence changes the appropriate response.

| Supported attribution | Likely response |
|---|---|
| `K` Knowledge | refresh or revoke source; fix retrieval／packet compilation; expose conflicts; retry with corrected packet |
| `O` Operator | reject artifact; change implementation or revision; tighten contract; invoke independent Operator |
| `C` Cognitive Core | improve packet interface; change reasoning／integration configuration; escalate; clarify; abstain |
| `V` Verifier／Selector | quarantine acceptance; add independent oracle; reduce feedback exposure; revise selection policy |
| `P` Provenance／substitution | block or quarantine; repair receipts／authority; disclose actual contribution; audit bypass path |

Exact unique causation is not necessary to make these choices. Conversely, attribution is low value if two labels always produce the same recovery or if instrumentation costs exceed the avoided debugging, false-acceptance, disclosure, or human-review cost.

A future design should therefore measure attribution overhead and actionability, not only label accuracy.

## 10. Recommendation

### `PIVOT TO COARSER ATTRIBUTION`

Do not proceed with an experiment whose target is exact five-way unique root-cause classification.

The evidence supports a narrower and more defensible target:

1. preserve the five architectural boundaries but treat `P` as an orthogonal provenance-integrity axis;
2. allow set-valued and multi-role attribution;
3. grade claims by observation, intervention, sufficiency, and limited minimality;
4. require positive upstream sufficiency evidence before assigning a Core failure;
5. use prefix／state-preserving targeted replay rather than independent retry;
6. begin with known injected single faults, then interactions, then natural failures;
7. keep unresolved and observationally equivalent cases explicit;
8. assess whether attribution changes recovery or architecture choices enough to justify its cost.

This recommendation is stronger than `HOLD`: a bounded experimental design appears possible after the target is revised. It is weaker than `PROCEED TO BOUNDED EXPERIMENT DESIGN` under the original wording: exact categorical root-cause attribution remains insufficiently identifiable.

A later human decision may authorize one experiment-design specification around the revised target. This review does not create that decision.

## 11. Preserved durable state and stop point

This review does **not**:

- reopen or modify Gate A `PASS / CLOSED`;
- reopen or modify Gate B `FAIL / CLOSED`;
- change any frozen score, benchmark, retrospective, or acceptance criterion;
- resolve FIM／syntax-aware MVSS `HOLD` or resume DELULU work;
- supersede ADR 0003;
- revise specification v0.2;
- validate the Cognitive Decomposition Hypothesis;
- select a workflow instance, model, Operator, Verifier, Selector, runtime, or hardware;
- authorize download, inference, training, quantization, GPU work, implementation, benchmark creation, task sampling, oracle creation, statistical methods, thresholds, or a Gate;
- authorize federation, marketplace, token, reputation, settlement, or governance work.

Stop for human review of the recommendation and ontology.

## 12. Primary source notes

- [Halpern and Pearl, *Causes and Explanations: A Structural-Model Approach, Part I: Causes*](https://arxiv.org/abs/cs/0011012) — counterfactual actual causality through structural equations.
- [Johnson, Brun, and Meliou, *Causal Testing: Finding Defects' Root Causes*](https://arxiv.org/abs/1809.06991) — minimally different passing／failing executions and applicability limits.
- [Alvaro, Rosen, and Hellerstein, *Lineage-driven Fault Injection*](https://doi.org/10.1145/2723372.2723711) — backward reasoning from correct outcomes and targeted fault combinations.
- [Lin et al., *REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces*](https://arxiv.org/abs/2606.09071) — targeted prefix-preserving replay; sufficiency without uniqueness／minimality.
- [*Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems*](https://arxiv.org/abs/2604.22708) — full observability, replay, expert-consensus labels, and low step-level attribution accuracy.
- [Zhang et al., *AgenTracer: Who Is Inducing Failure in the LLM Agentic Systems?*](https://arxiv.org/abs/2509.03312) — counterfactual replay and programmed fault injection for attribution data.
- [Cemri et al., *Why Do Multi-Agent LLM Systems Fail?*](https://arxiv.org/abs/2503.13657) — descriptive MAST failure taxonomy and system-design interventions.
- [GraphTracer, arXiv:2510.10581](https://arxiv.org/abs/2510.10581) — **excluded as evidence** because the authors withdrew it for a fundamental methodological error affecting the main results.
- [Neeman et al., *DisentQA*](https://arxiv.org/abs/2211.05655) — parametric／contextual knowledge entanglement and counterfactual separation.
- [Ru et al., *RAGChecker*](https://arxiv.org/abs/2408.08067) — fine-grained retrieval／generation diagnostics.
- [Turpin et al., *Language Models Don't Always Say What They Think*](https://arxiv.org/abs/2305.04388) — unfaithful chain-of-thought explanations.
- [Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*](https://arxiv.org/abs/2306.05685) — judge agreement and documented position／verbosity／self-enhancement biases.
- [Dwork et al., *Generalization in Adaptive Data Analysis and Holdout Reuse*](https://arxiv.org/abs/1506.02629) — adaptive reuse and holdout overfitting.
- [Huang et al., *On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents*](https://arxiv.org/abs/2408.00989) — controlled fault injection and interaction with system structure.
