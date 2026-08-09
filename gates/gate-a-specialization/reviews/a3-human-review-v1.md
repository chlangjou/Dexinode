# A3 Human Review — Benchmark v1.0.0

- Date: 2026-08-09
- Reviewer role: Human decision owner
- Reviewed commit: `6b8d3c0854cc1770e459ec9454ee7d78afd049ce`
- Benchmark: `gate-a-cross-skill-v1.0.0`
- Decision: **CHANGES REQUIRED**
- Gate A decision: **PENDING**

## What is approved

The A3 execution process itself is accepted:

- the benchmark was authored and frozen before any selected model was executed;
- all three models are assigned the same complete cross-skill benchmark;
- mathematics and software-coding are both represented;
- scoring is deterministic and does not use an LLM judge;
- the neutral Qwen prompt/template policy and 4,096-token common context control are respected;
- provenance and contamination limitations are explicitly recorded;
- no candidate model output was inspected while constructing the benchmark.

The frozen v1.0.0 artifacts must remain unchanged as an audit record.

## Required methodological revision before A4

### 1. Statistical power / granularity

The current benchmark has 16 binary cases per domain. Each case therefore changes domain accuracy by 6.25 percentage points. Gate A's predefined performance signal requires at least 10 percentage points of primary-domain improvement and a 95% bootstrap improvement interval excluding zero.

With only 16 cases, a small but threshold-exceeding difference can remain statistically underpowered. The revised benchmark should target **at least 48 cases per domain** (96 total), unless another size is analytically justified before execution.

### 2. Ceiling-effect risk

The mathematics v1.0.0 set is dominated by foundational/intermediate short-answer problems. The coding set similarly contains many common foundational/intermediate implementation tasks. The revised benchmark must include a planned difficulty distribution with meaningful intermediate and advanced cases in both domains while retaining deterministic scoring and the approved context envelope.

Recommended target distribution per domain:

- 20–25% foundational;
- 45–55% intermediate;
- 25–30% advanced.

Difficulty labels remain pre-execution design labels and must not be calibrated using candidate-model results.

### 3. Coding execution isolation

Before A4/A5, the runner must implement an actual bounded isolation mechanism for model-generated Python. The benchmark/review record must treat isolation as a required preflight condition for coding scores to be valid.

## Revision rules

- Do not modify the frozen v1.0.0 files in place.
- Create a new benchmark version that explicitly supersedes v1.0.0 for Gate A execution.
- Preserve v1.0.0 and this review record.
- Do not execute General, Math, or Coder models while revising the benchmark.
- Do not inspect candidate outputs or tune cases from selected-model performance.
- Gate acceptance criteria remain unchanged.
- Keep all cases inside the approved shared template and 4,096-token total context policy.

## Human checkpoint

A3 remains active. A4 is not authorized until the revised benchmark is reviewed.