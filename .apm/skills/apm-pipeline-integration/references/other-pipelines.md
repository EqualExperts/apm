# Azure Pipelines and other CI

For Azure Pipelines, inspect the runner OS, available Python/APM installation method, authentication and pipeline conventions. The documented standalone Unix installer supports a user-local prefix; CI must expose its bin directory to the step that invokes APM. For Azure DevOps dependencies, use a scoped secret or an authorised workload identity service connection. When relying on an Azure CLI bearer session, omit `ADO_APM_PAT` so credential precedence does not select it instead. Do not assume a service connection or permissions exist.

For other CI systems, use an approved, pinned APM distribution appropriate to the runner and run the selected install, compile, audit or pack commands. Keep credentials in the CI secret store and make them available only to steps that need them. Repository executable helper scripts must be Python; CI platform configuration and commands should respect the target repository's conventions.

Consult the [CI integration guide](https://microsoft.github.io/apm/integrations/ci-cd-pipelines/) for platform-specific details and test in the actual runner when available.
