# Scoring attempt 2 — valid scores, generic failure-reason receipt

This pass used the corrected attached-stdin judge invocation and produced
complete 96-case scores under the approved policy. Its aggregate scores are
preserved here, but the per-case reason for 11 rejected coding cases was
reported as the wrapper-level `source_or_judge_exception`: the judge emitted a
specific rejection and then the outer handler caught its deliberate
`SystemExit`, replacing the final JSON line.

The score values were deterministic and the pass had no infrastructure stop,
but the receipt was superseded so the durable root records preserve the more
specific rejection reasons. The only watchdog event was the expected 2-second
timeout for one coding case; all containers were cleaned up.
