# Provenance

Independently authored for the EE marketplace on 2026-11-12. GuicedEE package identities and instructions were reviewed at [ai-rules commit 5b243e2ec3b332212c2755d4e1e46fc855446a41](https://github.com/GuicedEE/ai-rules/tree/5b243e2ec3b332212c2755d4e1e46fc855446a41). The repository default branch changed from master to main during verification; the reviewed catalogue identifies guicedee-ai-rules and contains 118 packages.

No upstream skill source was copied into this package. Install the original GuicedEE skills in the consumer and preserve their own licences/metadata. This skill orchestrates their use rather than vendoring a second framework manual. Public website installation guidance corroborates the marketplace identity.

Experimental: long-term named maintenance ownership remains unassigned. Requires compatible JDK/Maven, APM, dependency access and the selected consumer harness. No MCP server is required. Installation validation, structural checks and sample runtime evidence are not cross-harness or production certification. Exact evidence and limitations are recorded in the PR.

APM 0.26.0 failed with plugin recursion; checksum-verified APM 0.35.1 installed all five baseline packages into an isolated consumer at the pinned revision. Skill entrypoints, metadata and the installed creator validator were checked. Non-agent metadata warnings did not remove those verified files; other harness targets remain untested. The existing unrelated di marketplace emitted stale-cache warnings and was left unchanged.

GuicedEE 2.5.1 fixture: Maven 4.0.0-rc-7 / JDK 25, JPMS main/test separation, dual-registered binding SPI, awaited loading and idempotent terminal destroy passed one JUnit test with zero failures/errors/skips. The installed framework baseline validator passes. No Quarkus dependency is permitted by the fixture Enforcer rules. HTTP/event-bus migration, security, persistence, native-image and packaged process-startup acceptance are not claimed by this injection/lifecycle fixture.
