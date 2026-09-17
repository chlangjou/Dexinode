# Open questions

This is the active research backlog. Questions should move into bounded decision records or experiments only when they become concrete and receive explicit human authorization.

## Resolved architecture-boundary question

Does the [v0.2 bounded repository-repair specification](specifications/bounded-repository-repair-verifiable-execution-v0.2.md) define a sufficiently narrow, attributable, and falsifiable execution／search boundary while keeping model size, reasoning architecture, inference hardware, attempt count, benchmark, and thresholds replaceable?

[Human review](research/2026-08-14-verifiable-execution-v0.2-human-review.md) answered **yes** and accepted v0.2 as the current architecture boundary. This is an architecture decision, not evidence that the design works.

## Current provisional long-horizon hypothesis

The [Cognitive Decomposition Hypothesis and route review](research/2026-08-17-cognitive-decomposition-hypothesis-route-review.md) adopts this research framing:

> A useful system may be partially decomposable into a trusted Local Control Plane; a resource-bounded Cognitive Core with semantic grounding, automatic foundation capabilities, and deliberate／recurrent integration; external Knowledge／Memory and Operator／Capability planes; and independent Verification.

Knowledge–reasoning decoupling is expected to be partial. J-Space and DMoE are evidence examples, not selected Dexinode components. Skill remains a capability contract rather than a model, Adapter, node, or cognitive location.

## Highest-decision-value unresolved question

Should Dexinode open a separate decision issue to formulate exactly one decomposition-attribution experiment, and can the chosen bounded workflow distinguish these failure sources well enough to justify execution?

1. missing, stale, conflicting, or incorrectly selected knowledge;
2. missing or incorrect operator capability;
3. Cognitive Core comprehension, reasoning, or integration failure;
4. candidate selection or verifier failure;
5. hidden Remote or human substitution.

No experiment, benchmark, Gate, model run, J-Space work, DMoE work, or implementation is authorized while this remains unresolved.

## Cognitive Core and decomposition boundary

- What is the minimum complete local configuration that can understand intent, request missing information, maintain task state, integrate evidence, compare candidates, stop, abstain, and escalate correctly?
- Which language, semantic, world-model, and automatic capabilities must remain jointly pretrained inside the core?
- Which knowledge can be externalized without destroying conceptual grounding or increasing reader-integration failures?
- How should model size, recurrence depth, context policy, tools, operators, verifier support, runtime, and hardware be compared as one complete configuration?
- Does additional latent／recurrent computation lower the minimum viable core size, or mostly amplify capabilities already supplied by a larger backbone?
- When is one local general model still the simplest adequate Cognitive Core?
- Can a local core operate without a hidden Remote backbone or unrecorded human selection?
- What evidence would falsify the claim that a separate local Cognitive Core provides value over a strong monolithic or Remote agent?

## Knowledge and memory plane

- How should foundational semantic knowledge be distinguished from factual, current, private, domain, and episodic knowledge that can be externalized?
- Can a large workspace be compiled into a bounded task packet without losing critical dependencies, bindings, or constraints?
- How should raw source, structured facts, project/task state, procedures, failures, and derived summaries differ?
- How are stale, conflicting, revoked, poisoned, or legally restricted knowledge sources reconciled and recovered?
- When does correct retrieval fail because the core cannot reconcile or use the evidence?
- Does parametric knowledge injection offer measurable benefits over retrieval after update cost, compatibility, interference, and verification are counted?
- How can automatic packets be compared with complete human-selected knowledge without prematurely freezing a benchmark?
- Does memory improve verified downstream action rather than only factual recall?
- What provenance and revocation contract is needed for knowledge artifacts from independent providers?

## Operator／Capability plane and integration packets

- Which capabilities are best supplied by deterministic software, formal solvers, compilers, databases, learned Adapters, complete models, agents, Remote services, or humans?
- What output schema lets a Cognitive Core reuse an operator result on a structurally new requirement?
- Which entities, role bindings, relations, constraints, confidence, evidence, and unresolved questions must be preserved?
- When should an operator return an intermediate claim, a candidate artifact, a score, a refusal, or a final result?
- Can independently developed operators compose without hidden coupling or semantic loss?
- How should compatibility be bound to model revision, runtime, quantization, tokenizer, tool version, or other substrate identity?
- How are malicious or backdoored parameter artifacts, tools, and services evaluated and contained?
- How should capability contribution be attributed when the final result combines the core, several operators, Remote support, and human repair?
- Are there bounded operator classes whose value survives complete configuration and verifier costs?

## Deliberative workspace and recurrent／latent reasoning watch

- Do workspace-like representations recur across open model families, training stages, and scales?
- Which tasks use a deliberate workspace and which remain automatic?
- What mechanism decides what enters the workspace, and when does that mechanism fail?
- Can workspace state preserve relations, variable bindings, causality, uncertainty, and procedural structure rather than only a sparse concept list?
- Can an external knowledge or operator result influence the core through observable, causally load-bearing intermediate state?
- Which recurrent interfaces survive compute-, parameter-, memory-, data-, and task-matched comparisons?
- How should recurrence depth, wall time, FLOPs, memory, and stopping be observed without requiring private chain-of-thought?
- Does faster or deeper reasoning improve verified completion, or only increase candidate volume and verifier exposure?
- Which material event should trigger a workspace／latent-reasoning evidence refresh?

J-Space is not assumed to be a cross-model ABI, and raw latent state is not a planned Dexinode network protocol.

## Loop, search, selector, and verifier risk

- Which fixed loops reliably lower the Cognitive Core capability requirement?
- When do planning, reflection, graph search, or multi-agent patterns only add retries, latency, false consensus, or benchmark overfit?
- Can a single agent sequentially reproduce a homogeneous multi-agent workflow?
- For which repair classes does additional search produce materially different hypotheses rather than correlated paraphrases?
- How should parent lineage and shared model／prompt／context／training dependencies be used to estimate candidate correlation?
- Which selector can identify a valid candidate without reproducing the generator's preferences?
- What verifier independence classes are operationally useful?
- How does adaptive reuse of compiler／test feedback change the evidentiary meaning of a pass?
- How should false acceptance be controlled when many candidates see the same incomplete verifier?
- When are hidden or holdout checks necessary, and when would they create benchmark rather than workflow evidence?
- What stopping policy prevents “try until pass” while retaining value from fast inference?
- How should verifier execution, sandboxing, selection, and human review costs be counted against generation savings?

## User workflow and system value

- Which real task would a user knowingly choose a resource-bounded local configuration for rather than a strong cloud agent?
- What quality, active-human-time, latency, privacy/offline, resilience, and failure-loss thresholds define “good enough”?
- Is repository repair still the strongest first workflow because it exposes deterministic tools, immutable bases, provenance, and recoverable effects?
- Which tasks can be decomposed and verified, and which remain irreducibly global or high risk?
- Can a controlled comparison distinguish value from local privacy, knowledge locality, operator access, reasoning depth, search, verification, and Remote fallback?
- If every important step still calls a Remote model, what measurable value remains in the local core and Control Plane?

## Trust, security, and engineering

- Which authority must remain in deterministic local software rather than a learned component?
- Can Remote disclosure remain task-scoped while preserving enough semantics to succeed?
- How are prompt injection, poisoned memory, untrusted artifacts, malicious operators, and side effects prevented from persisting across tasks?
- Can responsibility-level `core_substitution`, `operator_substitution`, `remote_substitution`, and `human_substitution` be detected without access to private chain-of-thought?
- Can approved pseudonymization mappings round-trip across files and messages with stable placeholders and fail-closed restoration?
- What fraction of sensitive entities is missed, and when does pseudonymization destroy task semantics?
- How should deterministic storage, indexing, versioning, deduplication, and audit logs be implemented?
- How much human review and rework does the complete workflow require?

## Routes closed as primary research programs

The following are no longer active default routes. Their historical evidence remains preserved.

- `One Skill = one standalone model`.
- `One Skill = one network node`.
- Broad-domain routing that hands the complete task to one Specialist as a General replacement.
- A fixed 4B–8B Resident or reasoning boundary.
- Distributed whole-model inference／idle compute as a required decentralization thesis.
- Continuous small-model catalog and leaderboard maintenance.
- Parametric procedural Skill or J-Space ABI as the immediate next Gate.
- Re-running Gate A／B because a newer model exists without a new falsifiable system question.
- Network-first federation, marketplace, token, reputation, settlement, or governance design.

“Closed” here means closed as a project foundation or current phase, not scientifically disproven.

## Preserved but dormant

### FIM／syntax-aware MVSS

FIM remains `HOLD`. It may later appear as an operator implementation, but no DELULU artifact, licensing, verifier, comparability, or runtime closure is authorized.

### Model, runtime, and hardware evidence

Refresh only when a material change affects the minimum-core, decomposition, or complete-system question. Do not maintain an exhaustive standing catalog.

### Independent providers and network

Independent providers may eventually supply knowledge, operators, verifiers, compute, or complete capabilities. No network prototype is authorized until one trust domain demonstrates measurable local composition and verification value.

## Longer-term conditional network backlog

### Agent Swarm cooperation and institutional layer

This is a dormant future architecture pressure, not an active Dexinode research route or implementation authorization.

If Dexinode later involves independently operated capability providers with different owners, incentives, costs, reliability, and authority boundaries, cooperation can no longer be treated only as an orchestration or model-alignment problem.

The working hypothesis is:

- robust cooperation should rely primarily on protocol, capability isolation, verification, incentives, and bounded failure containment;
- cooperative model post-training is defense in depth, not the primary security boundary;
- the target is conditional, incentive-compatible cooperation rather than unconditional cooperation or cooperation as a universal dominant strategy;
- low switching cost, revocable authority, evidence recording, and rerouting may be more important than requiring high interpersonal trust between agents;
- identity and reputation may eventually need separate scopes for operator, provider, capability version, implementation, endpoint, verifier, and supply chain.

If this pressure becomes active, Skill Contracts may need to expand beyond input/output semantics to include authority, cost, SLA, verification, failure semantics, revocation, arbitration, and optional settlement hooks.

Activation condition: one trust domain must first demonstrate measurable composition and verification value. This note does not authorize federation, marketplace, token, reputation-system, settlement, governance, or Agent Swarm implementation work.

### Value and scope

- What can a capability and evidence fabric provide that conventional local plugins, agent tool protocols, or distributed job systems cannot?
- Which independently provided knowledge, operators, verifiers, or compute sources create durable value?
- Is Dexinode primarily a protocol, runtime, federation toolkit, or evidence portability layer?

### Capability semantics and discovery

- How narrow should a capability contract be?
- How are compatible versions and substrate constraints negotiated?
- How are probabilistic quality, domain limits, side effects, required authority, and evidence represented?
- Can discovery remain expressive without collapsing into unmatchable natural-language claims?

### Verification, reputation, and security

- Which tasks allow deterministic verification, and when is replication cheaper?
- How do we prevent verifier collusion, shared blind spots, prompt injection, exfiltration, malicious artifacts, and dependency substitution?
- Should reputation attach to a provider, capability version, artifact, verifier set, or complete supply chain?
- Can reputation remain consumer-specific and portable without one global authority?

### Decentralization, operations, and economics

- Which components must truly be decentralized to improve resilience, privacy, competition, or anti-capture properties?
- What is the minimum viable federation model?
- How are intermittent providers, artifact transfer, updates, revocation, legal jurisdiction, liability, and compliance handled?
- Is direct payment necessary, and how are failed or partially accepted tasks accounted for?
- At what stage would a token add real utility rather than distraction?

## Naming and project identity

- Is “Dexinode” sufficiently distinct in trademarks, packages, and domains?
- Which domain should anchor the project?
- Should the public name emphasize decentralization, capabilities, weaving, evidence, or nodes?
- When should the working name become a formal naming decision?