# A5 specialist cross-evaluation summary

Status: complete, pending human review. This is a descriptive handoff only;
it does not calculate a new acceptance threshold or assign a Gate decision.

All three rows use the frozen `gate-a-cross-skill-v1.1.0` benchmark and the
same neutral template, deterministic generation policy, BF16/no-quantization
runtime, selected L40, and approved coding judge-v2 policy.

| model | mathematics | software-coding | overall |
| --- | ---: | ---: | ---: |
| General baseline | 10/48 (20.8333%) | 36/48 (75.0000%) | 46/96 (47.9167%) |
| Math specialist | 0/48 (0.0000%) | 0/48 (0.0000%) | 0/96 (0.0000%) |
| Coder specialist | 12/48 (25.0000%) | 39/48 (81.2500%) | 51/96 (53.1250%) |

Descriptive specialist-minus-General deltas:

- Math specialist: mathematics -20.8333 percentage points; software-coding
  -75.0000 points; overall -47.9167 points.
- Coder specialist: mathematics +4.1667 points; software-coding +6.2500
  points; overall +5.2083 points.

Difficulty-stratified scores:

| model | math foundational / intermediate / advanced | coding foundational / intermediate / advanced |
| --- | --- | --- |
| General baseline | 4/10 · 6/24 · 0/14 | 9/10 · 19/24 · 8/14 |
| Math specialist | 0/10 · 0/24 · 0/14 | 0/10 · 0/24 · 0/14 |
| Coder specialist | 4/10 · 6/24 · 2/14 | 9/10 · 22/24 · 8/14 |

Both specialist runs completed 96/96 generation and scoring records. Neither
run had an infrastructure-invalid case or coding judge timeout. The Math run
sent six extracted coding sources to the judge and rejected 42 responses
before execution under the frozen source-extraction rules; the Coder run sent
all 48 coding sources to the judge.

Run evidence:

- Math: `a5-math-specialist-20260809T092120Z-ai01-gpu0/`
- Coder: `a5-coder-specialist-20260809T092120Z-ai01-gpu0/`
- General reference: `a4-general-baseline-20260809T082430Z-ai01-gpu0/`

Gate A remains `PENDING HUMAN REVIEW`; A6 is not authorized by this summary.
