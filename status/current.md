# Current Research Status

- Updated: 2026-08-10
- Active gate: **Gate B — Orchestration Advantage**
- Gate A final decision: **PASS / CLOSED**
- Gate B final decision: **PENDING HUMAN REVIEW**
- Active stage: **B5 — evidence report complete, pending final human decision**
- B5 recommendation: **FAIL**
- Session handoff: `HANDOFF.md`

## Approved Gate B evidence set

Executable benchmark: `gate-b-orchestration-v1.1.1`

Benchmark root: `experiments/gate-b/benchmark-v1.1.1/`

Router: `experiments/gate-b/router-v2/`

B1R2 human review: `gates/gate-b-orchestration/reviews/b1r2-v1.1.1-human-review.md` — **APPROVED**.

B2 static qualification: `gates/gate-b-orchestration/reviews/b2-static-qualification.md` — **PASS / COMPLETE**.

B3B4 human review: `gates/gate-b-orchestration/reviews/b3b4-v1.1.1-human-review.md` — **APPROVED AS VALID COMPARABLE EXECUTION EVIDENCE**.

B5 report: `gates/gate-b-orchestration/evidence-report.md` — recommendation **FAIL**.

## B3B4 execution

Execution ID:

`gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`

Evidence root:

`experiments/gate-b/runs/gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0/`

Protocol validity:

- 96/96 routes persisted before selected-model output;
- 48 Math-specialist routes, 48 General routes, 0 fallback;
- General generated 96/96 first;
- no General result inspection/scoring/review between phases;
- Math specialist generated exactly the frozen 48 routes;
- composition/scoring occurred only after both phases;
- Qwen2.5-Coder was not executed;
- zero generation failures;
- Coding judge: 48 records, zero infrastructure failures, zero timeouts;
- no result-driven retry/rerouting, performance early stop, or post-output benchmark/protocol change.

The earlier execution ID `gate-b-b3b4-v1.1.1-20260810T013717Z-ai01-gpu0` is preserved as a preflight-only failure caused by the runner reading token-manifest field `id` instead of `case_id`. Formal inference never started and no model output was created; this is non-contaminating invalid/preflight history.

## Results

| Policy | Overall | Mathematics | Coding |
|---|---:|---:|---:|
| General-only | 76/96 = 79.17% | 40/48 = 83.33% | 36/48 = 75.00% |
| Skill-routed | 77/96 = 80.21% | 41/48 = 85.42% | 36/48 = 75.00% |

Paired routed-minus-General:

- overall: **+1.04 pp**, paired-bootstrap 95% CI **[0.00, +3.125] pp**;
- Mathematics: **+2.08 pp**, CI **[0.00, +6.25] pp**;
- Coding: **0.00 pp**;
- router accuracy: **96/96 = 100%**.

The only paired Math improvement was `math-41`: General incorrect, Math specialist correct. There were no reverse Math regressions; the other 47 paired Math correctness outcomes were unchanged.

## Frozen acceptance outcome

Satisfied:

- minimum evidence;
- structural freshness/leakage controls;
- router information boundary;
- resource/execution parity;
- frozen execution sequence;
- router quality;
- Coding non-target protection.

Not satisfied:

- routed overall improvement >= +10 pp;
- overall improvement CI excludes zero;
- routed Mathematics improvement >= +10 pp;
- Mathematics improvement CI excludes zero.

No unresolved material methodology defect requires INCONCLUSIVE. Under the frozen acceptance definition, the valid fresh execution supports a **FAIL recommendation**.

## Interpretation

The router itself was not the bottleneck: it routed the benchmark 100% correctly. The measured specialist advantage did not generalize strongly enough to the structurally fresh Gate B Math distribution. A broad registry entry such as `Mathematics -> Math specialist` therefore appears too coarse for reliable expected-utility routing.

This does not invalidate Gate A or the broader Dexinode thesis. Gate A established that same-size specialization can exist; Gate B shows that the advantage can be strongly distribution-sensitive and must be validated at finer capability granularity and across multiple independent panels.

## Current authorization

**No additional Gate B selected-model execution is required or authorized for the current v1 evidence set.**

The next action is the final human Gate B choice: **PASS / FAIL / INCONCLUSIVE**. The repository evidence recommendation is **FAIL**.
