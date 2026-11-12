# Provenance and boundaries

Independently authored for this marketplace on 2026-11-12 from the official Quarkus and Eclipse Vert.x sources linked in [migration decisions](migration.md). No third-party skill or vendor example source was copied. This is not vendor-endorsed migration tooling.

Experimental status; long-term named maintenance ownership is unassigned. Requires the consuming project, compatible JDK/build tooling, dependency access and approved test services. No additional application framework, MCP server or installed skill is required. Supporting security/data libraries must be selected for actual application needs.

The PR and CI record structural validation, manual instruction review, hidden-content audit, source/workflow/secret/Python-dependency scans and isolated JVM fixtures. These checks do not certify security or establish cross-harness, native-image or production compatibility. Quarkus extension removal requires application-specific evidence beyond the fixture surface.

Local evidence (2026-11-12): Maven 4.0.0-rc-7 / Java 25 verified Quarkus 3.40.1 and pure Vert.x 5.1.10 fixtures, one test each with zero failures/errors/skips. Both exercise HTTP JSON success, missing-route 404 and event-consumer failure mapped to 503. The target additionally awaits startup/close and verifies NO_HANDLERS after consumer removal. Maven Enforcer rejects Quarkus dependencies, including transitives, in the target. CI repeats on Java 17. Fixtures are under `tests/fixtures/quarkus-to-vertx-baseline` and `tests/fixtures/quarkus-to-vertx`; they are repository evidence, not installed skill requirements. Startup-failure recovery, authentication, data access, clustering, telemetry, packaged signal handling and native images remain outside this fixture coverage.
