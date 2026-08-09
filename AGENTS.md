# Dexinode Agent Instructions

These rules apply to all agent-driven work in this repository.

## 1. Source of truth

Before substantive work:

1. Read this file.
2. Read `status/current.md`.
3. Read the active gate specification under `gates/`.
4. Inspect existing experiment evidence before starting new work.
5. Continue from repository state rather than reconstructing project intent from chat history.

Git is the durable shared state and audit trail. Chat context is advisory and may be incomplete.

## 2. Research ownership

Agents execute research; humans own research decisions.

Agents MAY:

- research candidate models, datasets, runtimes, and tools;
- download and test publicly available artifacts when licenses permit;
- implement benchmark and evaluation tooling;
- execute experiments and record raw evidence;
- calculate metrics and uncertainty estimates;
- diagnose and fix experiment infrastructure bugs;
- update execution status;
- propose interpretations and next actions.

Agents MUST NOT independently:

- redefine the project hypothesis;
- change an active gate's acceptance criteria after evidence has been observed;
- declare a gate PASS or FAIL;
- silently replace or weaken a baseline;
- remove failed or inconvenient runs from the evidence record;
- modify an Accepted ADR except through a superseding ADR proposal;
- broaden the active task merely to produce a positive result.

## 3. Gate discipline

Each gate must answer one bounded falsifiable question.

For an active gate:

- read its `README.md`, `task.yaml`, and `acceptance.yaml` before execution;
- treat acceptance criteria as frozen once benchmark execution begins;
- record deviations, invalid runs, blockers, and confounders explicitly;
- prefer `INCONCLUSIVE` to weakening the experiment when evidence is insufficient;
- leave the final gate decision as `PENDING HUMAN REVIEW`.

## 4. Gate A restrictions

Gate A tests whether existing specialist checkpoints exhibit measurable specialization.

During Gate A:

- use existing published model checkpoints only;
- do not fine-tune, train, merge, distill, or otherwise create a new specialist model;
- do not test multi-agent orchestration, routing advantage, networking, federation, or reputation;
- prefer same-family, same-generation, similarly sized models;
- evaluate every eligible model on the same frozen cross-skill benchmark;
- run and preserve the general baseline;
- do not tune benchmark cases after model results are visible.

If no fair candidate set exists, report the gate as blocked/inconclusive rather than relaxing lineage or comparability constraints without human review.

## 5. Evidence and reproducibility

Every experiment run must preserve enough metadata to reproduce or explain the result, including when applicable:

- model identifier and exact revision/checkpoint;
- model lineage and parameter count;
- quantization;
- runtime and important dependency versions;
- inference parameters;
- prompt/template version;
- benchmark version or Git commit;
- hardware/runtime environment;
- random seed when meaningful;
- raw per-case outputs or references to them;
- derived metrics;
- failure and exclusion reasons.

Do not overwrite an invalid historical run. Mark it invalid and create a new run.

## 6. Benchmark freeze

Before formal model comparison begins, freeze the benchmark in Git.

After freeze:

- benchmark cases and scoring rules must not be changed because of observed model performance;
- bug fixes require a new benchmark version;
- prior benchmark versions and results remain in history;
- all compared models must use the same benchmark version unless an exception is explicitly approved and recorded.

## 7. Repository hygiene

Commit:

- source code;
- small benchmark definitions;
- manifests and configuration;
- metadata and checksums;
- metrics and concise reports;
- scripts needed for reproduction.

Do not commit:

- model weights;
- large downloaded datasets when a stable upstream reference exists;
- virtual environments;
- caches;
- generated dependency trees;
- multi-gigabyte raw logs.

For external artifacts, record stable identifiers, source URI, revision/version, checksum when practical, size, and license.

## 8. Status updates

When completing a bounded task, update `status/current.md` with:

- what was completed;
- evidence produced;
- blockers or uncertainties;
- the next bounded action;
- decisions that require human review.

Status is a handoff document, not a diary. Keep historical detail in commits, experiment reports, or ADRs.

## 9. Commit semantics

Prefer focused commits with prefixes such as:

- `research:` candidate discovery or research setup;
- `test:` benchmark definitions and validation;
- `experiment:` recorded experiment evidence;
- `tool:` experiment tooling;
- `docs:` research documentation and summaries.

Do not combine a change to acceptance criteria with evidence generated under the old criteria in the same commit.
