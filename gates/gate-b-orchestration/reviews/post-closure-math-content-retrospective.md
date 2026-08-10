# Gate B Post-Closure Mathematics Content Retrospective

Date: 2026-08-10
Status: **POST-CLOSURE / NON-RERUN RETROSPECTIVE**
Gate B final decision remains: **FAIL / CLOSED**

## Scope

This retrospective was performed after the final human Gate B decision using only preserved Gate B v1.1.1 prompts, frozen scoring artifacts, per-case records and raw responses. No model was rerun and no frozen benchmark artifact was patched in place.

The purpose is to distinguish mathematical solution competence from answer-contract/extraction behavior and to document one additional oracle defect discovered after closure.

## Finding 1 — `math-23` oracle is incorrect

Frozen prompt:

> A condition affects 2 percent of a population. A test detects it 95 percent of the time and has a 3 percent false-positive rate. Given a positive result, find the probability the person has the condition.

Frozen oracle: `19/48`.

Correct exact posterior:

- true-positive mass = `(2/100)*(95/100) = 19/1000 = 95/5000`;
- false-positive mass = `(98/100)*(3/100) = 147/5000`;
- posterior = `95/(95+147) = 95/242 ~= 0.392562`.

Therefore the frozen `19/48` oracle is an arithmetic error.

Both preserved model responses independently computed the denominator `0.0484` and a posterior near `0.392`, i.e. the correct numerical answer. The frozen rational extractor rejected both decimal-form answers, so both received score 0. Correcting only the oracle while leaving the frozen extractor unchanged would not change the paired score vector.

This defect is material to absolute benchmark correctness but non-differential for the observed General-vs-routed delta.

## Finding 2 — several shared zero scores are answer-contract false negatives

Human inspection of preserved raw responses shows that both General and Math specialist solved the underlying mathematics correctly on:

- `math-11` complex multiplication: both obtain real=11, imaginary=10;
- `math-12` median/MAD: both obtain median=12, MAD=6;
- `math-17` absolute-value roots: both obtain -3 and 6.

The frozen structured-object adapter rejected these because the final representation did not match its accepted structured schema/tuple syntax. These are common-mode scoring false negatives, not mathematical-content failures.

## Finding 3 — the only frozen paired Math improvement is representation, not content

`math-41` was the sole case whose frozen semantic score changed from General 0 to Math specialist 1.

Both responses solve the expected-value problem correctly:

- General concludes `0.75`;
- Math specialist concludes `3/4`.

The frozen `semantic_rational` extractor accepts the specialist's exact rational form but rejects General's decimal form. Therefore the observed +1/48 Mathematics advantage is an answer-representation/extraction effect rather than a difference in mathematical solution correctness.

## Finding 4 — shared genuine failures are largely arithmetic/self-check failures

Two preserved cases show both checkpoints selecting an appropriate solution method but failing basic arithmetic verification:

- `math-16`: both apply inclusion-exclusion correctly in form, but General miscomputes the arithmetic to 22 and Math specialist miscomputes it to 19; correct answer is 21.
- `math-32`: both enumerate the nine products correctly, then General sums them as 50 and Math specialist as 57; the correct sum is 49, so the expected value is 49/9.

These are consistent with a missing or weak final verification/self-review step rather than missing domain-method knowledge.

## Finding 5 — `math-36` wording is interpretation-sensitive

The prompt says "Independent fair trials" but does not explicitly state success probability `p=1/2`. Both checkpoints return the correct general geometric form `(1-p)^3 p` rather than substituting `p=1/2` to obtain `1/16`.

The benchmark intended "fair" to mean equal-probability binary success/failure, but the wording is weaker than an explicit `p=1/2` contract. This is common-mode and does not change the paired comparison.

## Retrospective content-level comparison

Among the eight Mathematics cases scored incorrect for General under the frozen adapter:

- content-correct for both: `math-11`, `math-12`, `math-17`, `math-23`, `math-41`;
- content-incorrect for both: `math-16`, `math-32`;
- wording-sensitive/common outcome: `math-36`.

Thus the only frozen paired scoring advantage (`math-41`) disappears under a human mathematical-content reading. The two checkpoints have the same content-level correctness classification across the inspected Gate B Mathematics panel.

This is a retrospective diagnostic, not a replacement official score. It strengthens rather than weakens the final Gate B FAIL conclusion: the broad `Mathematics -> Math specialist` route did not demonstrate a substantive held-out mathematical-content advantage.

## Implication for future Dexinode evaluation

Future gates should explicitly separate:

1. task/specification comprehension;
2. domain-method selection;
3. derivation/computation correctness;
4. final verification/self-review;
5. answer representation / handoff-contract compliance.

A single end-to-end exact-answer score collapses these dimensions and can falsely attribute a formatting advantage to domain competence or hide mathematically correct responses behind interface mismatch.

## Relationship to the General-meta-capability hypothesis

The retrospective is consistent with, but does not prove, the hypothesis that a General model may retain stronger broad comprehension/review capabilities while a specialist focuses capacity or training signal on domain solution patterns. In the current Gate B data, however, neither checkpoint clearly dominates self-review: both make arithmetic verification errors, and most originally shared failures are common-mode contract/extraction effects.

A future causal test must manipulate or independently score comprehension, solution, verification and formatting rather than infer them from final exact-answer accuracy.
