# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A5R1 — Interface Protocol and Fresh Benchmark Freeze

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

## Selected models remain unchanged

- General: `Qwen/Qwen2.5-7B-Instruct` @ `a09a35458c702b33eeacc393d103063234e8bc28`
- Math specialist: `Qwen/Qwen2.5-Math-7B-Instruct` @ `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`
- Coder specialist: `Qwen/Qwen2.5-Coder-7B-Instruct` @ `c03e6d358207e414f1eca0bb1891e29f1db0e242`

Gate acceptance criteria are unchanged.

## v1.1 execution history — preserved

The frozen `gate-a-cross-skill-v1.1.0` benchmark and all A4/A5 run evidence remain immutable audit history.

Strict v1.1 scores were:

| model | mathematics | software coding | overall |
| --- | ---: | ---: | ---: |
| General | 10/48 (20.83%) | 36/48 (75.00%) | 46/96 (47.92%) |
| Math specialist | 0/48 (0%) | 0/48 (0%) | 0/96 (0%) |
| Coder specialist | 12/48 (25.00%) | 39/48 (81.25%) | 51/96 (53.13%) |

These remain valid measurements of behavior under the exact v1.1 strict wire/output contract.

## A5 human review — interface confounder confirmed

Durable review:

`gates/gate-a-specialization/reviews/a5-interface-confounder-human-review.md`

Reviewed A5 commit:

`c95da721f0e55e0bda1c55f3dee9f4c95c814034`

The complete v1.1 three-row matrix is **not accepted as a task-capability matrix**.

The Math specialist's zero row is dominated by output-interface incompatibility:

- reviewed mathematics responses often solve the task correctly but end in conventional `\\boxed{...}` mathematics rather than the required `ANSWER:` marker;
- for example `math-01` derives 6, `math-02` derives 28, `math-03` derives 56, `math-04` derives -40, and `math-05` derives 24, yet v1.1 scores them zero because the exact `ANSWER:` marker is absent;
- Math-specialist mathematics records are rejected by the strict answer-marker rule rather than demonstrating zero mathematical competence;
- coding responses similarly often include a plausible implementation plus prose/examples or additional code blocks, causing strict source extraction rejection such as `multiple_code_blocks`.

A2 had already identified the Math checkpoint's chat-template / boxed-answer behavior as a material confounder. The A5 evidence demonstrates that a shared neutral role-delimiter template alone was insufficient to remove the behavioral interface difference.

Therefore:

- do not interpret Math specialist 0/96 as capability zero;
- do not authorize A6 from the v1.1 matrix;
- do not patch v1.1 scoring in place;
- do not rescore only the Math specialist with relaxed rules;
- do not switch only the Math specialist to its native chat template.

## Research implication

The experiment exposed a Dexinode-relevant design fact: specialist checkpoints can require different behavioral output handling even within a shared family/tokenizer lineage. A skill network should distinguish **task competence** from **wire/handoff-format compliance** and provide an explicit deterministic normalization contract.

This is useful architectural evidence, but it is not a Gate A PASS.

## Completed bounded task: A5R1 — frozen pending human review

Human-approved remediation contract:

`gates/gate-a-specialization/execution/a5r-interface-remediation.yaml`

Created and froze `gate-a-cross-skill-v1.2.0` before any further selected-model
execution. Durable artifacts are under
`experiments/gate-a/benchmark-v1.2.0/`.

A5R1 requirements:

1. author **fresh** 48 mathematics + 48 software-coding case instances;
2. retain the 10 foundational / 24 intermediate / 14 advanced distribution per domain;
3. do not reuse v1.1 case text or exact constants/oracles;
4. retain the same candidates, revisions, BF16/no-quantization policy, common 4096-token envelope, neutral Qwen role-delimiter chat envelope, approved Docker/L40/runtime policy, and Gate acceptance thresholds;
5. define one common model-agnostic tolerant handoff contract for all three models;
6. primary scoring must measure deterministic task semantics while strict interface compliance is reported separately;
7. mathematics normalization may accept the frozen canonical `ANSWER:` grammar or one frozen conventional boxed-final-answer grammar, with ambiguity rejected and no expected-value-guided extraction;
8. coding normalization must deterministically identify the first Python fenced block whose AST defines the required entrypoint, ignoring surrounding prose/non-selected example blocks; source execution remains only in judge-v2;
9. adapter behavior must be frozen and validated only on committed synthetic fixtures;
10. record provenance, contamination limitations, token counts, scoring, adapter tests, and manifest;
11. execute **no General, Math, or Coder model** during A5R1;
12. stop for human review after v1.2 is frozen.

Evidence produced:

- 96 fresh self-authored cases: 48 mathematics and 48 software coding, each
  with the required 10/24/14 difficulty distribution and frozen case order;
- common neutral Qwen role-delimiter template with unchanged candidate set,
  revisions, BF16/no-quantization, no-tools, 4096-token envelope, and
  `max_new_tokens: 1024` controls;
- deterministic math semantic normalizer and coding AST extractor, with
  strict-interface metrics reported separately;
- 13 synthetic adapter tests, all passing;
- exact pinned-tokenizer counts for all 96 cases: maximum 187 input tokens,
  maximum 1211 including the 1024-token generation budget;
- manifest, scoring, provenance, contamination limitations, and file hashes.

No General, Math, or Coder checkpoint was executed or inspected. v1.1.0 and
all A4/A5 runs remain unchanged and preserved as historical evidence.

Uncertainties:

- contamination absence is not claimed because common mathematical structures
  and standard algorithms can occur in pretraining or educational material;
- author difficulty labels are not model-calibrated;
- the v1.2 coding-isolation receipt remains a later execution prerequisite,
  inherited from the approved judge-v2 policy.

Next bounded action: human review of the frozen v1.2 benchmark and handoff
contract. A5R2 may begin only after that review; A6 remains inactive.

Human review required: confirm fresh-case provenance, semantic normalization,
strict metrics, synthetic adapter tests, token/context validation, and that
Gate acceptance thresholds remain unchanged.

## Later A5R2 — not yet authorized

After human approval of v1.2, General + Math specialist + Coder specialist will all run the complete fresh 96-case benchmark again under one unchanged protocol. No v1.1 score may be substituted into that matrix, and there will be no human result review between the three model runs except for genuine infrastructure/methodological failure.

## Approved execution substrate retained for future runs

- host `ai01`;
- Docker Engine 29.5.3 / `runc`;
- exactly one NVIDIA L40 UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- formal inference: 40 GiB / 16 CPUs;
- A4b package/runtime and deterministic generation policy;
- approved Docker judge-v2 isolation and 2-second watchdog;
- Gate-specific caches independent of Ollama/Open-WebUI.

## Next human checkpoint

Review the frozen v1.2 benchmark, common output/handoff contract, deterministic semantic adapter, synthetic tests, provenance, difficulty balance, and token/context controls. A5R2 and A6 remain inactive until that review is recorded.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
