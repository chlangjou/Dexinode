# Hybrid Agent Architecture Research — Human Review

- Review date: 2026-08-11
- Reviewer／decider: Human project owner
- Worker recommendation: `HOLD`
- Accepted decision: **`PROCEED TO BOUNDED ARCHITECTURE SPEC`**
- Decision issue: [#29](https://github.com/chlangjou/Dexinode/issues/29)
- Durable decision: [ADR 0002](../decisions/0002-proceed-to-bounded-repository-repair-spec.md)

## Reviewed artifacts

- [Hybrid Agent evidence map](hybrid-agent-evidence-map.md)
- [Agent-specialized small-model landscape](agent-specialized-small-model-landscape.md)
- [Hybrid Resident-Agent architecture hypothesis](dexinode-hybrid-architecture-hypothesis.md)
- [Worker research decision](hybrid-agent-research-decision.md)

All four deliverables were complete and mutually consistent enough for decision review. The Worker respected the authorization boundary: no model weights, inference, GPU work, benchmark, Gate, Gate A/B change, FIM HOLD resolution, DELULU continuation, commit, or push occurred during research.

## Review finding

The evidence is accepted; the Worker verdict is not.

The Worker treated “integrated real-work evidence already exists” as a prerequisite for a bounded architecture specification. The original decision vocabulary required a credible path that could be specified and later falsified. Integrated evidence is therefore a later validation input, not a prerequisite for defining the interfaces and attribution needed to collect it.

This distinction is narrow:

- **accepted:** there is enough component evidence to specify one bounded configuration;
- **not accepted:** the configuration, a 4B–8B Resident Model, the context envelope, or its user value has already been validated.

## Criteria mapping

| Predeclared `PROCEED` condition | Evidence found | Human disposition |
|---|---|---|
| credible Local Resident Core path | deterministic local authority + 4B–8B candidate region + versioned memory + bounded packet + verifier + fallback | sufficient to specify; not validated |
| Remote not required on every step | bounded GUI, tool, coding, extraction, and verification signals exist locally | sufficient to preserve the hypothesis; frequency remains open |
| at least two absolute-small end-to-end capability classes | MAI-UI-2B, xLAM-2 3B／8B, and SERA-8B cover three regions | satisfied as capability-region evidence |
| memory／context／loop responsibilities can be separated | Worker responsibility matrix and canonical／derived／working split | satisfied as decomposition |
| full-workflow observables are measurable | quality, active human time, latency, disclosure, fallback, severe failure, recovery | satisfied as measurability; no threshold consensus |

## Source spot-checks

The central limitations survived source review:

- LongMemEval-V2 supports a substantial retrieval-to-reader reconciliation gap and shows strong-controller dependence.
- OneFlow supports a strong single-agent／simpler-workflow baseline against homogeneous multi-agent claims.
- MemSecBench supports persistent poisoning and incomplete selective repair.
- MAI-UI-2B, xLAM-2, and SERA-8B provide end-to-end signals within distinct, harness-confounded configurations.
- Qwen3.5-4B remains official-metadata evidence for a Resident candidate, not an integrated Resident Core result.

No single vendor score is promoted into a major conclusion or cross-model ranking.

## Required corrections incorporated

1. “Long-term state outside context is universally necessary” is reduced from `ESTABLISHED` to a `PARTIALLY SUPPORTED` Dexinode design constraint.
2. The SERA-8B 80GB statement now distinguishes the 8B model-card recommendation from the paper hardware section, which explicitly discusses SERA-32B.
3. The model landscape is explicitly non-exhaustive and is not a candidate registry.
4. The Worker `HOLD` remains visible as provenance; the human `PROCEED` decision is recorded separately.
5. 8K–32K, 70%, -30%, and -50% remain provisional and are not copied into acceptance criteria.

## One authorized bounded question

> For a recoverable repository-repair workflow whose result can be checked by deterministic tests, what minimum responsibility contract, packet/receipt schema, state transitions, and escalation boundary should a 4B–8B Local Resident Core have so that later evidence can determine whether it works without a Remote Model managing every step?

The next artifact is a specification only. Model selection, benchmark design, execution planning, and Gate creation remain outside authorization.
