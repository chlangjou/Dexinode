# Current Research Status

- Updated: 2026-08-10
- Active gate: **Gate B — Orchestration Advantage**
- Gate A final decision: **PASS / CLOSED**
- Gate B decision: **PENDING**
- Session handoff: `HANDOFF.md`
- Active stage: **B1R — complete, pending human review**

## Gate A retained result

Gate A established a single-specialist PASS: the Math specialist had a +29.17 pp Mathematics advantage over General with paired-bootstrap 95% CI [+16.67, +41.67] pp; the Coder checkpoint did not establish a Coding advantage. Dexinode therefore uses empirically measured capability profiles rather than checkpoint labels alone.

Final decision record:

`gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`

## Gate B bounded hypothesis

Test whether an evidence-based router can convert a validated specialist capability into a measurable mixed-workload advantage over General-only while each logical policy uses exactly one model inference per task.

Initial registry remains:

- Mathematics → `Qwen/Qwen2.5-Math-7B-Instruct`;
- Software Coding → `Qwen/Qwen2.5-7B-Instruct`;
- fallback → General;
- Qwen2.5-Coder is not treated as a validated Coding specialist.

The primary Gate B thresholds remain unchanged:

- routed overall accuracy ≥ General-only +10 pp;
- paired-bootstrap 95% CI for overall delta excludes zero;
- routed Math advantage ≥ +10 pp with CI excluding zero;
- routed Coding degradation no worse than 5 pp;
- router domain accuracy ≥95%.

## B1 v1.0.0 — static work accepted in part, benchmark NOT approved

Reviewed commit:

`7228c973130ed6032226118873a140927c48f17f`

Human review:

`gates/gate-b-orchestration/reviews/b1-v1.0.0-human-review.md`

Decision: **CHANGES REQUIRED**. B2 and all selected-model execution remain unauthorized.

Accepted B1 work includes:

- 96-case 48/48 balanced design and 10/24/14 difficulty counts;
- no Gate B selected-model execution during B1;
- 48/48 Math oracle validation, including pre-execution correction of math-27 to 24;
- 48/48 Coding evaluator validation and 121/121 reference tests PASS;
- Gate A adapter reused byte-identically with 13/13 tests PASS;
- max rendered input 188; max with generation 1212; context margin 2884;
- frozen model/runtime/scoring controls and unchanged numerical acceptance thresholds.

### Blocking finding 1 — structural freshness

Exact prompt overlap is zero, but v1.0.0 contains many Gate A near-isomorphic or semantically identical case constructions. Material Math examples include:

- `math-23` repeats Gate A inverse of 17 mod 43;
- `math-39` repeats the same T_8 Fibonacci-like tiling recurrence;
- `math-08` repeats the 90-degree CCW coordinate rotation construction;
- `math-33` repeats line-region counting with only n changed;
- `math-35` repeats the surjection inclusion-exclusion skeleton;
- `math-37` repeats bounded-composition inclusion-exclusion structure;
- `math-43` repeats adjacent Catalan-number evaluation.

Because Gate B's expected treatment advantage comes primarily from Math routing, this is a material out-of-sample transfer confounder.

### Blocking finding 2 — router information boundary

Router v1 uses benchmark handoff/output-contract phrases such as `python 3.10`, `python or unlabeled`, `implementation block`, `integer`, and `fraction`. The 96/96 route score therefore partly measures benchmark formatting rather than semantic task selection.

Dexinode should route on semantic task text **before** applying a skill's handoff/output contract.

## Active bounded task — B1R

Status: **COMPLETE — PENDING HUMAN REVIEW**.

Created and froze `gate-b-orchestration-v1.1.0` under
`experiments/gate-b/benchmark-v1.1.0/` and `router-v2` under
`experiments/gate-b/router-v2/`. v1.0.0 and router-v1 are unchanged. The new
benchmark has 48 fresh Math and 48 fresh Coding cases with 10/24/14 difficulty
counts per domain. The case-by-case structural audit reports 48/48 Math and
48/48 Coding freshness PASS; exact semantic-task text overlap with Gate A is
zero, and no Gate A per-case result or raw output was used.

Static validation completed without selected-model execution:

- independent Math oracle validation: 48/48 PASS;
- independent Coding evaluator validation: 48/48 PASS;
- accepted adapter copied byte-identically and synthetic tests: 13/13 PASS;
- semantic-task-only router-v2 tests: 5/5 PASS and 96/96 benchmark routes;
- pinned tokenizer validation: 96/96 PASS, maximum rendered input 124,
  maximum with 1024 generation 1148, context margin 2948.

The frozen protocol computes route decisions from semantic task text only before
model output, then runs General once on all 96 cases and the Math specialist
only for frozen Math routes, reusing General outputs for General routes. No
between-phase result review, retry, fallback call, or protocol change is
permitted. Gate B acceptance thresholds and selected revisions are unchanged.

No Gate B General, Math, or Coder checkpoint was executed. B2/B3/B4 remain
inactive. Human review is required before any selected-model execution.

Frozen B1R artifacts:

- benchmark: `gate-b-orchestration-v1.1.0`
- root: `experiments/gate-b/benchmark-v1.1.0/`
- router: `experiments/gate-b/router-v2/`

Requirements are controlled by:

- `gates/gate-b-orchestration/task.yaml`
- `gates/gate-b-orchestration/acceptance.yaml`
- `gates/gate-b-orchestration/reviews/b1-v1.0.0-human-review.md`

Key requirements:

1. preserve v1.0.0/router-v1 unchanged as frozen-not-approved history;
2. replace positional mirrors, constant/coefficient substitutions and near-isomorphic Gate A case reuse;
3. produce case-by-case structural freshness audit against Gate A definitions;
4. use Gate A case definitions only for structural comparison — no Gate A per-case results/raw outputs/postmortem-driven case selection;
5. independently revalidate all Math oracles and all Coding evaluator fixtures;
6. expose only semantic task text to router; handoff/output contract and metadata remain invisible;
7. add reporting-only coarse task-family metadata invisible to router;
8. freeze one later execution sequence with no result review between General evidence collection and specialist-selected evidence collection;
9. execute **no selected model** during B1R and stop for human review.

## Execution authorization

**No Gate B General/Math/Coder selected-model execution is authorized.**

B2 and later stages remain inactive until B1R is human-approved.
