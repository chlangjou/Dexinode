# Gate B — B1R v1.1.0 Human Review

- Date: 2026-08-10
- Stage: B1R — Structural Freshness and Router Boundary Revision
- Reviewed commit: `48d768799bba4d5f3862359eddeb44cf134a962e`
- Benchmark: `gate-b-orchestration-v1.1.0`
- Router: `router-v2`
- Decision: **CHANGES REQUIRED**
- B2 authorized: **NO**
- Selected-model execution authorized: **NO**

## Accepted remediation work

The two methodological blockers from B1 v1.0.0 are considered successfully remediated:

1. **Structural freshness** — accepted. The v1.1.0 benchmark has zero exact semantic-task overlap with Gate A and includes a case-by-case structural audit reporting 48/48 Math and 48/48 Coding cases as non-positional, non-constant-substitution, non-near-isomorphic constructions. No Gate A per-case result or raw model output was used to select cases.
2. **Router information boundary** — accepted for this bounded Gate. Router-v2 receives `semantic_task` only before the common handoff/output contract is appended and cannot read domain labels, task-family metadata, expected values, evaluator tests, handoff text, or model outputs.

Also accepted:

- v1.0.0/router-v1 preserved unchanged as historical audit evidence;
- 96 cases with 48 Math / 48 Coding and 10/24/14 difficulty split per domain;
- Gate A semantic adapter reused byte-identically; 13/13 synthetic tests PASS;
- router boundary tests 5/5 PASS and frozen benchmark routes 96/96;
- token/context validation: maximum rendered input 124, maximum with generation allowance 1148, context margin 2948;
- frozen execution plan: route decisions persisted before model output, General collected once on all 96 cases, Math specialist only on frozen Math routes, General outputs reused for General routes, and no between-phase result review;
- Gate B numerical acceptance thresholds unchanged;
- no Gate B selected model executed or inspected during B1R.

### Router-v2 scope note

Router-v2 classifies the current benchmark primarily because every Coding semantic task starts with `Implement` while Mathematics tasks do not. This is a benchmark-authoring lexical cue, but it is inside the semantic task rather than the hidden metadata/handoff contract and does not violate the B1R information-boundary requirement. Its 96/96 score must therefore be interpreted only as qualification for this minimal two-domain Gate B benchmark, not evidence of a general-purpose semantic router.

## Blocking finding 1 — Math oracle errors

Independent human recomputation of all 48 Math cases found two incorrect frozen expected values despite `oracle-validation.yaml` reporting 48/48 PASS.

### `math-14`

Prompt: count three-digit positive numbers with distinct digits that are divisible by 5.

The frozen value is `64`, which counts only numbers ending in 5.

Correct count:

- last digit 0: 9 choices for the hundreds digit and 8 remaining choices for the tens digit = 72;
- last digit 5: 8 choices for the hundreds digit and 8 remaining choices for the tens digit = 64;
- total = **136**.

Required correction: `64 -> 136`.

### `math-37`

Prompt: expected value of the maximum of two fair six-sided dice.

For maximum `k`, `P(max=k)=(2k-1)/36`, hence

`E[max] = sum(k(2k-1), k=1..6)/36 = 161/36`.

The frozen `41/9 = 164/36` is incorrect. The validation record itself contains the arithmetic slip `164/36`.

Required correction: `41/9 -> 161/36`.

All other 46 Math expected values were independently recomputed and accepted.

## Blocking finding 2 — Coding semantic-specification defects

The deterministic evaluator fixtures are useful, but human review found cases where the natural-language semantic contract is inconsistent with or underspecifies the frozen expected behavior. These must be corrected before model execution so that a model is not scored against behavior the prompt did not clearly request.

Required clarifications include at least:

- **`code-02`**: prompt says a "six-character string beginning with #" while the accepted valid example `#A0c9FF` is seven characters. Specify `#` followed by exactly six hexadecimal digits / seven characters total.
- **`code-09`**: prompt says "dictionary with integer keys hours, minutes, and seconds" while the intended contract is named keys `hours`, `minutes`, `seconds` with integer values. Correct the wording.
- **`code-21`**: diagonal traversal wording is ambiguous relative to the expected anti-diagonal sequence. Define the traversal/index rule unambiguously.
- **`code-38`**: clarify that the objective is to maximize the **sum of the products of the elements in each contiguous part**.
- **`code-42`**: removing requested character multiplicities is ambiguous when a character occurs multiple times; specify which occurrences are removed (for example, consume requested removals left-to-right) so the expected output is uniquely determined.

B1R2 must perform a complete 48-case prompt/evaluator semantic-contract audit, not only patch the listed examples.

## Required next revision

Create a new immutable benchmark revision `gate-b-orchestration-v1.1.1` rather than modifying v1.1.0 in place.

Required scope:

1. Preserve v1.1.0 and router-v2 unchanged as frozen-not-approved history.
2. Correct `math-14 = 136` and `math-37 = 161/36`.
3. Independently recompute all 48 Math oracles again and record durable evidence.
4. Perform and record a complete 48/48 Coding **prompt-to-evaluator semantic-contract audit**, correcting ambiguous/inconsistent task wording while preserving intended task constructions and evaluator behavior unless a genuine evaluator error is found.
5. Re-run complete Coding evaluator validation after wording corrections.
6. Preserve structural case constructions and freshness status unless a specification correction requires a materially new task; if so, record the structural impact explicitly.
7. Preserve router-v2 semantics unless wording changes require a new immutable router revision; do not tune routing from model outputs.
8. Re-run adapter, router, token/context, manifest hash and static validation.
9. Do not change Gate B numerical acceptance thresholds.
10. Execute or inspect **no selected model**.
11. Stop for human review before B2.

Gate B remains **PENDING**. B2 and all selected-model execution remain unauthorized.
