# Gate B semantic adapter

This directory is a byte-identical copy of the human-accepted Gate A v1.2.2
semantic adapter and its 13 synthetic tests. Gate B reuses the approved
semantic handoff behavior; it does not tune extraction rules from any selected
model output. The primary score is semantic correctness. Strict interface
compliance remains a separate secondary metric.

Run the synthetic tests with:

```text
python3 -m unittest discover -s experiments/gate-b/benchmark-v1.0.0/adapter -p 'test_*.py'
```

The adapter never executes candidate code. Coding source execution remains
exclusively inside the approved later judge-v2 sandbox.
