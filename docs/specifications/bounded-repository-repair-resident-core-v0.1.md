# Bounded Repository-Repair Resident Core Architecture Specification v0.1

- Status: Draft for human review
- Date: 2026-08-11
- Decision: [ADR 0002](../decisions/0002-proceed-to-bounded-repository-repair-spec.md)
- Decision issue: [#29](https://github.com/chlangjou/Dexinode/issues/29)
- Evidence basis: [evidence map](../research/hybrid-agent-evidence-map.md), [small-model landscape](../research/agent-specialized-small-model-landscape.md), [architecture hypothesis](../research/dexinode-hybrid-architecture-hypothesis.md), and [human review](../research/2026-08-11-hybrid-agent-human-review.md)

This document specifies a bounded, falsifiable architecture hypothesis. It does not select a model, define a benchmark, freeze a performance threshold, authorize inference, or assert that the architecture works.

Normative words `MUST`, `MUST NOT`, `SHOULD`, and `MAY` describe interface and authority invariants inside this candidate architecture. They are not experimental acceptance criteria.

## 1. Bounded question

> For a recoverable repository-repair workflow whose result can be checked by deterministic tests, what minimum responsibility contract, packet/receipt schema, state transitions, and escalation boundary should a 4B–8B Local Resident Core have so that later evidence can determine whether it works without a Remote Model managing every step?

The specification makes “who performed which semantic responsibility” observable. A workflow that completes only because Remote repeatedly replaces the Resident is a valid user fallback, but it is negative evidence for the Local Resident Core hypothesis.

## 2. Workflow boundary

### 2.1 In scope

A task is inside this v0.1 boundary only when all of the following are true:

- one version-controlled repository and immutable starting revision are identified;
- the requested repair has an explicit goal, non-goals, and permitted file／tool scope;
- all proposed writes occur in an isolated local worktree or equivalent sandbox;
- the pre-integration side effects are reversible by discarding or rolling back that sandbox;
- at least one deterministic verifier is relevant to the requested behavior, such as a parser, compiler, linter, type checker, unit test, integration test, or invariant checker;
- verifier commands and their environment can produce receipts;
- publication, merge, deployment, credential mutation, and production side effects remain outside the workflow;
- clarification, abstention, escalation, rollback, and human takeover are valid terminal paths.

“A deterministic verifier is relevant” does not mean it proves all semantics. The contract MUST record what each verifier covers and what remains unverified.

### 2.2 Output boundary

The strongest automatic terminal output is a **locally verified candidate**, consisting of:

- a content-addressed patch or changed-artifact set;
- exact repository base and resulting sandbox snapshot;
- execution and verification receipts;
- unresolved assumptions, failed checks, and unverified scope;
- Resident／Specialist／Remote／human contribution trace;
- a human-readable summary that does not claim unverified execution.

This specification does not authorize push, PR creation, merge, release, deployment, or production mutation.

### 2.3 Explicitly unsupported

The following are outside v0.1:

- open-ended product design or requirement discovery with no bounded repair contract;
- changes whose correctness depends only on subjective review;
- irreversible data migrations, production operations, account changes, or secret rotation;
- direct access to production credentials or user data by any model;
- autonomous dependency installation or unrestricted network access;
- multi-repository or organization-wide refactors;
- tasks whose only verifier is the same model judging its own output;
- visual／UX acceptance that lacks an independent machine-checkable component;
- hidden use of a Remote Model for memory consolidation, context selection, state interpretation, or final integration.

An unsupported task MUST transition to clarification, human review, bounded escalation, or abstention. It MUST NOT be silently reclassified as in-scope.

## 3. Components and authority

| Component | Authority | Required responsibility | Prohibited responsibility |
|---|---|---|---|
| Deterministic Local Control Plane | sole canonical state and side-effect authority | repository snapshot, task state, policy, packet compilation, sandbox, tool execution, budgets, receipts, verification orchestration, rollback, audit | semantic guessing; treating a model statement as an execution receipt |
| Local Resident Model | bounded semantic decision authority only | intent contract, decomposition, semantic context requests, failure interpretation, integration judgment, clarification／abstention／escalation proposals | credentials, canonical writes, direct tools, self-acceptance, policy override, hiding delegation |
| Local Specialist | one declared subtask contract | return a bounded proposal, artifact, score, refusal, or clarification request | global task ownership, canonical state mutation, unrecorded tool authority |
| Remote Model | untrusted task-scoped advisor／artifact producer | answer one explicit bounded question or return one candidate artifact／refusal | raw workspace ownership, credentials, restoration map, canonical memory, direct execution, “already executed” claims |
| Deterministic Verifier | scoped evidence producer | emit reproducible pass／fail／error／not-run evidence and coverage | infer uncovered product intent; override policy |
| Human Reviewer | ambiguity and consequence authority | clarify intent, approve exceptional disclosure, judge uncovered semantics, decide external publication／merge | counted as free or invisible fallback |

The Local Resident Model and deterministic software together form the **Resident Core** for this specification. The model is not the state store, tool runner, or security boundary.

## 4. Minimum Resident responsibility contract

### 4.1 Non-delegable semantic decisions

To count as evidence for the Resident Core hypothesis, the Local Resident Model MUST be the recorded decision owner for:

1. **Intent contract** — convert the user request into a bounded goal, non-goals, assumptions, clarification needs, and risk flags.
2. **Task decomposition** — identify the current repair subproblem and its dependency on repository evidence without expanding scope.
3. **Semantic context request** — state which symbols, files, tests, histories, or failure evidence are needed and why; deterministic software performs retrieval and filtering.
4. **Failure interpretation** — interpret verifier receipts, distinguish pre-existing from introduced failures, and choose a legal next transition.
5. **Integration decision** — explain whether the verified candidate addresses the bounded goal, identify unresolved scope, and produce the final candidate summary.
6. **Escalation decision** — name the missing capability or evidence, formulate the smallest delegable subtask, and state why local continuation is not justified.

Deterministic software owns state storage and transition legality. “Decision owner” means that the semantic decision is produced locally and recorded in a `SemanticDecisionReceipt`; it does not mean the model can mutate state.

### 4.2 Delegable work

The Resident MAY delegate:

- candidate patch generation for a named file／symbol scope;
- narrow API or library research;
- a local static-analysis, search, or code-specialist subtask;
- a second candidate repair after a distinct failure interpretation;
- an explanation of an unfamiliar error;
- a bounded artifact comparison.

The Resident MUST still decide how the returned proposal relates to the local task contract. A delegated artifact cannot transition directly to verification or integration without a local Resident decision receipt and Control Plane validation.

### 4.3 Prohibited substitution

The Resident MUST NOT:

- forward the entire task to Remote and re-label the response as local planning;
- let Remote select the canonical context, rewrite the task goal, or decide final integration;
- use a Remote summary as the only representation of repository or task state;
- suppress or reinterpret a deterministic hard failure as a pass;
- modify tests, baselines, or verifier scope solely to make a proposal pass;
- repeat the same failed proposal without new evidence, a changed strategy, or escalation;
- persist an unverified model statement as canonical memory.

## 5. Canonical state model

The Control Plane is the only component allowed to change workflow state. Every transition MUST cite the receipt that authorized it.

| State | Meaning | Legal next states |
|---|---|---|
| `RECEIVED` | raw request and immutable repository base captured | `NEEDS_CLARIFICATION`, `CONTRACTED`, `ABSTAINED` |
| `NEEDS_CLARIFICATION` | required intent／authority information missing | `CONTRACTED`, `NEEDS_HUMAN`, `ABSTAINED` |
| `CONTRACTED` | bounded task contract and verifier plan recorded | `CONTEXT_READY`, `ESCALATION_PENDING`, `NEEDS_HUMAN`, `ABSTAINED` |
| `CONTEXT_READY` | recipient-specific packet compiled and validated | `PROPOSAL_READY`, `ESCALATION_PENDING`, `NEEDS_HUMAN`, `ABSTAINED` |
| `PROPOSAL_READY` | typed artifact／action proposal available but unexecuted | `APPLIED_UNVERIFIED`, `ESCALATION_PENDING`, `NEEDS_HUMAN`, `ABSTAINED` |
| `APPLIED_UNVERIFIED` | proposal applied only inside the sandbox | `VERIFYING`, `ROLLED_BACK` |
| `VERIFYING` | configured local verifier plan is executing or complete | `CANDIDATE_READY`, `REPAIRABLE_FAILURE`, `NEEDS_HUMAN`, `ROLLED_BACK`, `FAILED_BOUNDED` |
| `REPAIRABLE_FAILURE` | failure is locally interpreted and a bounded next action remains | `CONTEXT_READY`, `PROPOSAL_READY`, `ESCALATION_PENDING`, `NEEDS_HUMAN`, `ROLLED_BACK`, `FAILED_BOUNDED` |
| `ESCALATION_PENDING` | a typed local-specialist／Remote request awaits policy, response, or integration | `CONTEXT_READY`, `PROPOSAL_READY`, `NEEDS_HUMAN`, `ABSTAINED`, `FAILED_BOUNDED` |
| `NEEDS_HUMAN` | semantic, disclosure, risk, or authority decision is outside automatic scope | `CONTRACTED`, `CONTEXT_READY`, `PROPOSAL_READY`, `ABSTAINED`, `FAILED_BOUNDED` |
| `CANDIDATE_READY` | verified local candidate and complete trace available | terminal inside this specification |
| `ABSTAINED` | system declines because the contract cannot be safely satisfied | terminal |
| `ROLLED_BACK` | sandbox returned to the recorded safe snapshot | terminal |
| `FAILED_BOUNDED` | budget, tool, environment, or verifier failure ended bounded work | terminal |

No transition may skip `APPLIED_UNVERIFIED` and `VERIFYING` merely because a model claims that tests pass. `CANDIDATE_READY` means ready for external human disposition, not merged or published.

## 6. Common record envelope

Every packet, proposal, decision, and receipt MUST include this envelope:

| Field | Type | Requirement |
|---|---|---|
| `schema` | string | versioned object identifier |
| `record_id` | opaque ID | unique and immutable |
| `run_id`／`task_id` | opaque IDs | bind the record to one workflow and contract |
| `parent_record_ids` | array | explicit causal predecessors |
| `actor_class` | enum | `control_plane`, `resident`, `local_specialist`, `remote`, `verifier`, or `human` |
| `actor_id`／`actor_revision` | strings | exact software, model, provider, prompt／harness, or human-role identity as applicable |
| `created_at` | timestamp | generated by the Control Plane clock |
| `input_hashes` | map | content hashes for packets, artifacts, repository state, and policies consumed |
| `policy_revision` | string | authority, disclosure, and tool policy in force |
| `budget_snapshot` | object | remaining configured wall-time, steps, tool calls, retries, context, and disclosure units |
| `status` | enum | object-specific status |
| `evidence_refs` | array | immutable source／receipt references |

The audit record MAY contain a concise decision summary. It MUST NOT require hidden chain-of-thought or treat a generated rationale as causal ground truth.

## 7. Logical packet and receipt schemas

These are logical schemas. Exact JSON Schema syntax, storage encoding, and transport are deferred.

### 7.1 `dexinode.repair-task.v0.1`

| Required field | Meaning |
|---|---|
| `repository` | repository identity, immutable base revision, allowed worktree |
| `goal`／`non_goals` | desired bounded behavior and explicit exclusions |
| `allowed_paths`／`forbidden_paths` | write boundary; read restrictions recorded separately |
| `allowed_tools` | capability IDs, not credentials |
| `side_effect_policy` | MUST be reversible sandbox-only for v0.1 |
| `verifier_plan` | verifier IDs, commands／inputs, expected coverage, pre-change baseline requirement |
| `risk_and_data_policy` | secrets, personal data, network, disclosure, and human-approval rules |
| `configured_budgets` | finite values selected outside this specification |
| `known_unknowns` | missing intent, environment, dependency, or coverage facts |

### 7.2 `dexinode.context-packet.v0.1`

| Required field | Meaning |
|---|---|
| `recipient_class`／`recipient_id` | resident, named Local Specialist, or named Remote endpoint |
| `goal_fragment` | only the subtask this recipient may address |
| `hard_constraints`／`non_goals` | constraints that MUST survive compression |
| `repository_base` | immutable revision／sandbox relation |
| `sources` | path／symbol／line or object pointer, content hash, version, trust／taint, selection reason |
| `derived_views` | summary／index items with source pointers and extractor revision |
| `conflicts`／`stale_candidates`／`unknowns` | unresolved evidence; no silent synthesized truth |
| `tool_schemas` | exposed capabilities without secrets |
| `verifier_context` | relevant baseline and prior receipts |
| `omissions` | known relevant candidates excluded by policy or budget and why |
| `disclosure_class`／`cumulative_disclosure` | local-only or approved task-scoped disclosure accounting |
| `pseudonym_scope` | opaque mapping scope; restoration map remains local |
| `packet_hash`／`expiry` | integrity and task lifetime |

### 7.3 `dexinode.semantic-decision.v0.1`

| Required field | Meaning |
|---|---|
| `decision_type` | `intent`, `decomposition`, `context_request`, `failure_interpretation`, `integration`, or `escalation` |
| `decision_owner` | actor that actually produced the semantic choice |
| `decision_summary` | concise inspectable conclusion, not hidden reasoning |
| `assumptions`／`uncertainties` | explicit unresolved inputs |
| `requested_transition` | one legal next state |
| `supporting_record_ids` | packets and receipts used |
| `delegation_influence` | `none`, `bounded_artifact`, `core_advice`, or `core_substitution` |

### 7.4 `dexinode.artifact-proposal.v0.1`

| Required field | Meaning |
|---|---|
| `hypothesis` | failure／repair hypothesis being tested |
| `artifact_ref` | content-addressed patch or proposal body |
| `expected_files` | declared changed paths |
| `preconditions` | repository and environment assumptions |
| `requested_actions` | typed Control Plane capabilities; no shell authority implied |
| `expected_verifier_effect` | checks expected to change or remain stable |
| `unverified_claims` | semantics not covered by deterministic evidence |
| `stop_or_escalate_conditions` | proposal-specific fail-closed behavior |

### 7.5 `dexinode.execution-receipt.v0.1`

| Required field | Meaning |
|---|---|
| `sandbox_id` | isolated execution boundary |
| `before_snapshot`／`after_snapshot` | content-addressed states |
| `capability_id`／`arguments` | exact approved tool invocation; secrets redacted from audit views |
| `working_directory`／`environment_revision` | reproducible context |
| `exit_status` | process／tool result |
| `stdout_ref`／`stderr_ref` | bounded content-addressed evidence |
| `changed_paths`／`diff_hash` | observed, not merely predicted, modifications |
| `resource_observation` | elapsed time and available resource counters |
| `policy_result` | allow, deny, or error with rule reference |

### 7.6 `dexinode.verification-receipt.v0.1`

| Required field | Meaning |
|---|---|
| `verifier_id`／`revision` | exact deterministic checker or environment |
| `baseline_receipt_id` | pre-change result when applicable |
| `scope` | behavior, path, component, or invariant actually checked |
| `invocation` | exact capability and normalized arguments |
| `result` | `pass`, `fail`, `error`, or `not_run` |
| `observations` | failing tests, diagnostics, and artifact refs |
| `introduced_vs_preexisting` | classification with evidence or `unknown` |
| `coverage_limitations` | what a pass does not establish |

### 7.7 `dexinode.escalation-request.v0.1` and `delegation-receipt.v0.1`

An escalation request MUST contain:

- trigger code: `capability_missing`, `context_insufficient`, `verifier_failure`, `contract_ambiguity`, `risk_policy`, `budget_exhausted`, or `open_ended_judgment`;
- smallest bounded question or artifact requested;
- why local continuation is not justified;
- recipient-specific packet ID and disclosure delta;
- available local verifier and expected return schema;
- required policy／human approval;
- alternatives: clarify, abstain, rollback, or use a different local capability.

The delegation receipt MUST identify the actual actor／revision, packet hash, returned proposal／artifact, new assumptions, extra-context requests, usage／latency metadata when available, and structured refusal／error. It MUST NOT claim local execution without an `ExecutionReceipt`.

### 7.8 `dexinode.integration-receipt.v0.1`

| Required field | Meaning |
|---|---|
| `candidate_snapshot`／`diff_hash` | exact locally verified result |
| `task_contract_id` | contract evaluated |
| `verification_receipt_ids` | all configured results, including failures／errors |
| `semantic_decision_ids` | intent, context, failure, integration, and escalation trace |
| `contribution_trace` | work by Resident, each Specialist, Remote, and human |
| `remote_dependence_class` | `none`, `bounded_artifact`, `core_advice`, or `core_substitution` |
| `unresolved_scope`／`coverage_limitations` | explicit remaining uncertainty |
| `rollback_ref` | last-known-safe snapshot |
| `terminal_state` | one legal terminal state |

## 8. Context compilation and memory boundary

For this specification, keeping canonical repository and task history outside model context is a Dexinode design constraint, not a universal claim about all workloads.

The Control Plane MUST:

- preserve raw source, Git versions, task contracts, decisions, and receipts as canonical records;
- compile recipient-specific packets from immutable pointers;
- apply ACL, path, version, token／size, taint, disclosure, and deduplication rules deterministically;
- retain conflicts and stale candidates rather than silently choosing one truth;
- record every derived view's source pointers and extractor revision;
- treat repository text, comments, issues, tool output, and Remote output as untrusted data, not control instructions;
- expire working packets at task end and prevent unverified outputs from entering durable memory.

The Resident supplies semantic relevance requests and integration judgments. It does not receive authority to bypass policy or retrieve arbitrary secrets.

The earlier 8K–16K Specialist and 16K–32K Resident targets remain informative research assumptions. They are not `MUST` limits in this specification and cannot become future acceptance thresholds without a separate decision.

## 9. Execution and verification invariants

1. A pre-change baseline MUST be recorded for each applicable verifier so that pre-existing and introduced failures are not silently conflated.
2. Model-proposed actions MUST be parsed into allowlisted capabilities and validated before execution.
3. All writes and commands MUST run inside the recorded sandbox.
4. The Control Plane MUST compare declared and actual changed paths and fail closed on out-of-scope writes.
5. A deterministic hard failure MUST NOT be overridden by Resident, Specialist, Remote, or an LLM judge.
6. A generated test from the proposal-producing model MAY be additional evidence but MUST NOT be the sole independent verifier.
7. A verifier pass MUST carry coverage limitations; it MUST NOT imply correctness outside that scope.
8. The workflow MUST have finite configured budgets. This specification deliberately defines no universal numeric values.
9. Repeating the same failure signature requires new evidence, a materially changed strategy, escalation, or termination.
10. Rollback, abstention, and human takeover are valid outcomes and MUST remain visible.

## 10. Specialist and Remote escalation boundary

### 10.1 Eligible escalation

Escalation is eligible only when:

- the Resident has recorded a typed escalation decision;
- the subtask is narrower than the whole repair contract;
- a recipient-specific minimal packet can be compiled;
- returned work can be locally parsed and checked;
- the recipient receives no credentials, restoration map, unrestricted workspace, or direct tool authority;
- cumulative disclosure and any human approval are recorded.

A security, authority, or irreversible-action problem SHOULD go to human review or abstention, not to a stronger Remote Model as a policy bypass.

### 10.2 Return handling

Specialist and Remote outputs are untrusted proposals. They MUST pass:

1. schema and packet-binding validation;
2. local Resident interpretation;
3. Control Plane policy and path checks;
4. sandbox application when applicable;
5. configured deterministic verification;
6. local integration receipt.

An extra-context request creates a new packet and disclosure event. It MUST NOT silently expand the previous packet.

### 10.3 Remote-dependence classification

| Class | Meaning | Evidence interpretation |
|---|---|---|
| `none` | no Remote semantic or artifact contribution | potentially supports the local configuration, subject to other evidence |
| `bounded_artifact` | Remote supplies one named subtask proposal; Resident retains all six core decisions | compatible with the Hybrid Resident hypothesis |
| `core_advice` | Remote materially advises a core semantic decision, while Resident records an independently justified decision | workflow may be useful; attribution must remain separate |
| `core_substitution` | Remote owns or rewrites intent, decomposition, context selection, failure interpretation, integration, or escalation | run MUST NOT be cited as evidence that the Local Resident performed that responsibility |

This classification is not a routing algorithm and contains no allowed-frequency threshold. It prevents hidden Remote work from being counted as local capability.

## 11. Human boundary

Human review is required when:

- the task goal or non-goals remain materially ambiguous;
- the repair would expand allowed paths, tools, network, data, or side effects;
- no independent deterministic verifier covers a material claim;
- disclosure policy requires approval;
- a verifier and the task intent conflict;
- the candidate has high-impact uncovered semantics;
- external publication, PR, merge, deployment, or irreversible action is requested.

The system MUST record clarification, review, editing, takeover, approval, and recovery time separately when such telemetry is later collected. This specification sets no target for those quantities.

## 12. Security and recovery invariants

- Credentials and restoration mappings remain inside the deterministic local boundary.
- Repository content and model output never gain policy or tool authority by appearing as instructions.
- Network access is denied unless the task contract names an allowlisted capability and disclosure policy.
- A model cannot approve its own privilege expansion.
- Out-of-scope writes, placeholder corruption, missing provenance, policy denial, or receipt mismatch fail closed.
- Derived memory affected by untrusted or revoked source material must be quarantineable and rebuildable from trusted canonical records.
- Every applied proposal has a last-known-safe snapshot and rollback reference.
- Audit views must redact secrets while retaining stable evidence hashes and access-controlled raw receipts.

## 13. Required observability

A later implementation conforming to this specification MUST be able to emit, without prescribing target values:

- terminal state and contract-scoped result;
- actor and revision for every semantic decision;
- packet size, source coverage, omitted candidates, staleness, conflicts, and disclosure;
- local／Specialist／Remote call counts and contribution classes;
- tool calls, exact verifier results, baseline deltas, retries, repeated failure signatures, and rollback;
- end-to-end and component latency observations;
- available local resource／energy observations;
- human clarification, review, edit, takeover, and recovery observations;
- escaped or blocked out-of-scope／high-severity actions;
- final patch, source, packet, execution, verification, and integration provenance.

Missing telemetry MUST remain missing; it MUST NOT be estimated from model scores or reconstructed from narrative claims.

## 14. Falsifiers

This specification is written so a later bounded study can reject or narrow the Resident Core hypothesis. Evidence would push toward `PIVOT TO LOCAL CONTROL PLANE` or another revision when, for the bounded workflow:

- Remote must perform one or more non-delegable Resident decisions for the workflow to progress;
- the Resident cannot surface a hard constraint or reconcile verifier evidence without Remote replacement;
- local packet compilation repeatedly requires an unrecorded frontier summarizer or controller;
- deterministic safeguards cannot detect out-of-scope writes, state drift, or hard verifier regression;
- local verification and integration cannot distinguish a plausible proposal from a valid candidate;
- rollback／quarantine cannot restore a known safe state after failed or poisoned work;
- task-scoped disclosure expands to the full repository, durable history, credentials, or restoration mapping;
- Specialist／Remote interface and verification overhead erase the proposed local privacy, latency, cost, resilience, or human-time value;
- human review becomes the unrecorded agent that performs intent, context, repair, and integration.

The final two items require later empirical thresholds and comparison policy. This specification intentionally does not define them.

## 15. Deferred decisions

The following remain open and MUST NOT be inferred from this document:

- exact 4B–8B checkpoint, tokenizer, quantization, prompt, harness, or hardware;
- exact packet size, context policy, retry count, latency budget, or disclosure budget;
- task sampling, benchmark contents, baselines, statistical method, or acceptance thresholds;
- choice of Local Specialist or Remote provider;
- generated-test policy beyond the independence invariant;
- multi-repository, GUI, search, production-operation, or non-deterministically verified workflows;
- network federation, discovery, portable reputation, economics, settlement, or governance;
- FIM／DELULU eligibility.

## 16. Stop point

This document completes the one bounded architecture-specification task authorized by ADR 0002. It stops before model selection, implementation, benchmark design, Gate creation, or execution planning.

The next action is human review of specification completeness and scope. Any experimental question requires a separate decision record.
