# Audit patterns

`apm audit --ci` runs baseline checks and, in supported versions, drift replay and discovered organisational policy. Confirm CLI behaviour and policy source; an explicit unavailable policy should fail rather than be silently ignored. Use `--no-cache` where fresh policy is needed, and only omit policy or drift when the user explicitly accepts the reduced coverage.

Install then audit when the job needs materialised outputs. Installation may restore some managed output before audit sees the checked-out bytes; edited managed skill members have distinct preservation behaviour. For committed-output integrity, use the official action's setup-only mode followed by audit, provided the pinned CLI supports scratch hydration from the lockfile. Verify that the scratch replay succeeds and does not mutate the checkout. Ignored deployment roots have no committed bytes for content-integrity and drift comparison, reducing coverage.

Use a committed, current lockfile and appropriate repository read access. Inspect the actual action and CLI version, existing workflows, target scope and trigger paths; don't impose a fixed path filter that misses relevant files. Required branch checks or rulesets require separate repository configuration and confirmation of the hosted job name.

Source: [Enforce in CI](https://microsoft.github.io/apm/enterprise/enforce-in-ci/). Verify the current page and action documentation before applying version-specific options.
