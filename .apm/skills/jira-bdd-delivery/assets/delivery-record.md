# Jira BDD delivery record

## Scope and authority

Record the selected issue key/URL, project and site, snapshot timestamp, repository and inspected revision, source of the request, and authorized code, PR and Jira actions. List the bounded issue set for a batch and dependencies. Do not include credentials or unnecessary client data.

## Completion boundary

Default: verified implementation and a review-ready PR. Record any stricter ticket/project Definition of Done and the actual workflow state required at this stage. Distinguish agent delivery completion from Jira closure, merge and deployment.

## Rules and acceptance evidence

For each criterion record its stable ID, business rule, scenario IDs, unresolved questions, implementation files, test commands and observed results at an exact revision. Keep planned, failed, skipped, blocked and passed evidence distinct.

## Current work

Record branch/worktree, PR URL and head revision, required CI results, current operation, worker ownership where applicable, and remaining criteria. Link existing artifacts rather than duplicating them.

## Agent task graph

Record the parent/run identity, execution mode (parallel or sequential), observed platform capabilities and limits. For each child record its task/generation, stage, criterion IDs, input revision, dependencies, workspace/write ownership, status, descendants and result evidence. Record parent acceptance, integration revision, stale/cancelled tasks and combined verification. One parent owns external updates for the run.

## Iteration history

For each meaningful cycle record the criterion, diagnosis or planned change, resulting artifacts, checks and evidence, and next action. Capture changed assumptions and decision sources.

## Blockers and resumption

State the concrete blocker, attempts and findings, required decision or external event, and the exact next step. Record the last known ticket revision/status and which evidence needs refreshing on resume.

## External updates and outcome

Record published PRs, authorized Jira update identifiers and confirmed state. Include prepared-but-unsent updates separately. End with the verified delivery boundary met, actual Jira state and work still awaiting others.
