# Gate A Handoff References

Use this file as a map, not as a second source of truth. If a reference disagrees with `status/current.md` or `gates/gate-a-specialization/task.yaml`, inspect Git history and the relevant human review before proceeding.

## Mandatory read order for a resumed session

1. `AGENTS.md`
2. `HANDOFF.md`
3. `status/current.md`
4. `gates/gate-a-specialization/README.md`
5. `gates/gate-a-specialization/task.yaml`
6. `gates/gate-a-specialization/acceptance.yaml`
7. the active human review named in `status/current.md`

## Current active review / task

- Active review: `gates/gate-a-specialization/reviews/a5r1-v1.2.1-human-review.md`
- Remediation contract: `gates/gate-a-specialization/execution/a5r-interface-remediation.yaml`
- Active Agent branch: `agent/gate-a-a5r1-v1.2.2-oracle-validation`
- Target benchmark: `experiments/gate-a/benchmark-v1.2.2/`

Known required v1.2.2 corrections:

- `math-23`: `1/4` -> `1/3`
- `math-30`: `432` -> `240`

The active revision must validate all 48 Math oracles, not only these two.

## Benchmark lineage

### v1.1.0 — historical strict-interface benchmark

Root:

`experiments/gate-a/benchmark-v1.1.0/`

Status:

- historically approved and executed;
- retained as strict-interface/interoperability evidence;
- not accepted as the final semantic-capability matrix because Math-specialist outputs were interface-confounded.

Important review:

`gates/gate-a-specialization/reviews/a5-interface-confounder-human-review.md`

### v1.2.0 — semantic adapter introduced, Math freshness rejected

Root:

`experiments/gate-a/benchmark-v1.2.0/`

Status:

- frozen-not-approved;
- semantic adapter/scoring design accepted;
- Coding set accepted;
- Math set rejected for structural near-isomorphism with observed v1.1 cases.

Review:

`gates/gate-a-specialization/reviews/a5r1-v1.2-human-review.md`

Key reusable artifacts:

- `experiments/gate-a/benchmark-v1.2.0/adapter/semantic_adapter.py`
- `experiments/gate-a/benchmark-v1.2.0/adapter/test_adapter.py`
- `experiments/gate-a/benchmark-v1.2.0/scoring.yaml`

### v1.2.1 — structural freshness accepted, oracle errors found

Root:

`experiments/gate-a/benchmark-v1.2.1/`

Status:

- frozen-not-approved;
- Math structural freshness accepted;
- two incorrect Math expected values found in human oracle review;
- must remain immutable.

Important artifacts:

- `experiments/gate-a/benchmark-v1.2.1/freshness-audit.yaml`
- `experiments/gate-a/benchmark-v1.2.1/cases/math.yaml`
- `experiments/gate-a/benchmark-v1.2.1/manifest.yaml`

Review:

`gates/gate-a-specialization/reviews/a5r1-v1.2.1-human-review.md`

## Candidate identity

General baseline:

- model: `Qwen/Qwen2.5-7B-Instruct`
- revision: `a09a35458c702b33eeacc393d103063234e8bc28`

Math specialist:

- model: `Qwen/Qwen2.5-Math-7B-Instruct`
- revision: `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`

Coder specialist:

- model: `Qwen/Qwen2.5-Coder-7B-Instruct`
- revision: `c03e6d358207e414f1eca0bb1891e29f1db0e242`

Eligibility review:

`gates/gate-a-specialization/reviews/a2-human-review.md`

A2 established:

- same Qwen2.5 7B lineage and exact 7,615,616,512 parameter scale;
- byte-identical tokenizer JSON/vocab/merges;
- BF16/no-quantization policy;
- common 4096-token envelope;
- Math checkpoint has a materially different native chat/boxed-answer behavior.

## Execution environment references

Docker qualification root:

`experiments/gate-a/execution/a4-docker-qualification/`

Reviews:

- `gates/gate-a-specialization/reviews/a4a-docker-qualification-human-review.md`
- `gates/gate-a-specialization/reviews/a4a-judge-hardening-human-review.md`

Approved inference GPU:

- NVIDIA L40
- UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`
- Docker Engine 29.5.3
- runtime `runc`

Approved judge-v2 evidence:

- `experiments/gate-a/execution/a4-docker-qualification/judge-isolation-preflight-v2.json`
- `experiments/gate-a/execution/a4-docker-qualification/judge_isolation_probe_v2.py`

Judge constraints include:

- CPU-only;
- no network/GPU/host mounts/Docker socket;
- read-only root + private tmpfs;
- `--cap-drop=ALL`;
- `no-new-privileges`;
- `pids.max=1` / `RLIMIT_NPROC=1:1`;
- subprocess creation empirically denied;
- 256 MiB / 0.5 CPU;
- 1 MiB file limit;
- 2-second host watchdog.

## Preserved executed runs

### General v1.1 baseline

Root:

`experiments/gate-a/runs/a4-general-baseline-20260809T082430Z-ai01-gpu0/`

Human review:

`gates/gate-a-specialization/reviews/a4b-general-baseline-human-review.md`

Strict v1.1 metrics:

- Math 10/48 = 20.83%
- Coding 36/48 = 75.00%
- Overall 46/96 = 47.92%

### Math specialist v1.1

Root:

`experiments/gate-a/runs/a5-math-specialist-20260809T092120Z-ai01-gpu0/`

Strict v1.1 metric: 0/96.

Interpretation: **not capability zero**. Raw responses demonstrated correct sampled mathematical solutions ending in `\\boxed{...}` and coding implementations embedded in prose/multiple blocks. This run is preserved as interface-compliance evidence.

### Coder specialist v1.1

Root:

`experiments/gate-a/runs/a5-coder-specialist-20260809T092120Z-ai01-gpu0/`

Strict v1.1 metrics:

- Math 12/48 = 25.00%
- Coding 39/48 = 81.25%
- Overall 51/96 = 53.13%

Do not mix these v1.1 rows with later v1.2.x semantic rows.

## Gate acceptance

Authoritative file:

`gates/gate-a-specialization/acceptance.yaml`

Key frozen concepts:

- primary metric accuracy;
- specialist primary-domain improvement target >= 10 percentage points absolute over General;
- 95% bootstrap CI for improvement must exclude zero;
- specialization must be domain-specific/concentrated rather than merely a uniformly stronger model;
- Agent provides recommendation only; final Gate decision belongs to human review.

Do not change these thresholds based on observed A4/A5 outcomes.

## Research-process / coordination references

- `docs/research-process.md`
- `AGENTS.md`
- `status/current.md`

Branch discipline:

- `agent/<task>` = single-writer execution branch;
- `integration/<task>` = review/reconciliation surface;
- reviewer does not push onto active Agent branch;
- no routine force-push;
- failed/stale evidence is preserved rather than overwritten.

## Next likely artifacts

If v1.2.2 passes human review, expect:

- an approved `experiments/gate-a/benchmark-v1.2.2/`;
- a new A5R2 Agent branch;
- three complete v1.2.2 run directories: General, Math, Coder;
- one three-row semantic competency summary;
- later `gates/gate-a-specialization/evidence-report.md` from A6.
