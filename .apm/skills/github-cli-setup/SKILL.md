---
name: github-cli-setup
description: Set up or troubleshoot GitHub CLI for local agent-assisted work, including installation, host and account selection, interactive authentication and read-only repository access verification.
---

# GitHub CLI Setup

Identify the workspace, OS, shell, GitHub host and intended account/repository from current context. Inspect existing GitHub CLI installation and authentication before changing anything. Read [setup and authentication](references/setup.md) for installation choices, credential precedence and multi-account handling.

Install or repair GitHub CLI only as needed, using the official package source for the environment. Preserve unrelated Git configuration and existing credentials. Have the user complete interactive login locally when required; never ask for a token or device code in chat, print tokens, or copy credential files into the project.

Select the intended host explicitly. A saved-account switch affects that host outside the current repository; do not silently switch accounts to fix a project-specific problem. Respect existing folder-scoped configuration. Authentication, Git commit identity and Git transport are separate concerns.

Verify the effective account and one intended repository using [verification and diagnosis](references/verification.md). Environment tokens can override saved credentials, so a successful login or account switch alone is not proof of the effective identity. Diagnose permission failures before broadening scopes or replacing credentials.

Report installed version, host, effective account when relevant, repository-read evidence and unresolved actions. A read check does not prove push, administration, organisation membership or Pages entitlement. Do not perform remote mutations merely to demonstrate readiness.

This independently authored capability is experimental, with no cross-platform or cross-harness setup verification yet. It requires command execution, network access to the chosen GitHub host and user-owned credentials. It supports guidance for Windows, macOS and Linux; named maintenance ownership remains to be assigned before curated promotion.
