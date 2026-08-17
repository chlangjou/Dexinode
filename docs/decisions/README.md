# Architecture Decision Records

Use this directory for decisions that materially constrain Dexinode's protocol, implementation, governance, or research direction.

## Status values

- **Proposed** — under active discussion.
- **Accepted** — current working decision.
- **Superseded** — replaced by a later record.
- **Rejected** — considered and deliberately not adopted.

## Naming

Use NNNN-short-title.md.

Example: 0001-first-prototype-domain.md.

## Template

    # NNNN — Decision title

    - Status: Proposed
    - Date: YYYY-MM-DD
    - Deciders:
    - Supersedes:
    - Superseded by:

    ## Context

    What problem or uncertainty requires a decision?

    ## Decision drivers

    - Driver one
    - Driver two

    ## Options considered

    ### Option A

    Benefits, costs, risks, and unknowns.

    ### Option B

    Benefits, costs, risks, and unknowns.

    ## Decision

    What is the current choice?

    ## Consequences

    What becomes easier, harder, required, or prohibited?

    ## Validation

    What evidence or experiment could confirm or overturn this decision?

## Working rule

Do not create an ADR for every idea. Use one when a choice changes future work, closes a meaningful alternative, or needs an explicit condition for reconsideration.

## Records

- [0001 — Use a hybrid resident-agent frame for the next research stage](0001-hybrid-resident-agent-research-frame.md) — Accepted, 2026-08-10; decision issue [#27](https://github.com/chlangjou/Dexinode/issues/27).
- [0002 — Proceed to a bounded repository-repair Resident Core specification](0002-proceed-to-bounded-repository-repair-spec.md) — Accepted, 2026-08-11; decision issue [#29](https://github.com/chlangjou/Dexinode/issues/29).
- [0003 — Reframe the Resident Core as a resource-bounded verifiable execution fabric](0003-resource-bounded-verifiable-execution-fabric.md) — Accepted, 2026-08-14; partially supersedes ADR 0002's fixed single-Resident／4B–8B premise; decision issue [#30](https://github.com/chlangjou/Dexinode/issues/30).
