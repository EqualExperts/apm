---
name: "verification-before-completion"
description: "Use before reporting that a change is complete, a defect is fixed, or checks pass; match each claim to current evidence."
---

# Verification Before Completion

Identify what evidence supports each intended claim. Run the appropriate checks against the final changed state, inspect their exit status and relevant output, and report the actual scope. Reuse current results when no subsequent change invalidates them; do not repeat expensive checks solely for presentation.

Distinguish focused tests, full suites, builds, static checks, hosted CI, deployment and runtime acceptance. A successful build does not prove a bug is fixed. For a defect, verify the original reproduction and appropriate regression coverage. Review the diff against the requested requirements, including unrelated changes and omissions.

If another agent or tool reports success, inspect the resulting artifacts and evidence before adopting that claim. Do not infer authorization to delegate or publish from this workflow.

When checks are skipped, blocked, timed out or unavailable, say so and limit the conclusion accordingly. Honour explicit instructions not to run tests. Report meaningful warnings and remaining uncertainty without claiming unsupported assurance.

Read [worked scenarios](references/scenarios.md) when applying the workflow to ambiguous results. See [provenance and limitations](references/provenance.md) for upstream attribution and adaptation boundaries.
