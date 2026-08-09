# A4 Human Review — Execution Environment Blocker

- Date: 2026-08-09
- Reviewer role: Human decision owner
- Reviewed run: `a4-general-baseline-20260809T064011Z-ai01`
- Reviewed commit: `353d51e8fbac1ee81814efd1c28ceab83cd17c04`
- Decision: **A4 remains active; execution environment qualification required**
- Gate A decision: **PENDING**

## Accepted evidence

The A4 attempt behaved correctly and is accepted as a valid fail-closed execution record:

- the exact `ai01` host/runtime was recorded before execution;
- the approved bounded-isolation preflight was attempted before any model load;
- bubblewrap failed while creating the required network namespace with `NETLINK_ROUTE: Operation not permitted`;
- the baseline and both specialists were not executed;
- no benchmark, scoring, template, candidate set, or Gate acceptance criterion was changed.

The failure is therefore an execution-context blocker, not evidence against the Gate A specialization hypothesis and not a benchmark-definition failure.

## Additional infrastructure evidence considered

The host user `rd` is outside the existing AI containers and has Docker daemon access through the `docker` group. The existing `ollama` container demonstrates that Docker on `ai01` can expose both NVIDIA L40 GPUs and CUDA-capable NVIDIA devices to a container. The existing `open-webui` and `ollama` services are treated as independent infrastructure and are not part of the Gate A benchmark runtime.

## Human decision: qualify Docker as the A4 execution substrate

A4 may proceed to an execution-environment qualification substage using Docker, subject to the controls below.

### Existing AI services are out of scope

Do not modify, restart, recreate, reconfigure, or depend on the existing `ollama` or `open-webui` containers for Gate A execution. Do not change permissions on their host bind mounts and do not use their model cache as the Gate A model artifact source.

They may be inspected read-only as evidence that NVIDIA GPU passthrough is available.

### Dedicated inference container

The intended Gate A inference runtime is a dedicated disposable/reproducible container that will eventually:

- use one explicitly selected NVIDIA L40 GPU;
- load the exact pinned Hugging Face checkpoint revision;
- use BF16 with no quantization;
- use the frozen Transformers/template/generation policy;
- never execute model-generated Python.

During the qualification task, do not download or load the Qwen checkpoint. Only prove that a dedicated container can see the selected GPU and record the exact container/runtime identity.

### Dedicated coding judge container

Generated Python must be scored in a separate CPU-only Docker container. The qualification must demonstrate controls equivalent to or stronger than the previously intended bubblewrap boundary:

- no network;
- no host working tree, home directory, Docker socket, model cache, or unrelated host filesystem visibility;
- read-only root filesystem except explicitly private temporary storage;
- dropped Linux capabilities;
- `no-new-privileges`;
- bounded CPU, memory, PID/process count, file size/output, and wall-clock execution;
- no GPU devices;
- fail-closed behavior with a preserved machine-readable preflight receipt.

The existing frozen benchmark v1.1.0 files must not be edited. A Docker qualification policy/receipt may be added as A4 execution evidence outside the frozen benchmark directory. This is an explicit human-approved execution-policy amendment, not a change to benchmark cases, scoring, template, candidate set, or Gate acceptance criteria.

## A4a qualification boundary

The next Agent task is qualification only. It may inspect Docker/NVIDIA configuration and create disposable test containers and Gate-specific qualification artifacts. It must not:

- download or execute any selected Qwen model;
- run any benchmark case;
- modify the existing `ollama` or `open-webui` services;
- weaken the isolation requirements merely to obtain a passing result;
- proceed to A4 baseline inference.

## Human checkpoint

After Docker qualification, human review must approve the exact inference-container and judge-container execution policy and the passing receipts before baseline inference is authorized.

A5 remains inactive.
