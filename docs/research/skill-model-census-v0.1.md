# Dexinode Skill Model Census v0.1

**Snapshot date:** 2026-08-09  
**Status:** Initial family screening; model binaries have not yet been downloaded or executed.  
**Purpose:** Select the first model family and task domain for testing whether orchestration of small, specialized models can outperform or economically match a much larger generalized model.

## 1. Decision summary

Qwen2.5 is the strongest first-round family.

It is currently the only screened family that combines all of the following:

- a clean dense-Transformer size ladder from 0.5B through 32B and 72B;
- an approximately 21× comparison between 1.5B and 32B;
- official generalized, coding, and mathematics variants;
- existing third-party 0.5B–1.5B task specialists for Text-to-SQL, SQL revision, and function calling;
- an Apache-2.0 generalized 32B baseline that is feasible on the available 2× NVIDIA L40 system;
- tasks with executable, objective verification.

The best initial task candidate is **adaptive Text-to-SQL**, not repository-level bug repair. Existing SLM-SQL checkpoints already provide a specialized SQL generator and a separate merge/revision model. SQL execution supplies the deterministic verifier that Dexinode needs.

This is not yet a final task-domain ADR. Before selection is locked, the checkpoints, licenses, prompt formats, and inference path must pass a local smoke test.

## 2. Research question

The first experiment should answer:

> Under matched tool access and measured compute budgets, can a dynamically orchestrated team of 0.5B–1.5B Qwen2.5-based SQL specialists reach or exceed Qwen2.5-32B-Instruct on held-out Text-to-SQL tasks, with materially lower latency or GPU cost?

This separates three effects:

1. **Domain pretraining:** Qwen2.5-Coder-1.5B versus Qwen2.5-1.5B.
2. **Task specialization:** SLM-SQL-1.5B versus Qwen2.5-Coder-1.5B.
3. **Orchestration:** adaptive generator + executor + revision versus a single specialist call.

## 3. Fixed constraints

- Only Transformer-family models are in scope for the first census. JEPA and SSM/linear-attention hybrids are deferred.
- Same family and generation are preferred so that specialization is not confused with architectural or tokenizer differences.
- The initial small model target is approximately 0.5B–3B; the large control should ideally be 14B–32B.
- Checkpoints must be downloadable and locally runnable. Model-card claims alone are insufficient.
- The first task must have an objective verifier.
- Public benchmark scores are screening evidence, not the final result. Repository-, schema-, or dataset-level held-out and private tests are required.
- The first orchestrator should be a fixed, replayable state machine. A learned router is added only after the model and harness effects are measured separately.
- Available accelerator capacity is 2× NVIDIA L40 with approximately 46 GB VRAM each.

## 4. Family-level screening

| Family | Relevant size ladder | Existing specialist supply | Large generalized control | First-round status | Main reason |
|---|---:|---|---|---|---|
| **Qwen2.5** | 0.5B, 1.5B, 3B, 7B, 14B, 32B, 72B | Official Coder/Math; Hammer; xLAM-2; SLM-SQL | Qwen2.5-32B-Instruct | **Pass / priority** | Best causal controls and several executable skills |
| **Qwen3 dense** | 0.6B, 1.7B, 4B, 8B, 14B, 32B | SLM-SQL-0.6B and many newer derivatives, but fewer paired task specialists | Qwen3-32B | Reserve | Excellent ladder, less mature controlled specialist supply |
| **Gemma 2** | 2B, 9B, 27B | ShieldGemma at 2B/9B/27B | Gemma-2-27B | Reserve | Clean safety-classification specialist, but weak fit for an executable multi-skill task |
| **Gemma 3** | 1B, 4B, 12B, 27B | Domain derivatives exist, but the small/large task-specialist pairing still needs audit | Gemma-3-27B | Census pending | Good ladder; verification and licensing friction depend on the selected derivative |
| **DeepSeek-Coder v1** | 1.3B, 5.7B, 6.7B, 33B | SLM-SQL-1.3B and code derivatives | No equivalent generalized 33B control in the same code family | Reserve | Strong scale gap, weaker causal separation |
| **Llama 3.2 text** | 1B, 3B | Many community derivatives | No same-generation 14B–32B text control | Reject for Experiment 1 | Missing large same-generation control |
| **Granite 3.3** | 2B, 8B | Enterprise and guardian variants | Granite-3.3-8B | Reject for Experiment 1 | Only 4× size gap |
| **Phi-3** | 3.8B, 7B, 14B | Many derivatives, but no clear first-round task-specialist pair | Phi-3-medium-14B | Reject for Experiment 1 | Small scale gap and weaker specialist chain |
| **Qwen3.5** | 0.8B, 2B, 4B, 9B, 27B plus MoE sizes | Ecosystem is rapidly forming | Qwen3.5-27B | **Out of current scope** | Uses a hybrid Gated DeltaNet/attention architecture, conflicting with the Transformer-only constraint |

## 5. Qwen2.5 candidate inventory

| Role | Candidate | Parameters | Specialization level | License status | Evidence / caveat |
|---|---|---:|---|---|---|
| Small generalized baseline | Qwen2.5-1.5B-Instruct | 1.54B | General instruction | Apache-2.0 | Required to measure domain and task gains |
| Small coding baseline | Qwen2.5-Coder-1.5B-Instruct | 1.5B class | Broad code domain | Apache-2.0 | Not by itself a narrow Skill Model |
| SQL generation specialist | cycloneboy/SLM-SQL-1.5B | 1.5B class | Text-to-SQL generation; SFT + GRPO | Apache-2.0 on the checkpoint page | Checkpoint published, but its README is empty; research reproducibility is incomplete because the repository still lists inference-code release as TODO |
| SQL merge/revision specialist | CscSQL-Merge-Qwen2.5-Coder-0.5B-Instruct | 0.5B class | Candidate comparison and SQL revision | CC-BY-NC-4.0 | Separate role and input contract make it a strong Dexinode Skill candidate |
| Alternate SQL revision specialist | CscSQL-Merge-Qwen2.5-Coder-1.5B-Instruct | 1.5B class | Candidate comparison and SQL revision | CC-BY-NC-4.0 | Useful for measuring whether revision needs the larger small model |
| Function-calling specialist | MadeAgents/Hammer2.1-1.5b | 1.5B class | Tool choice and argument generation | Checkpoint is CC-BY-NC-4.0; code repository is Apache-2.0 | Based on Qwen2.5-Coder; BFCL evaluation and training/evaluation code are available |
| Function-calling alternative | Salesforce/xLAM-2-1b-fc-r | 1B label / approximately 1.5B class | Multi-turn function calling | CC-BY-NC-4.0, research release | Same Qwen2.5 generation; 1B/3B/32B specialist ladder exists |
| Mathematics domain specialist | Qwen2.5-Math-1.5B-Instruct | 1.5B class | Mathematics CoT/TIR | Apache-2.0 | Useful for a later heterogeneous math + code experiment |
| Large generalized control | Qwen2.5-32B-Instruct | 32.5B | General instruction | Apache-2.0 | Primary approximately 21× control |
| Large coding control | Qwen2.5-Coder-32B-Instruct | 32.5B | Broad code domain | Apache-2.0 | Upper control that prevents a misleading win against only a generalized model |

### Classification note

Qwen2.5-Coder and Qwen2.5-Math are **domain specialists**, not necessarily narrow, independently contractable Skill Models. SLM-SQL, its merge/revision checkpoint, Hammer, and xLAM-2 are closer to the intended Skill Model definition because their input/output roles and evaluation targets are narrower.

## 6. Recommended Experiment 1 candidate

### Adaptive Text-to-SQL skill chain

Proposed runtime path:

1. Receive natural-language request, database schema, and allowed SQL policy.
2. Invoke the 1.5B SQL generation specialist for a small initial candidate set.
3. Parse and execute candidates in an isolated read-only database.
4. If candidates agree and pass policy checks, stop early.
5. If results disagree, invoke the 0.5B merge/revision specialist with execution evidence.
6. Retry within a predeclared budget.
7. If confidence remains low, abstain or fall back to the 32B model.
8. Record every call, candidate, execution result, decision, and final receipt for replay.

The Dexinode contribution is not merely connecting two checkpoints. It is the **budget-aware policy** that decides when a cheap specialist is sufficient, when revision is justified, and when the expensive generalized model is required.

### Required comparison arms

| Arm | System | Question answered |
|---|---|---|
| C0 | Qwen2.5-1.5B-Instruct + executor | Raw small generalized baseline |
| C1 | Qwen2.5-Coder-1.5B-Instruct + executor | Benefit of code-domain pretraining |
| S0 | SLM-SQL-1.5B, single candidate + executor | Benefit of task specialization |
| S1 | SLM-SQL generator + adaptive execution/vote + merge specialist | Benefit of specialist orchestration |
| L0 | Qwen2.5-32B-Instruct + the same database tools and retry budget | Primary large generalized control |
| L1 | Qwen2.5-Coder-32B-Instruct + the same tools and budget | Large domain-specialist upper control |

Run two budget regimes:

- **Matched budget:** equal wall-time, GPU-seconds, or token budget, reported separately rather than collapsed into one proxy.
- **Quality frontier:** allow each system to use its preferred strategy and plot verified accuracy against actual compute.

### Measurements

- execution accuracy and result-set equivalence;
- syntax-valid and policy-valid SQL rate;
- schema-linking error rate;
- abstention precision and fallback frequency;
- number of model calls and generated candidates;
- input/output tokens by node;
- GPU-seconds and energy proxy by node;
- peak VRAM and wall-clock latency;
- accuracy per GPU-second and per generated token;
- performance on public, schema-held-out, and private databases.

### Preliminary success criteria

These should be finalized after a 20–50 case pilot supplies variance and latency estimates.

- S1 must materially outperform S0 under the same small-model compute budget.
- S1 should reach within 2 percentage points of L0 while using at least 5× less measured GPU time, or exceed L0 at lower total compute.
- The stretch result is S1 exceeding both L0 and L1 on held-out execution accuracy.
- Gains must persist on database schemas absent from training and prompt-tuning data.
- The system must abstain or fall back rather than silently emit policy-invalid SQL.

## 7. Why the published SLM-SQL result is promising but not sufficient

The SLM-SQL paper reports 67.08% execution accuracy on BIRD development for its Qwen2.5-Coder-1.5B-based system, versus 28.40% for the unadapted 1.5B Coder entry in its comparison table. It also reports strong Spider transfer results and publishes generation and merge/revision checkpoints.

However, its default inference procedure uses up to 64 SQL-generation samples and 8 merge/revision samples. A 1.5B model called dozens of times is not automatically cheaper than a 32B model called once. Parallelism can improve latency while still consuming substantial total compute.

Therefore Dexinode should not reproduce the headline score alone. It should measure an **adaptive accuracy–compute frontier**:

- start with 1–4 candidates;
- stop as soon as execution evidence is sufficiently consistent;
- invoke revision only on disagreement;
- escalate to 32B only for hard or out-of-scope cases.

This is the cleanest place to test whether routing and skill handoff add value beyond task fine-tuning.

## 8. Current risks and open checks

1. **License:** The SLM-SQL generator checkpoint is marked Apache-2.0, but the merge/revision checkpoint, Hammer checkpoint, and xLAM-2 are marked CC-BY-NC-4.0. Any chain using those non-commercial components is research-only unless they are replaced or relicensed.
2. **Reproducibility:** SLM-SQL publishes checkpoints and datasets, but its repository still marks inference-code release as unfinished. Prompt and decoding behavior may have to be reconstructed.
3. **Benchmark overlap:** SynSQL-derived training data includes material related to BIRD and Spider. Public scores cannot be treated as contamination-resistant evidence.
4. **Verifier weakness:** Execution accuracy can accept coincidentally equivalent results. Hidden database instances, result-set comparison, SQL policy checks, and mutation tests are needed.
5. **Test-time scaling cost:** High sample counts can erase the nominal parameter advantage.
6. **Harness sensitivity:** Chat templates, tool parsers, candidate grouping, and retry rules can dominate the outcome. Every arm needs a frozen, replayable configuration.
7. **Family purity:** SLM-SQL begins from Qwen2.5-Coder rather than Qwen2.5 general. Both C0 and C1 controls are therefore mandatory.

## 9. Next verification gates

### Gate A — Artifact audit

- Resolve exact checkpoint revisions and file hashes.
- Confirm model-tree lineage, tokenizer identity, context length, chat template, and license for every checkpoint.
- Verify that each checkpoint loads without undocumented custom code.

### Gate B — Minimal local smoke test

- Run 20–50 simple, unseen schemas.
- Confirm the exact SQL extraction format.
- Measure one-call latency and VRAM for 0.5B, 1.5B, and quantized/BF16 32B controls.
- Determine whether the revision model accepts the evidence format described in the paper.

### Gate C — Frozen experiment contract

- Define the Skill Manifest for SQL generation and SQL revision.
- Freeze prompts, decoding parameters, timeouts, retry limits, and receipts.
- Pre-register budget regimes and failure categories.

### Gate D — Private evaluation set

- Generate or curate schemas that are absent from BIRD, Spider, and SynSQL.
- Create multiple database instances per semantic query to reduce coincidental correctness.
- Keep the final test split sealed until the policy is frozen.

Only after Gates A and B pass should Dexinode adopt Text-to-SQL as `ADR-0002: Initial Task Domain`.

## 10. Primary sources

- [Qwen2.5 model collection](https://huggingface.co/collections/Qwen/qwen25)
- [Qwen2.5-32B-Instruct model card](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)
- [Qwen2.5-Coder collection](https://huggingface.co/collections/Qwen/qwen25-coder)
- [Qwen2.5-Coder-32B-Instruct model card](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)
- [Qwen2.5-Math-1.5B-Instruct model card](https://huggingface.co/Qwen/Qwen2.5-Math-1.5B-Instruct)
- [SLM-SQL paper](https://arxiv.org/abs/2507.22478)
- [SLM-SQL repository and checkpoint list](https://github.com/CycloneBoy/slm_sql)
- [Hammer repository](https://github.com/MadeAgents/Hammer)
- [Hammer2.1-1.5b model card](https://huggingface.co/MadeAgents/Hammer2.1-1.5b)
- [xLAM-2-1b-fc-r model card](https://huggingface.co/Salesforce/xLAM-2-1b-fc-r)
- [xLAM-2-32b-fc-r model card](https://huggingface.co/Salesforce/xLAM-2-32b-fc-r)
- [Qwen3 official release](https://qwenlm.github.io/blog/qwen3/)
- [Gemma 3 model card](https://ai.google.dev/gemma/docs/core/model_card_3)
- [ShieldGemma-2B model card](https://huggingface.co/google/shieldgemma-2b)
- [Llama 3.2 model card](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_2/)
- [Granite 3.3 2B model card](https://huggingface.co/ibm-granite/granite-3.3-2b-instruct)
- [Phi-3 mini model card](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
- [DeepSeek-Coder repository](https://github.com/deepseek-ai/DeepSeek-Coder)
- [Qwen3.5-2B architecture and model card](https://huggingface.co/Qwen/Qwen3.5-2B)
