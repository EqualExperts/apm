# Version selection

Documentation snapshot checked 2026-11-15:

| Component | Observed stable release | Official evidence |
| --- | --- | --- |
| Micronaut platform (target) | 5.2.6 | [Release announcement](https://micronaut.io/2026/11/11/micronaut-framework-5-2-6/) and [platform dependency matrix](https://micronaut-projects.github.io/micronaut-platform/latest/guide/) |
| Spring Boot (source reference) | 4.1.2 | [System requirements and stable versions](https://docs.spring.io/spring-boot/system-requirements.html) |

At invocation, check [Micronaut releases](https://micronaut.io/category/release-announcements/) and the platform matrix again. Select the newest stable release unless the user specifies a line; exclude milestones, release candidates and snapshots. Record date, URLs and exact versions. If offline, label this snapshot stale rather than claiming a current lookup. Inventory the application's actual Spring version; upgrading Spring before replacing it is not a prerequisite.

Micronaut platform, Core, plugins and individual modules have separate version numbers. Use the platform's managed dependencies and compatible build tooling; do not stamp 5.2.6 onto every artifact. Verify release artifacts resolve with the project's repositories and wrapper before porting code.

The [Micronaut 5 Core guide](https://docs.micronaut.io/5.2.x/core/) sets a JDK 25 baseline. Align compiler, CI, container runtime and native toolchain. The platform guide excludes Kotlin/Maven from version 5 support; Kotlin projects need a Gradle migration or an explicitly agreed older target. Do not silently downgrade the target or change build systems.

Review the platform's breaking changes before translating older recipes. Check Jackson 3 integration and custom serializers separately from Micronaut Serialization; retaining Jackson annotations does not establish Databind compatibility. Test wire payloads. Recheck the selected Micronaut for Spring module against the actual Spring APIs instead of assuming latest-to-latest compatibility.

These are researched version targets, not a tested compatibility matrix. The older fixture evidence in [provenance](provenance.md) does not validate Micronaut 5.
