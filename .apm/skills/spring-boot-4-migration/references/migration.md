# Migration decisions

Consult the [official Boot 4.0 migration guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide) and [4.0 requirements](https://docs.spring.io/spring-boot/4.0/system-requirements.html) before edits. Resolve discrepancies in favour of the target-version documentation. This skill targets the 3.5-to-4.0 boundary; later Boot 4 minor versions need their own release notes.

| Area | Decision and evidence to collect |
| --- | --- |
| Baseline | Boot 4.0 requires Java 17+, Framework 7 and Servlet 6.1/Jakarta EE 11. Kotlin requires 2.2+, native images GraalVM 25+. Check the target patch's Maven/Gradle requirements and actual wrapper; do not mandate Java 25 for an ordinary JVM deployment. |
| Starters | Use technology-specific main and test starters. Prefer `spring-boot-starter-webmvc` for MVC and retain WebFlux for reactive applications. Add Flyway/Liquibase starters where their auto-configuration is needed. Classic starters are a temporary module-granularity bridge, not a restoration of removed APIs or all third-party libraries. |
| Tests | Replace Boot `MockBean`/`SpyBean` with Framework `MockitoBean`/`MockitoSpyBean` and check semantics, especially spies and context hierarchy. MVC test imports move to `org.springframework.boot.webmvc.test.autoconfigure`; add the relevant test starter. Plain Mockito fields require Mockito initialization. `SpringBootTest` no longer automatically configures WebTestClient or TestRestTemplate; MockMvc already required explicit auto-configuration on Boot 3. |
| Jackson | Migrate Jackson 3 databind imports to `tools.jackson`; retain Jackson annotations in `com.fasterxml.jackson.annotation`. Never apply a blanket namespace replacement. Test payloads, dates, enums, nulls, custom modules and exception handling. The temporary `spring-boot-jackson2` bridge needs a removal plan. |
| Properties | Run the temporary properties migrator and inspect diagnostics. MongoDB connection properties move to `spring.mongodb`, while Spring Data-specific settings can remain under `spring.data.mongodb`. Compare exact keys rather than blanket prefix replacement. Remove the migrator and test again. |
| Removed features | Undertow does not meet the Boot 4.0 Servlet baseline; choose a supported server. Embedded executable launch scripts are removed, but ordinary executable jars still work with `java -jar`. Inventory removed Session integrations and Pulsar Reactive support if used. |
| Security and integrations | Check Spring Security 7, Spring Cloud and independently versioned integrations against their own compatibility guidance. Preserve authorization decisions and test denied as well as allowed requests. Verify database migration ordering and rollback constraints in an isolated environment. |
| Operations | Check startup, health, probes, metrics, tracing and deployment container compatibility. Preserve endpoint exposure rules. Measure performance if it is an acceptance requirement; do not assume a dependency upgrade improves it. |

## Authoritative references

- [Boot 4.0 release notes](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Release-Notes) for defaults and behaviour changes.
- [Framework 7 migration](https://github.com/spring-projects/spring-framework/wiki/Upgrading-to-Spring-Framework-7.x) for nullability and removed APIs.
- [Jackson 3 migration](https://github.com/FasterXML/jackson/blob/main/jackson3/MIGRATING_TO_JACKSON_3.md) for serialization changes.
- [Security migration](https://docs.spring.io/spring-security/reference/migration/index.html) for the selected security version.
- [OpenRewrite Boot 4 recipe](https://docs.openrewrite.org/recipes/java/spring/boot4/upgradespringboot_4_0-community-edition) when automation is appropriate. Review current recipe composition and licensing; do not assume every migration is automated.
