# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: **PENDING HUMAN REVIEW**
- Session handoff: `HANDOFF.md`
- Active stage: **A6 — evidence report complete pending final human decision**

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

## Frozen candidate set

- General: `Qwen/Qwen2.5-7B-Instruct` @ `a09a35458c702b33eeacc393d103063234e8bc28`
- Math specialist: `Qwen/Qwen2.5-Math-7B-Instruct` @ `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`
- Coder specialist: `Qwen/Qwen2.5-Coder-7B-Instruct` @ `c03e6d358207e414f1eca0bb1891e29f1db0e242`

Gate acceptance criteria remain unchanged.

## A5R1 — approved

Approved benchmark: `gate-a-cross-skill-v1.2.2`

- reviewed commit: `cdd691472aa5f08c3284e881c1048956a7d52987`;
- human review: `gates/gate-a-specialization/reviews/a5r1-v1.2.2-human-review.md`;
- 48/48 Math oracle validation PASS;
- `math-23 = 1/3`, `math-30 = 240`, `math-37 = 9/95`;
- coding set byte-identical to accepted v1.2 predecessor;
- semantic adapter/scoring behavior unchanged;
- synthetic adapter tests 13/13 PASS;
- no selected model executed during benchmark construction.

## A5R2 — approved

Reviewed commit: `6168558b74fca06e1ef80f41b86cc997915c41b7`

Human review:

`gates/gate-a-specialization/reviews/a5r2-v1.2.2-human-review.md`

Decision: **APPROVED**. A6 authorized.

Accepted capability matrix:

| Role | Overall | Math | Coding |
|---|---:|---:|---:|
| General baseline | 68/96 (70.83%) | 30/48 (62.50%) | 38/48 (79.17%) |
| Math specialist | 64/96 (66.67%) | 44/48 (91.67%) | 20/48 (41.67%) |
| Coder specialist | 69/96 (71.88%) | 36/48 (75.00%) | 33/48 (68.75%) |

Execution validity accepted:

- all three rows generated 96/96 responses with zero generation failures;
- frozen order General → Math → Coder; no result inspection between rows;
- frozen benchmark/template/adapter/scoring/candidate revisions/acceptance criteria unchanged after execution began;
- four failed attempts stopped in General preflight before model load/output and remain preserved;
- accepted coding judge rows had zero infrastructure failures; General and Math each had one frozen-policy 2-second timeout;
- post-execution scorer edit affected elapsed-time receipt metadata only; rows were rescored from preserved raw outputs without model reruns.

Non-blocking metadata issue: `load_elapsed_seconds` in the inference receipt spans model load plus generation and must not be interpreted as model-load latency.

## A6 — complete pending final human decision

Evidence report:

`gates/gate-a-specialization/evidence-report.md`

Machine-readable summary:

`experiments/gate-a/a6-evidence-summary.yaml`

Recommendation: **PASS**.

Key frozen-criteria findings:

- minimum evidence: satisfied;
- candidate comparability: satisfied;
- Math specialist primary-domain delta: **+29.17 pp**, paired-bootstrap 95% CI **[+16.67, +41.67] pp** — passes ≥10 pp and excludes zero;
- Math specialist non-primary coding delta: **−37.50 pp**, CI **[−52.08, −22.92] pp** — strong domain-specific tradeoff;
- Coder specialist primary coding delta: **−10.42 pp**, CI **[−22.92, +2.08] pp** — does not demonstrate claimed coding advantage;
- specialization signal: satisfied by the Math specialist's concentrated profile;
- unresolved material methodological defect: none identified;
- strong two-specialist pass preference: **not satisfied**.

This is therefore a **single-specialist PASS recommendation, not a strong two-specialist pass**.

## Next human checkpoint

The human owner must now assign the final Gate A decision: PASS, FAIL, or INCONCLUSIVE.

Gate B remains inactive until an explicit human Gate A PASS decision is recorded. No additional model execution is required for the current Gate A evidence set.
