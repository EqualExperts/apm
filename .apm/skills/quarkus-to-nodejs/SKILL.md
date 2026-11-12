---
name: quarkus-to-nodejs
description: Migrate or review a Quarkus application moving to Node.js, replacing managed framework facilities and preserving externally observable contracts. Use for explicit framework/language migration, not a Quarkus upgrade or adding a client library.
---

# Quarkus to Node.js

Read [provenance and limits](references/provenance.md). Inventory Quarkus extensions, routes, CDI scopes, event consumers, config, security, persistence, schedules and deployment assumptions. Record baseline versions and failing tests before edits.

Follow [target-specific migration decisions](references/migration.md). Select the target toolchain and architecture explicitly. Map every used Quarkus facility to a replacement; deleting annotations does not implement their behaviour. Preserve unrelated work.

Start with a vertical slice and compare its wire contract against Quarkus. Preserve authentication, authorization, validation, transactions, serialization, deadlines and request isolation. Missing integrations are blockers to resolve, not reasons to disable tests or silently change behaviour.

Use [acceptance scenarios](references/verification.md). Review dependencies, packaging, configuration and resource ownership. Remove Quarkus dependencies and deployment assumptions only after replacements pass. Production cutover and database changes are separate from migration validation.

Report versions, selected libraries, contract changes, commands, outcomes, unperformed checks and blockers. Compilation, synthetic fixtures and production acceptance are distinct. Do not promise performance gains without measurements.
