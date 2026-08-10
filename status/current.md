# Current Research Status

- Updated: 2026-08-10
- Gate A — Specialist Validation: **PASS / CLOSED**
- Gate B — Orchestration Advantage: **FAIL / CLOSED**
- Gate B final decision record: `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
- Gate B post-closure retrospective: `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`
- Session handoff: `HANDOFF.md`
- No new research gate is active yet.

## Gate B frozen evidence

Benchmark: `gate-b-orchestration-v1.1.1`

Execution ID: `gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`

Evidence root: `experiments/gate-b/runs/gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0/`

Frozen scores:

| Policy | Overall | Mathematics | Coding |
|---|---:|---:|---:|
| General-only | 76/96 = 79.17% | 40/48 = 83.33% | 36/48 = 75.00% |
| Skill-routed | 77/96 = 80.21% | 41/48 = 85.42% | 36/48 = 75.00% |

Paired routed-minus-General:

- overall: **+1.04 pp**, paired-bootstrap 95% CI **[0.00, +3.125] pp**;
- Mathematics: **+2.08 pp**, CI **[0.00, +6.25] pp**;
- Coding: **0.00 pp**;
- router accuracy: **100%**.

The frozen +10 pp overall and +10 pp Mathematics thresholds were not met. The human owner assigned final **FAIL**.

## Post-closure Mathematics errata and content review

After closure, preserved raw outputs were inspected without rerunning a model or patching the frozen benchmark. The retrospective found:

- `math-23` oracle is wrong: frozen `19/48`; correct posterior **95/242 ~= 0.392562**. Both checkpoints independently computed approximately 0.392, while the frozen exact-rational extractor rejected both decimal answers.
- `math-11`, `math-12`, and `math-17` are mathematically correct for both checkpoints but were rejected by the frozen structured-output parser.
- `math-41`, the sole frozen paired Math improvement, is mathematically correct for both checkpoints: General returned `0.75`; Math specialist returned `3/4`. The +1 case is therefore an answer-representation effect, not a mathematical-content advantage.
- `math-16` and `math-32` are genuine shared arithmetic/self-check failures after both checkpoints selected an appropriate method.
- `math-36` is interpretation-sensitive; both returned the same general `(1-p)^3 p` solution rather than assuming `p=1/2` from the phrase `fair trials`.

Under a human mathematical-content classification of these inspected cases, the specialist's frozen +1 Math advantage collapses to **no content-level paired advantage**.

### Protocol-purity caveat

The frozen acceptance definition listed a benchmark oracle defect as an INCONCLUSIVE condition. The post-closure `math-23` discovery therefore creates a literal-protocol caveat and is explicitly preserved in the final decision and acceptance record.

It is non-differential for the paired result and cannot move the specialist toward the +10 pp thresholds; the content-level retrospective moves the observed specialist advantage from +1 case to zero. The final human Gate B label remains **FAIL / CLOSED** unless explicitly revised by the human owner.

## Architectural interpretation

Gate A and Gate B together imply:

1. specialization can create large capability divergence on one measured distribution;
2. a checkpoint label or broad domain such as `Mathematics` is not a sufficient skill identity;
3. end-to-end exact-answer scores confound task comprehension, domain method selection, computation, self-review and answer-contract compliance;
4. capability entries should be finer-grained and validated across multiple structurally independent panels;
5. routing should estimate expected utility by task subtype rather than assume a broad specialist is uniformly superior.

## Post-Gate hypothesis: General meta-capabilities

A plausible but **not causally established** explanation for the Gate A / Gate B contrast is that the General checkpoint may retain stronger cross-domain meta-capabilities such as natural-language comprehension, specification grounding, ambiguity resolution, answer selection and self-checking, while specialist training primarily strengthens domain solution patterns.

Current evidence does not yet prove that General is better at self-review: both checkpoints share arithmetic verification failures. The hypothesis should therefore be tested by independently scoring comprehension, method selection, derivation/computation, verification and answer representation.

## Candidate next research design

Before any new GPU/model run, define a bounded gate that separates:

1. task/specification comprehension;
2. domain-method selection;
3. derivation/computation or implementation correctness;
4. final verification/self-review;
5. answer representation / handoff-contract compliance;
6. generalization across independent task families.

A later or parallel efficiency gate can then test whether a substantially smaller specialist retains near-General quality on a validated narrow skill while materially reducing VRAM, latency, energy, concurrency or deployment cost.

## Authorization

**Gate B v1 is closed. No additional Gate B selected-model execution is authorized.**

The next step is research-design work only until a new gate, benchmark and acceptance criteria are explicitly frozen.
