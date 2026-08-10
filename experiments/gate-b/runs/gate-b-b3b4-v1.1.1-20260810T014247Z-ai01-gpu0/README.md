# Gate B B3B4 execution evidence

Execution ID: `gate-b-b3b4-v1.1.1-20260810T014247Z-ai01-gpu0`

Status: **COMPLETE — PENDING HUMAN REVIEW**.

This run executed the approved Gate B B3B4 sequence on `ai01`, using the
frozen `gate-b-orchestration-v1.1.1` benchmark and `router-v2`:

1. all 96 semantic-task-only route decisions were persisted;
2. General ran once on all 96 cases;
3. General results were not inspected between phases;
4. the Math specialist ran only on the persisted 48 Math routes;
5. both output collections completed before scoring or composition.

No Coder checkpoint was executed. No retry, fallback, voting, ensemble,
result-driven rerouting, performance early stop, benchmark change, protocol
change, or acceptance-threshold change occurred.

The complete evidence is summarized in [execution-validation.yaml](execution-validation.yaml),
with raw responses, receipts, per-case scores, judge records, route decisions,
composition, and aggregate metrics preserved beside this file.
