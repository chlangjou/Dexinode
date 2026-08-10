# Current Research Status

- Updated: 2026-08-10
- Active gate: **Gate B — Orchestration Advantage**
- Gate A final decision: **PASS / CLOSED**
- Gate B final decision: **PENDING HUMAN REVIEW**
- Active stage: **B3B4 — comparable policy execution**
- Session handoff: `HANDOFF.md`

## Gate B pre-execution state

Final executable benchmark:

`gate-b-orchestration-v1.1.1`

Benchmark root:

`experiments/gate-b/benchmark-v1.1.1/`

Router:

`experiments/gate-b/router-v2/`

B1R2 human review:

`gates/gate-b-orchestration/reviews/b1r2-v1.1.1-human-review.md`

Decision: **APPROVED**.

B2 static qualification:

`gates/gate-b-orchestration/reviews/b2-static-qualification.md`

Decision: **PASS / COMPLETE**.

Accepted static evidence:

- 96 cases: 48 Math + 48 Coding; 10 foundational / 24 intermediate / 14 advanced per domain;
- structural freshness and semantic-task-only router boundary accepted;
- Math oracle validation 48/48 PASS, including corrected `math-14 = 136` and `math-37 = 161/36`;
- Coding evaluator validation 48/48 PASS;
- Coding prompt-to-evaluator semantic-contract audit 48/48 PASS;
- semantic adapter 13/13 tests PASS and behavior unchanged;
- router-v2 5/5 tests PASS and target benchmark routes 96/96;
- token/context 96/96 PASS; max input 124; max with generation 1148; margin 2948;
- model revisions, BF16/no-quantization controls, scoring, protocol, resources, and numerical acceptance thresholds unchanged;
- no Gate B selected model was executed before B3B4 authorization.

A stale informational `case_file` label inside the v1.1.1 case YAML still names v1.1.0. The actual v1.1.1 path/manifest/hash/runtime identity is correct; this is recorded as non-material metadata hygiene and does not affect execution or scoring.

## Active B3B4 execution contract

Selected-model execution is **authorized only under this frozen sequence**:

1. Compute and persist all 96 router-v2 decisions from `semantic_task` before the first selected-model output.
2. Run General `Qwen/Qwen2.5-7B-Instruct` revision `a09a35458c702b33eeacc393d103063234e8bc28` once on all 96 cases in frozen order.
3. Do **not** inspect, score, summarize, or human-review General results before specialist evidence collection completes.
4. Run Math specialist `Qwen/Qwen2.5-Math-7B-Instruct` revision `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d` only on frozen `mathematics_specialist` routes.
5. Reuse preserved General outputs for General/fallback routes when composing the routed policy.
6. Only after both evidence phases are complete, compose and score General-only and skill-routed rows and compute frozen paired metrics.
7. No Coder checkpoint, retry, voting, ensemble, second-model fallback, result-driven rerouting, benchmark/protocol patch, performance early stop, or acceptance-threshold change is allowed.
8. A genuine infrastructure/methodological failure may stop execution; preserve all partial/invalid evidence and do not tune from observed results.
9. After comparable evidence is complete, commit and stop for human review before B5/final Gate B decision.

Primary thresholds remain unchanged:

- routed overall ≥ General +10 pp;
- paired-bootstrap 95% CI for overall delta excludes zero;
- routed Math ≥ General Math +10 pp with CI excluding zero;
- routed Coding degradation no worse than 5 pp;
- router domain accuracy ≥95%.

Gate B final PASS/FAIL remains a human decision.
