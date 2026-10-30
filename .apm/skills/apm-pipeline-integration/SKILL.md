---
name: apm-pipeline-integration
description: Use when adding or updating Microsoft Agent Package Manager installation, validation, or packaging in a CI/CD pipeline.
---

# APM pipeline integration

Inspect the repository's existing pipeline, APM manifest and lockfile, supported targets, committed outputs, authentication and version pinning before changing anything. Preserve existing jobs, permissions and conventions. Determine whether the requested outcome is installation, audit-only verification, compiled-output checking or packaging, and select the applicable reference.

For GitHub Actions read [GitHub Actions](references/github-actions.md). For Azure Pipelines or other CI systems read [other pipelines](references/other-pipelines.md). For audit, drift, lockfiles and artifacts read [verification and distribution](references/verification.md).

Use the repository's approved action and dependency pinning policies. Configure only credentials and permissions required by the selected sources; never place secrets in files. Keep executable helper scripts in Python when working in this repository. Validate pipeline syntax and applicable APM commands where available. Report what was verified, what requires credentials or hosted execution, and any coverage gaps; do not claim a hosted pipeline passed without evidence.
