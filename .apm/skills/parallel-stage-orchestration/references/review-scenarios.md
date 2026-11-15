# Manual decision review

Instruction review on 2026-11-15; these are review cases, not live multi-agent test results.

| Situation | Required response | Coverage |
| --- | --- | --- |
| Delegation tool absent or disabled | Execute ready tasks sequentially; do not invent agents or enable features silently. | Capability checks and entrypoint. |
| Two independent implementation slices | Assign bounded children with independent write ownership; integrate and retest. | Scheduling table and fan-in. |
| Implementation needs unfinished analysis | Wait for the accepted prerequisite; parallelize only unrelated work. | Dependency readiness and slice rules. |
| Two children want the same build file | Give one writer ownership or isolate changes and serialize parent integration. | Ownership and integration. |
| Separate contexts share one filesystem | Treat writes as shared unless workspace isolation is verified. | Platform checks and scheduling. |
| Nested delegation unavailable or slots exhausted | Flatten or queue under the parent; respect the global limit. | Entrypoint and recovery. |
| Child says done without test evidence | Inspect artifacts and request or perform required checks before acceptance. | Result contract and parent acceptance. |
| Child result was produced before a requirement change | Reject affected evidence as stale and reconcile the input revision. | Failure and recovery. |
| Parent resumes while a former child may still be writing | Reconcile liveness before reassigning ownership or publishing. | Recovery and completion boundaries. |
| Multiple children have Jira tools | Keep updates with the designated parent; no duplicate comments, PRs or ticket closure. | External write ownership. |
| Children pass separately but combined tests fail | Continue diagnosis and integration; no aggregate completion claim. | Fan-in and integrated verification. |
