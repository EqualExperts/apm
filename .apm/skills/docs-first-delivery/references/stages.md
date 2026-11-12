# Delivery stages

For adoption, inspect the existing build, documentation, tests and entrypoints first. Produce a small map of observed facts and gaps; do not replace working conventions merely to fit this workflow. For continuation, recheck the latest record against the checkout before treating its claims as current.

| Stage | Useful output | Exit evidence |
| --- | --- | --- |
| 1. Scope and architecture | Outcome, exclusions, actors, boundaries, constraints, current behaviour and proposed change; diagrams only where useful. | The problem is understood; consequential unknowns are resolved or explicitly block dependent work. |
| 2. Contracts and design | Observable acceptance criteria, interfaces, data and error contracts, security boundaries and integration decisions. | Happy paths and relevant failure paths are testable; design agrees with repository policy and compatibility requirements. |
| 3. Implementation plan | Ordered slices, criterion-to-test mapping, dependencies, risks, migration and recovery steps where needed. | Each slice has a concrete verification method; decisions and required review gates have been satisfied. |
| 4. Delivery and verification | Implementation, tests, updated docs and dated evidence. | Acceptance criteria map to observed outcomes; gaps are visible and completion claims are bounded. |

Reuse existing specifications and decisions rather than duplicating them. A small change can use one concise record. A complex change may need linked architecture, contract and plan files. Never manufacture approval, policy compliance or runtime behaviour to fill an artifact.

## Review and scope changes

Record who or what established a required gate and whether prior authorization covers it. A general permission to implement does not resolve an ambiguous product decision. A documented blanket approval can waive repeated pauses while preserving the stage outputs. A skip marks an optional artifact as inapplicable with a reason; it does not convert missing acceptance evidence into a pass.

When implementation reveals a contradiction, describe the conflicting contract and observation, update the affected specification and tests within authorized scope, and obtain a decision if the change affects agreed behaviour. Do not silently rewrite acceptance criteria to fit failing code.

## Verification matrix

Use stable criterion identifiers and record: expected behaviour, affected component, test/check, observed result, evidence location and remaining gap. Include negative cases relevant to the change, such as rejected authorization, invalid input, partial failure, duplicate delivery or concurrent updates. Do not add unrelated infrastructure or run production repairs merely to populate the matrix.

Run focused checks first, then the consuming project's required checks. Verify the actual changed artifacts were tested. Report the revision, environment, command, test counts and skips. Record CI and deployed behaviour separately from local evidence.
