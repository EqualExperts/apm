# Spring Boot and Micronaut Migration Pack

An experimental selection for modernising Spring applications. Maintainer: Equal Experts APM maintainers. The [pack selection](spring-modernisation.json) includes:

- [Spring Boot 3 to 4](../../.apm/skills/spring-boot-4-migration/SKILL.md): move through a verified Boot 3.5 baseline to Boot 4.0, covering dependency changes, Jackson 3, configuration and tests.
- [Spring to Micronaut](../../.apm/skills/spring-to-micronaut/SKILL.md): assess and migrate to the latest stable Micronaut, checking current releases, toolchain requirements and behavioural contracts.

Choose the path that matches the requested outcome. A Boot 4 upgrade is not a prerequisite for moving to Micronaut. If both are explicitly required as successive milestones, establish and verify each baseline separately. The Boot skill covers the 3.x-to-4.0 major transition; it does not cover a subsequent 4.0-to-4.1 upgrade. The Micronaut skill records current target selection and compatibility constraints in its linked references.

Each skill remains independently usable and retains its provenance and verification boundaries. The consuming project supplies its source, compatible build tooling, dependency access and approved test services. Confirm the chosen target's requirements before making changes; including both skills does not establish compatibility between all source and target versions.

This pack is a catalogue selection, not a native managed-stack manifest. The website expands it into the two package installation commands. Review the selection and pin the provider revision for reproducibility. It grants no deployment or external-write permissions.

Catalogue validation checks membership and rendering. It does not demonstrate an application migration, consumer installation or production compatibility.
