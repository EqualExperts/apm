# Provenance and verification boundaries

Independently authored for this marketplace on 2026-11-12 from the official sources linked in [migration decisions](migration.md). No third-party skill or vendor example source was copied. Research found official Spring integration guides, but no dedicated migration skill with sufficient evidence to adopt confidently. Vendor documentation is linked, not redistributed; this is not a vendor-endorsed skill.

The Micronaut for Spring guide inspected on that date identifies version 6.1.0 and limits compatibility to documented features. Native migration and annotation compatibility are distinct paths. Do not infer support for every Spring version.

Experimental: long-term named maintenance ownership remains unassigned. Requires consuming source, compatible JDK/build tooling, dependency access and approved test services. No MCP server or other skill is required. Cross-harness support is not established.

The PR and CI record structural validation, hidden-content audit, secrets/workflow/Python/dependency scans and isolated Maven tests. Existing Boot fixtures supply Spring evidence; a native Micronaut fixture checks real HTTP and DI. These bounded checks are not security certification or a production migration.

Local verification on 2026-11-12 used Maven 4.0.0-rc-7 and Java 25. Spring Boot 3.5.16 and Micronaut platform 4.10.24 each passed one real-HTTP contract test with zero failures/errors/skips: constructor injection, JSON success payload/content type and missing-route status. Fixtures are under `tests/fixtures/spring-to-micronaut-baseline` and `tests/fixtures/spring-to-micronaut` in the marketplace repository, not required installed skill resources. CI repeats both on Java 17. Security, persistence, compatibility-bridge, Gradle/Kotlin, native-image and packaged deployment acceptance remain unverified.
