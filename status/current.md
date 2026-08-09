# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A5R1 — Interface Protocol and Fresh Benchmark Freeze (v1.2.1 revision required)

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

## Selected models remain unchanged

- General: `Qwen/Qwen2.5-7B-Instruct` @ `a09a35458c702b33eeacc393d103063234e8bc28`
- Math specialist: `Qwen/Qwen2.5-Math-7B-Instruct` @ `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`
- Coder specialist: `Qwen/Qwen2.5-Coder-7B-Instruct` @ `c03e6d358207e414f1eca0bb1891e29f1db0e242`

Gate acceptance criteria are unchanged.

## v1.1 history — preserved

The v1.1 benchmark and all A4/A5 evidence remain immutable audit history. Human review found the Math-specialist strict-interface zero row to be dominated by output-interface incompatibility rather than valid capability-zero evidence.

Durable review:

`gates/gate-a-specialization/reviews/a5-interface-confounder-human-review.md`

A6 remains inactive.

## A5R1 v1.2.0 — frozen, NOT approved

Agent freeze commit reviewed:

`f4a808cde0e76860408011b1a1c69f38665d7b29`

Frozen artifacts remain preserved under:

`experiments/gate-a/benchmark-v1.2.0/`

Human review:

`gates/gate-a-specialization/reviews/a5r1-v1.2-human-review.md`

Decision: **CHANGES REQUIRED**.

### Accepted v1.2.0 components

The interface-remediation design is accepted and may be reused unchanged in v1.2.1 unless a genuine implementation bug is found:

- semantic task score separated from strict interface-compliance metrics;
- deterministic Math adapter based on expected type/schema only before value comparison;
- conflicting semantic Math candidates rejected;
- AST-only coding extraction selecting the first qualifying Python/unlabeled fenced block defining the requested top-level entrypoint;
- no execution during source extraction;
- strict-interface metrics remain secondary diagnostics;
- 13/13 synthetic adapter tests pass;
- common neutral Qwen envelope, candidates/revisions, BF16/no-quantization policy, context/generation controls, Docker/L40 runtime, coding judge-v2 policy, and Gate thresholds remain unchanged;
- no selected model was executed during A5R1 construction.

### Why v1.2.0 is not approved

The software-coding cases sampled are materially fresh relative to v1.1.

The mathematics set, however, has substantial structural/near-isomorphic reuse of v1.1 case skeletons. Exact strings, constants, and answers differ, but the opening cases closely mirror the already-observed v1.1 sequence (linear equation, fractional-number word problem, ratio counters, arithmetic sequence, divisor count, urn probability, midpoint, and related structures), often primarily changing coefficients or constants.

Because selected-model behavior on those v1.1 structures was already observed before the remediation was designed, exact-string overlap alone is not a sufficient freshness test.

This is a benchmark-construction issue, not an adapter failure and not a Gate result.

## Completed bounded task: v1.2.1 structural-freshness revision — frozen pending human review

Created and froze a new benchmark version:

`gate-a-cross-skill-v1.2.1`

Target root:

`experiments/gate-a/benchmark-v1.2.1/`

Do not edit v1.2.0 in place.

Required revision:

1. preserve/reuse the accepted v1.2 semantic adapter, scoring contract, strict metrics, template, tokenizer/runtime controls, and coding set unless a genuine bug is found;
2. replace all 48 mathematics cases with structurally fresh instances, not simple coefficient/constant substitutions of v1.1 cases;
3. retain 10 foundational / 24 intermediate / 14 advanced Math cases;
4. avoid one-to-one positional mirroring of v1.1 Math cases;
5. broad mathematical skill families may remain comparable, but use different constructions/compositions and freshly computed oracles;
6. recompute token counts and verify every rendered input plus 1024 generation tokens fits 4096;
7. add a freshness audit record covering exact prompt/oracle overlap and explicit structural/near-isomorphic review;
8. do not use selected-model performance to select cases or difficulty labels;
9. execute no General, Math, or Coder checkpoint;
10. stop for human review after v1.2.1 is frozen.

Evidence produced:

- 48 replacement self-authored Math cases with the required 10/24/14
  foundational/intermediate/advanced distribution;
- accepted v1.2.0 coding case set, adapter behavior, semantic scoring, strict
  metrics, template, tokenizer/runtime controls, and judge-v2 policy reused;
- machine-readable/manual freshness audit covering all 48 Math cases;
- exact prompt overlap with v1.1 Math: 0;
- exact normalized expected-oracle overlap with v1.1 Math: 0;
- complete nonempty per-case numeric-tuple overlap: 0; lexical numeric-literal
  union overlap: 22, recorded as ordinary notation rather than structural reuse;
- 13/13 synthetic adapter tests passed;
- exact pinned-tokenizer counts for all 96 cases: maximum 187 input tokens,
  maximum 1211 including the 1024-token generation budget, leaving 2885 tokens
  of context margin.

The remediation design was informed by the observed v1.1 interface confounder.
No selected-model raw response was used as an adapter fixture, no expected
value was used to choose a generated candidate, no v1.2.1 case/oracle/difficulty
label was tuned using selected-model performance, and no selected model was
executed during v1.2.1 construction. v1.2.0 remains unchanged.

Uncertainties: contamination absence is not claimed; common mathematical
structures and standard algorithms may occur in pretraining or educational
material. Difficulty labels remain author labels, not model-calibrated results.

Next bounded action: human review of the frozen v1.2.1 Math structural
freshness, provenance wording, adapter/scoring identity, difficulty balance,
and token/context controls. A5R2 and A6 remain inactive.

### Documentation correction

Do not claim the remediation was created "without observing selected-model outputs." v1.1 outputs were observed and motivated the remediation.

The correct provenance distinction is that selected-model raw outputs were not used as adapter fixtures, expected values were not used to choose extracted candidates, and v1.2.1 cases/oracles/difficulty labels must not be tuned using selected-model performance on those cases.

## A5R2 — inactive

After human approval of v1.2.1, General + Math specialist + Coder specialist will all run the complete benchmark under one unchanged protocol, with no result review between model runs except genuine infrastructure/methodological failure.

## Approved execution substrate retained

- host `ai01`;
- Docker Engine 29.5.3 / `runc`;
- exactly one NVIDIA L40 UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- formal inference: 40 GiB / 16 CPUs;
- A4b package/runtime and deterministic generation policy;
- approved Docker judge-v2 isolation and 2-second watchdog;
- Gate-specific caches independent of Ollama/Open-WebUI.

## Next human checkpoint

Review the frozen `gate-a-cross-skill-v1.2.1` benchmark, especially Math structural freshness, provenance wording, freshness audit, adapter/scoring identity, difficulty balance, and token/context controls. A5R2 and A6 remain inactive until that review is recorded.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
