# DMoE Parametric Knowledge Injection — Material Evidence Review

- Date: 2026-08-16
- Scope: pre-Gate external research evidence
- Primary source: [Yue et al., *Decoupled Mixture-of-Experts for Parametric Knowledge Injection*, arXiv:2606.14243v1](https://arxiv.org/abs/2606.14243)
- Related decision: [ADR 0003](../decisions/0003-resource-bounded-verifiable-execution-fabric.md)
- Related specification: [Repository-Repair Verifiable Execution Fabric Specification v0.2](../specifications/bounded-repository-repair-verifiable-execution-v0.2.md)
- Evidence cutoff: 2026-08-16
- Disposition: **NEW MATERIAL EVIDENCE / NO DURABLE STATE CHANGE**

This record captures a materially relevant external research result without reopening or modifying any closed Gate, accepted decision, HOLD state, or current specification. It separates paper-supported observations from Dexinode-specific inference and from questions that remain open.

## Executive conclusion

DMoE materially weakens any assumption that a Dexinode Skill must be a standalone specialist model. The paper demonstrates that learned capability can be modular below whole-model granularity: a frozen base model can receive independently trained, independently updatable, selectively routed parameter modules representing fine-grained knowledge units.

However, the demonstrated capability is **parametric knowledge injection**, not procedural skill injection. The paper does not establish that tiny adapters can transfer repository repair, coding methodology, mathematical self-verification, tool use, or long-horizon agent behavior. It also does not establish an untrusted multi-provider skill ecosystem.

The appropriate Dexinode interpretation is therefore architectural rather than product-level:

> A Skill may eventually be a versioned capability artifact rather than a standalone model, but the viable artifact types, compatibility contract, verification requirements, and procedural-transfer limits remain open.

This evidence is compatible with ADR 0003 and specification v0.2. It does not currently justify superseding either one.

## 1. Paper-supported observations

### 1.1 Decoupled parametric experts exist in the evaluated setting

DMoE keeps the dense base model frozen while decoupling both the router and the expert modules from that base. External knowledge is partitioned into knowledge units, and each unit can be represented by a lightweight parameter-efficient expert trained independently. Experts can be added, removed, or updated without retraining the dense backbone.

**Evidence state:** `SUPPORTED BY PAPER`.

### 1.2 Expert activation is conditional and fine-grained

The evaluated architecture uses token uncertainty to decide whether external expert support is needed and a lightweight retriever to choose relevant experts. The main experiments use BM25 routing and a top-k expert budget. The paper's ablations show that both *when* to activate experts and *which* experts to select affect performance; always activating experts is not beneficial.

**Evidence state:** `SUPPORTED BY PAPER`.

### 1.3 The expert substrate can be extremely small relative to the base model

For the Llama-3.2-1B experiment, the authors instantiate one expert per passage-level knowledge unit, producing 27,613 experts. With the default LoRA configuration, one expert contains 122,880 trainable parameters and occupies approximately 481 KiB on disk. The complete bank is about 13.08 GiB and remains primarily on disk; only selected experts are loaded for triggered decoding steps.

The paper also states that passage-level granularity is not mandatory: units may be grouped into coarser document／cluster experts or made finer when routing precision is more important.

**Evidence state:** `SUPPORTED BY PAPER IN ITS KNOWLEDGE-INJECTION SETTING`.

### 1.4 Final-layer attachment preserves KV-cache reuse

DMoE attaches experts only to the final-layer feed-forward network. This design allows previously computed attention KV-cache state to remain valid when the active expert set changes during autoregressive decoding.

**Evidence state:** `SUPPORTED BY PAPER`.

### 1.5 DMoE is not a universal efficiency winner

The paper's aggregate efficiency table reports approximately:

| Method | Average time / sample | Average GPU memory |
|---|---:|---:|
| Basic-RAG | 1.89 s | 2.54 GB |
| FLARE | 9.26 s | 13.97 GB |
| PRAG | 1.36 s | 4.83 GB |
| SFT-LoRA | 1.67 s | 4.82 GB |
| DMoE | 2.67 s | 7.24 GB |

Thus DMoE is substantially more efficient than the evaluated dynamic FLARE baseline, largely because it preserves KV-cache reuse, but static Basic-RAG, PRAG, and SFT-LoRA can have lower per-sample latency and／or memory in this setup. The paper itself characterizes DMoE as broadly competitive rather than dominant on every dataset, base model, or metric.

**Evidence state:** `SUPPORTED BY PAPER`; this is a required counterweight to interpreting DMoE as a free efficiency gain.

## 2. What the paper does not establish

The following claims remain **NOT ESTABLISHED** by arXiv:2606.14243:

- a ~481 KiB expert is a standalone model or independent reasoning engine;
- tiny parameter modules can inject procedural rather than factual／semantic capability;
- adapters can reliably inject coding, debugging, repository repair, mathematical reasoning, self-verification, tool use, or long-horizon agent behavior;
- independently authored experts compose safely or additively;
- expert combinations avoid interference, correlated failure, or emergent behavior outside the evaluated setting;
- third-party or malicious experts can be accepted safely;
- expert provenance, signatures, licensing, reputation, attestation, or sandbox policy are sufficient for open participation;
- an expert trained for one exact base-model revision remains compatible with another revision, tokenizer, architecture, quantization, runtime, or injection point;
- DMoE is superior to RAG or whole-model specialization on total workflow cost in general;
- consumer-device or idle-compute deployment economics are production-ready;
- distributed inference, federation, marketplace, settlement, or network governance are validated.

The paper should therefore be treated as strong evidence for **modular parametric knowledge capability**, not as direct evidence for a decentralized procedural-skill network.

## 3. Dexinode-specific inference

The following items are project inferences. They are not claims made or proven by the DMoE authors.

### I1 — `Skill != standalone model` becomes a materially stronger possibility

Early Dexinode reasoning often used a standalone specialist model as the concrete Skill substrate. DMoE supplies a credible counterexample at the knowledge-capability level: useful learned specialization can exist as a small parameter artifact attached to a shared base model.

Provisional project statement:

> **A Dexinode Skill MAY be a versioned, testable capability artifact rather than a standalone model.**

Possible substrates may eventually include whole models, PEFT／LoRA modules, knowledge packs, tools, deterministic algorithms, verifiers, agents, or remote services. This record does not select or standardize any substrate.

**Dexinode state:** `PARTIALLY SUPPORTED / NEW MATERIAL EVIDENCE`.

### I2 — Capability granularity may need to be much finer than broad domain labels

Gate B remains the pinned result that perfect broad-domain routing did not create material held-out advantage for the evaluated General／Math／Coder configuration. DMoE independently demonstrates a design where routing granularity is tied to individual knowledge units rather than broad domains.

The combined interpretation is limited but important:

> DMoE is consistent with, but does not prove, the Dexinode inference that capability identity may need to be substantially finer-grained than labels such as `Math` or `Coding`.

This does not reopen Gate B or retroactively change its acceptance criteria.

**Dexinode state:** `PARTIALLY SUPPORTED`.

### I3 — Decentralization should distinguish compute from capability ownership

DMoE exposes a possible architecture in which a common local base performs inference while independently produced capability artifacts are distributed separately. If procedural capability modules eventually prove viable, Dexinode would not necessarily require every Skill provider to operate a complete inference node.

This separates two hypotheses:

1. **compute decentralization** — inference executes across many independently operated compute nodes;
2. **capability production／ownership decentralization** — independently produced capability artifacts can be distributed and used under a common execution boundary.

DMoE materially strengthens the plausibility of the second mechanism at the knowledge-module level. It does not validate either mechanism for a Dexinode network.

**Dexinode state:** `OPEN / ARCHITECTURAL INFERENCE`.

### I4 — ADR 0003's substrate-neutral control boundary is strengthened, not superseded

ADR 0003 deliberately moved the project foundation away from one fixed model size and made the evaluated unit a complete Local Decision Configuration. Specification v0.2 likewise treats models, deterministic logic, tools, verification, search, stopping, fallback, and runtime as replaceable configuration under a stable local authority boundary.

DMoE adds another plausible learned-component form below whole-model granularity. That is compatible with the existing abstraction:

> learned capability may be replaceable not only at the whole-model level but also at the parameter-module level.

No ADR or specification change is required by this evidence alone.

**Dexinode state:** `SUPPORTING EVIDENCE FOR CURRENT ABSTRACTION / NOT A NEW DECISION`.

### I5 — A future Skill ABI／compatibility contract may become a first-class problem

A parameter artifact is only meaningful relative to material compatibility constraints such as base model and revision, architecture, target layer, tokenizer, PEFT method, rank, runtime, quantization, merge／activation policy, and possibly combinations with other experts.

If parameter-level skills become relevant to Dexinode, capability identity will need to bind these compatibility properties rather than treat a skill name as portable behavior.

**Dexinode state:** `NEW OPEN QUESTION`.

## 4. Impact matrix

| Dexinode claim or premise | DMoE impact | Current interpretation |
|---|---|---|
| A Skill must be a standalone specialist model | materially weakened | `REJECT AS FOUNDATION`; not required by v0.2 |
| Whole-model specialization can exist | unchanged | `ESTABLISHED` only in Gate A's pinned scope |
| Broad domain labels are sufficient routing contracts | no rescue; further conceptual doubt | Gate B remains `FAIL / CLOSED` in pinned scope |
| Tiny parameter modules can encode modular knowledge | strong new evidence | `ESTABLISHED IN PAPER SCOPE` |
| Tiny modules can encode transferable procedural skills | not tested | `OPEN` |
| Capability identity should be substrate-neutral | strengthened | `PARTIALLY SUPPORTED` |
| Distributed compute is required for decentralization | weakened as a necessary premise | `OPEN / NOT REQUIRED AS FOUNDATION` |
| Capability production／ownership can be decentralized | conceptually strengthened | `OPEN` |
| Trusted Local Control Plane remains useful across substrates | structurally compatible | `PARTIALLY SUPPORTED / UNVALIDATED END TO END` |
| Parameter-level skills require an ABI／compatibility identity | newly salient | `OPEN` |
| Untrusted parameter artifacts can be safely accepted | not addressed | `OPEN / HIGH TRUST RISK` |

## 5. Consequences for current architecture work

This evidence does **not** require a rewrite of the current candidate architecture. It instead reinforces the reason ADR 0003 removed a fixed Resident-model premise.

If Dexinode later generalizes its long-term Skill Declaration, a model-neutral definition such as the following may be more durable:

> **Skill: a versioned capability artifact with explicit compatibility, invocation, provenance, policy, and verification contracts.**

This is a candidate definition only. It is not adopted by this record and should not be propagated into canonical architecture or protocol documents without a separate human decision.

## 6. Preserved durable state

This evidence record does **not**:

- reopen, modify, or reinterpret away Gate A `PASS / CLOSED`;
- reopen, modify, or relabel Gate B `FAIL / CLOSED`;
- change any frozen Gate score, benchmark, oracle record, execution receipt, or retrospective;
- resolve FIM／syntax-aware MVSS `HOLD` or resume DELULU work;
- supersede or edit ADR 0003;
- edit or revise specification v0.2;
- change `status/current.md`;
- select a base model, PEFT method, adapter framework, router, runtime, or hardware;
- authorize model download, training, inference, GPU work, implementation, benchmark construction, task sampling, statistical methods, thresholds, or a new Gate;
- authorize federation, marketplace, reputation, token, settlement, governance, or distributed-node implementation.

The current authorization boundary remains unchanged.

## 7. Potential future decision questions — not authorized

This paper raises several bounded research questions with potentially high decision value, but this record does not authorize them.

### Candidate A — Parametric Procedural Skill

> Can an independently packaged parameter-efficient module transfer a bounded **procedural** capability to a shared base model on structurally fresh tasks, while preserving general capability and producing a meaningful total-cost advantage over base-only, RAG, whole-model specialization, or Remote fallback?

This is the most direct missing bridge between DMoE's knowledge result and the Dexinode Skill thesis.

### Candidate B — Skill artifact compatibility／ABI

> What minimum compatibility identity is required to make a parameter-level capability artifact reproducible and safely reject incompatible base-model, runtime, quantization, or composition configurations?

### Candidate C — Untrusted Skill verification

> Can an untrusted third-party parameter artifact be evaluated with enough behavioral coverage, provenance, sandboxing, and rollback to make local activation acceptable under a bounded workflow?

Any one of these would require a new human decision before benchmark design, artifact selection, training, inference, or implementation.

## 8. Stop point

Record DMoE as material new evidence supporting capability-substrate modularity below whole-model granularity. Preserve the current architecture boundary and all prior Gate／HOLD decisions unchanged.

Stop before opening a new decision issue, changing canonical architecture documents, selecting a research question, or authorizing execution.