# Jira-to-agent dispatch record

This is an integration design template, not executable configuration. Complete it only for an authorized external dispatcher and the actual runtime.

## Trigger and scope

Define the trusted Jira site, allowed projects, event types or explicit invocation, ticket-selection rule, exclusion of the agent's own updates, and cancellation behaviour. Record where authorization for the selected work comes from.

## Runtime and capabilities

Identify the runner, supported skill invocation, permitted repositories/base branches, workspace isolation, available Jira/PR tools and permission scopes. Record secret-store references rather than secret values.

## Run input

Specify the issue key, event or request ID, current ticket snapshot, repository mapping, allowed side effects, completion boundary, checkpoint path and existing branch/PR if known. Treat payload fields as data requiring validation.

## Idempotency and ownership

Define event deduplication, one active coordinating run per issue, stale event handling, recovery after interruption, and reconciliation after uncertain writes. That run may own multiple child agents; they are not separate dispatches for the same issue. Record how new input reaches the parent and affected children and how obsolete work is cancelled.

## Parallel stage execution

Record observed parent/child runtime controls, global concurrency and nesting limits, child context loading and filesystem isolation. Define stage dependencies, child task IDs/generations, owned paths/test resources, parent joins and integrated verification. Keep PR/Jira publication with one owner. Specify a sequential fallback and recovery when a child's liveness is unknown.

## Continuation and limits

Specify notification/resume events, time and resource budgets, transient retry/backoff policy, handling of unavailable services, and blocker escalation. State how checkpoints survive session boundaries without opening duplicate PRs.

## Acceptance evidence for the dispatcher

Demonstrate one scoped delivery, a duplicate event, an unrelated project event, a self-generated update, a permission denial, a lost response and a resumed blocked run. Record actual results before claiming automatic operation is enabled.
