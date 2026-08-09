# Gate A — Specialist Validation

## Question

Do existing specialist model checkpoints exhibit reproducible, measurable specialization relative to a closely related general-purpose baseline?

## Why this Gate exists

Dexinode's later routing and orchestration hypothesis assumes that different models or skills expose meaningfully different competency surfaces. Gate A tests that assumption before adding orchestration complexity.

Gate A does **not** test whether orchestration is better than one model. It tests whether measurable specialization exists strongly enough to make routing worth testing later.

## Scope

Gate A includes:

- discovery of comparable existing specialist checkpoints;
- verification of lineage, license, and runtime feasibility;
- construction of a cross-skill benchmark;
- a frozen general-purpose baseline;
- cross-evaluation of all eligible models on the same benchmark;
- reproducible metrics and uncertainty estimates;
- evidence and confounder reporting.

Gate A excludes:

- fine-tuning, training, model merging, or distillation;
- multi-agent orchestration;
- skill routing;
- remote node transport;
- registry, reputation, settlement, federation, or adversarial-node behavior.

## Execution stages

### A1 — Candidate Scout

Find candidate sets that make a fair specialization test possible.

Target set:

- at least 1 general-purpose baseline;
- at least 2 specialist checkpoints;
- at least 2 distinguishable skill domains;
- same family/generation preferred;
- similar parameter scale preferred;
- public availability and usable license;
- feasible on available experiment hardware.

Output: `experiments/gate-a/candidates.yaml`.

A1 ends with human review. Do not automatically continue into formal benchmark execution.

### A2 — Candidate Eligibility

After human approval, verify exact revisions, lineage, parameter scale, tokenizer/chat-template compatibility, license, runtime requirements, and confounders.

A candidate may be rejected without changing the Gate result.

### A3 — Benchmark Construction and Freeze

Construct a benchmark covering every selected specialist's claimed primary domain and at least one non-primary domain.

The benchmark must produce a cross-skill competency matrix, not isolated specialist-only scores.

Before execution:

- define cases and scoring rules;
- validate deterministic scoring where possible;
- record benchmark manifest and version;
- freeze benchmark content in Git.

After freeze, model results may not be used to tune cases or thresholds.

### A4 — General Baseline

Run the general model first under the frozen benchmark and fixed inference policy.

Record complete reproducibility metadata and per-case results.

### A5 — Specialist Cross-Evaluation

Run every specialist over the same complete benchmark, including domains outside its claimed specialization.

Use the same inference policy unless the checkpoint requires a documented model-specific template. Any exception is an experimental variable and must be recorded.

### A6 — Evidence Report

Produce a report containing:

- candidate set and lineage;
- benchmark version;
- environment and inference policy;
- per-model metrics;
- cross-skill competency matrix;
- uncertainty estimates;
- invalid runs and failures;
- confounders;
- unexpected findings;
- reproducibility notes;
- agent interpretation;
- recommended outcome.

The final line must remain `Gate decision: PENDING HUMAN REVIEW` until human review occurs.

## Core evidence shape

The useful signal is not simply that one model is stronger. The target is differentiated competency, for example:

| Model | Skill A | Skill B |
|---|---:|---:|
| General | 65 | 67 |
| Specialist A | 82 | 61 |
| Specialist B | 60 | 84 |

A model that beats the baseline equally across all domains may be a generally stronger model rather than evidence of specialization.

## Interpretation

### Evidence supporting specialization

Strong evidence has both:

1. a meaningful advantage over the general baseline in the claimed primary domain; and
2. a competency profile showing that the advantage is domain-specific or materially concentrated in the claimed specialization.

### Evidence against specialization

If fair, comparable specialist checkpoints do not materially outperform the baseline in their claimed domains, the specialization hypothesis may fail for the tested family and workload.

### Inconclusive evidence

Examples:

- no sufficiently comparable specialist set exists;
- lineage is uncertain enough to invalidate comparison;
- benchmark contamination cannot be controlled;
- license/runtime restrictions prevent fair execution;
- scoring is invalid or underpowered;
- a methodological defect is discovered after freeze.

Do not convert an inconclusive result into a positive one by weakening comparability rules after observing evidence.
