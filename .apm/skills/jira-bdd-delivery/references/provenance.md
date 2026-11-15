# Scope, sources and limitations

Independently authored for this marketplace on 2026-11-15 from primary Cucumber and Atlassian documentation. No third-party skill, vendor example, implementation or client ticket was copied. The example is invented. Vendor sources remain linked under their own terms; no vendor endorsement or imported software licence is claimed.

Sources reviewed:

- [Cucumber BDD](https://cucumber.io/docs/bdd/) for collaborative discovery and behavioural examples.
- [Example Mapping](https://cucumber.io/docs/bdd/example-mapping/) for separating business rules, examples and unanswered questions.
- [Gherkin reference](https://cucumber.io/docs/gherkin/reference/) and [writing better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/) for scenario structure and observable behaviour.
- [Jira Cloud issue API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/) for issue reads and workflow-specific transitions.
- [Jira webhooks](https://developer.atlassian.com/cloud/jira/platform/webhooks/) and [rate limits](https://developer.atlassian.com/cloud/jira/platform/rate-limiting/) for external integration boundaries.

APM-specific decisions: use verified implementation plus a review-ready PR as the default agent delivery boundary; preserve stricter ticket criteria; distinguish Jira state from delivery state; maintain resumable evidence; require progress from each iteration; bound identical transient retries; reconcile writes on retry; and honour actual user/harness permissions. These are authored workflow choices, not Cucumber or Atlassian guarantees.

Tier: experimental. Stewardship: Equal Experts APM maintainers; individual long-term ownership unassigned. Requires authorized ticket context, the target repository and its build/test tools. Live issue reads/writes and PR publication need suitable authenticated integrations and network access. There is no required MCP brand, mandatory Cucumber installation or dependency on SPDD. The skill does not install a runner or enable a background trigger.

Review [the scenario cases](review-scenarios.md) for instruction-level checks. Structural/content checks and catalogue browser tests do not establish live Jira integration, autonomous completion, cross-harness reliability or production acceptance. No client tickets, external transitions, PR deliveries or live triggers were exercised for this addition.

Parent/child coordination is an optional APM workflow mode: the parent owns the ticket run and external updates, children execute ready independent tasks, and joined results are verified at the combined revision. The companion parallel-stage-orchestration skill supplies platform documentation; it is not required for sequential ticket delivery.
