# Bounded Repository-Repair Verifiable Execution Fabric Specification v0.2

- Status: Draft for human review
- Date: 2026-08-14
- Decision: [ADR 0003](../decisions/0003-resource-bounded-verifiable-execution-fabric.md)
- Decision issue: [#30](https://github.com/chlangjou/Dexinode/issues/30)
- Evidence basis: [strategic reorientation review](../research/2026-08-14-strategic-reorientation-review.md)
- Prior specification: [Resident Core v0.1](bounded-repository-repair-resident-core-v0.1.md), preserved as provenance

This document supersedes v0.1 as the current candidate architecture boundary. It does not invalidate v0.1's historical role, select a model, define a benchmark, freeze a performance threshold, authorize implementation or inference, or assert that the architecture works.

Normative words `MUST`, `MUST NOT`, `SHOULD`, and `MAY` describe interface, authority, attribution, and safety invariants inside this candidate architecture. They are not experimental acceptance criteria.

## 1. Bounded question

> For a recoverable repository-repair workflow with relevant deterministic checks, what minimum control-plane, Local Decision Configuration, attempt／candidate, verification, selection, and escalation contracts would let later evidence determine whether a resource-bounded local configuration is useful without assuming a fixed model size, model count, reasoning architecture, or Remote Model dependency?

The specification makes observable:

- who or what produced each semantic decision and proposal;
- which complete configuration was available;
- how many attempts were made and how they were related;
- which verifiers each attempt could observe or adapt to;
- why one candidate was selected, rejected, escalated, or stopped;
- which responsibilities were supplied by Local, Remote, deterministic, or human components.

A workflow may complete through Remote or human fallback. Completion alone is not evidence that the local configuration supplied the responsibility being evaluated.

## 2. Architectural invariant

The current candidate is:

`Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric`

The **Deterministic Local Control Plane** owns canonical state, policy, authority, side effects, receipts, verifier invocation, budgets, and recovery.

The **Local Decision Configuration** is the complete local learned and procedural configuration used for one run:

`model(s) + memory／context policy + harness／loop + tools + verifier(s) + search／stopping policy + fallback／human policy + runtime／hardware`

It may contain one general model, several local models, Specialists, deterministic planners or selectors, visible token loops, hidden-state recurrence, or no learned component for a particular decision. Its composition MUST be recorded. No component gains authority merely because it is local or intelligent.

## 3. Workflow boundary

### 3.1 In scope

A task is inside v0.2 only when all of the following are true:

- one version-controlled repository and immutable starting revision are identified;
- the requested repair has an explicit goal, non-goals, allowed paths, tools, data, and side effects;
- all proposed writes occur in an isolated local worktree or equivalent sandbox;
- pre-disposition effects are reversible by discard or rollback;
- at least one deterministic verifier is relevant to the requested behavior;
- verifier commands, inputs, revisions, visibility, environment, and results can produce receipts;
- candidate generation, application, verification, and selection operate under finite configured budgets;
- publication, merge, deployment, credential mutation, and production effects remain outside the workflow;
- clarification, abstention, escalation, rollback, failure, and human takeover are valid terminal paths.

A deterministic verifier may cover only part of the requested semantics. The task contract MUST record coverage and uncovered scope. Search volume MUST NOT be used to convert partial coverage into a claim of complete correctness.

### 3.2 Strongest automatic output

The strongest automatic output is a **locally verified candidate set with one disposition recommendation**, containing:

- the immutable repository base and every resulting sandbox snapshot;
- all attempt, proposal, application, verification, and selection receipts;
- the selected candidate, if any, and all materially distinct rejected or invalid candidates;
- verifier coverage, exposure, failures, errors, and unresolved assumptions;
- complete Local／Specialist／Remote／deterministic／human contribution traces;
- rollback references and a human-readable summary that does not claim unverified execution.

`CANDIDATE_READY` means ready for external human disposition. It does not authorize push, PR creation, merge, release, deployment, or production mutation.

### 3.3 Explicitly unsupported

The following are outside v0.2:

- open-ended product design with no bounded repair contract;
- changes whose material correctness depends only on subjective review;
- irreversible data migrations, production operations, account changes, or secret rotation;
- direct model access to production credentials or unrestricted user data;
- unrestricted dependency installation or network access;
- multi-repository or organization-wide refactors;
- tasks whose only acceptance mechanism is the proposal-producing model judging itself;
- visual／UX acceptance without an independent machine-checkable component;
- hidden Remote or human work in context selection, failure interpretation, selection, integration, or stopping;
- unbounded search or “try until something passes” policies;
- modification, deletion, or weakening of verifier scope solely to obtain a pass.

Unsupported work MUST transition to clarification, human review, bounded escalation, or abstention.

## 4. Logical roles and authority

Logical roles MUST remain attributable even when one physical component fills several roles.

| Role | Required responsibility | Prohibited authority or inference |
|---|---|---|
| Deterministic Local Control Plane | canonical state, policies, packet compilation, sandboxes, typed tools, budgets, receipts, verifier invocation, stopping enforcement, rollback, audit | semantic guessing; accepting a model statement as an execution or verification receipt |
| Intent／decomposition owner | bounded goal, non-goals, current subproblem, assumptions, clarification and risk flags | expanding scope or changing policy without human authority |
| Context requester／compiler | learned or rule-based relevance request plus deterministic retrieval, filtering, provenance, and disclosure enforcement | using an untraceable summary as canonical state |
| Proposal generator | one typed repair hypothesis and candidate artifact | direct canonical writes, self-acceptance, hidden tools, or “already executed” claims |
| Candidate selector／integrator | compare eligible candidates against the task contract, receipts, coverage, cost, and uncertainty | replacing hard verifier failure with preference; reporting only the winner |
| Deterministic verifier | reproducible scoped evidence with baseline and coverage | inferring uncovered product intent or overriding policy |
| Model-assisted verifier／critic | additional fallible evidence with exact configuration and independence disclosure | sole automatic authority for material correctness |
| Remote capability | one task-scoped proposal, artifact, score, refusal, or clarification request | credentials, restoration map, canonical memory, unrestricted workspace, or direct side effects |
| Human reviewer | intent clarification, exceptional disclosure, uncovered semantics, high-impact disposition, publication／merge decisions | invisible or zero-cost fallback |

The same local model MAY generate and select candidates, but the records MUST disclose role coupling. A candidate's own generator score is not independent verification.

## 5. Local semantic responsibility contract

For a run to support the Local Decision Configuration hypothesis, the configuration inside the local trust boundary MUST own and record these decisions:

1. **Intent contract** — bounded goal, non-goals, assumptions, clarification needs, authority, and risk flags.
2. **Task decomposition** — current repair subproblem and dependencies without scope expansion.
3. **Semantic context request** — which source, symbols, tests, history, failures, or interfaces are needed and why.
4. **Failure interpretation** — whether evidence is pre-existing, introduced, incomplete, correlated, or actionable, and the next legal transition.
5. **Candidate selection／integration** — whether an eligible candidate addresses the contract, why it is preferred, and what remains uncovered.
6. **Stopping／escalation** — why another local attempt is justified, why search should stop, or what smallest bounded external contribution is required.

These decisions need not be produced by one model. The receipt MUST identify the actual local component and complete configuration used for each decision.

### 5.1 Delegable work

The Local Decision Configuration MAY delegate:

- candidate generation for a named file／symbol scope;
- narrow API, library, or diagnostic research;
- local static analysis, search, or code-specialist work;
- a materially distinct repair hypothesis after failure;
- bounded candidate comparison or criticism;
- explanation of an unfamiliar tool or verifier result.

A returned artifact cannot transition directly to application, selection, or integration. It must pass local schema, policy, sandbox, and verification handling.

### 5.2 Substitution attribution

| Class | Meaning | Evidence interpretation |
|---|---|---|
| `local_configuration` | local components own all six semantic responsibilities | potentially supports the local hypothesis, subject to verification and cost evidence |
| `bounded_artifact` | Remote supplies one named proposal／artifact; local configuration retains all six decisions | compatible with a hybrid local configuration |
| `core_advice` | Remote materially advises one semantic responsibility; local component records an independently supported decision | useful workflow evidence, but responsibility attribution remains mixed |
| `core_substitution` | Remote owns or rewrites one or more semantic responsibilities | MUST NOT support the claim that the local configuration performed that responsibility |
| `human_substitution` | human performs unplanned intent, context, repair, failure, selection, or stopping work | MAY complete the task; MUST be counted separately from automatic local capability |

## 6. Complete configuration identity

Every run MUST bind its claims to a `dexinode.capability-configuration.v0.2` record. Applicable fields include:

| Field | Requirement |
|---|---|
| `model_components` | provider, model ID, exact revision, local／Remote location, role, tokenizer／template when relevant |
| `quantization_and_reasoning_mode` | precision／quantization plus token, recurrent, latent, diffusion, or other disclosed inference mode |
| `runtime_and_hardware` | runtime revisions, accelerators／CPU, memory limits, concurrency, and material serving settings |
| `memory_and_context_policy` | stores, indexes, retrieval／compaction revisions, packet policy, and effective limits |
| `harness_and_prompts` | harness, system／role instructions, tool protocol, graph／loop policy, and versions |
| `tools_and_authority` | typed capability revisions and policy-granted permissions |
| `search_policy` | candidate diversity mechanism, maximum configured attempts, parallelism, mutation／repair policy |
| `selection_and_stopping` | ranking／eligibility policy, termination conditions, fallback triggers |
| `verifier_set` | verifier revisions, coverage, independence class, visibility, and invocation policy |
| `fallback_and_human_policy` | Local Specialist, Remote, clarification, review, edit, takeover, and approval rules |

Advertised context length, active parameter count, total parameter count, or tokens per second MAY be recorded but MUST NOT substitute for complete configuration identity or measured task behavior.

Missing configuration or resource telemetry MUST remain missing.

## 7. Run and attempt state

### 7.1 Run states

The Control Plane is the only component allowed to change run state. Each transition MUST cite its authorizing receipt.

| State | Meaning | Legal next states |
|---|---|---|
| `RECEIVED` | request and immutable base captured | `NEEDS_CLARIFICATION`, `CONTRACTED`, `ABSTAINED` |
| `NEEDS_CLARIFICATION` | material intent／authority input missing | `CONTRACTED`, `NEEDS_HUMAN`, `ABSTAINED` |
| `CONTRACTED` | task, verifier, disclosure, and budget contract recorded | `CONTEXT_READY`, `NEEDS_HUMAN`, `ABSTAINED` |
| `CONTEXT_READY` | initial local packet compiled and validated | `SEARCHING`, `ESCALATION_PENDING`, `NEEDS_HUMAN`, `ABSTAINED` |
| `SEARCHING` | one or more bounded attempts are active or eligible | `SELECTING`, `ESCALATION_PENDING`, `NEEDS_HUMAN`, `FAILED_BOUNDED`, `ROLLED_BACK` |
| `SELECTING` | attempt set is closed for current policy and eligible candidates are compared | `CANDIDATE_READY`, `SEARCHING`, `ESCALATION_PENDING`, `NEEDS_HUMAN`, `FAILED_BOUNDED`, `ROLLED_BACK` |
| `ESCALATION_PENDING` | bounded Local Specialist／Remote request awaits policy, result, or attribution | `CONTEXT_READY`, `SEARCHING`, `SELECTING`, `NEEDS_HUMAN`, `ABSTAINED`, `FAILED_BOUNDED` |
| `NEEDS_HUMAN` | intent, disclosure, authority, or uncovered semantics exceed automatic scope | `CONTRACTED`, `CONTEXT_READY`, `SEARCHING`, `SELECTING`, `ABSTAINED`, `FAILED_BOUNDED` |
| `CANDIDATE_READY` | selected locally verified candidate plus complete attempt set is available | terminal inside v0.2 |
| `ABSTAINED` | system safely declines the contract | terminal |
| `ROLLED_BACK` | sandboxes restored or discarded with receipts | terminal |
| `FAILED_BOUNDED` | budget, environment, tool, verifier, or policy ended work | terminal |

Returning from `SELECTING` to `SEARCHING` requires a recorded new hypothesis, new evidence need, or materially changed strategy. It MUST NOT mean repeating until the same exposed verifier passes.

### 7.2 Attempt states

Each attempt has a separate lineage and state:

| State | Meaning | Legal next states |
|---|---|---|
| `PLANNED` | hypothesis, parent candidates, generator, packet, and budget allocated | `PROPOSED`, `INVALID`, `CANCELLED` |
| `PROPOSED` | typed artifact available but not applied | `APPLIED_UNVERIFIED`, `INVALID`, `CANCELLED` |
| `APPLIED_UNVERIFIED` | proposal applied only in its sandbox | `VERIFYING`, `INVALID`, `ROLLED_BACK` |
| `VERIFYING` | configured verifier sequence is running or complete | `ELIGIBLE`, `REJECTED`, `INVALID`, `ROLLED_BACK` |
| `ELIGIBLE` | no hard failure under recorded verifier coverage | terminal for attempt; enters run selection |
| `REJECTED` | hard failure or contract mismatch | terminal for attempt |
| `INVALID` | policy, provenance, environment, schema, or receipt integrity failure | terminal for attempt |
| `CANCELLED` | stopped before application by budget or supersession | terminal for attempt |
| `ROLLED_BACK` | applied sandbox restored or discarded | terminal for attempt |

An attempt cannot become `ELIGIBLE` from a model assertion or selector preference.

## 8. Common record envelope

Every packet, decision, attempt, proposal, execution, verification, selection, escalation, and integration record MUST include:

| Field | Requirement |
|---|---|
| `schema`／`record_id` | versioned object type and immutable unique ID |
| `run_id`／`task_id`／`attempt_id` | causal scope; `attempt_id` may be absent only for run-level records |
| `parent_record_ids` | explicit causal predecessors and candidate lineage |
| `actor_class`／`actor_id`／`actor_revision` | actual deterministic, model, Local Specialist, Remote, verifier, or human actor |
| `configuration_id` | complete v0.2 capability configuration used |
| `created_at` | Control Plane timestamp |
| `input_hashes` | packets, artifacts, repository states, policies, and verifier inputs consumed |
| `policy_revision` | authority, disclosure, tool, and search policy in force |
| `budget_snapshot` | remaining configured wall time, attempts, tool calls, context, disclosure, and applicable resource units |
| `status`／`evidence_refs` | object status and immutable supporting receipts |

Audit records MAY contain concise decision summaries. They MUST NOT require hidden chain-of-thought or treat generated rationales as causal ground truth.

## 9. Required logical records

Exact JSON Schema and storage encoding are deferred. The following logical information is mandatory.

### 9.1 Repair task and context packet

`dexinode.repair-task.v0.2` MUST contain repository／immutable base, goal, non-goals, allowed and forbidden paths, typed tools, reversible side-effect policy, verifier plan, data／risk policy, finite configured budgets, and known unknowns.

`dexinode.context-packet.v0.2` MUST contain recipient and role, goal fragment, hard constraints, source pointers with hashes／versions／taint／selection reasons, derived views with provenance, conflicts, stale candidates, omissions, tool schemas, verifier context, disclosure accounting, packet hash, and expiry.

Canonical repository and task history remain outside model context. This is a Dexinode trust and reproducibility constraint, not a universal claim about model architecture.

### 9.2 Semantic decision receipt

`dexinode.semantic-decision.v0.2` MUST identify:

- decision type: `intent`, `decomposition`, `context_request`, `failure_interpretation`, `selection_integration`, or `stopping_escalation`;
- actual decision owner and configuration;
- concise inspectable conclusion;
- assumptions, uncertainty, and supporting receipts;
- requested legal transition;
- delegation influence and human influence classes.

### 9.3 Attempt and proposal records

`dexinode.attempt-plan.v0.2` MUST identify hypothesis, parent candidate／failure, generator role and configuration, packet, allowed tools, verifier visibility, diversity claim, allocated budget, and stop conditions.

`dexinode.artifact-proposal.v0.2` MUST identify artifact hash, expected changed paths, preconditions, typed actions, expected verifier effects, unverified claims, and proposal-specific stop or escalation conditions.

`dexinode.execution-receipt.v0.2` MUST identify sandbox, before／after snapshots, typed invocation, environment revision, exit status, bounded stdout／stderr evidence, observed paths／diff hash, policy result, elapsed time, and available resource observations.

### 9.4 Verification receipt

`dexinode.verification-receipt.v0.2` MUST identify:

- verifier ID, exact revision, environment, invocation, and input hash;
- baseline receipt when applicable;
- scope, coverage limitations, and independence class;
- whether the generator or selector could observe the verifier definition, expected answer, prior result, or failure detail;
- exposure count or the best available equivalent for the current run／candidate lineage;
- result: `pass`, `fail`, `error`, or `not_run`;
- observations and introduced／pre-existing／unknown classification;
- whether the verifier or its tests changed from the contracted base, and why.

### 9.5 Attempt-set and selection receipt

`dexinode.attempt-set.v0.2` MUST enumerate every planned attempt and terminal state, parent relationships, shared model／prompt／context／data dependencies, verifier exposure, cancellation reason, and cumulative resource observations.

`dexinode.selection-receipt.v0.2` MUST identify:

- the closed attempt set considered;
- eligibility rules and configured selector revision;
- selected candidate or no-selection outcome;
- deterministic failures that excluded candidates;
- comparison dimensions and tie handling;
- coverage differences and unresolved uncertainty;
- generator／selector／verifier coupling;
- Remote and human influence;
- reason to stop, search again, escalate, or abstain.

Reporting only the selected attempt is prohibited.

### 9.6 Escalation and integration receipts

An escalation request MUST name the missing capability or evidence, smallest bounded request, disclosure delta, available local verifier, expected return schema, policy／human approval, and alternatives.

The integration receipt MUST bind the selected sandbox snapshot and diff to the task contract, configuration, complete attempt set, all relevant verifier and semantic-decision receipts, contribution trace, substitution class, unresolved scope, rollback reference, and terminal state.

## 10. Search, selection, and verifier invariants

1. Every run and attempt has finite configured budgets. v0.2 defines no universal numeric values.
2. Search MUST preserve all attempts, including invalid, rejected, timed-out, cancelled, and rolled-back attempts.
3. Parallel or repeated attempts MUST record shared ancestry and known correlation sources. They MUST NOT be described as independent without evidence.
4. A deterministic hard failure cannot be outvoted by candidate count, selector score, model judge, Remote advice, or human preference inside automatic scope.
5. Tests, verifier commands, baselines, and coverage cannot be changed solely to make a candidate eligible.
6. Generated tests from a proposal-producing model MAY add evidence but cannot be the sole independent verifier.
7. Reusing verifier feedback for repair changes the candidate's exposure history and MUST be recorded.
8. Passing a repeatedly exposed verifier MUST NOT be represented as held-out generalization evidence.
9. A selector MUST compare coverage and uncertainty, not only pass count or scalar model score.
10. More attempts do not imply higher confidence unless candidate diversity, selector recall, verifier false acceptance, correlation, and exposure are addressed by a later evaluation design.
11. A model-based verifier MAY criticize or rank eligible candidates, but its provenance, coupling, and fallibility remain visible.
12. Missing or inconsistent receipts fail closed for automatic eligibility.

## 11. Memory and context boundary

The Control Plane MUST:

- preserve raw source, Git revisions, contracts, decisions, attempts, failures, and receipts as canonical records;
- compile role- and recipient-specific packets from immutable pointers;
- enforce ACL, path, version, size, taint, disclosure, and deduplication policy deterministically;
- retain conflicts, stale candidates, and omissions rather than silently synthesize one truth;
- treat repository text, comments, issues, tool output, model output, and Remote output as untrusted data;
- prevent unverified proposals or summaries from becoming durable fact;
- quarantine and rebuild derived memory affected by revoked or poisoned sources.

No 8K, 32K, 64K, or advertised maximum context figure is a v0.2 requirement. Effective context is part of complete configuration evidence.

## 12. Security and recovery invariants

- Credentials, policy authority, and restoration mappings remain inside the deterministic local boundary.
- A model cannot approve its own privilege, scope, disclosure, tool, or network expansion.
- Model and repository content never acquire control authority by appearing as instructions.
- Every command and write runs through an allowlisted typed capability in the recorded sandbox.
- Declared and observed paths are compared; out-of-scope changes fail closed.
- Network access requires a named capability, recipient, data policy, and disclosure receipt.
- Every applied attempt has a last-known-safe snapshot and rollback reference.
- Candidate sandboxes are isolated from one another unless a recorded lineage intentionally derives one from another.
- Audit views redact secrets while retaining stable hashes and access-controlled raw evidence.

## 13. Human boundary

Human review is required when:

- goal, non-goals, authority, or risk remain materially ambiguous;
- scope, tools, network, data, disclosure, or side effects would expand;
- no independent deterministic verifier covers a material claim;
- a verifier conflicts with task intent or two authoritative verifiers conflict;
- candidate semantics are high impact and uncovered;
- external publication, PR, merge, deployment, or irreversible action is requested.

Human clarification, editing, candidate creation, verifier interpretation, selection, takeover, approval, and recovery time MUST be separately attributable when later measured. Human work is not a free selector or hidden repair loop.

## 14. Required observability

A conforming future implementation MUST be able to emit, without prescribing target values:

- complete configuration identity;
- run and attempt terminal states;
- actor and configuration for each semantic decision;
- packet size, source coverage, omissions, staleness, conflicts, and disclosure;
- attempt count, lineage, parallelism, diversity claim, cancellation, and cumulative resource observations;
- candidate diffs, tool calls, sandbox states, and rollback;
- verifier revisions, coverage, independence, exposure, results, and baseline deltas;
- selection inputs, exclusions, coupling, uncertainty, and stopping reason;
- local／Specialist／Remote calls and responsibility contribution classes;
- wall time, visible token usage, available hidden-compute or recurrence observations, hardware, memory, energy, and cost observations;
- human clarification, review, edit, takeover, approval, and recovery observations;
- escaped or blocked out-of-scope and high-severity actions;
- final source, packet, decision, attempt, execution, verification, selection, and integration provenance.

Hidden chain-of-thought is neither required nor treated as audit evidence.

## 15. Falsifiers

Evidence should reject or narrow this architecture if, for the bounded workflow:

- canonical state, policy, credentials, or side effects cannot remain under deterministic local authority;
- Remote or human substitution is required for material semantic responsibilities but cannot be exposed reliably;
- complete configuration identity cannot be reproduced well enough to interpret results;
- verifier false acceptance or adaptive overfitting rises uncontrollably with attempts;
- candidate correlation makes additional search materially redundant while costs continue to grow;
- selectors cannot distinguish valid from plausible candidates under recorded coverage;
- verifier and sandbox costs erase the quality, privacy, resilience, latency, cost, or human-time value;
- local packet compilation requires an unrecorded frontier controller;
- rollback, isolation, or quarantine cannot restore a known safe state;
- task-scoped disclosure repeatedly expands to unrestricted repository state, credentials, or restoration mappings;
- the Local Control Plane adds no measurable value over a conventional single-provider agent under a later fair comparison;
- human review becomes the unrecorded agent performing intent, context, repair, selection, and recovery.

These falsifiers require later metrics and comparison policies. This specification deliberately freezes none.

## 16. Deferred decisions

The following MUST NOT be inferred from v0.2:

- model provider, family, parameter count, active parameters, quantization, or checkpoint;
- one-model versus multi-model local configuration;
- token, recurrent, latent, diffusion, or other reasoning architecture;
- runtime, accelerator, custom silicon, context limit, or concurrency;
- attempt count, diversity method, selector, retry, latency, energy, disclosure, or cost budget;
- task sampling, benchmark, baselines, statistical method, false-accept method, or thresholds;
- Local Specialist or Remote provider;
- exact generated-test, holdout-verifier, or secret-test policy;
- implementation language, storage schema, or transport;
- multi-repository, GUI, scientific, production-operation, or subjective workflows;
- federation, discovery, portable reputation, economics, settlement, governance, or marketplace;
- FIM／DELULU eligibility.

## 17. Stop point

This document completes the strategic revision authorized by ADR 0003. It stops before implementation, model selection, inference, benchmark design, Gate creation, or execution planning.

The next action is human review of whether v0.2 preserves the bounded workflow while making configuration, search, verification, selection, and substitution sufficiently attributable. Any experiment requires a separate human decision record.
