# Readiness evidence

Run the smallest useful checks from the chosen assistant's execution environment. For GitHub workflows, the following are read-only checks after substituting the intended host and repository:

```text
git --version
gh --version
gh auth status --active --hostname HOST
gh api --hostname HOST user --jq .login
gh repo view HOST/OWNER/REPO --json nameWithOwner,viewerPermission
```

Use the literal host and repository supplied by the user or verified from the workspace. Do not execute placeholder values. Report identity only as needed for the user's task; never include token output.

| Check | Evidence | Limitation |
| --- | --- | --- |
| Tool installed | Version command succeeds | Does not prove service access |
| Assistant can invoke tool | Same command succeeds in its runtime | Does not establish unattended auth |
| Authentication | Correct active account and identity query | Does not prove repository permission |
| Repository access | Read query for the intended repository succeeds | Does not prove push or deployment permission |
| Skill discovery | Selected harness exposes the installed skill | Does not prove the workflow was completed |

Do not create issues, push commits, provision resources or send messages merely to test setup. Stop dependent steps when interactive login, organisational authorisation or missing access blocks progress. Distinguish these from package-install failures.

Report ready, partial or blocked with the specific evidence and next action. No changes required is a valid result when existing setup passes. Do not claim all-platform or all-harness compatibility based on one machine.
