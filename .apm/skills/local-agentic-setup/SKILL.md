---
name: local-agentic-setup
description: Prepare a consultant's local environment for agent-assisted work by checking the chosen assistant, project tooling and CLI access, configuring missing prerequisites and verifying readiness.
---

# Local Agentic Setup

Establish the operating system, shell, workspace, chosen assistant and requested services from available project context. Ask only for missing choices that affect setup. Read [prerequisites](references/prerequisites.md) before making changes.

Inventory existing installations and configuration first. Distinguish a missing executable from a PATH problem, an unauthenticated session from missing repository access, and a configured CLI from a tool the assistant can actually invoke. Preserve working installations and unrelated account configuration.

Prepare only the requested capabilities. For GitHub, use `github-cli-setup` when available; otherwise consult its official documentation through the prerequisites reference. This skill remains usable independently. Jira and cloud setup require the particular product, account and engagement requirements; do not assume their setup skills are installed or configure all providers by default.

Use official installation guidance for the detected environment. Apply routine changes already authorised by the task; surface broader system changes or choices that need the user's input. Let the user complete interactive authentication in their own terminal or browser, then continue verification. Do not request credentials in chat or place them in project templates.

Verify readiness from the assistant's execution environment using [verification](references/verification.md). Report observed versions, selected non-secret context, checks performed, changes made and remaining blockers. Installing an APM skill supplies guidance; it does not prove the CLI, assistant or account is configured.

This capability is experimental. Its instructions target Windows, macOS and Linux shells, but end-to-end setup across those environments and assistant harnesses has not been verified. It needs local command execution and network access for installation and service checks. No MCP server is required. Named maintenance ownership remains to be assigned before promotion to curated.
