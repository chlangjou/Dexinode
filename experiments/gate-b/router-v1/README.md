# Gate B router v1

The router is a deterministic CPU-only prompt classifier. `route_prompt` takes
exactly one string containing the task prompt and returns one registered route:

- `mathematics_specialist` for mathematical task language;
- `general_baseline` for software-coding task language;
- `fallback` for unsupported or ambiguous prompts.

The router has no filesystem, network, model, benchmark-metadata, expected-
answer, evaluator-test, or model-output access. It is called before model
inference and cannot issue retries, fallback calls, voting, or ensemble calls.
The hidden domain labels used by tests and later scoring are not passed to the
router.

Run synthetic and benchmark-wide tests with:

```text
python3 -m unittest discover -s experiments/gate-b/router-v1 -p 'test_*.py'
```
