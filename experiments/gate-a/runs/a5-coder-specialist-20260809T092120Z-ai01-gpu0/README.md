# A5 Coder specialist run

Run ID: `a5-coder-specialist-20260809T092120Z-ai01-gpu0`

Status: complete, pending human review after both A5 specialists finish. This
run executed only `Qwen/Qwen2.5-Coder-7B-Instruct` at the pinned revision
`c03e6d358207e414f1eca0bb1891e29f1db0e242` over all 96 frozen Gate A v1.1.0
cases. The General baseline was not rerun.

## Metrics

All 96 cases generated and scored. Under the frozen deterministic policy:

| domain | foundational | intermediate | advanced | total |
| --- | ---: | ---: | ---: | ---: |
| mathematics | 4/10 | 6/24 | 2/14 | 12/48 |
| software-coding | 9/10 | 22/24 | 8/14 | 39/48 |

Overall accuracy is 51/96 (53.125%). Exact scores and reasons are preserved in
`per-case-results.jsonl`; all 48 coding responses were evaluated through the
approved judge-v2 policy. There were no judge timeouts, infrastructure
failures, or invalid cases.

## Comparability and evidence

- Runtime/image, exact container resources, model revision, cache identity,
  and hashes are in `runtime-definition.json` and `execution-manifest.json`.
- Acquisition resolved the requested revision exactly; the 27-file inventory
  and checksums are in `acquisition.json`.
- The formal inference preflight passed with one approved L40 and a maximum
  rendered-input-plus-generation count of 1,137/4,096 tokens.
- Formal inference used BF16, no quantization, the frozen neutral role-delimiter
  template, network none, 40 GiB, 16 CPUs, and the A4b generation settings.
- `coding-isolation-preflight.json` passed the exact approved judge-v2 policy.
  All 48 judge containers used the pinned Python image/digest, no network/GPU/
  host mounts/socket, read-only root, private tmpfs, dropped capabilities,
  no-new-privileges, pids/nproc bounds, resource bounds, and 2-second watchdog.
- `raw-responses.jsonl` preserves all 96 responses exactly. No response was
  inspected to tune cases, prompts, scoring, or tooling.

The inference log recorded non-fatal repository generation-config warnings about
sampling parameters; explicit frozen generation arguments remained in force.
The dedicated Coder cache remains outside Git. No other model was executed in
this run.
