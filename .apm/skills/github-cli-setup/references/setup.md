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

This changes the active saved account for that host, not just the current repository. For scoped work, preserve existing scoped credential handling or use an already approved process-specific environment. Always recheck effective identity. Do not run `gh auth token`, use token-display options or expose `hosts.yml` as diagnostic output.

Git transport setup is optional and separate. Do not run `gh auth setup-git` or rewrite credential helpers unless the task requires Git transport configuration and its scope is understood. Do not alter global author email or signing settings to repair CLI authentication.

## Sources

Reviewed against official documentation on 2026-10-31; confirm installed-command help when behaviour differs:

- [Login and credential storage](https://cli.github.com/manual/gh_auth_login)
- [Authentication status](https://cli.github.com/manual/gh_auth_status)
- [Account switching](https://cli.github.com/manual/gh_auth_switch)
- [Environment variables and precedence](https://cli.github.com/manual/gh_help_environment)
- [Git credential configuration](https://cli.github.com/manual/gh_auth_setup-git)
