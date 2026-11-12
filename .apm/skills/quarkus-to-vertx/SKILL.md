---
name: quarkus-to-vertx
description: Remove Quarkus from an application and replace its managed runtime and extensions with explicitly wired Eclipse Vert.x components. Use for a Quarkus-to-pure-Vert.x migration or review, preserving reactive execution, HTTP contracts, event-bus behaviour and resource lifecycle.
---

# Quarkus to pure Vert.x

Read [provenance and evidence boundaries](references/provenance.md). This experimental skill targets framework removal, not a Quarkus upgrade or a replacement application framework.

Inventory Quarkus extensions, augmentation/build plugins, Arc/CDI beans, configuration, startup/shutdown observers, routes/REST resources, event consumers, security, persistence, messaging and deployment assumptions. Record the resolved Vert.x version separately from the Quarkus version. Baseline observable contracts and tests before removing dependencies.

Build an explicit replacement map using [migration decisions](references/migration.md). Pure Vert.x means no Quarkus runtime, augmentation or extension dependency remains in the target. Use constructor wiring and explicit ownership rather than introducing another application framework. Supporting libraries are allowed when the feature requires them; identify them and their lifecycle instead of pretending Vert.x Core replaces every extension.

Prefer removing Quarkus against a compatible Vert.x version before a separate major-version upgrade. Pin a coherent Vert.x BOM and compatible clients; consult version-specific APIs. Keep core Vert.x, Mutiny wrappers and other adapters distinct. Do not mix types or remove a still-needed reactive library merely because Quarkus supplied it transitively.

Implement a vertical slice with one owned Vert.x instance, asynchronous deployment/startup, explicit routing and event consumers, constructor-injected services and deterministic shutdown. Await startup futures before readiness; propagate bind/deployment failures and clean up partially started resources. Close only resources owned by that component. Do not block an event loop with joins, sleeps, JDBC or synchronous clients; compose futures and use approved worker execution for blocking work.

Port each extension's behaviour before deleting it. Preserve authentication, authorization, validation, transaction semantics, deadlines, context and cancellation. Removing an annotation does not replace its enforcement. Do not weaken TLS, expose management routes or disable security to obtain a green test.

Run [acceptance scenarios](references/verification.md), then inspect source, effective build and runtime dependencies for Quarkus remnants. Replace the Quarkus bootstrap, packaging, test harness and deployment configuration. Preserve unrelated work and keep production/data changes outside local migration validation.

Report removed facilities, replacements, exact versions, changed contracts, executed tests and remaining blockers. Distinguish compile, real HTTP/event-bus evidence, packaged startup and production acceptance. Never report a complete framework removal while relying on a Quarkus test/runtime classpath.
