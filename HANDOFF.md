# Dexinode Session Handoff

Repository: `chlangjou/Dexinode`

Canonical branch: `main`

Integration surface: Draft PR [#28](https://github.com/chlangjou/Dexinode/pull/28)

Snapshot: 2026-08-14

Git is the durable source of truth. This file is intentionally compact for a fresh session.

## Start here

Read in this order:

1. `AGENTS.md`
2. `HANDOFF.md`
3. `status/current.md`
4. `docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md`
5. `docs/specifications/bounded-repository-repair-verifiable-execution-v0.2.md`
6. `docs/research/2026-08-14-strategic-reorientation-review.md`
7. `docs/architecture.md`

Read the prior decision and specification for provenance:

- `docs/decisions/0002-proceed-to-bounded-repository-repair-spec.md`
- `docs/specifications/bounded-repository-repair-resident-core-v0.1.md`
- `docs/research/2026-08-11-hybrid-agent-human-review.md`

Read Gate closure records only when their evidence is needed:

- `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
- `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

Do not reopen Gate A/B execution unless a new human decision explicitly requires it.

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

Durable lesson: broad-domain classification is not per-task success prediction.

Gate conclusions apply to pinned models, benchmark, runtime, and date. They are not universal claims about all later models of the same parameter range.

## Preserved decisions

- FIM / syntax-aware MVSS eligibility remains **`HOLD`**.
- ADR 0002 remains accepted history: write one bounded, falsifiable repository-repair specification before any experiment.
- Specification v0.1 remains unchanged as the single-Resident／4B–8B candidate produced under ADR 0002.
- No experimental Gate is active.

## Current strategic decision

[Issue #30](https://github.com/chlangjou/Dexinode/issues/30) and [ADR 0003](docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md) record the human decision to continue Dexinode while moving the foundation up one abstraction layer:

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

Replace the mandatory single 4B–8B Resident Model with a **Local Decision Configuration**:

`model(s) + memory/context policy + harness/loop + tools + verifier(s) + search/stopping policy + fallback/human policy + runtime/hardware`

Reasons recorded in the strategic review:

- locally deployable and distilled model capability is moving quickly;
- model-specific inference hardware can change attempt economics abruptly;
- automated research loops increase the expected turnover of model assumptions without proving a fixed acceleration rate;
- latent/recurrent reasoning may decouple capability from parameter count and visible reasoning tokens;
- cheap attempts move the bottleneck toward candidate diversity, selection, verifier independence, false acceptance, and exposure.

The review explicitly corrects two overstatements:

- Discovery Loop is a company founded by senior former Google researchers, not a DeepSeek spinout;
- Taalas' 17K tokens/sec is a vendor result for aggressively quantized, model-specific silicon with an acknowledged quality caveat, not a general hardware baseline.

## Current bounded artifact

`docs/specifications/bounded-repository-repair-verifiable-execution-v0.2.md`

Question:

> For a recoverable repository-repair workflow with relevant deterministic checks, what minimum control-plane, Local Decision Configuration, attempt／candidate, verification, selection, and escalation contracts would let later evidence determine whether a resource-bounded local configuration is useful without assuming a fixed model size, model count, reasoning architecture, or Remote Model dependency?

The strongest automatic output remains a locally verified candidate set for human disposition. Push, PR, merge, deployment, credentials, production mutation, and irreversible work remain outside scope.

Key v0.2 additions:

- complete configuration identity rather than model identity alone;
- logical separation of generator, selector, verifier, policy, Remote, and human roles;
- per-attempt state and candidate lineage;
- verifier revision, coverage, independence, visibility, and exposure;
- complete attempt-set and selection receipts;
- explicit Remote and human substitution attribution;
- no assumption that more attempts imply reliability.

## Current bounded task

Human-review specification v0.2 for boundedness, authority, attribution, verifier risk, replaceability, and absence of frozen performance criteria.

Stop after review. Any implementation, model run, benchmark, threshold, or Gate requires a separate decision issue.

## Hard stop conditions

Do not:

- select or download a checkpoint;
- run inference, quantization, GPU, custom-hardware, or deployment work;
- implement the runtime;
- create or freeze a benchmark, task set, baseline, statistical method, or threshold;
- add or activate a Gate;
- modify Gate A/B evidence or conclusions;
- resolve FIM HOLD or continue DELULU work;
- reopen routing economics;
- design federation, token, reputation, settlement, governance, or a marketplace.

## Next human decision

Accept specification v0.2 as the current falsifiable boundary or request a focused revision. Do not infer authorization for an experiment from specification acceptance.
