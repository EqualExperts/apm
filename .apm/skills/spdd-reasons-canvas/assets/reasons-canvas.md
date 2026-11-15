# REASONS canvas

Record the outcome, artifact identity, source requirement/analysis links, inspected revision and actual decision status. Preserve existing repository locations and naming.

## Requirements

State user-visible outcomes, scope exclusions and acceptance criteria with stable IDs. Include expected failure behaviour where relevant. Keep assumptions and unresolved decisions explicit.

## Entities

Describe domain concepts, state and relationships. Distinguish existing structures from proposed ones. Link source evidence; add a Mermaid diagram only when useful.

## Approach

Record the chosen strategy, trade-offs and rejected alternatives that explain the decision. Identify unresolved choices and constraints on implementation.

## Structure

Identify affected components, interfaces and dependencies. Describe where the change fits and which existing boundaries must remain. Use Mermaid for useful diagrams with supporting prose.

## Operations

Define ordered, independently verifiable work. Give each operation an identifier, prerequisites, intended changes, acceptance-criterion links and planned checks. Preserve necessary public signatures and contracts without reproducing implementation bodies.

## Norms

Link applicable repository conventions for code, tests, logging, documentation and review. Explain any agreed exception; do not invent organisation policy.

## Safeguards

Record applicable invariants, authorization, privacy, compatibility, performance and data-integrity boundaries. Associate each safeguard with a planned check or explicit review. State which claims need unavailable environments.

## Acceptance evidence

For each criterion record its operation, implementation location, verification command or review, observed result and remaining gap. Mark planned checks as planned, never passed.

## Decisions and change record

Record intent changes and their source, unresolved decisions, superseded reasoning, and code-driven structural updates. Preserve the distinction between desired behaviour and observed implementation.
