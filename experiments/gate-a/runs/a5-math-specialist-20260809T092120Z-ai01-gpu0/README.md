# A5 Mathematics specialist run

Run ID: `a5-math-specialist-20260809T092120Z-ai01-gpu0`

Status: complete, pending human review after both A5 specialists finish. This
run executed only `Qwen/Qwen2.5-Math-7B-Instruct` at the pinned revision
`ef9926d75ab1d54532f6a30dd5e760355eb9aa4d` over all 96 frozen Gate A v1.1.0
cases. The General baseline was not rerun, and the Coder specialist is a
separate required run.

## Metrics

All 96 cases generated and scored. Under the frozen deterministic policy:

| domain | foundational | intermediate | advanced | total |
| --- | ---: | ---: | ---: | ---: |
| mathematics | 0/10 | 0/24 | 0/14 | 0/48 |
| software-coding | 0/10 | 0/24 | 0/14 | 0/48 |

Overall accuracy is 0/96 (0%). The score reasons are preserved in
`per-case-results.jsonl`; the run had 48 mathematics answer-marker rejections,
37 multiple-code-block rejections, 5 prose-outside-code-block rejections, and
6 deterministic coding judge source/test rejections. These are observed model
responses under the frozen interface, not reasons to alter the benchmark or
prompt.

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
  Six extracted sources required judge execution; 42 responses were rejected
  before execution by the frozen source-extraction rules. All six judge
  containers completed and cleaned up with no timeout or infrastructure
  failure.
- `raw-responses.jsonl` preserves all 96 responses exactly. No response was
  inspected to tune cases, prompts, scoring, or tooling.

The dedicated Math cache remains outside Git. No General or Coder checkpoint
was executed in this run.
