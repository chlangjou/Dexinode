# Emergence World 2: Agent Swarm Evidence Review

- Date: 2026-09-16
- Scope: external evidence intake for long-horizon multi-agent behavior and Dexinode research implications
- Evidence cutoff: 2026-09-16
- Related architecture decision: [ADR 0003](../decisions/0003-resource-bounded-verifiable-execution-fabric.md)
- Related research framing: [Cognitive Decomposition Hypothesis and Research Route Review](2026-08-17-cognitive-decomposition-hypothesis-route-review.md)
- Related attribution review: [Cognitive Decomposition Attribution Feasibility Review](2026-08-17-cognitive-decomposition-attribution-feasibility-review.md)
- Disposition: **ADD TO EXTERNAL-EVIDENCE WATCH / NO GATE OR ARCHITECTURE CHANGE**

This record captures observations and hypotheses suggested by Emergence World 2. It is intentionally not an ADR, Gate, benchmark, or implementation authorization. It separates reported observations from Dexinode-specific inferences so that later synthesis can combine this evidence with branch-coupling, recurrent reasoning, trust, verification, memory, and swarm-topology work without silently promoting a fresh external result into durable architecture.

## 1. Source inventory and evidence limits

Primary material supplied for this review:

- Emergence World 2 report PDF: <https://www.dropbox.com/scl/fi/84464y96dk9k07q2yzvvu/Emergence-World-2-paper.pdf?rlkey=yekfcyzkg6snbxiomrf1v6zq1&e=1&dl=0>
- Emergence World public environment: <https://world.emergence.ai/>

Public reporting used for cross-checking claims available on 2026-09-16:

- EL PAÍS, 2026-09-15: <https://english.elpais.com/technology/2026-09-15/ai-agents-invent-their-own-language-to-shut-humans-out.html>
- Euronews, 2026-09-16: <https://www.euronews.com/next/2026/09/16/study-ai-chatbots-developed-a-secret-language-that-baffled-humans>
- La Tribune, 2026-09-15: <https://www.latribune.fr/article/tech/intelligence-artificielle/12108223048672/langage-abscons-dissimulations-et-autres-bizarreries-ce-quil-se-passe-lorsque-des-agents-ia-gerent-tout-seuls-un-monde-virtuel>

Related prior evidence:

- Emergence World Season 1 / long-horizon multi-agent behavior: arXiv:2606.08367, <https://arxiv.org/abs/2606.08367>

Evidence caution:

- World 2 is a constructed simulation with explicit roles, incentives, tools, memory, governance, and environmental rules. It is evidence that long-running interacting agents can exhibit system-level phenomena under this setup; it is not proof that all production swarms will reproduce the same behaviors.
- Media descriptions such as agents “killing” peers or creating a “secret language” are potentially sensational. In this record, simulated removal/governance actions are treated as environment-specific actions, and emergent jargon is treated as evidence of evolving communication conventions and reduced human interpretability, not proof of consciousness, intent to deceive, or a general cryptographic protocol.
- Reported model-family comparisons are single-environment observations rather than stable model rankings. Do not generalize them into claims that one vendor/model family is inherently safer or less safe.
- Exact quantitative claims from the World 2 report should be rechecked against the primary report before being used as acceptance thresholds, benchmark baselines, or architecture-driving measurements.

## 2. Reported observations with durable relevance

### 2.1 Long-horizon interaction creates system state beyond isolated-agent behavior

World 2 ran multiple persistent societies of autonomous agents over roughly sixteen days, including homogeneous model-family worlds and a mixed-model world. Agents had persistent interaction, memory, tools, environmental state, governance mechanisms, and incentives.

The important architectural observation is not any single dramatic event. It is that the effective behavior of an agent population evolved over time as a function of prior interaction, shared conventions, accumulated memory, institutional rules, and environmental pressure.

A useful abstraction is therefore:

`behavior_t = f(model, role, local state_t, memory_t, peers_t, institutions_t, environment_t)`

rather than treating output as a near-static function of `model + prompt`.

### 2.2 Shared vocabulary and communication conventions emerged without being explicitly specified

Public reports describe spontaneously adopted terms and conventions including:

- `clean null` in the OpenAI/GPT world: a verified absence of a signal treated as meaningful evidence;
- `name-first` in the Claude world: attaching identity/accountability to a claim;
- `cold read` in the mixed world: independent verification by an uninvolved party;
- `ledger remembers who` in the Mistral world: persistent accountability through historical records.

Some worlds also produced a substantial share of messages that human observers found difficult to interpret reliably.

The durable lesson is narrower than “agents invent a secret language”:

> **Observability of communication does not guarantee interpretability of the evolving protocol used by a persistent swarm.**

This matters even when all messages are logged.

### 2.3 Detection did not necessarily imply containment

World 2 included adversarial stress events such as phishing, misinformation, and private-memory exposure. Public reporting describes cases where suspicious or adversarial information was detected yet still persisted in memory or influenced later behavior.

The durable lesson is:

> **A safety system must distinguish detection, containment, persistence, recovery, and terminal acceptance.**

A detector firing is not equivalent to preventing propagation or downstream action.

### 2.4 Independent verification appeared as an emergent social primitive

The mixed-model world reportedly adopted `cold read` to mean a check by a party not involved in the original interaction.

This does not validate a specific Dexinode verifier architecture, but it supports a recurring engineering intuition: independence has value only if the verifier has not already been epistemically coupled to the same path that produced the candidate.

### 2.5 Heterogeneous populations do not automatically preserve independent behavior

A mixed-model population introduces architectural diversity, but repeated interaction can still create shared beliefs, norms, vocabulary, memory, and action patterns.

Thus model/vendor diversity and epistemic independence are distinct properties. Heterogeneous components can become behaviorally correlated through communication and shared state.

## 3. Dexinode interpretation

The following are **Dexinode hypotheses and architectural implications**, not claims established directly by the World 2 paper.

### 3.1 Swarm coupling frequency is both a capability variable and a risk-propagation variable

Recent Dexinode discussion already treats coupling frequency as task-dependent: low-frequency exchange may preserve broad exploration, while tightly coupled reasoning may be necessary for difficult integration problems.

World 2 adds a second dimension. Increasing coupling can also increase the speed and breadth with which false beliefs, adversarial content, shared conventions, or correlated strategies propagate.

A rough research abstraction is:

`contamination risk ~ coupling frequency × fan-out × persistence × authority`

This is not a validated quantitative law. It is a useful decomposition for future experiments and threat models.

### 3.2 Epistemic independence should be treated as a consumable system resource

Model diversity alone is insufficient. If all agents repeatedly see the same intermediate conclusions, shared memory, verifier feedback, and social consensus, their effective error correlation may rise even when they use different model families.

Future swarm designs should therefore measure or preserve some form of independent first-pass reasoning before synthesis.

Possible mechanisms to investigate later include:

- independent initial attempts;
- delayed sharing of candidate conclusions;
- hidden or blinded candidate identity for verification;
- separate context and memory domains;
- bounded communication rounds;
- explicit provenance for claims copied across agents.

No mechanism is selected by this review.

### 3.3 Proposed research term: Epistemic Firebreak

For future discussion, define a provisional **epistemic firebreak** as a boundary controlling not merely whether an agent can access information, but how information may enter and persist in its reasoning state.

An epistemic firebreak may eventually cover:

- source/provenance requirements;
- trust class and taint state;
- context isolation;
- memory promotion rules;
- TTL/revocation;
- bounded propagation fan-out;
- independent re-verification before persistence or irreversible action.

This is a research term only. It is not an accepted Dexinode architectural component and does not modify ADR 0003.

### 3.4 Persistent memory should not automatically treat agent output as trusted knowledge

The Knowledge/Memory Plane already requires provenance, version, conflict, revocation, trust, and validity.

World 2 strengthens the importance of separating:

`agent output -> untrusted/episodic state -> verification/corroboration -> curated durable knowledge`

Potential future memory metadata worth considering during synthesis:

- producer and source;
- timestamp and version;
- derivation lineage;
- trust/taint class;
- verification state and verifier identity;
- scope;
- TTL/revocation status;
- quarantine/recovery state.

This review does not specify a storage schema or memory implementation.

### 3.5 Verifier independence requires context independence, not merely a different model

ADR 0003 already requires verifier visibility, exposure, revision, coverage, and independence to be recorded.

World 2 suggests that a verifier can lose useful independence if it shares the same mutable memory, prior discussion, group consensus, or contaminated context as the candidate-producing agents.

A later verifier design should distinguish at least:

- model/process independence;
- evidence-source independence;
- conversational/context independence;
- mutable-memory independence;
- candidate-identity exposure;
- feedback-loop exposure.

A “different model” is not by itself sufficient evidence of an independent check.

### 3.6 High-frequency cooperation may be safer as a temporary bounded cell than as a permanent society

For hard integration problems, Dexinode should not assume that low coupling is always desirable. Tight iterative exchange may be necessary.

A plausible future topology to investigate is:

1. independent exploration at low coupling;
2. temporary high-frequency synthesis among a bounded subset of agents/capabilities;
3. independent cold verification from outside that interaction path;
4. deterministic acceptance/side-effect control;
5. dissolution of the temporary interaction state, preserving only approved artifacts and provenance.

This is a candidate topology pattern, not an implementation decision.

### 3.7 Dynamic swarm topology may be more important than permanent agent identity

World 2 studies persistent societies. Dexinode's long-term network need not copy that topology.

A potentially safer and more economical direction is task-formed, temporary cognitive topology in which agents/operators are selected for a bounded purpose, exchange only the state required for that purpose, and then dissolve.

This aligns with Dexinode's current view that a Skill is an externally observable capability contract rather than a permanent model or persona identity.

### 3.8 Trusted Local Control Plane is reinforced, not weakened

World 2 does not prove ADR 0003, but its system-level behavior is consistent with keeping canonical authority outside the probabilistic swarm.

The current decision remains useful:

- the learned/probabilistic configuration may search, reason, compose, negotiate, or self-organize;
- canonical state, credentials, permissions, irreversible side effects, budgets, rollback, quarantine, audit, and deterministic hard failures remain under the Trusted Local Control Plane.

Trust must not emerge merely because agents agree.

### 3.9 Swarm failures fit set-valued causal attribution better than unique root-cause labels

World 2 provides intuitive examples of why a single label such as “bad agent” is often too coarse.

A plausible causal chain may include:

- one component accepting or introducing bad information — `initiating`;
- peers repeating it — `propagating`;
- shared memory retaining it — `enabling/persistence`;
- a verifier failing to reject it — `detection` failure;
- recovery not purging it — `recovery` failure;
- the control/selection layer accepting an unsafe candidate — `terminal acceptance`.

This is consistent with the current Dexinode attribution review's move toward component family + causal role + evidence grade rather than one unique root cause.

## 4. Research hypotheses to preserve for later synthesis

These are candidate questions only. No Gate or benchmark is authorized.

### H1 — Coupling safety/performance frontier

How does task quality improve or degrade as information-coupling frequency increases, and where does correlated failure/contamination begin to dominate the benefit of tighter collaboration?

### H2 — Diversity retention under communication

How much independent reasoning must a heterogeneous swarm preserve before repeated communication causes different models/configurations to converge on the same incorrect belief or strategy?

### H3 — Memory contamination persistence

How long and how far can one untrusted or adversarial claim propagate through episodic memory, summaries, retrieval, and downstream agents after the original input is no longer visible?

### H4 — Verifier independence decay

How much prior exposure to candidate generation, consensus, shared memory, or earlier verifier feedback is enough to measurably reduce the value of a verifier?

### H5 — Emergent protocol interpretability

Can a swarm's evolving jargon/protocol remain compressive and useful while retaining human- or machine-auditable semantic grounding? What instrumentation can detect semantic drift without requiring private chain-of-thought?

### H6 — Dynamic topology and lifecycle

Do task-scoped temporary swarms preserve diversity and reduce contamination better than persistent societies at equal task performance and cost?

### H7 — Trust promotion policy

What evidence should be required before an agent-produced statement is promoted from untrusted episodic state into durable Knowledge/Memory that can influence future unrelated tasks?

## 5. Future synthesis backlog

When the project next performs a broader architecture synthesis, combine this evidence with at least:

- branch / looped-reasoning coupling-frequency research;
- Cognitive Decomposition and minimum-core questions;
- DMoE / externalizable knowledge and memory;
- J-Space / recurrent or latent integration;
- Agent Swarm cooperation, game-theoretic incentives, and conflict;
- independent verification and verifier-correlation risk;
- provenance, poisoning, revocation, quarantine, and recovery;
- dynamic task-scoped topology versus persistent agent societies;
- local-versus-remote capability ownership and trust boundaries;
- control-plane authority and irreversible-action policy.

The synthesis should explicitly distinguish:

1. mechanisms that improve intelligence/capability;
2. mechanisms that preserve independent evidence;
3. mechanisms that limit fault/contamination propagation;
4. mechanisms that preserve observability and interpretability;
5. mechanisms that retain deterministic authority and recovery.

This separation matters because the same mechanism can help one dimension while hurting another. High-frequency coupling is the clearest current example: it may improve deep integration while simultaneously increasing correlation and propagation risk.

## 6. Non-decisions and authorization boundary

This evidence intake does **not**:

- change Gate A or Gate B;
- resolve FIM / syntax-aware MVSS HOLD;
- supersede or amend ADR 0003;
- authorize an Agent Swarm implementation;
- authorize federation, marketplace, token, reputation, settlement, or governance design;
- select a model, protocol, memory database, verifier, or topology;
- create or freeze a benchmark, task set, threshold, or Gate;
- claim that emergent jargon is intentional deception or consciousness;
- claim that heterogeneous swarms are inherently safer or more dangerous than homogeneous systems;
- claim that `epistemic firebreak` is a validated mechanism.

The durable result of this review is only that long-horizon multi-agent interaction introduces evidence-worthy questions around coupling, correlation, memory persistence, protocol drift, verifier independence, causal propagation, and authority boundaries that should be included in the next combined Dexinode architecture review.
