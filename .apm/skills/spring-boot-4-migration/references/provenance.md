# Provenance and review

Adapted on 2026-11-12 from [GitHub Awesome Copilot spring-boot-4-migration](https://github.com/github/awesome-copilot/tree/30a0d7465b14b05e05949d6588b99f7af0c537b4/skills/spring-boot-4-migration), pinned to `30a0d7465b14b05e05949d6588b99f7af0c537b4`. Upstream is MIT licensed; [the full licence](upstream-license.txt) preserves GitHub's copyright notice. This is an EE adaptation, not a Spring-endorsed skill.

Selected over less-established standalone collections because it provides an explicit 3.x-to-4.0 scope, topic references and official source links. Repository popularity is not proof of migration correctness.

Changes from upstream: concise harness-independent entrypoint, required APM metadata, focused references instead of the entire example library, no implicit dependence on other installed skills, no unverified upstream "verified" labels, no generic performance promises, and explicit security/runtime acceptance boundaries. Preserve MockMvc's pre-existing explicit setup requirement and Jackson annotations' unchanged namespace. Do not treat optional CycloneDX configuration as a prerequisite for every migration or enable Java preview features by default.

Reviewed against the official Boot 4.0 migration guide. Named long-term maintenance ownership remains unassigned; classify as experimental. Requires access to the consuming source, its supported JDK/build tool, dependency repositories and any approved test services. No MCP server or additional agent skill is required.

Validation evidence is recorded in the pull request and its CI runs. Structural/security scans are not certification; cross-harness, Gradle/Kotlin, native-image and production migration coverage must not be inferred from a sample Maven test.

Local evidence (2026-11-12): Maven 4.0.0-rc-7 / Java 25 ran `verify` against Boot 3.5.16 and 4.0.9 MVC fixtures, with two tests per version, zero failures/errors/skips. Both Spring contexts started and the JSON response and missing-route contracts passed. Fixtures live in the marketplace repository under `tests/fixtures/spring-boot-migration`; they are review evidence, not an installed skill dependency. This did not exercise a packaged server, security rules, persistence, native images or Gradle/Kotlin.
