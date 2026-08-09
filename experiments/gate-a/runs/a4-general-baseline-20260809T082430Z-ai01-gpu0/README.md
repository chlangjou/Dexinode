# A4b General baseline run

Run ID: `a4-general-baseline-20260809T082430Z-ai01-gpu0`

Status: complete, pending human review. This run executed only the pinned
General checkpoint on the frozen Gate A v1.1.0 benchmark. Math and coding
specialists were not downloaded or executed, and no benchmark, scoring rule,
template, candidate revision, or Gate acceptance criterion was changed.

## Result

The 96/96 cases generated and scored successfully. The deterministic aggregate
is 46/96 (`0.4791666667`): mathematics 10/48 (`0.2083333333`) and
software-coding 36/48 (`0.75`). Difficulty-stratified results are preserved in
`metrics.json`:

| domain | foundational | intermediate | advanced |
| --- | ---: | ---: | ---: |
| mathematics | 4/10 | 6/24 | 0/14 |
| software-coding | 9/10 | 19/24 | 8/14 |

The run had 50 failed cases scored as zero under the frozen rules: 38 math
cases and 12 coding cases. There were no infrastructure-invalid cases in the
final scoring pass. One coding case reached the approved 2-second host
watchdog; the container was killed and cleaned up. Other coding failures were
deterministic wrong-value or test-exception rejections recorded per case.

## Reproducibility

- Exact host, Docker, runtime, image, GPU, cache, and container identities are
  in `execution-manifest.json` and `runtime-definition.json`.
- The model resolved to revision
  `a09a35458c702b33eeacc393d103063234e8bc28`; artifact inventory and checksums
  are in `acquisition.json`. Model weights remain only in the dedicated Docker
  volume and are not committed.
- `inference-preflight.json` records the single approved GPU, BF16/no-
  quantization policy, frozen template, and 4096-token envelope.
- `coding-isolation-preflight.json` records the passing exact judge-v2
  preflight. Coding execution records use the same `python:3.10-slim` digest,
  no network/GPU/host mounts/socket, read-only root, private tmpfs, dropped
  capabilities, no-new-privileges, pids/nproc bounds, memory/CPU bounds,
  1-MiB file bound, bounded logs, and 2-second host watchdog.
- `raw-responses.jsonl` preserves every raw response. Derived deterministic
  scores and reasons are in `per-case-results.jsonl`; judge timing and cleanup
  evidence are in `coding-judge-records.jsonl`.

The first failed acquisition receipt and two superseded scoring receipts are
preserved under this run; they are not baseline metrics. No candidate output
was inspected to modify the frozen benchmark or scoring policy.

## Next action

Stop at A4b and require human review of this run before any A5 specialist
execution.
