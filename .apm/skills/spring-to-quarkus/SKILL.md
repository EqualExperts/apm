---
name: spring-to-quarkus
description: Assess, implement or review migration of a Spring or Spring Boot application to Quarkus, choosing native Quarkus APIs or documented Spring compatibility extensions and verifying HTTP, injection, configuration, security and persistence contracts. Use for framework replacement, not a Spring Boot version upgrade.
---

# Spring to Quarkus

Read [provenance and evidence boundaries](references/provenance.md). Inventory the source Spring/Boot version, JDK, language, build, MVC or WebFlux stack, bean lifecycle, configuration, security, data access, transactions, messaging and deployment. Establish observable contracts and a passing baseline before edits; preserve unrelated work.

Choose the destination with [migration decisions](references/migration.md): native CDI and Jakarta REST, or explicitly supported Spring annotation compatibility. Record unsupported features and a replacement for each. Do not assume that a Spring library works because its annotations compile, or infer Boot 4 compatibility from Boot 3 examples.

Resolve a compatible Quarkus platform, plugin and Java baseline from the selected release documentation. Replace Boot packaging and starters with selected Quarkus extensions. Preserve approved dependency sources and inspect the effective build and dependency tree.

Migrate one vertical slice through startup, constructor injection, configuration, HTTP binding, serialization and tests. Verify clean build-time augmentation and actual HTTP behaviour before expanding. Keep blocking persistence and network calls off event-loop threads; explicitly preserve cancellation and context when adapting Reactor to Mutiny.

Port security and integrations with negative-path tests. Preserve authorization, CSRF, TLS, transaction boundaries and database contracts. Do not widen access, enable destructive schema generation or silently start external test services to make tests pass.

Run [acceptance checks](references/verification.md). Remove obsolete Spring runtime and build components only after retained APIs have documented compatibility extensions or tested replacements. Review packaged execution separately from development mode; native-image support needs its own evidence.

Report the chosen strategy, pinned versions, unsupported features, changed contracts and commands with test counts, failures and skips. Distinguish local checks, CI and deployment. Upstream tools and this skill do not authorize commits, pull requests or production changes beyond the user's requested scope.
