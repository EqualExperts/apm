# Verify effective access

After checking version and authentication status, substitute the actual host and repository:

```text
gh api --hostname HOST user --jq .login
gh repo view HOST/OWNER/REPO --json nameWithOwner,viewerPermission
```

The first query verifies effective identity; the second checks read access to one known repository and reports its permission level. Avoid listing unrelated private repositories. The examples are read-only; write tests are unnecessary for setup.

| Observation | Next step |
| --- | --- |
| Executable missing in assistant only | Compare executable discovery and runtime boundaries before reinstalling |
| Saved login exists but identity is wrong | Check host and environment-token presence without revealing values |
| Host authentication succeeds, repository lookup fails | Confirm repository name, account, organisational SSO/token approval and access; a 404 can conceal an inaccessible private repository |
| Repository read works, feature operation fails | Check that operation's permissions, repository/organisation policy and plan entitlement; do not infer universal access |
| Login requires user interaction | Hand the local login step to the user and resume once completed |

Do not interpret JSON-formatted auth-status command success alone as healthy authentication; consult status fields and the actual API read. If the requested environment cannot run the checks, report that limitation rather than claiming setup complete.

## Review scenarios

- Existing healthy setup: verify without reinstalling, switching accounts or changing Git configuration.
- Multiple accounts plus an environment token: explain effective identity and avoid a host-wide switch that would not change the token-backed identity.
- Private repository access denied: report a partial setup and the access action needed; do not create a replacement repository or broaden token permissions by default.
- Missing CLI in a container: install or expose the CLI in the intended runtime, not merely on the host.

These scenarios guide future behavioural evaluation; they are not claims of completed testing. See [repository view](https://cli.github.com/manual/gh_repo_view) and [API requests](https://cli.github.com/manual/gh_api) for current flags.
