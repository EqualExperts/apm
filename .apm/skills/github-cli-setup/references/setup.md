# Installation and authentication

Use [official installation instructions](https://github.com/cli/cli#installation) for the detected OS. Inspect `gh --version` first and retain a working installation unless an upgrade is required. On Windows, the official WinGet package is `GitHub.cli`; on macOS, Homebrew uses `gh`. Linux packaging varies by distribution: use GitHub's linked distribution instructions rather than guessing a repository or executing an unreviewed installer. Check executable discovery again in the assistant's runtime after installation.

## Authentication flow

Check the intended host's active authentication without token display:

```text
gh auth status --active --hostname HOST
```

If interactive login is needed, the user can run:

```text
gh auth login --hostname HOST --web
```

Replace `HOST` with the verified host. The user completes the browser flow and any device-code step directly. GitHub CLI prefers secure credential storage but can fall back to a plaintext file when a credential store is unavailable. Do not force insecure storage; explain a fallback and establish an acceptable credential-storage route before calling setup complete. Avoid requesting additional scopes without a concrete need.

## Multiple accounts and environment precedence

For github.com, `GH_TOKEN` takes precedence over `GITHUB_TOKEN` and stored credentials. For enterprise hosts, inspect the applicable documented environment variables. Detect whether variables are present without printing their values or dumping the environment. Do not delete or override injected credentials automatically.

When the user intends a saved-account switch for the host, use:

```text
gh auth switch --hostname HOST --user ACCOUNT
```

This changes the active saved account for that host, not just the current repository. For scoped work, preserve existing scoped credential handling or use an already approved process-specific environment. Always recheck effective identity. Do not run `gh auth token` as standalone diagnostic output, use token-display options or expose `hosts.yml`. Capturing a credential directly into the intended process environment for APM is covered below.

Git transport setup is optional and separate. Do not run `gh auth setup-git` or rewrite credential helpers unless the task requires Git transport configuration and its scope is understood. Do not alter global author email or signing settings to repair CLI authentication.

## Supply GitHub authentication to APM

After verifying the intended saved GitHub account, set APM's dedicated variable in the terminal that will run APM. Preserve existing injected credentials unless replacing them is intentional. These commands capture the token without printing its value.

PowerShell:

```powershell
$env:GITHUB_APM_PAT = gh auth token --hostname github.com
```

Bash / Zsh:

```bash
export GITHUB_APM_PAT="$(gh auth token --hostname github.com)"
```

For a specific saved account, append `--user ACCOUNT` to the `gh auth token` invocation, replacing `ACCOUNT` with the verified login. This avoids changing the host-wide active account. Stop if credential retrieval fails; do not proceed with an empty variable. Never print the variable, enable shell tracing around credential capture, commit its value or put it in a generated install script.

Run marketplace registration and installation in that same terminal. The variable is inherited by child processes; an already-running IDE or agent does not receive it automatically. These examples do not persist the secret in a shell profile or machine environment.

Public github.com packages need no token, and current APM can use the active GitHub CLI login directly. The explicit variable selects a credential when that is needed. APM's GitHub lookup differs from GitHub CLI: per-organisation `GITHUB_APM_PAT_{ORG}`, then `GITHUB_APM_PAT`, `GITHUB_TOKEN`, `GH_TOKEN`, GitHub CLI and Git credentials. Check higher-priority organisation variables when diagnosing a wrong account, without displaying values. See the [APM authentication guide](https://microsoft.github.io/apm/consumer/authentication/) and [detailed lookup rules](https://github.com/microsoft/apm/blob/main/docs/src/content/docs/getting-started/authentication.md), reviewed 2026-11-12.

## Sources

Reviewed against official documentation on 2026-10-31; confirm installed-command help when behaviour differs:

- [Login and credential storage](https://cli.github.com/manual/gh_auth_login)
- [Authentication status](https://cli.github.com/manual/gh_auth_status)
- [Account switching](https://cli.github.com/manual/gh_auth_switch)
- [Environment variables and precedence](https://cli.github.com/manual/gh_help_environment)
- [Git credential configuration](https://cli.github.com/manual/gh_auth_setup-git)
