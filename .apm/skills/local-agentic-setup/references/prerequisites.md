# Choose and inspect the environment

Record the OS and shell, workspace path, intended assistant, required services and approved installation method. Use repository guidance and existing configuration before asking for information. Do not infer client accounts or subscription IDs from unrelated projects.

Check executables from the same environment the assistant uses. An IDE process, container or WSL session can have a different PATH and credential store from the user's terminal. Restart or refresh the relevant process after a PATH change before reinstalling anything.

For a GitHub-based workspace, inspect Git and GitHub CLI versions and confirm the repository remote belongs to the intended host. Review remote URLs locally and redact embedded credentials before reporting. Git author identity, commit signing, Git transport credentials and GitHub CLI authentication are distinct settings; do not replace global settings to fix one project.

Install only the selected assistant and requested tools. Use the product's current official installation instructions and the organisation's approved package source. Record the version actually installed, not a guessed latest version. Assistant installation and authentication are separate from installing the APM CLI or consuming this marketplace.

When APM needs an explicit GitHub credential, follow [Supply GitHub authentication to APM](../../github-cli-setup/references/setup.md#supply-github-authentication-to-apm) to capture the chosen GitHub CLI account's token into `GITHUB_APM_PAT` in the same terminal that runs APM. Verify retrieval succeeded without displaying the value. Public github.com packages do not require a token.

## Provider choices

| Capability | Input needed before setup | Official starting point |
| --- | --- | --- |
| GitHub | Host, account and repository | [GitHub CLI](https://cli.github.com/) |
| Jira | Exact CLI product, Jira deployment and site | [Atlassian CLI documentation](https://developer.atlassian.com/cloud/acli/) |
| Azure | Intended tenant and subscription | [Azure CLI installation](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) |
| Google Cloud | Intended account and project | [Google Cloud CLI installation](https://cloud.google.com/sdk/docs/install) |
| AWS | Intended account, role, region and profile | [AWS CLI installation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) |

These links route future setup requests; this initial capability does not implement a Jira or cloud-specific setup workflow. Do not substitute one Jira CLI for another solely because its executable is named similarly.

## Example request

“Prepare this workspace for my existing assistant and GitHub account. Keep my personal projects unchanged.”

Resolve the workspace and host, check existing tooling, repair only missing prerequisites, complete authentication with the user if necessary, and verify one repository read. Do not install every cloud CLI or switch machine-wide Git identity.

This guidance is independently authored for the EE marketplace. Linked vendor documentation supplies product-specific details; vendor content is not bundled or presented as an EE support guarantee.
