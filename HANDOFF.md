# Dexinode Session Handoff

Repository: `chlangjou/Dexinode`

Canonical branch: `main`

Integration surface: Draft PR [#28](https://github.com/chlangjou/Dexinode/pull/28)

Snapshot: 2026-08-17

Git is the durable source of truth. This file is intentionally compact for a fresh session.

## Start here

Read in this order:

1. `AGENTS.md`
2. `HANDOFF.md`
3. `status/current.md`
4. `docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md`
5. `docs/specifications/bounded-repository-repair-verifiable-execution-v0.2.md`
6. `docs/research/2026-08-17-cognitive-decomposition-hypothesis-route-review.md`
7. `docs/research/2026-08-17-j-space-j-cot-material-evidence-review.md`
8. `docs/research/2026-08-16-dmoe-parametric-knowledge-injection-evidence-review.md`
9. `docs/research/2026-08-14-verifiable-execution-v0.2-human-review.md`
10. `docs/architecture.md`

Read the earlier decision chain for provenance when needed:

- `docs/research/2026-08-14-strategic-reorientation-review.md`
- `docs/decisions/0002-proceed-to-bounded-repository-repair-spec.md`
- `docs/specifications/bounded-repository-repair-resident-core-v0.1.md`
- `docs/research/2026-08-11-hybrid-agent-human-review.md`

Read Gate closure records only when their evidence is needed:

- `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

Do not reopen Gate A/B execution unless a new human decision explicitly requires a materially different falsifiable question.

## Durable empirical state

### Gate A — Specialist Validation

**PASS / CLOSED.**

Same-family Qwen2.5-7B evidence established strong capability divergence on one pinned distribution. The Math checkpoint showed a large Mathematics advantage; the Coder checkpoint did not validate as a Coding specialist.

Durable lesson: a model label is not a capability identity.

### Gate B — Orchestration Advantage

**FAIL / CLOSED.**

Frozen execution: `gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`.

- General-only: 76/96 = 79.17%.
- Skill-routed: 77/96 = 80.21%.
- Overall delta: +1.04 pp, 95% CI [0, +3.125] pp.
- Router domain accuracy: 100%.

The frozen thresholds were not met. Post-closure content review found no paired Mathematics content advantage. Gate B remains `FAIL / CLOSED` with its oracle／protocol caveat.

Durable lesson: broad-domain classification is not per-task success prediction, and routing one complete task to one whole-model Specialist is not a sufficient integration architecture.

Gate conclusions apply to pinned models, benchmark, runtime, and date.

## Preserved decisions

- FIM / syntax-aware MVSS eligibility remains **`HOLD`**.
- ADR 0002 remains accepted history: write one bounded, falsifiable repository-repair specification before any experiment.
- Specification v0.1 remains unchanged as the single-Resident／4B–8B candidate produced under ADR 0002.
- ADR 0003 remains the current architecture decision.
- Specification v0.2 remains the accepted architecture boundary.
- No experimental Gate is active.

## Current near-term architecture

[ADR 0003](docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md) keeps the project foundation at:

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

The evaluated unit is a complete **Local Decision Configuration**:

`model(s) + memory/context policy + harness/loop + tools + verifier(s) + search/stopping policy + fallback/human policy + runtime/hardware`

The current bounded artifact is:

`docs/specifications/bounded-repository-repair-verifiable-execution-v0.2.md`

It defines one recoverable repository-repair workflow with deterministic local authority, reversible sandboxes, complete attempt and candidate lineage, verifier coverage and exposure, selection and stopping receipts, and explicit Remote／human substitution. The strongest automatic output is a locally verified candidate set for human disposition.

Acceptance does not validate the architecture or authorize execution.

## New material external evidence

### DMoE

The 2026-08-16 review records that DMoE supports independently updatable parametric knowledge modules in its evaluated setting. It does not establish procedural Skill injection, safe composition, open-provider trust, or universal efficiency superiority.

Strategic effect: `Skill = standalone model` is weakened, and capability ownership is separated from distributed inference.

### J-Space and J-CoT

The 2026-08-17 review records:

- causal evidence that evaluated Claude models use a small privileged workspace for deliberate control, intermediate reasoning, and flexible reuse;
- much routine language processing and familiar inference proceeds outside that workspace;
- J-CoT reports a recurrent J-Space interface on a reasoning-adapted Qwen3-8B backbone and scaling from 7B to 405B;
- J-Space is not the complete reasoning engine, a cross-model ABI, or proof that an 8B core is sufficient.

## Current provisional long-horizon hypothesis

The human project owner accepted the [Cognitive Decomposition Hypothesis and route review](docs/research/2026-08-17-cognitive-decomposition-hypothesis-route-review.md) as the current research framing:

> **Trusted Local Control Plane + resource-bounded Cognitive Core + external Knowledge／Memory Plane + heterogeneous Operator／Capability Plane + independent Verification.**

The Cognitive Core contains broadly pretrained language and semantic grounding, automatic foundation capabilities, and deliberate／recurrent integration. Knowledge–reasoning decoupling is expected to be partial rather than absolute.

J-Space is one possible internal workspace mechanism. DMoE is one possible knowledge substrate. Neither is a required Dexinode component.

Skill now means an externally observable capability contract. Its implementation may be a model, parameter artifact, knowledge source, tool, solver, agent, service, verifier, human, or composed configuration.

## Current research priorities

Continue only work that sharpens:

1. the minimum complete Cognitive Core and the boundary between foundational semantics and externalizable knowledge;
2. knowledge／memory provenance, freshness, conflict, revocation, poisoning, and reader reconciliation;
3. typed operator outputs preserving relations, role bindings, constraints, uncertainty, evidence, and actual contribution;
4. workspace and recurrent／latent reasoning under complete compute- and configuration-matched evidence;
5. deterministic authority, candidate lineage, verifier independence, false acceptance, stopping, and Remote／human substitution;
6. whether a bounded workflow can distinguish missing knowledge, missing operator capability, core integration failure, verifier failure, and substitution.

## Routes closed as primary directions

The following are closed as foundations or current phases, not declared scientifically impossible:

- `one Skill = one standalone model`;
- `one Skill = one network node`;
- broad-domain routing that replaces the General core with one Specialist;
- a fixed 4B–8B Resident or reasoning boundary;
- distributed whole-model inference／idle compute as a necessary decentralization thesis;
- continuous standalone-small-model landscape or leaderboard work;
- Parametric Procedural Skill or J-Space ABI as the immediate next Gate;
- re-running Gate A／B because a newer model exists without a new system hypothesis;
- network-first federation, marketplace, token, reputation, settlement, or governance design.

Whole-model Specialists, distributed compute, parameter modules, and independent providers remain optional implementations when later evidence supports them.

## Current bounded task

No experimental Gate, implementation task, model run, benchmark, or execution plan is active.

The only current integration surface is Draft PR [#28](https://github.com/chlangjou/Dexinode/pull/28). Repository-level disposition remains separate from research-record acceptance.

## Highest-decision-value unresolved question

Before any new Gate, determine whether one bounded recoverable workflow can attribute failures separately to:

1. missing or incorrect external knowledge;
2. missing or incorrect operator capability;
3. Cognitive Core comprehension／reasoning／integration failure;
4. selector or verifier failure;
5. hidden Remote or human substitution.

Only then may a separate human decision formulate exactly one experiment.

## Hard stop conditions

Do not:

- select or download a checkpoint;
- run inference, training, quantization, GPU, J-lens, J-CoT, DMoE, custom-hardware, or deployment work;
- implement the runtime;
- create or freeze a benchmark, task set, baseline, statistical method, or threshold;
- add or activate a Gate;
- modify Gate A/B evidence or conclusions;
- resolve FIM HOLD or continue DELULU work;
- design or implement federation, marketplace, token, reputation, settlement, governance, or a network prototype.

## Next human decision

Decide separately whether the decomposition-attribution question has enough decision value and measurement clarity to justify a new issue. Do not infer authorization for an experiment, implementation, or PR automation from the new research framing.