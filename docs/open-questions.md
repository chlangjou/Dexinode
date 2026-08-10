# Open questions

This is the active research backlog. Questions should move into experiments or decision records as they become concrete.

## Highest-decision-value question

Does the [bounded repository-repair specification](specifications/bounded-repository-repair-resident-core-v0.1.md) define a sufficiently narrow, attributable, and falsifiable Resident Core boundary without turning provisional assumptions into acceptance criteria?

Human review must answer this before any implementation, benchmark, Gate, or model run is considered.

## User workflow and task contract

- Which real task would a user knowingly choose the hybrid configuration for rather than a strong cloud agent?
- What quality, active-human-time, latency, privacy/offline, and failure-loss thresholds define “good enough” for that task?
- Which tasks can be decomposed and verified, and which remain irreducibly global or high risk?
- Is software engineering the strongest first domain because it exposes deterministic tools, tests, repository provenance, and real context pressure?

## Minimum Viable Resident Core

- What is the smallest local model/configuration that can clarify intent, maintain task state, choose tools, recover from failure, and escalate correctly?
- Which Resident Core functions are deterministic software problems, and which require learned judgment?
- Can an absolute-small model manage memory/context without a hidden remote large-model backbone?
- How should clarification, abstention, and escalation quality be measured?

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

## Agent-specialized small models

- Which edge-small or absolute-small models have end-to-end evidence for tool use, GUI operation, coding agents, search, context selection, routing, or verification?
- Which apparently small systems are actually large-total MoE models with low active parameters?
- Do tool-call syntax scores transfer to multi-turn recovery, clarification, and real environment success?
- Are there at least two bounded absolute-small capability classes worth retaining?

## Hybrid trust boundary

- Which work must stay in deterministic local software, a Local Resident Model, a Local Specialist, a Remote Model, or human review?
- Can remote disclosure remain task-scoped while preserving enough semantics to succeed?
- If every important step still calls a Remote Model, what measurable value remains in the Local Resident Model?
- How are prompt injection, poisoned memory, untrusted artifacts, and side effects prevented from persisting across tasks?
- How much human review and rework does the complete workflow require?

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
