# MVSS, GCI, routing, and FIM eligibility evidence baseline

- Date: 2026-08-10
- Status: Durable literature-synthesis baseline
- Experimental authorization: None
- Related decision: [ADR 0001](../decisions/0001-hybrid-resident-agent-research-frame.md)

## Closed empirical state

- Gate A — Specialist Validation: **PASS / CLOSED**.
- Gate B — Orchestration Advantage: **FAIL / CLOSED**.
- Gate B routed-minus-General: +1.04 percentage points overall with 95% CI [0, +3.125] pp; the later content review found no paired Mathematics content advantage.
- No experimental Gate is active.

## Consolidated evidence

| Claim | Current classification | Boundary for Dexinode |
|---|---|---|
| A smaller specialist can beat a larger/general model on some narrow, closed, verifiable distributions | `ESTABLISHED` as a bounded existence claim | Does not imply structural transfer, workflow reliability, or production value |
| Specialist advantage transfers across fresh task structures, interfaces, and workflows | `PARTIALLY SUPPORTED` | Gate B and independent medical/agent evidence show that benchmark-local advantage can disappear |
| Catastrophic forgetting fully explains specialist regressions | `CONTRADICTED` | General Capability Integration must separately cover comprehension, method use, execution, verification, and contract compliance |
| Dense 1–7B specialists are generally useful standalone replacements | `CONTRADICTED` as a general claim | Credible regions remain task-conditioned: classification, extraction, FIM, bounded code/math with executable checks |
| Heterogeneous models have per-query complementarity | `ESTABLISHED` | Complementarity does not make the winning model cheaply predictable |
| Domain/difficulty classification is equivalent to predicting `P(success | task, model)` | `CONTRADICTED` | Gate B had 100% domain routing accuracy without material utility gain |
| Pre-inference routing can recover useful quality/cost trade-offs | `PARTIALLY SUPPORTED` | Strongest for curated model ladders and stable traffic; OOD, version drift, regret, and model recall remain material |
| Routing can reduce average cost near a chosen quality floor | `ESTABLISHED` under specific production/research conditions | Does not prove consumer, idle, or edge decentralization |
| Full-stack absolute-small economics remain favorable after memory, context, verifier, fallback, cold start, P95, energy, and maintenance | `OPEN` | Parameter count or active parameters alone are insufficient |
| A distributed specialist network is already justified by routing evidence | `CONTRADICTED` | The decentralization thesis remains independently `OPEN` |

Representative primary sources include [Qwen2.5-Coder](https://arxiv.org/abs/2409.12186), [Qwen2.5-Math](https://arxiv.org/abs/2409.12122), [LLMRouterBench](https://aclanthology.org/2026.findings-acl.1881/), [RouteLLM](https://arxiv.org/abs/2406.18665), [medical-domain negative evidence](https://aclanthology.org/2025.gem-1.5/), and the repository's frozen Gate A/B records. Vendor production reports remain supporting evidence, not sole support for a major conclusion.

## MVRC and MVSS

Two scales must now be investigated together:

- **MVRC — Minimum Viable Resident Core:** the smallest local model-plus-agent configuration that can manage intent, state, tools, context assembly, recovery, and escalation at an acceptable quality and resource envelope.
- **MVSS — Minimum Viable Specialist Scale:** the smallest complete specialist service that remains useful on a specified task distribution and quality floor after its runtime, context, verifier, and lifecycle costs are included.

Neither is a universal parameter threshold. Active-small MoE models must report both total and active parameters and do not count as dense absolute-small evidence.

## FIM / syntax-aware eligibility

Decision: **`HOLD`**.

FIM remains a credible narrow candidate because absolute-small code families, native FIM interfaces, executable verification, and local/privacy-sensitive IDE use cases exist. It does not proceed to Gate design because the required eligibility set is incomplete:

1. DELULU paper and public artifact counts differ; only a pinned artifact could support future statistics.
2. Dataset rows inherit mixed source licenses, including unlicensed/proprietary markers; no human-approved allowlist exists.
3. Public verifier distribution is not closed with immutable image digests or a complete rebuild recipe.
4. The Qwen deployable scale ladder has a 3B license gap and incomplete exact-lineage comparability.
5. No common consumer runtime yet measures the full quality/resource frontier.

The HOLD is not being resolved in the current Hybrid Agent Architecture study. Gate design, model downloads, and inference remain unauthorized.

## Current research implication

The highest-value question is no longer which FIM model scores best. It is whether memory/context and harness engineering can create a credible local Resident Core and bounded specialist region without hiding the required intelligence in a remote large-model memory manager, verifier, judge, or retry budget.

The next Worker must therefore evaluate a complete configuration:

`model + memory + context policy + harness/loop + tools + verifier + fallback + human review`

Its stop point and decision vocabulary are defined in the [Hybrid Agent Architecture Worker brief](hybrid-agent-architecture-worker-brief.md).
