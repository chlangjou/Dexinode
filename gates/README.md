# Research Gates

A Gate is a bounded, falsifiable research checkpoint.

Each Gate directory should contain:

- `README.md` — human-readable purpose, scope, method, and interpretation guidance;
- `task.yaml` — machine-readable execution contract;
- `acceptance.yaml` — frozen evidence thresholds and outcome rules.

## Gate lifecycle

1. Proposed
2. Active
3. Evidence collection
4. Pending human review
5. PASS / FAIL / INCONCLUSIVE

Agents may move execution work through stages inside an Active Gate, but only humans may assign the final Gate outcome.

## Freeze rule

Acceptance criteria must be defined before formal evidence collection. Once comparative runs begin, criteria and benchmark scoring rules may not be changed in response to observed results.

Methodological corrections require a new version with preserved history.
