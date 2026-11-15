---
name: "spdd-sync"
description: "Reconcile an SPDD REASONS canvas with observed code changes after refactoring or implementation, distinguishing harmless structural drift from behavioural regressions and unapproved requirement changes. Use for code-to-spec synchronisation, not for approving changed product behaviour."
---

# SPDD code-to-spec synchronisation

Read [provenance and adaptation boundaries](references/provenance.md) and [drift decisions](references/drift-decisions.md). Identify the current canvas, relevant change set and existing verification evidence. Use source inspection and scoped diffs; do not infer intended requirements from the implementation alone.

Classify discrepancies as structural/naming changes, authorized behaviour changes, implementation defects or unresolved intent. Review affected interfaces, entity relationships, operation dependencies and safeguards. Record source locations and evidence for each classification.

For structural changes that preserve intended behaviour, update the affected Entities, Structure and Operations references and diagrams. Preserve the canvas identity and useful rationale. For authorized behaviour changes, trace the decision through Requirements, Safeguards and acceptance evidence before synchronising the remaining sections.

If code violates an unchanged requirement or safeguard, keep that requirement and record a defect. Do not overwrite error contracts, authorization rules or expected outcomes to match a regression. Resolve unclear intent before changing the specification; continue independent reconciliation where possible.

Recheck cross-section references and record whether behavioural equivalence was observed, tested or remains unverified. Do not run unavailable integrations or claim unexecuted checks succeeded. Follow repository rules for durable artifacts and use Mermaid for diagrams.

Report reconciled sections, discrepancies left open, evidence and required follow-up. Synchronisation updates documentation; it does not authorize unrelated code changes, a commit, release or deployment.

Use supported, permitted child agents for parallel read-only drift analysis of independent components at a fixed revision. Children return evidence and classifications; the parent reconciles conflicts and is the sole writer of the canonical canvas. Reject stale results after relevant input changes. Use parallel-stage-orchestration if installed for coordination; fall back to sequential review when delegation is unavailable.
