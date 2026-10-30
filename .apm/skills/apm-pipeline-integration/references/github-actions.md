# GitHub Actions

Use the official [microsoft/apm-action](https://github.com/microsoft/apm-action) according to its current inputs and the repository's action pinning policy. Inspect existing workflows before adding a job. For normal installation, configure the action and compile only where the selected targets and project require it. For a committed-output integrity gate, prefer setup-only mode followed by `apm audit --ci` before any installation that could restore altered managed files; check the installed APM version supports scratch hydration.

For private sources, configure the appropriate token as a CI secret or action input with access to the needed repositories. A default workflow token may access same-organisation repositories if granted permission; do not assume it can access arbitrary cross-repository or cross-organisation dependencies. For Azure DevOps with federated identity, configure OIDC and Azure login with the minimum permissions and do not set `ADO_APM_PAT` when relying on the inherited Azure CLI session.

Check the [official CI integration guide](https://microsoft.github.io/apm/integrations/ci-cd-pipelines/) and action documentation for current option names and authentication behaviour. Do not claim GitHub-hosted success until the job runs.
