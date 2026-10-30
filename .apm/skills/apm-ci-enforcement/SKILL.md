---
name: apm-ci-enforcement
description: Use when configuring or diagnosing Microsoft APM audit, policy enforcement, drift checks, or SARIF reporting in CI.
---

# APM CI enforcement

Inspect the existing pipeline, APM CLI and action versions, policy sources, lockfile, authentication and whether deployed outputs are committed before proposing or changing a gate. Preserve existing jobs and permissions. Identify the desired policy, drift and integrity coverage and any constraints on CI execution.

Read [audit patterns](references/audit-patterns.md) to choose an install-and-audit or audit-only gate. Read [reporting and diagnosis](references/reporting-and-diagnosis.md) when configuring SARIF, scheduled checks or investigating failures. Consult the current upstream documentation and the actual CLI version before relying on flags or scratch replay behaviour.

Apply the repository's action pinning rules and minimum necessary permissions. Use authorised secret stores for private sources. Do not silently weaken policy or disable checks. Validate configuration and available commands; report untested hosted execution, missing credentials, ignored outputs and other coverage limitations accurately.
