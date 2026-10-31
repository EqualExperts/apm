---
name: "systematic-debugging"
description: "Use when a test fails or software behaves unexpectedly and the cause needs investigation before a fix."
---

# Systematic Debugging

Read the full error and reproduce the smallest failing case. Record expected and observed behaviour, relevant versions and recent changes. If reproduction is intermittent, gather bounded diagnostics rather than guessing.

Trace data and control flow backward from the failure. At component boundaries inspect relevant inputs, outputs and configuration presence without printing secrets or client data. Compare a working path with the failing path and identify meaningful differences.

State a specific hypothesis and the evidence supporting it. Change one variable or run one discriminating experiment, then inspect the result. Reject contradicted hypotheses rather than stacking speculative fixes. Repeated failed attempts call for revisiting assumptions and scope; they do not prove that the architecture is wrong.

Once the cause is supported, add a regression test that reproduces it, implement a focused fix, and rerun the reproduction and affected checks. Use test-driven-development if installed for the red-green loop; this workflow also works independently. If evidence remains unavailable, state the unresolved cause and the next diagnostic needed. Preserve unrelated changes and respect access boundaries.

Read [worked scenarios](references/scenarios.md) when applying the workflow to ambiguous results. See [provenance and limitations](references/provenance.md) for upstream attribution and adaptation boundaries.
