# Provenance and scope

Independently authored for this marketplace on 2026-11-12 from official Quarkus documentation linked in [migration decisions](migration.md). The official migration overview links `quarkusio/skills`; this package references that upstream resource rather than copying or installing it. No upstream skill or vendor example source is redistributed. This is not a vendor-endorsed package.

Experimental; long-term named ownership remains unassigned. Requires consuming application source, compatible JDK/build tools, dependency access and approved test services. No MCP server or other installed skill is required. Cross-harness compatibility is not established.

The bounded fixture baseline pins Spring Boot 3.5.16 and Quarkus 3.40.1 on Java 17-compatible source. These versions are test evidence, not a universal target or a claim of latest-release coverage. CI runs both HTTP fixtures on Java 17. The pull request records actual local and hosted outcomes separately.

Structural validation, content audits and repository security scanners are distinct from behavioural migration tests. Python dependency auditing does not certify JVM dependencies or the security of a migrated application. Compatibility extensions, Boot 4 migration, Kotlin/Gradle, persistence, authentication, messaging, performance, native images and deployment remain outside this fixture's evidence.

Local verification on 2026-11-12: Maven 4.0.0-rc-7 / Java 25 ran both fixtures successfully, one real-HTTP test each with zero failures, errors or skips. The Quarkus package build also passed. This does not establish packaged process or native-image execution.
