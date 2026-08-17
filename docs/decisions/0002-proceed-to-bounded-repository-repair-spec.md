# 0002 — Proceed to a bounded repository-repair Resident Core specification

- Status: Accepted
- Date: 2026-08-11
- Deciders: Human project owner
- Decision issue: [#29](https://github.com/chlangjou/Dexinode/issues/29)
- Related review: [Hybrid Agent Architecture human review](../research/2026-08-11-hybrid-agent-human-review.md)
- Supersedes: None
- Superseded by: None

## Context

ADR 0001 authorized a literature-, official-metadata-, and production-evidence-only review of a complete Hybrid Resident-Agent configuration. The Worker returned all four required documents and recommended `HOLD`.

Human review accepted the evidence, limitations, and open questions, but rejected the decision mapping. The Worker required integrated real-work evidence before allowing a bounded architecture specification. The predeclared `PROCEED` condition was narrower: a credible Local Resident Core path, no requirement to call Remote on every step, at least two absolute-small end-to-end capability signals, separable responsibilities, and measurable workflow observables.

The Worker evidence itself identifies:

- a candidate 4B–8B Resident Core region with deterministic local authority, versioned memory, bounded packets, verifiers, and controlled fallback;
- GUI, multi-turn tool, and repository-repair absolute-small capability regions with end-to-end signals;
- a responsibility split across deterministic software, Resident Model, Specialist, Remote Model, and human review;
- observable quality, human-time, latency, disclosure, fallback, recovery, and failure dimensions.

These findings do not validate the architecture. They make it specific enough to define what later evidence would need to falsify.

## Decision drivers

- A specification should precede integrated validation so that responsibilities, attribution, interfaces, and falsifiers are not invented after results are observed.
- The next question must isolate Resident Core value from hidden Remote Model control, scaffold effects, and verifier effects.
- Repository repair provides recoverable side effects, Git provenance, and deterministic compiler/test evidence without claiming that all software work is objectively verifiable.
- Human and Remote contributions must be visible rather than counted as Local Resident capability.
- Provisional context and utility numbers must remain research assumptions, not architecture acceptance criteria.

## Options considered

### Accept the Worker `HOLD`

This would preserve caution but would require the integrated evidence that a bounded specification is intended to make testable. It reverses the order of specification and validation.

### Pivot immediately to a deterministic local control plane

This remains a valid future outcome if Remote Models substitute for all material semantic decisions. Current evidence does not yet justify removing the Local Resident hypothesis because several absolute-small capability regions and bounded SLM roles remain credible.

### Proceed to one bounded architecture specification

This records interfaces, authority, state transitions, evidence attribution, escalation, and falsifiers for a single recoverable workflow. It narrows the next uncertainty without selecting a model or creating an experiment.

## Decision

Choose **`PROCEED TO BOUNDED ARCHITECTURE SPEC`**.

Specify only this question:

> For a recoverable repository-repair workflow whose result can be checked by deterministic tests, what minimum responsibility contract, packet/receipt schema, state transitions, and escalation boundary should a 4B–8B Local Resident Core have so that later evidence can determine whether it works without a Remote Model managing every step?

The resulting [bounded repository-repair specification](../specifications/bounded-repository-repair-resident-core-v0.1.md) is a falsifiable hypothesis boundary. It is not a selected implementation, benchmark, Gate, acceptance threshold, model endorsement, or validated production architecture.

## Consequences

- Preserve the four Worker documents and their original `HOLD` recommendation as auditable Agent interpretation.
- Record the human override separately and make the accepted decision unambiguous.
- Define deterministic authority, non-delegable Resident semantic responsibilities, packet/receipt schemas, legal transitions, local verification, Remote disclosure, and contribution attribution.
- Classify a run that lets Remote perform a core Resident responsibility as `CORE_SUBSTITUTION`; the workflow may still complete, but that run cannot support the Resident Core thesis.
- Treat long-term state outside model context as a Dexinode design constraint with partial evidence, not a universal scientific necessity.
- Treat the model landscape as non-exhaustive evidence, not a frozen registry.
- Keep the 8K–32K context ranges and 70%／-30%／-50% screening values provisional.

The decision does **not** authorize:

- checkpoint selection, download, inference, quantization, or GPU work;
- benchmark construction, task sampling, acceptance thresholds, or a new Gate;
- changes to Gate A or Gate B;
- FIM HOLD resolution or DELULU continuation;
- routing-economics, token, reputation, settlement, or governance design.

## Validation and revisit

Human review should first determine whether the specification:

1. stays within one recoverable repository-repair workflow;
2. makes deterministic, Resident, Specialist, Remote, and human contributions independently traceable;
3. exposes rather than hides Remote substitution;
4. defines security, recovery, and unsupported-task boundaries;
5. leaves all performance thresholds and model choices unfrozen.

Only a later, separate human decision may formulate an experimental question or Gate.
