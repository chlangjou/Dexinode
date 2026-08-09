# Scoring attempt 1 — invalid infrastructure receipt

This scoring attempt is preserved and must not be used as baseline evidence.

- Status: invalid infrastructure attempt.
- Cause: the first scorer used `docker create` without `-i`, so the disposable
  judge did not retain an attached stdin stream for `docker start -ai`.
- Observed result: all 48 judge processes returned `JSONDecodeError` before
  reading a candidate payload; no candidate source was compiled or executed.
- Scope: all containers used the approved CPU-only judge-v2 policy and were
  cleaned up after each case.
- Repair: the scorer was corrected to create the container with `-i`; the
  corrected scoring pass is recorded at the run root.

The original per-case records, judge records, metrics, and summary are kept in
this directory as durable failed-attempt evidence.
