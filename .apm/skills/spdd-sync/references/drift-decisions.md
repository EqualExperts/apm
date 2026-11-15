# Drift decisions

Synchronisation reconciles evidence with intent; it does not make every implementation change correct.

| Observation | Classification and response |
| --- | --- |
| Internal class renamed; intended behaviour and relevant tests unchanged | Update structural references and diagrams; state the scope of verified equivalence. |
| Request says to add a new outcome and identifies the agreed decision | Update requirement and safeguards through the intent-change path, then reconcile implementation references and acceptance evidence. |
| Endpoint now permits access that the canvas denies | Record a regression; preserve the deny rule and expected test result. Do not synchronise the weaker permission into the specification. |
| Source and canvas disagree but no decision or adequate test evidence exists | Record unresolved intent or unverified drift; inspect relevant evidence and ask only for the missing decision. |
| A file was removed during an authorized refactor | Update references to the replacement where supported, preserving the rationale and criterion history. |

## Worked example

An internal `PriceCalculator` was renamed to `UsageCalculator`. The canvas still references the old class. The public usage endpoint and its accepted rounding rule are unchanged. Inspection and the relevant tests confirm the rename preserves those contracts. Update Entities, Structure and Operations with the new location, and record the checks inspected.

If the same diff also changes the rounding rule without an authorized requirement change, keep the existing rounding criterion and report the discrepancy. A green test rewritten to use the new value is insufficient evidence of accepted intent. A sync-only request does not authorize fixing the implementation as an additional task.
