# Reporting and diagnosis

For SARIF, grant only the required code-scanning permissions, produce a report at a known path, and arrange upload after an audit failure while preserving the failing job result. Handle missing reports and unavailable code scanning explicitly; avoid claiming findings were uploaded until the hosted run confirms it. Apply the repository's approved action pins. For scheduled sweeps, agree the cadence and scope and use complete reporting when supported.

Diagnose the reported check before changing files: inspect manifest and lockfile consistency, deployment ownership, missing outputs, integrity, subset selection, policy and drift. Regenerate or prune only when appropriate, preserve user changes, and review resulting diffs. Do not strip content, force an install, bypass a policy or edit organisational policy automatically merely to make the gate pass. Route exceptions through the existing authorised policy process.

Check `apm audit --ci --help` and the current [Enforce in CI guide](https://microsoft.github.io/apm/enterprise/enforce-in-ci/) for supported flags and SARIF output. Record local validation separately from CI results.
