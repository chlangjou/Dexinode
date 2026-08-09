# Gate B orchestration benchmark v1.1.0

`gate-b-orchestration-v1.1.0` is the B1R structural-freshness and router-boundary revision. It supersedes v1.0.0 for any future Gate B execution only after human review. v1.0.0 and router-v1 remain preserved audit artifacts; v1.0.0 is useful evidence of the original prompt-only protocol, while its structural freshness and router-boundary findings were not accepted for execution.

This freeze contains 96 self-authored cases: 48 mathematics and 48 software-coding. Each domain has 10 foundational, 24 intermediate, and 14 advanced cases. The Math and Coding instances are fresh relative to the Gate A definitions; the case-by-case structural record is in [freshness-audit.yaml](freshness-audit.yaml). No selected-model result, raw response, or per-case win/loss record was used to author, select, or tune a case.

The router boundary is explicit. `router-v2` receives only `case.semantic_task` before the common handoff contract is appended. It cannot see domain labels, task-family metadata, expected values, evaluator tests, handoff text, or model output. It deterministically routes the current semantic task inventory 96/96 in synthetic static tests. The common neutral Qwen role-delimiter template and pinned tokenizer policy are unchanged.

Math primary scoring uses the accepted deterministic semantic adapter: expected type/schema may guide extraction, but expected values never select a candidate; canonical and permitted boxed final forms are normalized, and conflicting candidates are rejected. Coding extraction remains AST-only, first qualifying fenced implementation block, with full-response Python fallback only when there are no fenced blocks. Generated source is executed only by the approved judge-v2 sandbox. Strict interface compliance is recorded separately and is not primary accuracy.

The execution protocol is frozen before model work: General runs once on all 96 cases; route decisions are persisted before model output; the Mathematics specialist runs only on frozen mathematics routes; General outputs are reused for General routes; no between-phase result review, retries, or result-driven rerouting is permitted. Controls remain BF16, no quantization, 4096 total context, 1024 maximum new tokens, deterministic generation, external tools disabled, and the Gate B acceptance thresholds unchanged.

Static evidence:

- [oracle-validation.yaml](oracle-validation.yaml): 48/48 Math expected values independently validated with exact arithmetic/enumeration.
- [evaluator-validation.yaml](evaluator-validation.yaml): 48/48 Coding evaluator fixtures independently audited.
- [adapter/test_adapter.py](adapter/test_adapter.py): 13/13 synthetic adapter tests pass.
- [router-v2/test_router.py](../router-v2/test_router.py): 5/5 router boundary tests pass and benchmark routing is 96/96.
- [token_counts.yaml](token_counts.yaml): maximum rendered input is 124 tokens; maximum input plus 1024 generation is 1148, leaving a 2948-token context margin.

No Gate B selected model was executed while constructing this benchmark. Gate B remains `PENDING HUMAN REVIEW`; B2 execution is not authorized by this commit.
