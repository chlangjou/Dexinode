# Dexinode Session Handoff

Repository: `chlangjou/Dexinode`
Canonical branch: `main`
Snapshot: 2026-08-10

Git is the durable source of truth. This file is intentionally compact for a fresh ChatGPT session.

## Start here

Read only what is needed, in this order:

1. `AGENTS.md`
2. `HANDOFF.md`
3. `status/current.md`
4. `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
5. `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`
6. `gates/gate-b-orchestration/evidence-report.md`

Also consult the File Library research report when available:

`Dexinode-specialist-llm-literature-review-2026-08-10.md`

Do not reopen old Gate A/B execution unless a new question specifically requires it.

## Closed experimental gates

### Gate A — Specialist Validation

**PASS / CLOSED.**

Same-size Qwen2.5-7B comparison established that specialization can produce strong capability divergence on a measured distribution. The Math checkpoint showed a large Math advantage on Gate A; the Coder checkpoint did not validate as a Coding specialist.

Key architectural lesson: checkpoint/domain labels are not sufficient skill identities; capability must be empirically registered.

### Gate B — Orchestration Advantage

**FAIL / CLOSED.**

Final decision record:
`gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`

Frozen execution:
`gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`

Frozen result:

- General-only: 76/96 = 79.17%; Math 40/48; Coding 36/48.
- Skill-routed: 77/96 = 80.21%; Math 41/48; Coding 36/48.
- Overall delta: +1.04 pp, 95% CI [0, +3.125] pp.
- Math delta: +2.08 pp, CI [0, +6.25] pp.
- Router domain accuracy: 100%.
- Frozen +10 pp overall and +10 pp Math requirements were not met.

Conclusion: perfect broad-domain routing did not create material system advantage because specialist advantage did not transfer strongly to the fresh panel.

## Important post-closure caveats

See:
`gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

Key findings:

- `math-23` has a frozen oracle error: correct Bayes posterior is `95/242`, not `19/48`; both models computed approximately the correct decimal and both were rejected by the rational-only scorer.
- `math-11`, `math-12`, `math-17` were mathematically correct for both models but rejected by answer-representation parsing.
- `math-41`, the sole frozen specialist win, was mathematically correct for both (`0.75` vs `3/4`); only specialist representation was accepted.
- `math-16` and `math-32` show genuine shared arithmetic/self-check failures.

These errata do not rescue Gate B; content-level retrospective makes the Math specialist advantage smaller, not larger. Preserve frozen scores as historical evidence and keep errata explicit.

## Current research pivot

Do **not** assume Dexinode is practical. Current position:

> Specialized/cheaper models are clearly possible and routing has real production value, but useful specialization may require a much larger model scale and stricter conditions than the original edge-small-model thesis assumed.

Separate three hypotheses:

1. **Specialization thesis** — a cheaper/specialized model can be better on a bounded task region.
2. **Routing thesis** — the system can predict before expensive inference when that model is good enough.
3. **Decentralization thesis** — the minimum viable specialist scale is small enough for distributed/idle/consumer compute.

Evidence for (1) and (2) exists in research and production. (3) remains open and is the most Dexinode-specific risk.

Important distinction:

- **Absolute-small**: roughly consumer/edge-deployable 1B–14B class.
- **Relative-small**: substantially cheaper than frontier, but still datacenter-scale (for example tens of billions active parameters or large MoE specialists).

Production routing can succeed with relative-small models without validating the edge-decentralization thesis.

## Literature review conclusions already absorbed

The literature review supports these concepts:

- catastrophic forgetting is not the whole problem;
- **General Capability Integration (GCI)** is a distinct concern: a specialist may retain general abilities yet fail to combine them reliably with domain expertise;
- mixed general/domain training can outperform pure specialization (Qwen2.5-Coder's reported code/general/math mixture is an important example, not a universal ratio);
- specialists may work as augmentation modules rather than full General-model replacements (e.g. specialist knowledge/derivation feeding a General reasoning core);
- model complementarity does not imply easy model selection; model-recall/oracle-gap is a central routing problem;
- routing should eventually estimate expected utility / probability of success, not merely classify domain;
- small-specialist quality/resource Pareto improvements exist, but often under narrow, identifiable, verifiable distributions.

## Current hypothesis about Qwen2.5 General / Math / Coder

All inherit a strong Qwen2.5 base, but later training objectives differ materially.

- General-Instruct emphasizes broad instruction following, human preference, structured behavior and general reasoning.
- Math adds >1T math-oriented continued pretraining plus math CoT/TIR, reward modeling and GRPO-style specialist alignment.
- Coder adds ~5.5T continued training with an explicit mixed code/general/math recipe, FIM/repository training, then coding-focused instruction/preference stages while deliberately retaining common data.

Plausible but unproven hypothesis:

> Specialist training may improve domain-method competence while changing the relative weighting/integration of general comprehension, grounding, verification and output-control abilities.

Do not treat this as established causality.

## Production examples that motivated the current pivot

Two relevant patterns should be verified from primary/credible sources when reused:

- OpenAI-style model ladders/routing: route easier work to cheaper/faster models and escalate harder tasks. Do not repeat an exact `1/10 compute` claim without primary evidence.
- Cursor-style routing/first-party specialist economics: first-party coding models and production routing can reduce dependence on frontier providers and improve inference economics, but successful specialists may still be datacenter-scale rather than edge-small.

The key research question is therefore no longer "can specialists exist?" but:

> At a required quality threshold, what is the minimum-cost / minimum-scale model that remains reliable, and can we predict when to use it cheaply enough?

## Next work: two parallel literature-first Worker sessions

No new GPU Gate is active. Run two independent research workers first.

### Worker A — Specialist Viability / Minimum Viable Specialist Scale

Research whether and at what scale specialists can retain:

- domain advantage;
- General Capability Integration;
- instruction/specification comprehension;
- reliability and verification;
- transferable advantage across fresh panels;
- meaningful VRAM/latency/energy/cost advantage.

Explicitly distinguish absolute-small from relative-small specialists.

Primary output: evidence on the **minimum viable specialist scale** by task regime and whether edge-scale specialists are realistic.

### Worker B — Routing / Model Recall / Escalation Economics

Research whether model complementarity can be converted into production savings through:

- pre-inference success prediction;
- cost/quality routing;
- model recall / oracle-gap reduction;
- confidence calibration and abstention;
- cheap-first cascades / escalation;
- verifier-assisted routing;
- production systems such as OpenAI/Cursor where publicly documented.

Primary output: evidence on whether routing can predict **P(success | model, task)** cheaply and robustly enough to beat a strong single model.

Both workers must be literature-first and actively seek negative evidence. Do not design a Dexinode benchmark until literature gaps are established.

## Main-session synthesis after Workers A/B

When both worker reports return, do not immediately start another model experiment.

Build an evidence matrix across:

- Specialist Viability
- Routing Predictability
- Deployment Scale

Classify major claims as:

- ESTABLISHED
- PARTIALLY SUPPORTED
- OPEN
- CONTRADICTED

Then decide whether the next falsifiable Gate should test:

1. minimum viable specialist scale / edge viability;
2. General Capability Integration;
3. routing success prediction / escalation;
4. specialist augmentation + verifier;
5. or whether evidence is too weak to justify further Dexinode-specific experimentation.

## Research discipline

Dexinode is currently a **possible architecture under potentially strict conditions**, not an assumed product direction.

Research goal: progressively narrow the region in which it could be practical. If that region becomes too narrow or expensive for decentralized deployment, record that as a valid negative result.

No new selected-model execution is authorized until a new bounded hypothesis, benchmark and acceptance criteria are explicitly frozen.