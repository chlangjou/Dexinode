# Agent context lifecycle and memory assembly — architecture-diversity watch

- Date: 2026-11-14
- Status: **passive research watch / knowledge supplement only**
- Evidence maturity: **task- and executor-specific Agent results; architectural generalization remains unproven**
- Dexinode disposition: **retain the signal, without new Gate, experiment, protocol requirement, or implementation priority**

## Source-supported signals

Three recent studies suggest that an Agent's effective working context is an **active execution variable**, not merely a passive archive:

1. **Periodic forgetting** — *Scaling Discovery Requires Forgetting* (arXiv:2610.20563) reports that restarting discovery Agents from the best candidate while discarding accumulated search history can escape stagnation on four studied tasks. Gains are relative to particular baselines, not universal.
2. **Fork-and-Flush** — *Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents* (arXiv:2610.07447) keeps the workspace but refreshes conversation context across parallel candidate trajectories. It improves average performance across studied long-horizon tasks, but not every task; long dependent reasoning may suffer from interruption.
3. **Memory assembly** — *MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning* (arXiv:2610.21091) reports that choosing and ordering retrieved experiences based on downstream results can outperform semantic-similarity-first memory use while reducing memory-token consumption.

Together these results support **context selection, retention, ordering, and restart as potentially useful controls for contemporary LLM-based Agents**. They do not establish a universal context-management law, nor a required Dexinode subsystem.

## Hypotheses worth retaining, not settled conclusions

- **Exploration versus continuity:** broad search may benefit from independent branches and fresh contexts; deep, dependency-heavy work may benefit more from preserving validated intermediate state. A task may switch between these regimes as it progresses.
- **Adaptive versus fixed intervention:** a progress-/novelty-aware closed-loop controller is plausible, but remains an engineering hypothesis. Diff size, token count, or small score improvements are not reliable stand-alone indicators of useful progress. Fixed-budget resets can remain a useful baseline or safety fallback.
- **Memory versus evidence:** retain verified artifacts, invariants, tool outputs, failure boundaries, and provenance outside transient chat history when appropriate. Do not automatically promote a model-generated summary or hypothesis into verified knowledge.
- **Experience distillation:** repeatable failures might become deterministic preflight checks or Skill guidance; contextual heuristics may still require retrieval. Prompt placement alone is not a security or correctness boundary.

## Important architecture and scaling uncertainty

These observations are **conditional on present model families, training, tasks, and Agent runtimes**. They may weaken, change form, or become more important with:

- stronger or longer-context frontier models, improved training, and model-native memory;
- recurrent/state-space approaches such as **Mamba**, or alternative internal working-state mechanisms;
- **JEPA-like** predictive/world-model representations or other architectures that change how agents reason and maintain state;
- **NCM-like** coarse-to-fine hierarchical representations and refinement, including architectures with different exploration and validation dynamics.

These are **distinct research directions**, not proven substitutes for Agent context management. There is currently insufficient evidence to conclude that they will eliminate the above problems, or that current prompting/GC approaches will remain valuable unchanged. Therefore **neither “fundamental breakthrough for Dexinode” nor “irrelevant once models improve” is justified**.

## Dexinode interpretation and disposition

The durable architectural choice remains to keep the **Consumer/Provider capability contract and verifiable Artifact/Execution Receipt boundary independent of Provider-internal cognition**. A Provider may implement context checkpointing, flushing, multi-branch exploration, learned memory selection, recurrent/latent reasoning, or entirely different mechanisms without imposing them on the external protocol.

**Watch, do not activate.** No change to ADR 0003/0004, reference v0.3, isolation invariants, Gate A (PASS/CLOSED), Gate B (FAIL/CLOSED), or FIM HOLD; no new experiments, benchmarks, implementation work, or scheduling policy are authorized. Revisit only if new evidence materially changes the external contract, verification assumptions, isolation boundary, or execution economics.

## Primary references

- Tan et al., *Scaling Discovery Requires Forgetting* (2026): https://arxiv.org/abs/2610.20563
- Cai et al., *Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents* (2026): https://arxiv.org/abs/2610.07447
- Xie et al., *MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning* (2026): https://arxiv.org/abs/2610.21091
- Related Dexinode NCM watch: [Next-Concept Modeling / hierarchical exploration](2026-11-14-next-concept-modeling-hierarchical-exploration-watch.md)
