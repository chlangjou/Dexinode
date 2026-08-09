# Gate A Experiment Workspace

This directory stores executable evidence for Gate A — Specialist Validation.

## Current stage

A1 — Candidate Scout.

Only candidate discovery is active. Do not create or execute the formal comparative benchmark until the candidate set receives human review.

## Expected structure

```text
experiments/gate-a/
├── README.md
├── candidates.yaml
├── benchmark/
│   ├── manifest.yaml
│   └── cases/
└── runs/
    └── <run-id>/
        ├── config.json
        ├── environment.json
        ├── results.jsonl
        ├── metrics.json
        └── summary.md
```

The benchmark and run directories may be created when their execution stages become active.

## Evidence rules

- Preserve raw per-case outcomes or stable references to them.
- Preserve invalid/failed runs and label the reason.
- Record exact model and benchmark revisions.
- Do not commit model weights or large caches.
- Prefer machine-readable outputs with concise human-readable summaries.
