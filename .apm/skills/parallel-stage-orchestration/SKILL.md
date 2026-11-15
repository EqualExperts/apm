---
name: "parallel-stage-orchestration"
description: "Coordinate SPDD, Jira BDD or other explicitly parallel delivery workflows with parent and child agents: schedule independent stages, isolate writes, collect evidence and verify integrated results. Use only where runtime delegation is available and permitted; retain a sequential fallback."
---

# Parallel stage orchestration

Coordinate dependent delivery stages with one accountable parent and scoped child agents. Read [scope and evidence](references/provenance.md), [platform capabilities](references/platforms.md) before selecting a runtime mechanism and [scheduling and integration](references/scheduling.md) before dispatch. This skill supplies a portable workflow contract; it does not add agent tools to a platform.

Inspect the active runtime and applicable instructions. Determine whether spawning, result collection, steering/cancellation, workspace isolation and nested delegation are actually available. Use allowed concurrency and budget limits from the current environment. When delegation is unavailable, disabled or prohibited, execute the same stage graph sequentially and report that mode honestly. Do not silently enable experimental features or change models, permissions or account settings.

The parent owns the requested scope, stage graph, acceptance criteria, current input revisions, resource budget and delivery checkpoint. Split work by independent outcomes and evidence boundaries. Dispatch only ready tasks whose inputs and prerequisites are satisfied. Stages from different independent slices can overlap; downstream work for a slice must wait for the upstream result it consumes.

Use [the child assignment](assets/child-assignment.md) to give each child the necessary context, criterion IDs, input revision, allowed files, output location, permitted tools/actions, dependencies and result contract. Explicitly pass applicable repository instructions and stage guidance; never assume a child inherits skills, conversation or tools. Keep permissions within the parent's authorization and the child's actual runtime restrictions.

Choose disjoint write ownership in a shared workspace, or isolated branches/worktrees where supported. Separate context windows do not establish filesystem isolation. Give overlapping analysis/review tasks read-only access and let the parent combine findings. Route shared schemas, common build files, a canonical canvas and integration conflict resolution through a single owner.

Prefer a parent with direct children. Allow child coordinators only when nested delegation is supported and permitted, descendants fit the global budget, and the parent can track and cancel the subtree. Otherwise flatten the same ready tasks under the parent. A child cannot expand scope, redefine acceptance, spawn an untracked tree or claim ticket completion.

Children return their task identity, input revision, status, changed artifacts, exact checks/results, unresolved decisions and remaining work. The parent inspects artifacts and evidence, reconciles conflicts, and integrates accepted changes in dependency order. Use result notifications or supported waits; do not treat a child's success message as a passing combined build.

After integration, run required checks against the actual combined revision. Invalidate results affected by changed requirements, contracts or files. Keep publication and Jira updates with one designated parent by default; children return evidence and proposed updates. No child independently closes a ticket or publishes duplicate PRs.

Continue scheduling ready work until the requested completion boundary is met or a concrete blocker prevents further progress. On cancellation, stale inputs, time limits or parent interruption, stop or checkpoint affected children, reconcile pending writes and preserve a resumable ledger. End with accepted results, combined verification and any active or blocked tasks; never report completion while relevant writers are still running.
