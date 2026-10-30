# Verification and distribution

Commit and maintain `apm.lock.yaml` when using locked package dependencies. Use `apm install --frozen` where supported to check that the manifest, lockfile and deployed paths agree; check target and APM version compatibility first. Choose between install-then-audit and audit-only intentionally: installation may restore managed outputs before drift can inspect them.

`apm audit --ci` includes lockfile checks and integration drift detection in supported versions. In audit-only CI, use a version that can hydrate a lock-pinned scratch installation when dependencies are absent. If deployed outputs are ignored rather than committed, there are no committed deployed bytes to compare, so content-integrity and drift coverage are limited. A separate compile-and-diff check can be appropriate for committed generated context; preserve unrelated files and scope the comparison to the actual outputs.

For distribution, distinguish APM-format archives from standalone plugin bundles. Use the APM archive format when downstream jobs need its install-time tree, and use the matching artifact path and restore method. Validate artifact names and retention with the repository's CI conventions. Pin CLI and action versions using the project's policy, and report whether compilation, audit, packaging or hosted execution actually ran.

See Microsoft's [CI integration](https://microsoft.github.io/apm/integrations/ci-cd-pipelines/) and [marketplace and package documentation](https://microsoft.github.io/apm/producer/pack-a-bundle/) for current CLI behaviour.
