# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A5R1 — v1.2.2 oracle-correction and complete static validation (completed pending human review)

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

## Selected models remain unchanged

- General: `Qwen/Qwen2.5-7B-Instruct` @ `a09a35458c702b33eeacc393d103063234e8bc28`
- Math specialist: `Qwen/Qwen2.5-Math-7B-Instruct` @ `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`
- Coder specialist: `Qwen/Qwen2.5-Coder-7B-Instruct` @ `c03e6d358207e414f1eca0bb1891e29f1db0e242`

Gate acceptance criteria are unchanged.

## Preserved history

The v1.1 benchmark and all A4/A5 execution evidence remain immutable audit history. The strict v1.1 Math-specialist zero row was human-reviewed as output-interface-confounded, not valid capability-zero evidence.

`gate-a-cross-skill-v1.2.0` is also preserved as frozen-not-approved because its Math case set reused too many v1.1 problem skeletons after those structures had already been observed.

Durable reviews:

- `gates/gate-a-specialization/reviews/a5-interface-confounder-human-review.md`
- `gates/gate-a-specialization/reviews/a5r1-v1.2-human-review.md`

A6 remains inactive.

## A5R1 v1.2.1 — structural freshness accepted, benchmark NOT approved

Agent freeze commit reviewed:

`33dc8227eee11ab462f111e3049b5e538d4ca9f7`

Frozen artifacts remain preserved unchanged under:

`experiments/gate-a/benchmark-v1.2.1/`

Human review:

`gates/gate-a-specialization/reviews/a5r1-v1.2.1-human-review.md`

Decision: **CHANGES REQUIRED**.

### What passed

The v1.2.1 Math structural-freshness revision is accepted in principle:

- 48 replacement Math cases with 10 foundational / 24 intermediate / 14 advanced;
- explicit case-by-case structural review against v1.1;
- no one-to-one positional mirroring or coefficient-only substitution identified in the committed audit;
- exact Math prompt overlap with v1.1 = 0;
- exact normalized oracle overlap = 0;
- complete nonempty numeric-tuple overlap = 0;
- accepted v1.2 coding set reused;
- accepted semantic adapter/scoring/strict metrics reused;
- 13/13 synthetic adapter tests pass;
- max rendered input = 187 tokens; max with 1024 generation allowance = 1211; context margin = 2885;
- provenance correctly acknowledges that v1.1 outputs motivated remediation while no selected-model raw output is used as an adapter fixture and no v1.2.1 case/oracle/difficulty label is tuned using selected-model performance.

### Benchmark-definition errors found during human oracle sanity review

Two frozen Math expected values are wrong:

1. `math-23` — two distinct digits selected in order from 1..9; probability their sum is divisible by 3.
   - total ordered pairs = 72;
   - favorable pairs = 24;
   - verified probability = **1/3**;
   - v1.2.1 frozen oracle incorrectly records `1/4`.

2. `math-30` — five labeled balls assigned to four labeled boxes with no box empty.
   - inclusion-exclusion: `4^5 - 4*3^5 + 6*2^5 - 4 = 240`;
   - verified answer = **240**;
   - v1.2.1 frozen oracle incorrectly records `432`.

These are `benchmark_definition_error` findings under the frozen scoring policy. v1.2.1 must not be patched in place and no selected model may be executed against it.

Human spot-checking of the other visible foundational/intermediate/advanced cases did not identify another oracle defect, but that does not replace full static validation.

## Active bounded task — v1.2.2

Create a narrow corrective benchmark version:

`gate-a-cross-skill-v1.2.2`

Target root:

`experiments/gate-a/benchmark-v1.2.2/`

### Completion state

The v1.2.2 benchmark is completely defined and frozen pending human review.
The v1.2.1 structurally fresh Math prompts, difficulty labels, and order are
carried forward; v1.2.0 and v1.2.1 remain unchanged audit artifacts.

Independent exact/static validation produced:

- Math oracle validation: **48/48 PASS** in `oracle-validation.yaml`;
- required corrections: math-23 `1/4` -> `1/3`, math-30 `432` -> `240`;
- additional inherited correction: math-37 `63/665` -> reduced `9/95`;
- coding cases SHA-256 identical to v1.2.0 and v1.2.1;
- adapter implementation/tests SHA-256 identical to v1.2.0 and v1.2.1;
- synthetic adapter tests: **13/13 PASS**;
- exact prompt overlap with v1.1: 0; normalized expected-oracle overlap: 0;
- complete numeric-tuple overlap: 0; lexical numeric-literal intersection: 22;
- rendered-input maximum: 187; maximum with 1024 generated tokens: 1211;
- remaining 4096-token context margin: 2885.

No selected model was executed or inspected during v1.2.2 construction. Gate
acceptance criteria and the selected candidate revisions are unchanged.

Requirements:

1. preserve v1.2.1 unchanged as frozen-not-approved audit evidence;
2. carry forward the v1.2.1 structurally fresh Math case constructions;
3. carry forward the accepted v1.2.0/v1.2.1 coding set unchanged;
4. carry forward the accepted semantic adapter, scoring contract, strict metrics, template, tokenizer/runtime controls, candidates/revisions, and Gate thresholds;
5. correct `math-23` expected value to `1/3`;
6. correct `math-30` expected value to `240`;
7. correct any additional oracle defect found by complete validation (math-37 is now `9/95`);
8. independently recompute and validate **all 48 Math oracles**, preserving a durable machine-readable/manual validation record;
9. refresh benchmark version identifiers, hashes, token counts/manifests as needed;
10. run 13 synthetic adapter tests and static/context validation;
11. execute no General, Math, or Coder checkpoint;
12. stop for human review before A5R2.

A5R2 and A6 remain inactive.

## Approved execution substrate retained for later A5R2

- host `ai01`;
- Docker Engine 29.5.3 / `runc`;
- exactly one NVIDIA L40 UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- formal inference: 40 GiB / 16 CPUs;
- A4b package/runtime and deterministic generation policy;
- approved Docker judge-v2 isolation and 2-second watchdog;
- Gate-specific caches independent of Ollama/Open-WebUI.

## Next human checkpoint

Review frozen `gate-a-cross-skill-v1.2.2`, especially the complete 48-case Math oracle validation record and confirmation that only the narrow corrective scope changed. A5R2 and A6 remain inactive until that approval.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
