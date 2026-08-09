# Gate A Cross-Skill Benchmark v1.2.0

This is the fresh interface-remediated benchmark for Gate A specialist
capability measurement. It supersedes `gate-a-cross-skill-v1.1.0` for future
Gate A capability measurement, while v1.1.0 and every associated A4/A5 run
remain preserved as immutable audit history. v1.1.0 remains useful strict-
interface/interoperability evidence. This version uses fresh case instances
because the interface remediation was designed after observing v1.1 outputs.

The benchmark has 96 cases in frozen order: 48 mathematics cases followed by
48 software-coding cases. Each domain has 10 foundational, 24 intermediate,
and 14 advanced cases. Every future model runs all 96 cases with equal case
weights; no selected model was executed during construction or validation of
this version.

## Common controls

The selected candidates, exact revisions, BF16/no-quantization policy,
external-tools-disabled policy, 4096-token total context envelope,
`max_new_tokens: 1024`, pinned byte-identical Qwen tokenizer, and neutral Qwen
role-delimiter envelope are unchanged. Repository/model-specific chat
templates are ignored. The same semantic system message is rendered for every
model and every case.

Gate acceptance thresholds are unchanged. This benchmark does not authorize
A5R2 or A6; it is frozen pending human review.

## Semantic handoff contract

Primary scoring measures task semantics. Strict interface compliance is
recorded separately and cannot erase a deterministically recoverable answer.

For mathematics, the adapter uses only the expected type/schema, never the
expected value, while extracting candidates. It accepts one canonical
`ANSWER:` integer, reduced rational, or strict JSON structured object, or one
conventional boxed integer, boxed fraction, or frozen-key-order boxed tuple.
Integer and rational candidates are normalized deterministically; structured
objects require exactly the frozen integer keys and canonicalize by key order.
Conflicting multiple valid final candidates are rejected.

For coding, the adapter scans Python or unlabeled fenced blocks in response
order and parses candidates with Python AST only. It selects the first block
with a top-level definition of the requested entrypoint, ignores prose and
later example/output blocks, and permits complete-response Python fallback
only when no fenced candidate exists and the full response defines the
entrypoint. Source execution remains exclusively inside the approved judge-v2
sandbox.

The separate strict metrics are `math_canonical_answer_contract` and
`coding_single_clean_source_block`; neither is a primary Gate A score.

## Validation and limitations

The adapter is validated only with newly authored synthetic fixtures. The
committed tests cover canonical and boxed math forms, boxed LaTeX fractions,
structured tuples, ambiguity and malformed rejection, surrounding prose,
example blocks, missing entrypoints, first-candidate behavior, full-response
fallback, and non-Python fences. All tests must pass before the freeze commit.

Cases and deterministic oracles are self-authored and were created before any
selected-model execution. No external dataset or public answer key was
copied. Contamination absence is not claimed: common mathematical structures
and standard algorithms may resemble pretraining or educational material.
Difficulty labels are author labels, not model-calibrated results. Later runs
must preserve raw responses and must not expose evaluator tests as model input.

The exact rendered token count for every case is in `token_counts.yaml`, using
the pinned Qwen2 tokenizer asset already established in A2. Every case obeys
`rendered_input_tokens + 1024 <= 4096`.

Gate decision: PENDING HUMAN REVIEW.
