# Catalogue

The website reads published packages from root `marketplace.json` and optional named selections from `stacks/*.json`. See the [website documentation](../docs/PAGES.md) for the implemented stack format and validation. Experimental TDD and Local Agentic Setup stacks are available as initial selections. Broader discovery records, ownership metadata and versioned stack installation remain planned as described in the [catalogue design](../docs/CATALOGUE.md).

The [Spring Boot and Micronaut Migration Pack](stacks/spring-modernisation.md) groups the Boot 3-to-4 and Spring-to-Micronaut skills as alternative migration paths.

The [SPDD Stack](stacks/spdd.md) combines five Structured Prompt-Driven Development stages with the existing testing, debugging and verification skills. It maintains a REASONS canvas alongside implementation and is distinct from the broader [SDD Stack](stacks/sdd.md).

[Jira BDD Delivery](../.apm/skills/jira-bdd-delivery/SKILL.md) is a separate ticket-driven skill. It iterates through acceptance scenarios, implementation and verification to a review-ready PR or a recorded blocker. Automatic Jira event dispatch requires an external runner; installing the skill alone does not enable one.

The [Jira BDD Delivery Stack](stacks/jira-bdd.md) includes that skill with testing, debugging, verification and [Parallel Stage Orchestration](../.apm/skills/parallel-stage-orchestration/SKILL.md). The SPDD Stack selects the same orchestration skill. Parent/child execution is conditional on actual platform capabilities and permissions, with sequential fallback.
