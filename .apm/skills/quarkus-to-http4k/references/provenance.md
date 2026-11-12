# Provenance and boundaries

Independently authored on 2026-11-12 from the official sources in [migration decisions](migration.md). No third-party skill or vendor code copied. This is not vendor endorsement or automatic Quarkus compatibility.

Experimental; long-term named maintenance ownership is unassigned. Requires consuming source, compatible http4k tooling, dependency access and approved test services. No MCP server or other installed skill required. Cross-harness support is unverified.

PR/CI records structural/security checks and synthetic HTTP evidence. Security, persistence, messaging equivalence, serialization edge cases, production cutover and performance remain application-specific. Scans do not certify migrated applications.

Local evidence (2026-11-12): http4k 6.61.0.0 / Kotlin 2.4.0: two JUnit tests passed on local JDK 25, one pure-handler test and one real SunHttp adapter test. CI uses JDK 21. The fixture emits a fixed JSON payload; it does not validate a general JSON codec or serialization edge cases. All targets match the existing Quarkus fixture's JSON success/content type, missing-route 404 and service-failure 503 contracts. This does not reproduce Quarkus event-bus delivery; that needs an application-specific messaging migration. Fixture paths and hosted checks are recorded in the PR.
