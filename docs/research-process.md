# Research Execution Process

Dexinode uses Git as durable shared state between human planning/review and agent execution.

## Roles

### Human / planning layer

Humans own:

- project goals and hypotheses;
- gate definitions;
- acceptance thresholds;
- major scope changes;
- interpretation of ambiguous evidence;
- final PASS / FAIL / INCONCLUSIVE decisions.

### Execution agent

Agents own:

- bounded research tasks;
- implementation and experiment tooling;
- candidate discovery;
- experiment execution;
- evidence capture;
- metrics and reproducibility metadata;
- proposed interpretations and next steps.

### Git repository

Git is the durable coordination surface for:

- specifications;
- decisions;
- task contracts;
- experiment definitions;
- evidence;
- status handoffs;
- audit history.

Git is not a runtime queue, heartbeat system, lock service, or real-time message bus.

## Research loop

1. Human discussion identifies a falsifiable question.
2. The question becomes a Gate specification with frozen acceptance criteria.
3. The active state is recorded in `status/current.md`.
4. An execution agent reads the repository state and performs one bounded task.
5. The agent commits code, evidence, metrics, and a status update.
6. The agent may recommend an outcome but may not declare the Gate result.
7. Humans review the evidence and record PASS, FAIL, or INCONCLUSIVE.
8. Only after that decision is the next Gate activated or the current Gate redesigned.

## Gate outcomes

### PASS

The predefined evidence threshold is satisfied and human review accepts that the evidence supports the Gate hypothesis.

### FAIL

A fair and sufficiently powered test was completed, but the predefined evidence threshold was not satisfied.

### INCONCLUSIVE

The test cannot answer the Gate question reliably. Examples include missing comparable models, license restrictions, benchmark contamination, insufficient runtime capacity, invalid scoring, or an unresolved confounder.

INCONCLUSIVE is not equivalent to FAIL.

## Evidence-before-conclusion rule

Agents should separate:

1. raw observations;
2. calculated metrics;
3. known confounders;
4. interpretation;
5. recommended outcome.

The final Gate outcome is a human decision.

## Change control

Once formal evidence collection begins:

- acceptance criteria are frozen;
- benchmark cases and scoring rules are versioned;
- baseline definitions are frozen;
- invalid runs are preserved and labeled rather than deleted;
- methodological changes require a new benchmark/experiment version or explicit human approval.

Accepted architectural or research decisions that materially constrain future work should use ADRs under `docs/decisions/`.

## Dogfooding objective

The research workflow should gradually exercise Dexinode concepts itself. Machine-readable Gate tasks may evolve into early versions of handoff contracts, evidence manifests, verification policies, and portable execution records.

This is useful only when it improves the research workflow. Do not force protocol complexity into early experiments before it is needed.
