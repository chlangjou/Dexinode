# Gate A Cross-Skill Benchmark v1.1.0

This directory contains the superseding A3 benchmark requested after human
review of v1.0.0. The frozen v1.0.0 artifacts remain unchanged in
`experiments/gate-a/benchmark/`.

The revised benchmark contains 48 mathematics cases and 48 software-coding
cases. Each domain has 10 foundational, 24 intermediate, and 14 advanced
cases (20.8%, 50.0%, and 29.2%). Every approved model receives all 96 cases;
the two specialist checkpoints are evaluated on both their primary and
non-primary domains.

The revision addresses ceiling-effect risk by replacing the 16-case domains
with broader multi-step coverage, adding advanced cases, adding adversarial
edge conditions to coding tests, and requiring difficulty-stratified reporting.
Cases and deterministic scoring were authored before any selected checkpoint
was executed. No candidate weights, candidate outputs, or comparative results
are present in this version.

The approved neutral Qwen role-delimiter template is preserved byte-for-byte
from v1.0.0. The same semantic system message, case prompt, no-tools policy,
BF16/no-quantization policy, and `max_new_tokens: 1024` policy remain in force.
Every rendered input must satisfy `rendered_input_tokens + 1024 <= 4096`.

Coding evaluation is fail-closed behind the mandatory actual bounded-isolation
preflight in `execution/coding_isolation_preflight.yaml`. A later coding run
must preserve a passing preflight receipt from the exact host/runtime/policy;
the runner must not score coding cases when the receipt is absent or failed.

This benchmark is frozen for human review. Gate decision: PENDING HUMAN REVIEW.
