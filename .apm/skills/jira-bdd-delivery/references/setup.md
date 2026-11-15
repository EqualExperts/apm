# Setup and environment configuration

Use this guide before the first ticket run or when access stops working. It covers Jira Cloud; for Data Center, use the installed version's authentication and REST documentation. Installing the skill supplies instructions. Jira access, repository credentials and any event runner must be configured in the consuming environment.

## 1. Install and choose the connection

In the [catalogue](https://equalexperts.github.io/apm/), select Jira BDD Delivery Stack, choose the target assistant and run its generated installation commands in the consuming repository. The stack includes five skills; refresh or start an agent session as required by that assistant. An existing installation of the delivery skill alone can also run sequentially.

Use an existing connected Jira integration when it exposes the needed operations. Use direct REST only when that is the chosen, permitted access method. Do not configure both merely to install this skill.

### Connected Jira integration

1. Open the assistant's integration settings and connect the organization's approved Jira integration. For Atlassian's hosted option, follow the [Rovo MCP setup guide](https://developer.atlassian.com/cloud/rovo-mcp/guides/getting-started/); its documented server URL at review time is `https://mcp.atlassian.com/v2/mcp`.
2. Complete the connector's sign-in and site-selection flow. Atlassian recommends OAuth for interactive use. Organization policy and the user's Jira permissions still apply.
3. Refresh the agent session if needed and discover the actual tools. Verify issue retrieval is available; separately check comment and transition capabilities if those actions are part of the requested delivery.

The OAuth route does not require the REST environment variables below. The connector manages authentication. If a selected connector uses API tokens instead, follow its own configuration schema: these variable names are not universal MCP settings.

### Direct Jira Cloud REST access

For a user-operated local script or agent REST adapter, use an account API token according to [Atlassian's token guide](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/). Choose scopes for the actual read/write operations, set an expiry and retain the token in approved secret storage. Account passwords are not API tokens. Shared integrations should follow the [Cloud authentication guidance](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/) rather than collecting users' tokens.

Use these names as this guide's convention for a local REST adapter. Configure its mapping explicitly if it expects different names. The skill itself is Markdown: it does not load a `.env` file or configure an HTTP client automatically.

| Variable | Value and use |
| --- | --- |
| `JIRA_BASE_URL` | Verified site origin, such as `https://your-team.atlassian.net`, without an issue path. Used for site identity and site-based API requests. |
| `JIRA_EMAIL` | Email of the Atlassian account that created the personal API token. |
| `JIRA_API_TOKEN` | The token, supplied through the process environment or the adapter's secret store. Never include its value in the task prompt, delivery record or repository. |
| `JIRA_CLOUD_ID` | The site's verified Cloud ID, required for the scoped-token gateway route below. It is not the organization ID or project key. |

Set these in the terminal, IDE launch environment or runner configuration that actually starts the REST-capable agent. For a runner, bind `JIRA_API_TOKEN` to a secret reference; for interactive use, use its secret input or credential store. A shell setting reaches new child processes, not an already-running IDE or remote agent. Restart or reconnect the relevant process and check variable presence without displaying values.

The following is a configuration example, not an executable script. Replace the non-secret placeholders and inject the real token separately. A `.env` file is effective only if the chosen adapter explicitly loads it; keep any real credential file outside version control.

```text
JIRA_BASE_URL=https://your-team.atlassian.net
JIRA_EMAIL=you@example.com
JIRA_API_TOKEN=<injected-secret>
JIRA_CLOUD_ID=<verified-site-cloud-id>
```

Record whether the personal token has scopes; do not guess from its length or value. Construct requests using the matching route:

| Account API token | API root for Jira Cloud v3 |
| --- | --- |
| With scopes | `https://api.atlassian.com/ex/jira/{JIRA_CLOUD_ID}/rest/api/3` |
| Without scopes, where the integration permits it | `{JIRA_BASE_URL}/rest/api/3` |

Both rows describe personal account tokens using HTTP Basic authentication with `JIRA_EMAIL` as username and `JIRA_API_TOKEN` as password. Let the HTTP client form the header; never log it. OAuth access tokens and service-account authentication have their own contracts and must not be substituted blindly. Obtain the Cloud ID using [Atlassian's site ID instructions](https://support.atlassian.com/jira/kb/retrieve-my-atlassian-sites-cloud-id/) and confirm it belongs to the selected site. Use verified HTTPS endpoints, retain certificate checks and do not forward credentials through an unexpected redirect.

## 2. Verify access without changing a ticket

Use one issue the user selected and is permitted to read. With a connector, call its issue-read tool using the discovered schema. With REST, request `GET {API_ROOT}/issue/{ISSUE_KEY}?fields=summary,status` using the API root above. Confirm the returned key and expected site/project. Do not enumerate the backlog to test connectivity.

Then retrieve the fields needed for delivery, including the project's actual acceptance-criteria fields. Discover custom-field identifiers rather than assuming a shared ID. Consult the [issue API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/) for endpoint scopes and permissions. When transitions are in scope, `GET {API_ROOT}/issue/{ISSUE_KEY}/transitions?expand=transitions.fields` discovers currently available transitions and requirements without taking one. A successful read does not establish permission to write, create a PR or complete a ticket.

| Result | Next check |
| --- | --- |
| No Jira tools or missing variables | Check the active agent process, connector installation and environment inheritance. |
| HTTP 401 | Check effective account, token expiry and authentication method without displaying credentials. |
| HTTP 403 | Check scopes, project/issue permissions and organization access policy. Repeated retries do not grant access. |
| HTTP 404 | Confirm the selected key and site/Cloud ID; inaccessible issues may also appear missing. |
| HTTP 429 | Respect `Retry-After` and the bounded retry rules in the delivery loop. |
| HTML, redirects or unexpected host | Check the API root and network/SSO configuration before sending further authenticated requests. |

## 3. Prepare delivery and start

Map the selected issue to the correct local checkout and remote repository. Verify its test/build commands and authenticate the repository integration separately for any authorized branch publication and PR work. Jira credentials do not provide Git hosting access. Record the selected issues, allowed actions, completion boundary and checkpoint location in [the delivery record](../assets/delivery-record.md). Keep credentials out of that record.

For a first run, adapt this synthetic request to the user's actual scope:

> Use jira-bdd-delivery for DEMO-42 in this checkout. Read the ticket, derive acceptance scenarios, implement and verify them, and prepare a review-ready PR using the authorized repository integration. Keep Jira updates within the agreed actions and continue until the delivery boundary is met or a concrete blocker is recorded.

A session can execute the loop once invoked. Automatic Jira-triggered runs additionally need the external dispatcher described in [Jira integration and dispatch](jira-integration.md); no environment variable in this guide enables one. Parent/child execution likewise depends on the active platform's capabilities and permissions, with sequential fallback.

Documentation reviewed on 2026-11-15. Setup instructions and local content checks do not establish a successful connection to any user's Jira instance.
