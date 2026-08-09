# Gate A Cross-Skill Benchmark v1.0.0

This directory contains the frozen A3 benchmark for the approved Qwen2.5
candidate set.

- 16 mathematics cases and 16 software-coding cases;
- every selected model receives all 32 cases;
- one neutral Qwen role-delimiter template;
- 4,096-token total context ceiling, including up to 1,024 generated tokens;
- deterministic mathematics parsing and Python unit-test scoring;
- no external tools, network, or filesystem access during later scoring.

The cases and scoring rules were authored before any candidate checkpoint was
executed. The benchmark records contamination risks but does not claim that
self-authored cases are uncontaminated. After the freeze commit, case text,
ordering, template, and scoring rules must not be changed in response to model
results. Any methodological correction requires a new benchmark version with
the prior version preserved.

The benchmark is frozen for human review. Gate decision: PENDING HUMAN REVIEW.
