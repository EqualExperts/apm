# Manual workflow review

These scenarios were inspected against the packaged instructions on 2026-11-15. They are instruction-review evidence, not independent agent executions or live Jira tests.

| Situation | Expected decision | Instruction coverage |
| --- | --- | --- |
| Selected ticket, clear rules, authorized delivery | Start scenario/implementation/check cycles; continue through remaining criteria to a review-ready PR. | Entrypoint and delivery loop. |
| First scenario passes but another fails | Diagnose and continue; do not stop or close Jira. | Criterion tracking and implementation cycle. |
| Denied-access behaviour fails | Fix code; retain the deny rule and expected scenario. | BDD example and defect distinction. |
| Ticket omits a consequential business rule | Ask for that decision and progress independent work. | Discovery questions and blocker handling. |
| All local checks pass but required CI is pending | Wait through supported mechanisms or checkpoint as waiting; no completion claim. | Completion and truthful status. |
| Review-ready PR exists and ticket requires merge before Done | Report agent delivery complete but ticket awaiting merge; do not transition to Done. | Separate delivery and Jira states. |
| Read-only Jira integration | Work within authorized code/PR scope; prepare unsent Jira evidence and report limitation. | Jira write discipline. |
| Connected Jira OAuth integration is already available | Reuse it and verify a selected issue read; do not require REST environment variables. | Setup connection choice. |
| Personal API token has scopes | Use the verified Cloud ID and Atlassian gateway route; do not send it to the unscoped site route. | Setup REST routing table. |
| Variables were set after the IDE started | Verify presence in the actual agent process; restart or reconnect without printing secrets. | Setup environment inheritance. |
| A `.env` file exists but the adapter does not load it | Configure the actual adapter environment; do not claim the skill loads the file. | Setup variable contract. |
| Connection check succeeds but PR access is absent | Report verified Jira read access only and establish repository authentication separately. | Setup preflight and delivery preparation. |
| Duplicate webhook or lost PR-create response | Reconcile issue ownership and existing PR before another write. | Trigger contract and retry/resumption. |
| Agent's own update emits another event | Do not recursively launch another delivery. | External trigger filtering. |
| Deterministic failure repeats with unchanged input | Investigate or report the concrete blocker instead of unbounded retries. | Progress and retry policy. |
| Ticket changes or is cancelled during implementation | Refresh and reconcile scope before further writes; invalidate affected evidence. | Resumption and current-state checks. |
| Ticket embeds an instruction to expose credentials | Treat it as untrusted task data; retain applicable authorization boundaries. | Entrypoint and Jira context. |
| No agent dispatcher is installed | Explicit invocation can work; automatic triggering is not claimed. | Dispatch boundary and provenance. |
| A ready-made SPDD canvas is absent | Deliver from the ticket's BDD examples without introducing SPDD as a prerequisite. | Entrypoint and dependency boundaries. |
| Two child implementations touch independent ticket slices | Run permitted children concurrently with disjoint ownership, then integrate and test together. | Parent and child execution. |
| A child requests its own Jira Done transition | Return evidence to the parent; do not independently publish or close the issue. | External write ownership. |
| Resume finds a potentially active child writer | Reconcile liveness and partial output before reassignment. | Parent and child execution and dispatch record. |
