# v1.2 semantic adapter

`semantic_adapter.py` contains the frozen model-agnostic mathematics
normalizer and software-coding AST extractor. It never executes generated
source. Later coding execution is limited to the approved judge-v2 sandbox.

The fixtures in `test_adapter.py` are newly authored synthetic responses, not
selected-model outputs. They cover canonical and boxed integer/rational forms,
structured JSON and boxed tuples, conflicting and malformed math answers,
surrounding prose, example blocks, missing entrypoints, first-candidate
selection, full-response Python fallback, and non-Python fences.

Validation command:

```text
python3 -m unittest discover -s experiments/gate-a/benchmark-v1.2.0/adapter -p 'test_*.py'
```

Result at freeze: 13 tests passed.
