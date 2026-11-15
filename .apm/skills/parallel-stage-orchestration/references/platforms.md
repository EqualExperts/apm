# Platform capability checks

Official documentation reviewed on 2026-11-15. These are documented integration options, not proof that this APM package has been executed successfully on each platform. Recheck the installed version, account policy and tools exposed in the current session before delegating.

| Platform surface | Documented mechanism | What to establish in the current run |
| --- | --- | --- |
| Codex / supported ChatGPT subagent sessions | [OpenAI subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents) describes parallel agents and parent orchestration. | Confirm spawn, follow-up, wait/result and stop controls. Observe active concurrency/depth and permission limits. Do not infer an isolated worktree from a separate agent thread. |
| Claude Code | [Subagent guidance](https://code.claude.com/docs/en/sub-agents) describes custom subagents, foreground/background execution and nested delegation. | Confirm available agent tools, configured limits, skill/context loading and workspace behaviour. Follow the current nested-delegation limits instead of hard-coding a depth. |
| GitHub Copilot app / CLI | [Delegation guidance](https://docs.github.com/en/copilot/concepts/agent-capabilities/choosing-and-delegating-agent-work/delegating-and-parallelizing-work-with-agents) describes the orchestrator and `/fleet` for independent subtasks. | Verify this surface exposes fleet/subagent execution and result collection. A generic Copilot target selection does not establish the same capability in every editor or hosted agent. |
| Cursor editor / CLI / Cloud Agents | [Subagent guidance](https://cursor.com/docs/subagents) describes separate child contexts and results returned to the parent. | Check the current surface's tools and workspace ownership. Cloud subagents use team-configured MCP servers, so local connector access must not be assumed. |
| Other or restricted runtime | No mechanism assumed. | Use discoverable, permitted parent/child controls if adequate; otherwise retain the task graph and execute it sequentially. |

The same workflow does not imply the same API or file format. This package creates no platform-specific agent configuration and does not install a scheduler. If configuration is requested, use the selected platform's current schema and repository conventions. Do not copy another platform's tool names, flags or configuration directories.

## Capability record

Before dispatch, record the platform/surface and version where available; permitted delegation; child context/tool loading; observed shared or isolated filesystems; concurrency/depth/budget limits; result and cancellation mechanisms; and available continuation support. Keep secrets out of this record.

If read-only child tools are available, use them for reviewers. A textual instruction to avoid edits is a task constraint, not a security sandbox. Children must respect the same user scope even when their runtime exposes broader tools. Tool absence is a reason to fall back or report a limitation, not to pretend a stage ran in another agent.
