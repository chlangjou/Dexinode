# Current Research Status

- Updated: 2026-08-10
- Active gate: **Gate B — Orchestration Advantage**
- Gate A final decision: **PASS / CLOSED**
- Gate B decision: **PENDING**
- Session handoff: `HANDOFF.md`
- Active stage: **B1R2 — oracle and semantic-contract remediation**

## Gate A retained result

Gate A established a single-specialist PASS: the Math specialist had a +29.17 pp Mathematics advantage over General with paired-bootstrap 95% CI [+16.67, +41.67] pp; the Coder checkpoint did not establish a Coding advantage. Dexinode therefore uses empirically measured capability profiles rather than checkpoint labels alone.

## Gate B hypothesis and unchanged thresholds

Gate B asks whether the validated Math specialist can be routed on a structurally fresh mixed workload to improve over General-only while both logical policies use one model inference per task.

Primary policies remain:

- General-only: General for all 96 tasks;
- Skill-routed: Math specialist for frozen Mathematics routes, General for Coding/fallback.

Thresholds remain unchanged:

- routed overall accuracy ≥ General-only +10 pp;
- paired-bootstrap 95% CI for overall delta excludes zero;
- routed Math advantage ≥ +10 pp with CI excluding zero;
- routed Coding degradation no worse than 5 pp;
- router domain accuracy ≥95%.

No selected-model execution is currently authorized.

## B1 v1.0.0 — frozen not approved

Reviewed commit: `7228c973130ed6032226118873a140927c48f17f`.

Human review: `gates/gate-b-orchestration/reviews/b1-v1.0.0-human-review.md`.

Decision: **CHANGES REQUIRED** because structural freshness was insufficient and router-v1 used handoff/output-contract cues. Artifacts remain preserved under `experiments/gate-b/benchmark-v1.0.0/` and `experiments/gate-b/router-v1/`.

## B1R v1.1.0 — frozen not approved

Reviewed commit: `48d768799bba4d5f3862359eddeb44cf134a962e`.

Human review: `gates/gate-b-orchestration/reviews/b1r-v1.1.0-human-review.md`.

Decision: **CHANGES REQUIRED**. B2 and selected-model execution remain unauthorized.

### Accepted B1R work

The prior two methodological blockers were successfully remediated:

- structural freshness: accepted; 48/48 Math and 48/48 Coding case-by-case audit PASS, exact semantic-task overlap with Gate A = 0;
- router boundary: accepted for this bounded Gate; router-v2 sees `semantic_task` only before handoff/output instructions are appended;
- adapter reused byte-identically; 13/13 tests PASS;
- router tests 5/5, benchmark routes 96/96;
- token/context validation: max input 124, max with generation allowance 1148, margin 2948;
- later execution sequence frozen as route-freeze → General 96 once → Math specialist frozen Math routes only → compose/score, with no between-phase result review;
- numerical acceptance thresholds unchanged;
- no Gate B selected model executed or inspected.

Router-v2's 96/96 score is benchmark-specific: all Coding semantic tasks begin with `Implement`, so this Gate does not claim a general-purpose/paraphrase-robust router.

### Blocking Math oracle defects

Independent human recomputation of all 48 Math cases found two errors in v1.1.0:

- `math-14`: three-digit distinct-digit multiples of 5. Frozen `64`; correct **136** (72 ending in 0 plus 64 ending in 5).
- `math-37`: expected maximum of two fair d6. Frozen `41/9`; correct **161/36**.

The other 46 Math expected values were independently accepted.

### Blocking Coding semantic-contract defects

Human review found prompt/evaluator mismatches or ambiguities that must be removed before model execution. At minimum:

- `code-02`: six-character wording conflicts with valid `#A0c9FF` (7 chars total);
- `code-09`: named keys vs "integer keys" wording;
- `code-21`: diagonal traversal rule ambiguous relative to evaluator;
- `code-38`: objective should explicitly be sum of per-part element products;
- `code-42`: which repeated character occurrences are removed is underspecified.

A complete 48/48 prompt-to-evaluator semantic-contract audit is required rather than patching only the known examples.

## Active bounded task — B1R2

Status: **COMPLETE — PENDING HUMAN REVIEW**.

Created immutable `gate-b-orchestration-v1.1.1` under
`experiments/gate-b/benchmark-v1.1.1/` without modifying v1.0.0, v1.1.0, or
router-v2. Corrected the two reviewed Math values: `math-14 = 136` and
`math-37 = 161/36`. Recomputed all 48 Math oracles independently.

Completed the full 48/48 Coding prompt-to-evaluator semantic-contract audit.
Clarified the five reviewed defects and additional indexing, tie, input-shape,
edge-case, and traversal wording; evaluator behavior and structural case
constructions were preserved.

Static validation passed: Math oracle 48/48, Coding evaluator 48/48, Coding
semantic-contract audit 48/48, adapter 13/13, router-v2 5/5 with target
benchmark routes 96/96, and token/context 96/96. Maximum rendered input is
124 tokens; maximum with 1024 generation is 1148; context margin is 2948.

No selected model was executed or inspected. Gate B thresholds, candidate
revisions, router boundary, and execution sequence remain unchanged. B2 and
all selected-model execution remain unauthorized; human review is required.

Target benchmark: `gate-b-orchestration-v1.1.1`.

Target root: `experiments/gate-b/benchmark-v1.1.1/`.

B1R2 must:

1. preserve v1.0.0/router-v1 and v1.1.0/router-v2 unchanged;
2. correct `math-14 = 136` and `math-37 = 161/36`;
3. independently recompute all 48 Math oracles and record durable evidence;
4. audit all 48 Coding semantic tasks against their evaluators, correcting ambiguous/inconsistent wording while preserving intended task constructions where possible;
5. re-run all Coding reference evaluator validation;
6. preserve accepted structural freshness and router information-boundary controls;
7. re-run adapter/router/token/context/static validation and refresh hashes;
8. keep all Gate B numerical thresholds unchanged;
9. execute or inspect **no General, Math, or Coder selected model**;
10. stop for human review before B2.

## Execution authorization

**No Gate B selected-model execution is authorized. B2 remains inactive until v1.1.1 is human-approved.**
