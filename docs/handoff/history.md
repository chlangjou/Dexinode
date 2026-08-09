# Gate A Condensed Research History

This is a compact chronology for session recovery. Detailed evidence remains in Git commits, run directories, and human review records.

## Project framing

Dexinode explores a decentralized AI skill network where specialist model nodes expose explicit skills and Agents coordinate them through explicit handoff contracts, evidence, verification, and later routing/orchestration mechanisms.

Gate A intentionally precedes orchestration. Its bounded question is whether existing specialist checkpoints exhibit reproducible, measurable specialization relative to a closely related general-purpose baseline.

Gate B — orchestration advantage — remains inactive until Gate A receives a human PASS decision.

## A1 — Candidate Scout

Selected same-family Qwen2.5 7B candidates:

- General: `Qwen/Qwen2.5-7B-Instruct`
- Math: `Qwen/Qwen2.5-Math-7B-Instruct`
- Coder: `Qwen/Qwen2.5-Coder-7B-Instruct`

A1 was merged via PR #3.

## A2 — Candidate Eligibility

Human-approved candidate comparability:

- exact 7,615,616,512 parameter count for all three;
- shared Qwen2ForCausalLM 7B architecture;
- byte-identical tokenizer JSON/vocab/merges;
- official BF16 checkpoints, no quantization;
- common 4096-token envelope;
- Math checkpoint native chat template differs and encourages step-by-step / boxed answers.

Decision at the time: use one shared neutral Qwen role-delimiter template to avoid granting the Math specialist a model-specific prompting advantage.

Review:

`gates/gate-a-specialization/reviews/a2-human-review.md`

A2 was merged via PR #4.

## A3 — Benchmark construction and freeze

### v1.0 rejected

Initial 16+16 benchmark was rejected because:

- too few cases for the >=10pp / bootstrap-CI acceptance design;
- ceiling risk;
- coding needed real isolation.

### v1.1 approved

`gate-a-cross-skill-v1.1.0` froze:

- 48 Math + 48 Coding;
- per-domain difficulty 10 foundational / 24 intermediate / 14 advanced;
- deterministic exact scoring;
- no LLM judge;
- neutral common template;
- all models later run all 96 cases.

Review:

`gates/gate-a-specialization/reviews/a3-human-review-v1.1.md`

A3 was merged via PR #5.

## A4 — General baseline infrastructure

### Host bubblewrap blocker

The first A4 attempt stopped before any model execution because host-side bubblewrap could not create the network namespace:

`bwrap: loopback: Failed to create NETLINK_ROUTE socket: Operation not permitted`

This was accepted as an execution-context blocker, not a Gate/benchmark failure.

### Docker qualification

Docker on `ai01` was qualified instead:

- existing Ollama/Open-WebUI left untouched;
- exactly one L40 exposed to dedicated inference;
- separate CPU-only judge container;
- no Ollama model-storage reuse.

GPU path was approved.

Judge v1 was then rejected as too weak because it allowed `pids-limit 32`, while the frozen A3 isolation policy required one process / subprocess denial.

Judge v2 hardened to:

- `pids.max=1`;
- `RLIMIT_NPROC=1:1`;
- subprocess creation denied with `EAGAIN`;
- 2-second host watchdog;
- all other network/filesystem/capability bounds retained.

Container UID 0 was accepted only because all capabilities are zero, `NoNewPrivs=1`, no host mounts/socket/network/GPU are present, root FS is read-only, and one-process enforcement was empirically verified.

Key merges:

- PR #6 — Docker execution direction
- PR #7 — preserve evidence / judge hardening required
- PR #8 — approve hardened judge and activate A4b

## A4b — General v1.1 baseline

Run:

`a4-general-baseline-20260809T082430Z-ai01-gpu0`

Results:

- Math 10/48 = 20.83%
- Coding 36/48 = 75.00%
- Overall 46/96 = 47.92%

All 96 cases generated/scored; no final infrastructure-invalid cases.

Low Math score was sanity-reviewed against raw responses and found to represent genuine incorrect direct answers under v1.1, not a parser bug.

A4b was approved and merged via PR #9.

## A5 — v1.1 specialist cross-evaluation

### Math specialist surprising zero row

Run:

`a5-math-specialist-20260809T092120Z-ai01-gpu0`

Strict v1.1 score:

- Math 0/48
- Coding 0/48
- Overall 0/96

Failure morphology review showed this was not capability zero. Examples:

- sampled Math foundational cases were solved correctly but ended in `\\boxed{...}` after worked reasoning rather than the required `ANSWER:` line;
- Coding responses often contained a plausible implementation block plus explanatory prose, examples, or multiple code blocks and were therefore rejected by the strict extractor.

Conclusion: common tokenizer + common neutral chat envelope did **not** imply common behavioral output interface.

### Coder specialist

Run:

`a5-coder-specialist-20260809T092120Z-ai01-gpu0`

Strict v1.1 results:

- Math 12/48 = 25.00%
- Coding 39/48 = 81.25%
- Overall 51/96 = 53.13%

### Human interpretation

The v1.1 three-row matrix was rejected as a task-capability matrix because the Math row was dominated by interface compliance.

The v1.1 results remain valid interoperability / strict-output evidence.

Architectural implication for Dexinode:

**Skill should be treated closer to Model + Handoff Contract / Adapter, not Model checkpoint alone.** Specialist fine-tuning can alter output behavior as well as task competence.

Review:

`gates/gate-a-specialization/reviews/a5-interface-confounder-human-review.md`

Merged via PR #10.

## A5R1 — semantic interface remediation

Human direction:

- do not patch v1.1;
- do not rescore only Math;
- create a fresh benchmark after the observed confounder;
- separate primary semantic competence from secondary strict interface compliance;
- use one common deterministic model-agnostic adapter;
- run all three models again only after the new protocol is frozen.

### v1.2.0

Introduced:

- deterministic Math semantic normalization accepting canonical `ANSWER:` or constrained boxed final forms by expected type/schema;
- ambiguity rejection before expected-value comparison;
- Coding AST extraction selecting the first Python/unlabeled fenced block defining the requested top-level entrypoint;
- surrounding prose / later examples ignored;
- strict interface compliance recorded separately;
- 13 synthetic adapter tests.

Human review accepted the adapter/scoring/Coding design but rejected the Math case set because many new Math cases were near-isomorphic copies of v1.1 problem skeletons with changed constants.

Review:

`gates/gate-a-specialization/reviews/a5r1-v1.2-human-review.md`

Merged via PR #11.

### v1.2.1

All 48 Math cases were replaced with structurally fresh constructions. A durable freshness audit recorded:

- exact prompt overlap = 0;
- exact normalized oracle overlap = 0;
- complete case numeric-tuple overlap = 0;
- 48/48 construction-level comparisons against nearest v1.1 families;
- no positional-mirroring / coefficient-only reuse identified.

Provenance wording was corrected: v1.1 outputs did inform remediation design, but selected-model raw outputs were not used as fixtures and no v1.2.1 case/oracle/difficulty was tuned from selected-model performance.

Human oracle sanity review then found two wrong expected values:

- `math-23`: `1/4` should be `1/3`;
- `math-30`: `432` should be `240`.

Under the frozen benchmark policy, v1.2.1 cannot be patched in place.

Review:

`gates/gate-a-specialization/reviews/a5r1-v1.2.1-human-review.md`

Merged via PR #12.

## Current — v1.2.2 oracle validation

Active branch:

`agent/gate-a-a5r1-v1.2.2-oracle-validation`

Required work:

- create `gate-a-cross-skill-v1.2.2`;
- carry forward v1.2.1 structures and accepted components;
- correct known `math-23` and `math-30` oracles;
- independently recompute all 48 Math expected values;
- preserve 48/48 validation evidence;
- rerun static token/context and 13 adapter tests;
- no selected model execution;
- stop for human review.

If approved, A5R2 will execute all three models over all 96 v1.2.2 cases under one unchanged protocol, producing the first acceptable semantic competency matrix.

## Merge / PR landmarks

Useful high-level checkpoints:

- PR #3 — A1 candidate scout
- PR #4 — A2 candidate eligibility
- PR #5 — A3 v1.1 benchmark approval
- PR #6 — Docker qualification direction
- PR #7 — A4a evidence / judge hardening
- PR #8 — hardened A4a approval
- PR #9 — General baseline approval / A5 activation
- PR #10 — A5 interface confounder / remediation
- PR #11 — v1.2.0 Math freshness revision required
- PR #12 — v1.2.1 oracle correction required

Current `main` immediately before this handoff work included PR #12 merge commit:

`4a5585ce8eb909714b09091647c92ee07dd8d99a`
