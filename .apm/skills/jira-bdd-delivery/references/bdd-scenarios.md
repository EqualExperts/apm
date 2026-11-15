# From ticket intent to executable examples

BDD starts with shared understanding of behaviour. From the selected ticket, identify the user outcome, business rules, concrete examples and unresolved questions. Retain a stable mapping from each acceptance criterion to its examples and verification. Ask for decisions that change observable behaviour; routine implementation choices can follow repository conventions.

Use business language and observable outcomes. A useful scenario describes initial context, an action and its result. Gherkin is suitable when the project already uses it: Given establishes context, When expresses the action and Then checks the outcome. Use Scenario Outline only when multiple data rows represent the same rule. Reuse domain vocabulary and step definitions; avoid a separate low-level UI script for every user action.

Cucumber is not compulsory. A project's existing integration or acceptance test runner can encode the same examples. Adding a new BDD framework is a separate dependency choice, not a prerequisite for applying this skill. A `.feature` document without working step definitions is a specification, not passing coverage.

For applicable rules consider normal, boundary, invalid, unauthorized and conflicting/concurrent cases. Test the real behaviour at the appropriate boundary and avoid asserting only that mocks were called. Use approved isolated data and retain the repository's requirements for integration services.

## Synthetic ticket example

This invented example contains no client data. Ticket `DEMO-42` requests order cancellation. The agreed rules are: an owner can cancel a pending order; another user is denied; a shipped order cannot be cancelled. The example assumes those rules were supplied, not inferred from existing code.

```gherkin
@DEMO-42
Feature: Cancel an order
  Scenario: Owner cancels a pending order
    Given a pending order belongs to the signed-in customer
    When the customer cancels the order
    Then the order is cancelled

  Scenario: Another customer cannot cancel the order
    Given a pending order belongs to a different customer
    When the signed-in customer attempts to cancel it
    Then the request is denied
    And the order remains pending

  Scenario: A shipped order cannot be cancelled
    Given a shipped order belongs to the signed-in customer
    When the customer attempts to cancel it
    Then the cancellation is rejected
    And the order remains shipped
```

Map the first scenario to criterion AC-1, the second to AC-2 and the third to AC-3. Exact HTTP codes, error payloads, race behaviour and side effects must come from the agreed contract. If unspecified and consequential, record questions rather than inventing them. A failure in AC-2 must not be addressed by weakening the deny rule.

Primary guidance: [BDD](https://cucumber.io/docs/bdd/), [Example Mapping](https://cucumber.io/docs/bdd/example-mapping/), [Gherkin reference](https://cucumber.io/docs/gherkin/reference/) and [writing better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/). Consult the parts relevant to the project's chosen runner and specification style.
