---
name: spring-to-micronaut
description: Assess, implement or review migration of a Spring or Spring Boot application to Micronaut, preserving HTTP, dependency injection, configuration, security and persistence behaviour. Use for explicit framework migration, not a Spring Boot version update or merely adding a Micronaut library to Spring.
---

# Spring to Micronaut

Read [scope and provenance](references/provenance.md) before interpreting validation claims. This experimental skill is independently authored from official documentation; it does not promise automatic Spring compatibility.

Inventory the Spring/Boot version, build wrapper, language/JDK, web stack, bean conditions, security, persistence, transactions, messaging and deployment model. Baseline tests and observable contracts before edits. Preserve unrelated work and use approved test services.

Choose a strategy using [migration decisions](references/migration.md). For a complete framework replacement, plan an explicit native migration. Use Micronaut for Spring only when the selected module version documents every retained Spring feature; its annotation translation is not a general Spring runtime. Resolve ambiguous scope using the application's concrete compatibility gaps.

Pin compatible platform, build-plugin and annotation-processor versions from target-version documentation. Retain the supported Java baseline unless the target requires a change. Do not infer Boot 4 or Security 7 compatibility from a guide for earlier Spring versions.

Migrate one vertical slice first: build and annotation processing, startup, constructor-injected service, controller, configuration, serialization and tests. Replace APIs deliberately rather than bulk-renaming annotations. Confirm generated beans and routes in a clean build. Preserve reactive behaviour and keep blocking work off Netty event-loop threads.

Port security, persistence and integrations with behaviour covered by tests. Do not bypass authorization, CSRF, validation or TLS, widen endpoint exposure or alter database schemas just to obtain a green build. Keep secrets out of diagnostics.

Run the [acceptance scenarios](references/verification.md), compare contracts and inspect dependencies. Remove Spring runtime dependencies only after remaining usages have explicit replacements or documented compatibility dependencies. Production deployment and data migration are separate actions, not prerequisites for validating this skill.

Report exact versions, chosen strategy, unsupported features, changed contracts, commands and outcomes. Distinguish compilation, context startup, real HTTP tests and production acceptance. Identify unperformed integration, native-image, Gradle and Kotlin checks.
