# Gate B orchestration benchmark v1.1.1

`gate-b-orchestration-v1.1.1` is the B1R2 oracle-correction and semantic-contract remediation revision. It supersedes v1.1.0 for any future Gate B execution only after human review. v1.1.0/router-v2 and v1.0.0/router-v1 remain preserved, unchanged frozen-not-approved audit artifacts.

The 96-case design is carried forward unchanged: 48 mathematics and 48 software-coding cases, with 10 foundational, 24 intermediate, and 14 advanced cases per domain. Structural freshness, semantic-task-only routing, the neutral Qwen role-delimiter template, adapter behavior, scoring contract, execution sequence, candidate revisions, generation controls, and Gate B thresholds are unchanged.

This revision corrects the two reviewed Math oracle defects: `math-14 = 136` and `math-37 = 161/36`. All 48 Math values were independently recomputed again in [oracle-validation.yaml](oracle-validation.yaml). The 48/48 Coding specifications were audited against their evaluators in [semantic-contract-audit.yaml](semantic-contract-audit.yaml). Wording was clarified where needed without changing evaluator behavior or task constructions; no selected-model output, performance, or Gate A per-case evidence was used.

The router boundary remains explicit. `router-v2` receives only `case.semantic_task` before the common handoff contract is appended. It cannot see domain labels, task-family metadata, expected values, evaluator tests, handoff text, or model output. Its benchmark-specific static qualification remains 96/96, with the scope limitation recorded in the manifest and inherited freshness audit.

Math primary scoring uses the accepted deterministic semantic adapter. Coding extraction remains AST-only, selecting the first qualifying fenced implementation block, with full-response Python fallback only when there are no fenced blocks. Generated source is executed only by the approved judge-v2 sandbox. Strict interface compliance remains secondary.

Static evidence:

- [oracle-validation.yaml](oracle-validation.yaml): 48/48 Math expected values independently validated.
- [semantic-contract-audit.yaml](semantic-contract-audit.yaml): 48/48 Coding prompt-to-evaluator contracts PASS.
- [evaluator-validation.yaml](evaluator-validation.yaml): 48/48 Coding evaluator fixtures PASS.
- [adapter/test_adapter.py](adapter/test_adapter.py): 13/13 synthetic adapter tests pass.
- [router-v2/test_router.py](../router-v2/test_router.py): 5/5 router tests pass and benchmark routing is 96/96.
- [token_counts.yaml](token_counts.yaml): exact pinned-tokenizer counts are recorded for all 96 cases; the maximum and context margin are in the manifest.

No Gate B General, Math, or Coder checkpoint was executed or inspected while constructing v1.1.1. Gate B remains `PENDING HUMAN REVIEW`; B2 execution is not authorized by this commit.
