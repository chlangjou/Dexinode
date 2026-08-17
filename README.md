# Dexinode

> Working name for a decentralized AI capability-and-evidence fabric.

Dexinode is an exploratory project about whether a trusted local control plane can coordinate a replaceable local Cognitive Core, external knowledge and memory, heterogeneous operators, Remote capabilities, tools, candidate search, and verifiers through explicit contracts—and whether that architecture can later support independently operated capability providers without depending on one AI provider.

This repository is currently a **feasibility and architecture notebook**, not a finished protocol or product.

## Why explore this?

Frontier AI capability is concentrating in a small number of large models, cloud providers, and closed orchestration stacks. At the same time, useful knowledge, private data, domain tools, formal solvers, specialized models, verifiers, and compute remain fragmented and difficult to combine safely.

Dexinode asks whether those resources can cooperate through an open capability and evidence layer:

- expose bounded capabilities rather than claim general intelligence;
- distinguish knowledge, operators, verification, and complete cognitive configurations;
- exchange typed requests, artifacts, intermediate claims, and evidence through explicit contracts;
- preserve local authority over state, credentials, disclosure, tools, side effects, and recovery;
- verify results instead of trusting self-reported capability;
- attribute actual contributions from Local, Remote, deterministic, learned, and human components;
- support independent providers and competing routing／selection policies without requiring every provider to host a complete model stack;
- resist capture by a single model provider, registry, verifier, or scoring authority.

## Working hypothesis

The project currently uses two compatible levels of hypothesis.

### Near-term architecture boundary

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

The evaluated unit is a complete Local Decision Configuration:

`model(s) + memory/context policy + harness/loop + tools + verifier(s) + search/stopping policy + fallback/human policy + runtime/hardware`

This is the accepted boundary in [ADR 0003](docs/decisions/0003-resource-bounded-verifiable-execution-fabric.md) and the [repository-repair specification v0.2](docs/specifications/bounded-repository-repair-verifiable-execution-v0.2.md). It is not a validated implementation.

### Provisional long-horizon research framing

> Useful intelligence may be partially decomposable into a trusted deterministic control plane; a resource-bounded Cognitive Core containing semantic grounding, automatic foundation capabilities, and deliberate／recurrent integration; external Knowledge／Memory and Operator／Capability planes; and independent Verification.

The Cognitive Core may use an internal deliberative workspace, explicit tokens, latent recurrence, or another reasoning mechanism. J-Space is one research example, not a Dexinode protocol. DMoE is one example of modular parametric knowledge, not the definition of a Skill.

Knowledge–reasoning decoupling is expected to be **partial**, not absolute. Language, reusable concepts, world priors, automatic routines, and the machinery that performs reasoning may remain deeply integrated inside the core.

This is a hypothesis to narrow and falsify—not a conclusion.

## What a Skill means now

A **Skill** is a versioned, externally observable capability contract. It is not assumed to be:

- one standalone model;
- one Adapter;
- one network node;
- one internal workspace location;
- or one implementation technology.

A Skill may be realized by knowledge, memory, deterministic algorithms, tools, learned operators, complete models, agents, Remote services, verifiers, humans, or a composed configuration. Capability identity must include the relevant substrate, compatibility, runtime, policy, provenance, and verification conditions.

## Repository map

- [Vision](docs/vision.md)
- [Core concepts](docs/core-concepts.md)
- [Architecture](docs/architecture.md)
- [Open questions](docs/open-questions.md)
- [Roadmap](docs/roadmap.md)
- [Current status](status/current.md)
- [Cognitive Decomposition Hypothesis and route review](docs/research/2026-08-17-cognitive-decomposition-hypothesis-route-review.md)
- [J-Space and J-CoT material evidence review](docs/research/2026-08-17-j-space-j-cot-material-evidence-review.md)
- [DMoE parametric knowledge-injection evidence review](docs/research/2026-08-16-dmoe-parametric-knowledge-injection-evidence-review.md)
- [Strategic reorientation review](docs/research/2026-08-14-strategic-reorientation-review.md)
- [Current bounded repository-repair specification](docs/specifications/bounded-repository-repair-verifiable-execution-v0.2.md)
- [Specification v0.2 human review](docs/research/2026-08-14-verifiable-execution-v0.2-human-review.md)
- [Prior Resident Core specification](docs/specifications/bounded-repository-repair-resident-core-v0.1.md)
- [Gate A／B and pre-Hybrid evidence](docs/research/README.md)
- [Decision records](docs/decisions/README.md)

## Current status

- Project name: **Dexinode** (working name)
- Stage: Cognitive Decomposition research framing accepted; no experimental execution authorized
- Repository visibility: public
- License: undecided
- Gate A — Specialist Validation: **PASS / CLOSED**
- Gate B — Orchestration Advantage: **FAIL / CLOSED**
- FIM / syntax-aware MVSS eligibility: **HOLD**
- Active experimental Gate: **none**
- Integration surface: Draft PR [#28](https://github.com/chlangjou/Dexinode/pull/28)

## Current research priorities

The project should continue only work that sharpens:

1. the minimum complete Cognitive Core and the boundary between foundational semantics and externalizable knowledge;
2. knowledge／memory provenance, freshness, conflict, revocation, poisoning, and reader integration;
3. typed operator outputs preserving relations, bindings, constraints, uncertainty, evidence, and actual contribution;
4. workspace and recurrent／latent reasoning under complete configuration- and compute-matched evidence;
5. deterministic authority, candidate lineage, verifier independence, false acceptance, stopping, and Remote／human substitution;
6. whether one bounded workflow can distinguish missing knowledge, missing operator capability, core integration failure, verifier failure, and hidden substitution.

No model, benchmark, task set, threshold, implementation, or Gate is currently selected.

## Routes no longer used as foundations

The project no longer assumes:

- `one Skill = one standalone model`;
- `one Skill = one network node`;
- a broad-domain router should hand the complete task to one Specialist as a General replacement;
- a fixed parameter range defines the Resident or reasoning role;
- distributed whole-model inference or idle compute is required for decentralization;
- continuous small-model leaderboard work is a standing project phase;
- DMoE procedural modules or a J-Space ABI should be the immediate next Gate;
- federation, marketplace, token, reputation, settlement, or governance should be designed before local composition and verification show measurable value.

These routes are closed as project foundations or current phases, not declared scientifically impossible. Whole-model Specialists, distributed compute, parameter modules, and independent nodes remain optional implementations where later evidence supports them.

## Principles

1. Evidence over capability claims.
2. Explicit contracts over implicit prompt conventions.
3. Replaceable components over provider lock-in.
4. Local-first and privacy-aware authority where useful.
5. Recovery and dispute handling as first-class protocol behavior.
6. Complete configurations and attempt sets over model-only or winner-only claims.
7. Skill as a capability contract, not a substrate assumption.
8. Knowledge, operators, reasoning, and verification should be distinguished before they are composed.
9. Decentralization is justified only by resilience, privacy, access, interoperability, competition, or anti-capture value.
10. Economics are optional until technical value is demonstrated.

## Contributing to the exploration

Record new ideas as dated evidence, hypotheses, alternatives, bounded specifications, experiments, or human decisions. Preserve the distinction between external research results and Dexinode inference. Avoid turning an attractive mechanism into a fixed architecture before it survives complete-system comparison and adversarial review.