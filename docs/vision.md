# Vision

## Problem statement

AI capability is concentrating around a small number of general-purpose models, cloud providers, and closed orchestration stacks. Meanwhile, private and current knowledge, domain tools, formal solvers, specialized models, verifiers, local data, and compute remain fragmented and difficult to combine safely.

Dexinode explores whether an open capability-and-evidence layer can let these independent resources cooperate while a trusted local boundary retains control of state, privacy, credentials, side effects, verification, rollback, and final disposition.

## Near-term architectural commitment

The current accepted architecture boundary is:

> **Trusted Local Control Plane + Resource-Bounded Verifiable Execution／Search Fabric**

The evaluated unit is the complete Local Decision Configuration rather than one model or parameter range:

`model(s) + memory/context policy + harness/loop + tools + verifier(s) + search/stopping policy + fallback/human policy + runtime/hardware`

This boundary is intended to survive changes in model scale, reasoning style, inference hardware, memory systems, and Local／Remote allocation. It remains unvalidated end to end.

## Provisional long-term cognitive hypothesis

The current research framing is that useful intelligence may be **partially** decomposable into:

1. a trusted deterministic Local Control Plane;
2. a resource-bounded Cognitive Core with language and semantic grounding, automatic foundation capabilities, deliberate／recurrent reasoning, and integration;
3. external Knowledge／Memory providers;
4. heterogeneous Operator／Capability providers;
5. independent Verification and selection.

A J-Space-like deliberative workspace is one possible internal mechanism of the Cognitive Core. It is not the complete reasoning engine or a network protocol. DMoE-like experts are one possible knowledge substrate. They are not the definition of a Skill.

The core is not assumed to reason without prior knowledge. Broad semantics, world priors, language, automatic routines, and the machinery that reads and writes intermediate state may remain deeply integrated through pretraining. The open question is which long-tail, current, private, episodic, and procedural capabilities can be externalized without losing reliable composition.

## Long-term network vision

A future Dexinode system would not require every task to move through a sequence of standalone Specialist models. Instead, a locally controlled Cognitive Core could discover and invoke independently provided resources such as:

- knowledge sources, indexes, and parameterized knowledge artifacts;
- deterministic algorithms, tools, compilers, solvers, and simulators;
- learned operators, Adapters, Specialist models, agents, and Remote services;
- memory and retrieval systems;
- verifiers, attestations, and challenge services;
- optional compute providers;
- complete cognitive configurations when justified.

Each provider would declare what capability it offers, which inputs and authority it requires, what compatibility constraints apply, which evidence it returns, and how failure, cancellation, update, and revocation work.

The Local Control Plane would preserve task state and policy, while the Cognitive Core or selector integrates eligible typed contributions. Verification would make incorrect, unavailable, malicious, or incompatible providers visible before durable side effects are accepted.

A useful Dexinode ecosystem would:

- keep sensitive work near its data where needed;
- let independent parties contribute capability without owning the complete AI stack;
- support provider, model, tool, verifier, and knowledge diversity;
- survive the refusal, failure, or replacement of individual providers;
- make requests, artifacts, intermediate claims, evidence, and substitutions inspectable;
- compare complete-system quality, latency, resource use, disclosure, and active human time;
- avoid making any single provider, registry, router, verifier, or scoring authority indispensable;
- reward demonstrated capability and evidence rather than scale, branding, or self-description alone.

This remains a long-term possibility. Current work does not assume the network layer is the first or primary source of value.

## Intended contribution

The project may eventually contribute at four levels:

1. **Capability semantics:** substrate-neutral declarations for Skills, knowledge artifacts, operators, verifiers, and complete configurations.
2. **Protocol:** interoperable request, invocation, handoff, evidence, selection, update, revocation, and recovery contracts.
3. **Runtime:** reference tools for local authority, discovery, context compilation, execution, sandboxing, verification, attribution, and rollback.
4. **Ecosystem:** portable evidence, consumer-specific reputation, and optional accounting across operators.

Protocol and evidence portability are more durable than any reference runtime or selected model.

## Design values

### Decentralization is a means

The goal is not decentralization for its own sake. It should improve resilience, access, privacy, interoperability, competition, provider choice, or resistance to capture. Distributed inference is one possible mechanism, not a requirement.

### Skill is a capability contract

A Skill is not synonymous with a model, Adapter, node, or latent representation. It is a versioned externally observable capability under explicit compatibility, policy, provenance, and verification conditions.

### Integration matters as much as capability

Correct knowledge or a strong bounded operator does not guarantee a correct system result. The Cognitive Core must understand, reconcile, and compose contributions under the current requirement, while failures remain attributable.

### Verification is part of execution

A handoff or invocation is incomplete until the caller can evaluate whether the returned result satisfies the contract. Verification may be deterministic, model-assisted, replicated, attested, or human-reviewed, and its limits must remain visible.

### Diversity is a resilience property

Diversity includes model families, knowledge sources, tools, operators, verifiers, hardware, organizations, jurisdictions, and reasoning modes. It reduces correlated failure and dependence on one supply chain.

### Local participation should be practical

Participation should not require operating a full foundation model, exposing private data, running a blockchain, or accepting unbounded liability. Providers may contribute knowledge, operators, verification, or compute at different layers.

### Replaceability over frozen model assumptions

Model size, active parameters, context window, latent reasoning interface, tokens per second, and hardware are configuration metadata rather than permanent architectural roles.

## Routes no longer used as foundations

Dexinode no longer assumes:

- one Skill must be one standalone model or one node;
- broad-domain routing should replace the General core with one Specialist;
- a fixed 4B–8B range defines local reasoning viability;
- distributed whole-model inference is necessary for decentralization;
- continuous model leaderboard research is the roadmap;
- J-Space or DMoE should be productized as the immediate next step;
- federation, reputation, marketplace, token, settlement, or governance should precede evidence of value inside one trust domain.

These routes may remain optional implementation choices where later evidence supports them.

## Non-goals for the current stage

- creating a new foundation model;
- selecting or implementing J-Space, J-CoT, DMoE, or another latent architecture;
- promising AGI or universal cognitive decomposition;
- launching a token or speculative market;
- solving universal truth or model alignment;
- fully permissionless execution before basic safety and verification are demonstrated;
- replacing all centralized AI services;
- opening a network prototype before local composition and attribution show measurable value.

## Long-term credibility criteria

The idea becomes more credible if staged evidence eventually demonstrates all of the following:

- a bounded workflow distinguishes missing knowledge, missing operator capability, Cognitive Core integration failure, verifier failure, and Remote／human substitution;
- independently supplied knowledge or operator capability improves verified completion on structurally fresh tasks;
- machine-readable declarations and contracts preserve compatibility, authority, provenance, and failure behavior;
- one incorrect, malicious, incompatible, or unavailable provider is detected and safely bypassed;
- the complete system is compared with strong monolithic and Remote baselines on quality, false acceptance, active human time, privacy, latency, and resource cost;
- at least two independently operated providers or trust domains add value beyond a conventional local plugin system;
- no central component is indispensable to the demonstrated benefit.

These are long-term criteria, not the current research exit condition.

## Failure signals

We should narrow or stop the project if:

- a resource-bounded Cognitive Core cannot reliably integrate complete and correct external evidence;
- knowledge, operator, and integration failures cannot be distinguished well enough for learning or recovery;
- coordination and verification overhead consistently exceed capability benefits;
- verifier false acceptance remains unacceptable under realistic search and feedback exposure;
- privacy, abuse prevention, liability, compatibility, or update risk make independent participation impractical;
- the same value is better achieved through a conventional local plugin or retrieval system;
- independent providers add no measurable resilience, privacy, access, competition, or anti-capture value;
- the Local Control Plane supplies no measurable value over a strong monolithic or Remote agent.