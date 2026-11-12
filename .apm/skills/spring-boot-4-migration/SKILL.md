---
name: spring-boot-4-migration
description: Migrate or review a Spring Boot 3.x application moving through 3.5 to Spring Boot 4.0, including modular starters, Jackson 3, configuration and tests. Use for an explicit major-version migration or resulting failures, not a Boot 3 patch update or a Boot 4.0 to 4.1 upgrade.
---

# Spring Boot 3 to 4 migration

Adapted from GitHub Awesome Copilot. Read [provenance and verification boundaries](references/provenance.md) before relying on its validation status. This is experimental guidance, not a production migration guarantee.

Inspect the build files, wrapper, Java toolchain, deployment container and directly managed integrations. Identify the requested target patch from current official release information; keep Boot dependency management authoritative and pin the selected version. Do not turn a Boot migration into an unrelated JDK or architecture rewrite. Use the project's existing Maven or Gradle wrapper and preserve unrelated work.

Read the [migration decisions](references/migration.md) and linked official guides for the affected features. Establish the existing build/test baseline before edits. Bring older Boot 3 applications to the latest appropriate 3.5 patch, resolve deprecations and establish a green baseline before moving to 4.0. Record pre-existing failures separately.

Apply focused changes in dependency order: parent/BOM or plugin, technology and test starters, imports and removed APIs, Jackson, configuration properties, then integration-specific adjustments. Run relevant tests after each coherent change. Inspect dependency resolution instead of masking errors with exclusions or arbitrary version overrides. Do not change authentication, authorization, CSRF, TLS, health exposure or serialization contracts just to make tests pass.

Use [verification scenarios](references/verification.md) to check compile, full tests, startup and observable behaviour. Read configuration with secret values redacted; do not publish environment dumps. Use approved test services and credentials. Do not run production migrations, deploy or publish merely to validate this skill.

Use the properties migrator only temporarily; remove it and repeat startup verification. OpenRewrite is optional: inspect the applicable recipe and pinned plugin/recipe versions, review the resulting diff and run the same acceptance checks. Automation does not establish correctness.

Report the source and target versions, changes, commands and outcomes, unresolved compatibility blockers and checks not performed. Distinguish package validation, sample migration evidence and the consuming application's acceptance. Never declare completion from compilation alone.
