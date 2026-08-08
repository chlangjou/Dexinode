# Feasibility roadmap

The roadmap is organized around reducing uncertainty, not maximizing feature count.

## Phase 0 — Frame the claim

Goal: identify the narrowest valuable hypothesis.

Deliverables:

- problem statement and non-goals;
- comparison with adjacent protocols and systems;
- one initial use case;
- baseline using a single general model;
- measurable success and stop criteria;
- initial threat and trust assumptions.

Exit condition: we can state what evidence would support or reject the project.

## Phase 1 — Local multi-specialist experiment

Goal: test whether explicit specialization and handoffs help before introducing networking complexity.

Candidate setup:

- three skills with different models or tools;
- structured skill manifests;
- one orchestrator/router;
- versioned handoff contracts;
- replayable execution log;
- deterministic checks where possible.

Measurements:

- completion quality;
- latency and compute cost;
- number and cause of retries;
- handoff failure rate;
- context passed between nodes;
- performance against the single-model baseline.

Exit condition: specialization produces a measurable advantage for at least one task class.

## Phase 2 — Independent nodes and verification

Goal: cross a real trust and operational boundary.

Add:

- signed node and skill identities;
- remote transport;
- receipts and provenance;
- at least two verification strategies;
- timeout, retry, fallback, and cancellation behavior;
- a deliberately faulty or adversarial node.

Exit condition: the workflow remains inspectable and completes safely despite one unreliable participant.

## Phase 3 — Federation and portable evidence

Goal: test discovery without a single authoritative registry.

Add:

- two registry implementations or synchronized catalogs;
- portable signed evidence;
- consumer-specific reputation calculations;
- privacy and locality constraints;
- diversity-aware routing.

Exit condition: a caller can change registry or router without republishing every skill or losing all historical evidence.

## Phase 4 — Operational pilot

Goal: evaluate usefulness under a real workload.

Candidate pilot qualities:

- bounded data and authority;
- clear baseline and owner;
- enough repeated tasks for measurement;
- recoverable failure;
- no irreversible economic mechanism.

Exit condition: operational users prefer the federated workflow for a concrete reason such as quality, privacy, resilience, cost, or provider independence.

## Phase 5 — Economics and open participation

Only begin if previous phases show that independent parties create durable value.

Investigate:

- accounting models;
- payment and dispute mechanisms;
- Sybil resistance;
- liability and compliance;
- incentive attacks;
- governance and protocol stewardship.

A blockchain or token is one possible implementation, not a prerequisite or default.

## Immediate next decisions

1. Choose the first task domain.
2. Define a single-model baseline.
3. Draft skill-manifest and handoff-contract schemas.
4. Choose two failure cases the prototype must survive.
5. Define measurements and a falsification threshold.
6. Decide whether the first implementation should be a simulator or runnable services.
