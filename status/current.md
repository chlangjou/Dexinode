# Current Research Status

- Updated: 2026-08-09
- Active gate: Gate A — Specialist Validation
- Gate decision: PENDING
- Active execution stage: A4b — General Baseline Execution (completed; pending human review)

## Objective

Determine whether existing specialized small-model checkpoints exhibit reproducible, measurable skill specialization relative to a closely related general-purpose baseline.

## Frozen Gate A controls

Approved candidate set:

- general baseline: `Qwen/Qwen2.5-7B-Instruct`
- mathematics specialist: `Qwen/Qwen2.5-Math-7B-Instruct`
- coding specialist: `Qwen/Qwen2.5-Coder-7B-Instruct`

Approved benchmark: `experiments/gate-a/benchmark-v1.1.0/`.

The frozen benchmark, scoring rules, neutral prompt template, candidate set, model revisions, and Gate acceptance criteria remain unchanged.

## A4 infrastructure history

The first A4 attempt stopped before model execution because host-side bubblewrap could not establish its network namespace. The failed run remains preserved at:

`experiments/gate-a/runs/a4-general-baseline-20260809T064011Z-ai01/`

Human review classified that result as an execution-context blocker, not a Gate or benchmark failure.

Docker on `ai01` was then qualified as the Gate A execution substrate.

### Inference GPU path — APPROVED

- host: `ai01`;
- Docker Engine 29.5.3, runtime `runc`;
- selected device: one NVIDIA L40;
- selected host GPU 0 UUID: `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- Docker DeviceRequest and observed container inventory both expose exactly that GPU;
- existing `ollama` and `open-webui` remain out of scope for modification or model-cache reuse.

Receipt:

`experiments/gate-a/execution/a4-docker-qualification/inference-gpu-preflight.json`

### Coding judge v2 — APPROVED

The hardened Docker judge satisfies the frozen A3 isolation/process policy.

Approved exact policy includes:

- `python:3.10-slim` at the recorded image/repository digests;
- CPU-only, no GPU/device requests;
- `--network none`;
- no host mounts or Docker socket;
- read-only root filesystem;
- private `/tmp` tmpfs;
- `--cap-drop=ALL`;
- `no-new-privileges`;
- `--pids-limit 1`;
- `--ulimit nproc=1:1`;
- 256 MiB memory and 0.5 CPU bounds;
- 1 MiB file-size bound and bounded logs;
- mandatory host-side 2-second watchdog.

The v2 receipt records 21/21 checks passing. Child-process creation was empirically denied with `BlockingIOError` / `EAGAIN`; the 2-second watchdog fired after 2008 ms and cleanup succeeded. All prior network/filesystem/device/capability/resource checks passed again.

The non-root UID attempt failed closed before Python startup. UID 0 inside the judge container is approved only with the exact recorded restrictions: the container is non-privileged, has zero effective/permitted/bounding capabilities, `NoNewPrivs=1`, no host mounts/socket/network/GPU, a read-only root, and `pids.max=1` with demonstrated subprocess denial.

Final A4a approval:

`gates/gate-a-specialization/reviews/a4a-judge-hardening-human-review.md`

A4a is complete.

## Active bounded task: A4b — General Baseline Execution

Authorized model:

- model: `Qwen/Qwen2.5-7B-Instruct`
- revision: `a09a35458c702b33eeacc393d103063234e8bc28`
- dtype: BF16
- quantization: none
- benchmark: `gate-a-cross-skill-v1.1.0`

A4b is now authorized to download and execute **only the pinned General baseline**.

### A4b execution — COMPLETE, PENDING HUMAN REVIEW

Run: `experiments/gate-a/runs/a4-general-baseline-20260809T082430Z-ai01-gpu0/`

- The pinned General model resolved exactly to revision
  `a09a35458c702b33eeacc393d103063234e8bc28` in the dedicated Gate cache.
- All 96 frozen cases generated successfully and all 96 were scored; no Math
  or Coder specialist was downloaded or executed.
- Deterministic result: 46/96 overall (`0.4791666667`); mathematics 10/48
  (`0.2083333333`); software-coding 36/48 (`0.75`).
- Difficulty results: mathematics foundational 4/10, intermediate 6/24,
  advanced 0/14; software-coding foundational 9/10, intermediate 19/24,
  advanced 8/14.
- The approved single GPU was visible: NVIDIA L40,
  `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`; sampled peak use was 16193 MiB.
- The coding judge-v2 preflight passed on the exact execution environment.
  All 48 coding judge containers were cleaned up; one case reached the
  approved 2-second watchdog and was scored 0 with preserved timing evidence.
- No infrastructure-invalid cases remained in the final scoring pass. The
  initial acquisition failure and two superseded scorer receipts remain
  preserved under the run directory.

Durable evidence includes the runtime/image and container manifest, model
artifact inventory, inference and judge preflight receipts, all raw responses,
per-case scores/reasons/timing, scoring metrics, and reproducible scripts.
Model weights remain outside Git in the dedicated Docker volume.

Required execution order:

1. create/use a Gate-specific model/cache location independent of existing Ollama storage;
2. define and record the exact dedicated inference image/runtime before benchmark results are observed;
3. verify the approved single-L40 UUID is the only visible GPU;
4. verify the frozen runtime/generation/template/context policy;
5. download the exact pinned General checkpoint revision and record artifact identity/checksums where practical;
6. run all 96 frozen cases with no early stopping or result-dependent changes;
7. preserve every raw response and per-case execution record;
8. score mathematics deterministically under the frozen scoring policy;
9. score coding responses only through the approved Docker judge v2 policy and mandatory 2-second watchdog;
10. preserve per-case scores/reasons, timing, failures, environment/image/model identities, and preflight/execution receipts;
11. calculate General baseline metrics without changing the benchmark or acceptance criteria;
12. stop for human review before A5.

A4b must NOT:

- execute Math or Coder specialist checkpoints;
- modify benchmark cases, scoring, prompt template, model revisions, or Gate acceptance criteria;
- use or repermission existing Ollama model storage;
- modify/restart/recreate `ollama` or `open-webui`;
- weaken the approved inference or judge isolation policy;
- proceed to A5.

## Next human checkpoint

Review the completed General baseline run, raw evidence, scoring, runtime
identity, and failures/exclusions. A5 remains inactive until that review is
recorded.

## Future gate

Gate B — Orchestration Advantage — remains inactive until Gate A receives a human PASS decision.
