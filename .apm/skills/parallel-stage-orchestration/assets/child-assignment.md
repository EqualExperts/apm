# Child agent assignment and result

## Identity and inputs

Record run ID, parent ID, child task ID, stage/slice, task generation, source revision and criterion/operation IDs. Link the current requirements and applicable repository/stage instructions. Include only authorized context needed for this assignment.

## Outcome and dependencies

State the concrete output, acceptance evidence required, prerequisite results already accepted, unresolved inputs and what this task must not change. Give the child a clear completion or blocker condition.

## Ownership and capabilities

Specify the workspace/branch, allowed write paths or read-only scope, shared resources reserved, available tools and authorized side effects. State who integrates results and publishes external updates. Record whether further delegation is allowed, the descendant limit and how descendants register with the parent.

## Execution and continuation

Record relevant commands, budget/deadline if configured, progress reporting, result location and cancellation/steering mechanism. Preserve current work on interruption and report partial state before reassignment.

## Child result

Return task ID/generation, input revision, status (completed, blocked, failed or cancelled), output revision if changed, exact artifact paths, changed files, criterion evidence, commands and observed outcomes, skipped checks, conflicts, partial writes and follow-up required. List descendant state if any. Do not claim aggregate ticket completion.

## Parent acceptance

Record accepted/rejected/stale disposition, inspected evidence, integration revision, conflict resolution, combined checks and the next ready tasks. Retain rejected results only as relevant diagnostic evidence, not as passing acceptance.
