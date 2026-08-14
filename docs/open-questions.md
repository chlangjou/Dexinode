# Open questions

This is the active research backlog. Questions should move into experiments or decision records as they become concrete.

## Highest-decision-value question

Does the [v0.2 bounded repository-repair specification](specifications/bounded-repository-repair-verifiable-execution-v0.2.md) define a sufficiently narrow, attributable, and falsifiable execution／search boundary while keeping model size, reasoning architecture, inference hardware, attempt count, benchmark, and thresholds replaceable?

Human review must answer this before any implementation, benchmark, Gate, or model run is considered.

## User workflow and task contract

- Which real task would a user knowingly choose the hybrid configuration for rather than a strong cloud agent?
- What quality, active-human-time, latency, privacy/offline, and failure-loss thresholds define “good enough” for that task?
- Which tasks can be decomposed and verified, and which remain irreducibly global or high risk?
- Is software engineering the strongest first domain because it exposes deterministic tools, tests, repository provenance, and real context pressure?

## Local Decision Configuration

- What is the lowest-resource complete local configuration that can clarify intent, request context, interpret failure, compare candidates, stop, and escalate correctly?
- Which responsibilities are best assigned to deterministic software, one model, several local models, a Specialist, or Remote fallback?
- Can a local configuration manage memory/context without a hidden Remote backbone or unrecorded human selection?
- Which capability changes come from model weights, context policy, harness, search, tools, verifier, hardware, or fallback?
- How should clarification, abstention, selection, and stopping quality be measured without freezing a model generation?
- When is the earlier single-model Resident Core still the simplest adequate Local Decision Configuration?

## Memory and context engineering

- Can a large workspace be compiled into an 8K–32K task packet without losing critical dependencies?
- How should episodic memory, structured facts, project/task state, procedure, failures, and source provenance differ?
- How are stale, conflicting, revoked, or poisoned memories reconciled and recovered?
- Does memory improve downstream action success rather than only factual recall?
- When does the reader fail to reconcile correct retrieved evidence?
- How can automatic packets be compared with human-selected gold context without prematurely freezing a benchmark?

## Loop, harness, workflow, and graph engineering

- Which fixed loops reliably lower the model-capability requirement?
- When do planning, reflection, graph search, or multi-agent patterns only add retries, latency, false consensus, or benchmark overfit?
- Can a single agent sequentially reproduce a homogeneous multi-agent workflow?
- Which gains depend on a scalar verifier that is unavailable in real work?
- How should model, harness, context policy, tool interface, budget, retries, and evaluator be reported separately?

## Candidate search, selection, and verifier risk

- For which repair classes does additional candidate search produce materially different hypotheses rather than correlated paraphrases?
- How should parent lineage and shared model／prompt／context／training dependencies be used to estimate candidate correlation?
- Which selector can identify a valid candidate without merely reproducing the generator's preferences?
- What verifier independence classes are operationally useful?
- How does adaptive reuse of compiler／test feedback change the evidentiary meaning of a pass?
- How should false acceptance be controlled when many candidates see the same incomplete verifier?
- When are hidden or holdout checks necessary, and when would they create benchmark rather than workflow evidence?
- How should verifier execution, sandboxing, selection, and human review costs be counted against cheap generation?
- What stopping policy prevents “try until pass” while still benefiting from fast inference?
- Can a later study distinguish search gain from test overfitting, selector leakage, Remote substitution, and human repair?

## Agent-specialized small models

- Which edge-small or absolute-small models have end-to-end evidence for tool use, GUI operation, coding agents, search, context selection, routing, or verification?
- Which apparently small systems are actually large-total MoE models with low active parameters?
- Do tool-call syntax scores transfer to multi-turn recovery, clarification, and real environment success?
- Are there at least two bounded absolute-small capability classes worth retaining?
- Which claims remain stable when the full configuration—including runtime, quantization, hardware, harness, search, and verifier—is pinned?
- What event should trigger a model-landscape refresh rather than continuous catalog maintenance?

## Model and inference architecture turnover

- Which distilled or locally deployable models materially cross a workflow frontier after independent end-to-end evaluation?
- When do model-specific accelerators improve total workflow economics after quality loss, refresh cadence, verifier cost, and hardware availability are included?
- Which recurrent／latent methods survive compute-, parameter-, memory-, and task-matched comparisons outside narrow reasoning benchmarks?
- How can hidden-state recurrence be observed and budgeted without requiring hidden chain-of-thought?
- Does faster inference improve verified completion, or only increase candidate volume and test exposure?
- How short should the validity period of model-specific evidence be, and which changes require a new configuration identity?

## Hybrid trust boundary

- Which work must stay in deterministic local software, a Local Resident Model, a Local Specialist, a Remote Model, or human review?
- Can remote disclosure remain task-scoped while preserving enough semantics to succeed?
- If every important step still calls a Remote Model, what measurable value remains in the Local Decision Configuration and Control Plane?
- How are prompt injection, poisoned memory, untrusted artifacts, and side effects prevented from persisting across tasks?
- How much human review and rework does the complete workflow require?
- Can responsibility-level `core_substitution` and `human_substitution` be detected without access to private chain-of-thought?

## Engineering-bound but not fully solved

- Can approved pseudonymization mappings round-trip across files and messages with stable placeholders and fail-closed restoration?
- What fraction of sensitive entities is missed, and when does pseudonymization destroy task semantics?
- How should deterministic storage, indexing, versioning, deduplication, and audit logs be implemented?

## Longer-term network backlog

### Value and scope

- Which tasks benefit enough from specialization to offset routing and verification overhead?
- Is Dexinode primarily a protocol, a runtime, a marketplace, or a federation toolkit?
- What can it provide that existing agent tool protocols and distributed job systems cannot?
- Should the first use case be software engineering, private enterprise knowledge, scientific work, or edge inference?

### Skill semantics

- How narrow should a skill be?
- How are compatible versions negotiated?
- Can capability descriptions remain expressive without becoming unmatchable natural-language claims?
- How do we represent probabilistic quality and domain limitations?
- How does a skill declare side effects and required authority?

### Routing and planning

- Does the caller select a complete workflow, or can downstream nodes delegate?
- How are cost, latency, quality, privacy, locality, and diversity traded off?
- How does the router explore new providers without risking important workloads?
- How do we detect routing loops and correlated model failures?
- Who pays for failed attempts and verification?

### Verification

- Which task classes allow deterministic verification?
- When is replication cheaper than sophisticated verification?
- How do we prevent verifier collusion, bribery, or shared blind spots?
- Can private inputs be verified without exposing them?
- What evidence is useful without leaking proprietary models or prompts?
- How do humans enter or override the acceptance process?

### Reputation

- Should reputation attach to a node, operator, skill version, model, or complete supply chain?
- How quickly should old evidence decay?
- How do new entrants avoid a permanent cold-start disadvantage?
- How do we resist Sybil identities and reputation laundering?
- Can reputation remain plural and consumer-specific while still being portable?

### Security and safety

- How are prompt injection and tool abuse contained across trust boundaries?
- What prevents a skill from exfiltrating task data?
- How are malicious skill declarations and dependency substitution detected?
- How are credentials delegated with least privilege and revoked?
- What tasks should never be routed to unknown nodes?
- How do we contain denial-of-service, poisoned evidence, and dispute spam?

### Decentralization and governance

- Which components must truly be decentralized to avoid capture?
- What is the minimum viable federation model?
- How are protocol changes proposed and adopted?
- How can conformance tests evolve without becoming a central gatekeeper?
- How do legal jurisdictions and export restrictions affect node participation?

### Economics

- Is direct payment necessary, or are reciprocal/federated quotas enough?
- What unit represents value: time, compute, task, verified result, or negotiated bundle?
- How are failed or partially accepted tasks accounted for?
- Could markets reward benchmark gaming or low-value task fragmentation?
- At what stage would a token add real utility rather than distraction?

### Operations

- How are nodes updated without silently changing a skill's behavior?
- What observability can be shared without revealing private workloads?
- How does the network handle intermittent edge nodes?
- How are large artifacts transferred and retained?
- What is the simplest deployment experience for a small local specialist?

### Naming and project identity

- Is “Dexinode” sufficiently distinct in trademarks, packages, and domains?
- Which domain should anchor the project?
- Should the public name emphasize decentralization, skills, weaving, or nodes?
- When should the working name become a formal naming decision?
