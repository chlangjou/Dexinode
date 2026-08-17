# J-Space and J-CoT — Material Evidence Review

- Date: 2026-08-17
- Scope: pre-Gate external research evidence
- Primary source: [Gurnee et al., *Verbalizable Representations Form a Global Workspace in Language Models*, arXiv:2607.15495v1](https://arxiv.org/abs/2607.15495)
- Supporting source: [Anthropic, *A global workspace in language models*](https://www.anthropic.com/research/global-workspace)
- Follow-on source: [Wu et al., *J-CoT: Chain-of-Thought in J-Space*, arXiv:2607.21981v1](https://arxiv.org/abs/2607.21981)
- Related DMoE evidence: [2026-08-16 DMoE review](2026-08-16-dmoe-parametric-knowledge-injection-evidence-review.md)
- Related decision: [ADR 0003](../decisions/0003-resource-bounded-verifiable-execution-fabric.md)
- Related specification: [Repository-Repair Verifiable Execution Fabric Specification v0.2](../specifications/bounded-repository-repair-verifiable-execution-v0.2.md)
- Evidence cutoff: 2026-08-17
- Disposition: **NEW MATERIAL EVIDENCE / NO EXPERIMENTAL AUTHORIZATION**

This record separates paper-supported observations from Dexinode-specific inference. It does not treat J-Space as a Dexinode protocol, select a model, authorize implementation, or claim that knowledge and reasoning have already been fully separated.

## Executive conclusion

The Anthropic paper provides causal evidence that Claude-family models contain a small, privileged set of verbalizable representations used for deliberate control, intermediate reasoning, flexible reuse, and broadcast to multiple downstream computations, while much routine language processing and familiar inference proceeds without those representations. The paper calls this set **J-Space** and interprets it as functionally workspace-like.

A separate work-in-progress paper, J-CoT, turns a model-specific J-Space coordinate system into a recurrent reasoning boundary. Its main experiments use a reasoning-adapted Qwen3-8B-Base model, and its scaling study includes dense 7B through 405B backbones. This is material evidence that a resource-bounded model can expose a usable workspace-like recurrent interface; it is not evidence that an untouched 8B model possesses the same rich global-workspace behavior demonstrated causally in Claude, nor that an 8B cognitive core is sufficient for Dexinode workloads.

The appropriate Dexinode interpretation is architectural:

> J-Space-like structure is evidence that deliberate reasoning may rely on a relatively compact shared workspace operating amid much larger automatic processing. It strengthens the plausibility of a partially decomposed cognitive architecture, but J-Space itself is neither the whole reasoning engine nor a cross-model Skill ABI.

## 1. Paper-supported observations

### 1.1 J-Space has workspace-like functional properties in the evaluated Claude models

The Anthropic paper identifies token-indexed directions using the Jacobian lens and reports five functional properties:

- contents can be verbally reported;
- the model can deliberately summon and hold them;
- they carry intermediate values used in silent reasoning;
- the same representation can be reused by different downstream computations;
- most routine processing does not require them.

The authors also report structural properties consistent with a shared workspace: coherent J-Space content appears in an intermediate band of layers, only tens of concepts are strongly active at once, and J-Space-aligned directions are read and written unusually broadly by model components.

**Evidence state:** `SUPPORTED BY PAPER IN THE EVALUATED CLAUDE MODELS`.

### 1.2 J-Space is causally involved, not merely a passive readout

The paper directly intervenes on J-Space representations. Examples include replacing an intermediate `spider` representation with `ant`, changing the model's later answer from eight legs to six, and replacing a country representation so that distinct downstream tasks produce the corresponding capital, language, continent, or currency for the substituted country.

These interventions support the claim that at least some downstream computation reads workspace representations as load-bearing intermediate state. They do not establish a universal semantic ABI or prove that every model operation passes through J-Space.

**Evidence state:** `CAUSALLY SUPPORTED IN PAPER SCOPE`.

### 1.3 Automatic capabilities and deliberate reasoning are functionally separable to a meaningful degree

When the paper suppresses active J-Space contents, the model retains substantial fluency, parsing, sentiment classification, passage-based factual extraction, and routine inference, while multi-step reasoning and other flexible tasks degrade sharply. In the language-identity intervention, the model continues fluent Spanish automatically even when its workspace-level language identity is redirected toward French; tasks that must name or flexibly use the language identity follow the workspace intervention.

This supports a distinction between:

- deeply practiced, automatic processing distributed through the broader model; and
- selective, deliberate integration through a shared workspace.

It does not imply that automatic processing is unimportant, cheap, or externally replaceable.

**Evidence state:** `SUPPORTED BY PAPER; BOUNDARY REMAINS TASK-DEPENDENT`.

### 1.4 Post-training can change what enters the workspace and thereby change behavior

The paper reports that post-training changes the model's workspace point of view. It also introduces counterfactual reflection training: the model is trained only on what it would say if interrupted and asked to reflect, rather than directly on the target behavior. The trained model subsequently surfaces reflection-related concepts in uninterrupted task contexts, improves behavior, and loses much of that improvement when those implanted J-Space directions are ablated.

This is stronger than treating J-Space as a fixed display of pre-existing abilities. It shows that training can alter a context-conditioned workspace writer／salience policy and that the resulting representations can causally affect behavior.

It does not prove that a completely novel procedural operator can be installed only by writing concepts into J-Space.

**Evidence state:** `SUPPORTED FOR WORKSPACE SHAPING / NOT PROCEDURAL-SKILL INSTALLATION`.

### 1.5 J-CoT uses J-Space as a recurrent interface on a resource-bounded open backbone

J-CoT represents the state crossing recurrent reasoning cycles as vocabulary-indexed J-Space coefficients. Within each cycle, the model still computes in its full hidden space. The main configuration uses Qwen3-8B-Base after a shared reasoning-adaptation stage, eight non-decoded carriers, a read layer at 12, a write layer at 28, and adaptive recurrence with a default maximum of eight cycles.

J-CoT-Zero adds no J-CoT-specific optimization beyond constructing the model-specific J-lens dictionaries and recurrent runtime. J-CoT-Train optimizes carrier embeddings and a small read gate while keeping the Transformer and J-lens dictionaries frozen.

Under the paper's matched setup, J-CoT-Zero slightly exceeds the strongest evaluated latent-reasoning baseline on the aggregate score, and J-CoT-Train raises the eight-benchmark average from 47.5 for SIM-Coconut to 50.2. The evaluated tasks include mathematical, scientific, coding, and structured path reasoning.

**Evidence state:** `REPORTED BY A SEPARATE WORK-IN-PROGRESS PAPER; INDEPENDENT REPLICATION ABSENT`.

### 1.6 Workspace-like recurrence appears usable below frontier scale, but scale still matters

J-CoT's scaling study includes Qwen2.5-7B, 14B, and 32B plus Llama-3.1-70B and 405B with multiple recurrent-depth budgets. The reported results show gains from additional recurrent reasoning at 7B as well as at larger sizes. They also show that performance increases with backbone capacity and that the largest model receives larger gains from deeper recurrence in the reported tests.

Therefore the evidence supports:

> a workspace-like recurrent interface can be useful at approximately 7B–8B scale in the evaluated setup.

It does **not** support:

> an 8B core is generally sufficient, or model scale no longer matters once a workspace exists.

**Evidence state:** `PARTIALLY SUPPORTED / SCALE-DEPENDENT`.

## 2. What the sources do not establish

The following claims remain **NOT ESTABLISHED**:

- J-Space is the complete reasoning engine rather than a privileged intermediate-state／broadcast layer;
- every language model contains the same workspace geometry or uses it for the same tasks;
- the Qwen3-8B J-CoT interface is functionally identical to Anthropic's causally characterized Claude workspace;
- an untouched 7B／8B model has sufficient semantic grounding, automatic capabilities, planning, integration, or reliability for Dexinode;
- the small number of active J-Space concepts implies that only a small fraction of model parameters is needed for reasoning;
- long-tail facts, foundational semantic concepts, language ability, world priors, and procedural competence can all be removed from the cognitive core;
- an independently trained Adapter, external Specialist, or Remote node can directly write valid J-Space state;
- J-Space coefficients are portable across model families, checkpoints, tokenizers, layers, quantizations, or revisions;
- J-Space is a safe or stable network protocol;
- a flat vocabulary-indexed readout captures all required relations, variable bindings, causal structure, or procedural state;
- J-CoT has production-ready latency, memory, security, interpretability, or tool-use economics;
- the J-CoT results have been independently replicated;
- knowledge–reasoning decoupling is complete or already product-ready.

J-CoT itself states that full hidden-space computation remains inside each recurrent cycle and only the cycle boundary is represented in J-Space. This is an important correction to any claim that J-Space alone performs reasoning.

## 3. Dexinode-specific inference

The following statements are project inferences rather than claims proven by the cited authors.

### I1 — A cognitive core should be distinguished from a monolithic knowledge container

The combined evidence makes it more plausible that a useful local core could be defined by responsibilities rather than by containing all available facts:

- semantic and language grounding;
- automatic foundational capabilities;
- deliberate workspace and recurrent computation;
- planning, integration, clarification, abstention, and escalation;
- use of external knowledge, memory, tools, and specialist operators.

This reframes the size question from “how small can a standalone Specialist be?” toward:

> What is the minimum complete cognitive core that can reliably integrate external knowledge and heterogeneous operators under a verifiable workflow?

**Dexinode state:** `NEW HIGH-PLAUSIBILITY RESEARCH HYPOTHESIS / UNVALIDATED`.

### I2 — Knowledge–reasoning decoupling is likely partial, not absolute

DMoE supplies evidence that long-tail or time-sensitive knowledge can be represented in independently updatable parameter modules. J-Space/J-CoT supplies evidence that deliberate intermediate state can be separated functionally from much automatic processing and reused recurrently.

Together they support the plausibility of separating:

- externalizable factual, private, current, and episodic knowledge; from
- a model-native cognitive substrate that still contains broad semantics, language, automatic routines, world priors, and reasoning machinery.

A zero-knowledge reasoner plus an arbitrary database is not supported. The likely boundary is partial and empirical.

**Dexinode state:** `OPEN / HIGH STRATEGIC IMPORTANCE`.

### I3 — Skill is a functional contract, not a single cognitive location

Human-visible capabilities may arise from different substrates:

- language fluency may be an automatic foundation capability;
- current facts may come from retrieval or parametric knowledge modules;
- formal algebra may come from a solver;
- repository repair may combine knowledge, tools, planning, recurrent reasoning, and verification;
- a Specialist model may contribute an operator or candidate artifact rather than replace the General core.

Therefore a Dexinode Skill should remain an externally observable capability contract, while its internal realization is configuration metadata.

**Dexinode state:** `STRENGTHENS EXISTING SUBSTRATE-NEUTRAL DEFINITION`.

### I4 — J-Space-like mechanisms should remain internal implementation candidates

A future Local Decision Configuration may use J-Space, another latent workspace, explicit scratchpads, recurrent state, or ordinary token reasoning. Dexinode should record the complete configuration and observable outcomes without requiring private chain-of-thought or exporting raw latent vectors.

Across trust domains, components should exchange typed claims, constraints, evidence, artifacts, and uncertainty—not model-specific hidden-state coordinates.

**Dexinode state:** `ARCHITECTURAL GUARDRAIL`.

### I5 — The long-term network may decentralize the capability supply chain rather than every reasoning step

If a local cognitive core integrates external inputs, independent parties may contribute:

- knowledge sources or parameterized knowledge artifacts;
- tools, solvers, learned operators, and specialist services;
- memory and indexing systems;
- verifiers and attestations;
- optional compute capacity.

The reasoning core itself need not be transferred between remote nodes for every step. This preserves a decentralization path while weakening distributed whole-model inference as a necessary foundation.

**Dexinode state:** `OPEN LONG-TERM ARCHITECTURAL INFERENCE`.

## 4. Impact matrix

| Claim or premise | J-Space／J-CoT impact | Current interpretation |
|---|---|---|
| Deliberate reasoning uses a privileged shared workspace in LLMs | strong causal evidence in Claude | `ESTABLISHED IN PAPER SCOPE` |
| Automatic language／routine capability is distinct from workspace reasoning | strong functional evidence | `PARTIALLY ESTABLISHED; TASK BOUNDARY OPEN` |
| Workspace-like recurrence can help a 7B–8B model | reported evidence | `PARTIALLY SUPPORTED / NOT INDEPENDENTLY REPLICATED` |
| J-Space is the complete reasoning engine | contradicted by the mechanism description | `REJECT` |
| An 8B cognitive core is sufficient for Dexinode | not shown | `OPEN` |
| Knowledge and reasoning can be fully separated | not shown | `OPEN` |
| Long-tail knowledge may be externalized while a core integrates it | conceptually strengthened with DMoE | `HIGH-PLAUSIBILITY HYPOTHESIS` |
| Skill must live in J-Space | not supported | `REJECT AS FOUNDATION` |
| J-Space can be a cross-model or network ABI | not supported | `REJECT AS CURRENT ENGINEERING ROUTE` |
| Recurrent／latent reasoning should remain replaceable configuration | strengthened | `PARTIALLY SUPPORTED` |
| Skill should be substrate-neutral | strengthened | `PARTIALLY SUPPORTED` |

## 5. Consequences for current project state

This evidence strengthens the abstraction adopted by ADR 0003:

- do not anchor the project to one model size;
- do not equate visible token loops with all reasoning;
- identify the complete Local Decision Configuration;
- keep authority, state, verification, rollback, and audit in the deterministic control plane;
- allow models, memory systems, operators, reasoning interfaces, and hardware to change.

It does not require a revision of specification v0.2. The current repository-repair boundary can later compare configurations with different cognitive cores or reasoning modes under the same authority and evidence contract.

## 6. Preserved durable state

This record does **not**:

- reopen or modify Gate A `PASS / CLOSED`;
- reopen or modify Gate B `FAIL / CLOSED`;
- change any frozen Gate score or retrospective;
- resolve FIM／syntax-aware MVSS `HOLD`;
- supersede or edit ADR 0003;
- revise specification v0.2;
- select or download a model;
- authorize J-lens construction, recurrent inference, training, GPU work, benchmark creation, implementation, or a new Gate;
- authorize a J-Space ABI, DMoE runtime, federation, marketplace, settlement, reputation, or governance implementation.

## 7. Stop point

Record J-Space as evidence for a model-native deliberative workspace and J-CoT as early evidence that a workspace-like recurrent interface can be useful at resource-bounded model scale. Treat both as architecture-level evidence, not as selected Dexinode components.

Stop before direct implementation or before inferring that knowledge, automatic skills, and reasoning have already been cleanly separated.