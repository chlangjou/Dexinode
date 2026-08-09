# A3 Human Review — Benchmark v1.1.0

- Date: 2026-08-09
- Reviewer role: Human decision owner
- Reviewed commit: `c83fd57749c57537664c4232e7a3a8ebbc6108dc`
- Benchmark: `gate-a-cross-skill-v1.1.0`
- Decision: **APPROVED FOR A4, SUBJECT TO EXECUTION PREFLIGHT**
- Gate A decision: **PENDING**

## Review summary

The superseding benchmark addresses the v1.0.0 review requirements without observing selected-model outputs.

Approved properties:

- 48 mathematics and 48 software-coding cases, 96 total;
- every selected model must run the complete cross-skill benchmark;
- per-domain difficulty distribution of 10 foundational, 24 intermediate, and 14 advanced cases;
- deterministic scoring with equal predeclared case weights and no LLM judge;
- frozen neutral Qwen role-delimiter template and identical semantic messages;
- all cases remain within the approved 4,096-token total context envelope;
- provenance, contamination risk, and difficulty-stratified reporting are explicit;
- v1.0.0 remains preserved as historical evidence and was not edited in place;
- Gate acceptance criteria and selected candidate models were not changed.

The 48-case domain size is accepted as materially better aligned with the predefined >=10 percentage-point signal and 95% bootstrap uncertainty requirement. Final statistical sufficiency is still determined from the observed paired case-level evidence after A4/A5, not assumed by design.

## Coding execution isolation

The fail-closed bounded-isolation policy is approved as a mandatory execution preflight.

The A3 preflight receipt on host `ai01` failed because bubblewrap could not establish the required network namespace. This is an execution-host blocker, not a benchmark-definition failure. No coding response may be compiled or scored on a host/runtime/sandbox identity until that exact environment produces a passing preflight receipt.

The failed receipt must remain preserved:

`experiments/gate-a/benchmark-v1.1.0/execution/preflight-receipt-a3.json`

## A4 authorization

A4 — General Baseline is authorized with this ordering:

1. select and record the exact A4 execution host/runtime;
2. run the frozen coding-isolation preflight on that exact environment;
3. if the preflight fails, stop without executing the baseline and report the blocker;
4. if the preflight passes, execute `Qwen/Qwen2.5-7B-Instruct` at its pinned revision over all 96 frozen v1.1.0 cases under the approved common inference policy;
5. preserve raw per-case responses, scoring reasons, environment metadata, timing, failures, and the passing preflight receipt;
6. stop for human review before A5.

A4 must not modify the benchmark, scoring rules, template, candidate set, or Gate acceptance criteria.