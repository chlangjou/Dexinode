# A4b Human Review — General Baseline

- Date: 2026-08-09
- Reviewer role: Human decision owner
- Reviewed commit: `2df6104d46e1520638fad79b8b6d8a670b3898f7`
- Run: `a4-general-baseline-20260809T082430Z-ai01-gpu0`
- Decision: **APPROVED**
- Gate A decision: **PENDING**
- Next authorized stage: **A5 — Specialist Cross-Evaluation**

## Evidence accepted

The General baseline run is accepted as the frozen comparison row for Gate A.

Accepted evidence includes:

- exact model `Qwen/Qwen2.5-7B-Instruct` at revision `a09a35458c702b33eeacc393d103063234e8bc28`;
- BF16, no quantization, Transformers 4.41.1, PyTorch 2.2.2+cu121 and the recorded runtime package set;
- one selected NVIDIA L40 on `ai01`, UUID `GPU-e1760d1d-d9a5-29ce-32f0-bbd70bc98664`;
- all 96 frozen v1.1.0 cases generated and scored;
- no infrastructure-invalid case in the final scoring pass;
- frozen neutral Qwen role-delimiter prompt/template and 4,096-token total context policy;
- raw responses, per-case score reasons, timing, model artifact checksums, runtime/image identities, and preserved failed/superseded attempts;
- coding scores produced only through the approved Docker judge-v2 isolation policy.

Accepted General metrics:

- mathematics: 10/48 = 20.8333%;
- software coding: 36/48 = 75.0000%;
- overall: 46/96 = 47.9167%;
- mathematics difficulty: foundational 4/10, intermediate 6/24, advanced 0/14;
- coding difficulty: foundational 9/10, intermediate 19/24, advanced 8/14.

## Mathematics sanity review

The low General mathematics score triggered a methodological sanity review before authorizing specialists.

The review found no evidence of a parser or scoring defect. Sampled foundational failures show that the raw model output itself contains an incorrect answer while the frozen oracle is straightforward and correct. For example, `math-01` asks for the solution to `5(2x - 3) = 4x + 21`, whose frozen expected answer is 6; the raw General response is `ANSWER: 3`, and the deterministic scorer correctly records an integer mismatch.

The model generally complied with the required one-line `ANSWER:` format, so the low mathematics score is not explained by widespread format rejection. It is therefore retained as observed baseline behavior under the already frozen direct-answer interface.

No chain-of-thought prompt, alternate chat template, answer-format change, or benchmark revision is authorized after observing this result. A5 specialists must receive the same frozen prompts and semantic interface.

## Formal inference resource policy for A5

The A4b formal inference container actually used:

- one selected L40 UUID as above;
- 40 GiB container memory limit;
- 16 CPU limit;
- read-only root with private tmpfs;
- `--cap-drop=ALL` and `no-new-privileges`;
- network disabled for formal inference;
- the dedicated Gate model cache mounted read-only during inference.

These formal-run resource controls are the comparison policy to preserve for A5. The smaller 4 GiB / 4 CPU values recorded in the earlier runtime-definition/preflight preparation are not the formal specialist inference limits.

## A5 comparability requirements

A5 is authorized to execute both approved specialist checkpoints across the complete frozen 96-case benchmark:

- `Qwen/Qwen2.5-Math-7B-Instruct` at revision `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`;
- `Qwen/Qwen2.5-Coder-7B-Instruct` at revision `c03e6d358207e414f1eca0bb1891e29f1db0e242`.

Each specialist must run all 48 mathematics and all 48 coding cases. No specialist-only subset, early stopping, or result-dependent adjustment is allowed.

The A4b inference/scoring logic is now frozen for comparison. The A5 executor may parameterize or duplicate the A4b runner only to substitute the authorized model ID, pinned revision, run identifiers, cache/output locations, and corresponding metadata. It must not change:

- prompt rendering or system/user semantic content;
- tokenization policy;
- generation settings;
- BF16/no-quantization policy;
- package/runtime versions;
- selected GPU and formal resource limits;
- scoring algorithms;
- coding unit tests;
- judge image/digest or isolation controls.

Any required substantive runtime, prompt, scorer, benchmark, or judge-policy change must stop A5 for human review before further specialist outputs are generated or scored.

## Interpretation guardrail

A4b alone does not establish specialization and does not decide Gate A. The General row is only the reference row for the later cross-skill competency matrix. A5 must complete both specialist rows before A6 computes specialist-minus-General deltas, uncertainty, domain concentration, and a Gate recommendation.

## Human checkpoint

A4b is approved. A5 Specialist Cross-Evaluation is authorized under the controls above. Final Gate A decision remains `PENDING HUMAN REVIEW`.
