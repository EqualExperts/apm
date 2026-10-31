---
name: "test-driven-development"
description: "Use when implementing a feature or fixing a bug with test-first red-green-refactor development."
---

# Test-Driven Development

Define the next observable behaviour and use the project's existing test runner. Write one focused test through a public interface, avoiding assertions about incidental implementation details.

Run the test before implementation. Confirm it fails because the behaviour is missing, not because of imports, syntax, unavailable services or a broken fixture. If it already passes, determine whether the behaviour exists or the assertion misses the requirement.

Make the smallest implementation change that satisfies the behaviour. Run the focused test and relevant regression checks. Refactor only after green, rerunning affected checks. Repeat for the next behaviour. Prefer real collaborators; isolate external boundaries when necessary and verify mock contracts.

For existing code, preserve user work. Add characterization or regression coverage rather than deleting implementation to recreate a test-first history. Report honestly when tests were added after implementation. Follow explicit user constraints, including skipped tests; documentation and mechanical changes may warrant structural checks instead of a fabricated red phase.

Record the failing assertion, passing result and relevant commands. Do not call unavailable or unexecuted checks passing.

Read [worked scenarios](references/scenarios.md) when applying the workflow to ambiguous results. See [provenance and limitations](references/provenance.md) for upstream attribution and adaptation boundaries.
