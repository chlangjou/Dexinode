# Current Research Status

- Updated: 2026-08-10
- Active gate: **Gate B — Orchestration Advantage**
- Gate A final decision: **PASS**
- Gate B decision: **PENDING**
- Session handoff: `HANDOFF.md`
- Active stage: **B1 — protocol, router, benchmark and acceptance freeze design**

## Gate A — closed PASS

Final human decision:

`gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`

Gate A demonstrated reproducible specialization in at least one same-family checkpoint under the frozen v1.2.2 protocol:

- General mathematics: 30/48 = 62.50%;
- Math specialist mathematics: 44/48 = 91.67%;
- Math specialist primary-domain delta: **+29.17 pp**;
- paired-bootstrap 95% CI: **[+16.67, +41.67] pp**;
- Math specialist coding delta: **-37.50 pp**, demonstrating a concentrated specialization/tradeoff profile;
- Coder specialist did not demonstrate a coding advantage over General.

Final Gate A classification: **single-specialist PASS**. The stronger preference for two independently validated specialists was not satisfied.

Architectural consequence: Dexinode must route using empirically measured capability profiles and explicit handoff contracts/adapters, not checkpoint labels alone.

## Gate B — active design stage

Gate definition:

`gates/gate-b-orchestration/README.md`

Controlling task:

`gates/gate-b-orchestration/task.yaml`

Proposed acceptance criteria:

`gates/gate-b-orchestration/acceptance.yaml`

### Bounded hypothesis

On a fresh 96-case mixed Math/Coding benchmark, a frozen deterministic prompt-only router using the Gate A empirical skill registry should outperform a General-only policy by at least **10 percentage points overall**, with a paired-bootstrap 95% confidence interval excluding zero, while using exactly **one model inference per task** under the same generation budget.

### Initial empirical registry

- Mathematics → validated `Qwen/Qwen2.5-Math-7B-Instruct`;
- Software coding → `Qwen/Qwen2.5-7B-Instruct`;
- Unknown/unsupported → General fallback;
- `Qwen/Qwen2.5-Coder-7B-Instruct` is **not** treated as a validated coding specialist because Gate A did not establish a coding advantage.

### B1 required design outputs

Before any Gate B selected-model execution:

1. create and statically validate a fresh 96-case benchmark (48 Math / 48 Coding);
2. create a deterministic CPU-only prompt-only router and synthetic tests;
3. validate all Math oracles and Coding evaluator tests;
4. prove the router cannot access hidden domain labels, expected answers, evaluator tests, or model outputs;
5. freeze token/context and common inference controls;
6. freeze General-only and skill-routed one-call-per-task policies;
7. freeze acceptance criteria and stop for human review.

## Gate B execution authorization

**Selected-model execution is NOT authorized during B1.**

No Gate B General/Math/Coder checkpoint may be executed or inspected until the B1 benchmark/router/protocol artifacts are complete and human-approved.

The current work is static research/design only. Multi-step agent chains, recursive delegation, networking, federation, reputation, and settlement remain outside Gate B v1 scope.
