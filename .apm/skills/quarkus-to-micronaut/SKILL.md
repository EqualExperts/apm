---
name: quarkus-to-micronaut
description: Assess, implement or review migration of a Quarkus application to the latest stable Micronaut, replacing Quarkus extensions while preserving HTTP, DI, configuration, security, data and reactive behaviour. Use for framework replacement, not a Quarkus version upgrade or adding a Micronaut library to Quarkus.
---

# Quarkus to Micronaut

Read [scope and provenance](references/provenance.md) for prerequisites and evidence limits. This experimental skill guides native framework replacement; shared Jakarta annotations do not establish runtime compatibility.

Inventory the actual Quarkus platform, extensions, language/JDK, build wrapper, REST stack, CDI features, configuration profiles, security, Panache/data access, Mutiny pipelines, messaging and deployment model. Baseline observable contracts before edits. Respect assessment-only requests and preserve unrelated work.

Resolve and pin the latest stable Micronaut target using [version selection](references/versions.md). Check JDK, build plugins, annotation processors and module alignment before porting code. Surface incompatible constraints explicitly; do not silently choose an older major or change the build system.

Use [migration decisions](references/migration.md) to map each extension to a concrete replacement, retained standalone library or unresolved gap. Replace Quarkus bootstrap and build augmentation with Micronaut bootstrap and compile-time processing. Migrate one vertical slice through injected service, configuration, HTTP, serialization and real HTTP tests first.

Port CDI lifecycle, REST bindings, security and data semantics deliberately. Rewrite Quarkus-specific Panache and extension APIs; do not rely on annotation renaming. Preserve reactive execution, cancellation and transaction context. Keep blocking work off event-loop threads and avoid converting asynchronous APIs into blocking waits to make compilation pass.

Run [acceptance scenarios](references/verification.md) against source and target. Remove Quarkus runtime, deployment artifacts and plugins after usages have replacements. Inspect transitive dependencies and generated metadata. Retain standalone libraries only with an explicit purpose and compatible versions.

Do not disable authorization, validation or TLS, expose management endpoints or change database schemas merely to pass tests. Use approved isolated test services and keep secrets out of diagnostics. Skill invocation does not authorize production deployment or data migration.

Report exact versions and sources, extension decisions, changed contracts, commands, test outcomes and remaining gaps. Separate compilation, context startup, real HTTP, integration, packaged JVM and native-image evidence. Do not infer production acceptance from a small fixture.
