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

### Integration / review layer

The integration layer reconciles Agent evidence with review decisions. It owns:

- review records;
- branch reconciliation;
- `status/current.md` and task-state conflict resolution;
- integration PRs proposed for merge to `main`;
- preservation of both execution evidence and review history when branches diverge.

Normal workflow should not require a human to manually edit Git conflict markers.

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

## Branch ownership

Use single-writer execution branches:

- `agent/<task>` — execution Agent work and evidence;
- `integration/<task>` — review decisions and reconciliation before merge;
- `main` — accepted durable project state.

Reviewers should not push directly into an active Agent execution branch. If review and execution diverge, preserve both branches and reconcile them in `integration/<task>`.

If an Agent has already completed work from stale state, push that work to a distinct candidate branch rather than force-pushing or asking a human to resolve conflicts manually.

## Research loop

1. Human discussion identifies a falsifiable question or next bounded decision.
2. The question becomes a Gate specification with frozen acceptance criteria.
3. The accepted active state is recorded in `main` through `status/current.md` and the relevant task contract.
4. An execution branch is created from the accepted base.
5. Before substantive work, the Agent fetches relevant remote refs and checks that the intended base has not changed unexpectedly.
6. The Agent reads the repository state and performs one bounded task.
7. The Agent commits and pushes code, evidence, metrics, and its proposed status handoff to its own branch.
8. Human/planning review evaluates the evidence without writing directly to the Agent branch.
9. The integration layer creates or updates `integration/<task>`, preserves review records, reconciles status/task state, and opens the merge candidate.
10. After integration review, the accepted state is merged to `main`.
11. Only then is the next bounded execution branch created.

## Divergence recovery

Branch divergence is treated as a normal coordination condition, not a reason to discard work.

When review state changes while an Agent is already working:

- preserve the review branch/state;
- preserve completed Agent work on its own candidate branch;
- do not routinely force push or overwrite either side;
- integrate the two in a separate integration branch;
- make the reconciled durable state explicit before merge.

The integration record should distinguish what the Agent actually observed during execution from review information incorporated afterward.

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

The branch-ownership and integration workflow is itself part of this dogfooding: executor evidence and reviewer decisions are independent artifacts that are reconciled explicitly rather than implicitly sharing mutable conversational state.

This is useful only when it improves the research workflow. Do not force protocol complexity into early experiments before it is needed.
