# Provenance and boundaries

Independently authored on 2026-11-12 from the official sources in [migration decisions](migration.md). No third-party skill or vendor code copied. This is not vendor endorsement or automatic Quarkus compatibility.

Experimental; long-term named maintenance ownership is unassigned. Requires consuming source, compatible Node.js tooling, dependency access and approved test services. No MCP server or other installed skill required. Cross-harness support is unverified.

PR/CI records structural/security checks and synthetic HTTP evidence. Security, persistence, messaging equivalence, serialization edge cases, production cutover and performance remain application-specific. Scans do not certify migrated applications.

Local evidence (2026-11-12): Node.js 24.22.1: one built-in test, zero failures/skips. The fixture uses native HTTP and no third-party npm dependencies. Its JavaScript example is kept in a linked reference and materialized temporarily by Python automation. All targets match the existing Quarkus fixture's JSON success/content type, missing-route 404 and service-failure 503 contracts. This does not reproduce Quarkus event-bus delivery; that needs an application-specific messaging migration. Fixture paths and hosted checks are recorded in the PR.
