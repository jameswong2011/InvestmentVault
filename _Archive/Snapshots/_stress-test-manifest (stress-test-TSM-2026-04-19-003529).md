---
type: stress-test-manifest
batch: stress-test-TSM-2026-04-19-003529
status: completed
ticker: TSM
date: 2026-04-19
---

# Stress Test Manifest

> Sidecar for `/stress-test TSM` run on 2026-04-19 (focus: China invasion of Taiwan). Used by `/rollback` Step 2.5d cascade detection: when the user selects this batch ID, the Log entry below is surfaced for strikethrough review.

## Research note created
- [[Research/2026-04-19 - TSM - Stress Test]]

## Thesis Log entry appended (Tier B — no snapshot)
- Target: `Theses/TSM - Taiwan Semiconductor.md`
- Entry date: 2026-04-19
- Entry text:
  ```
  - Stress test [[Research/2026-04-19 - TSM - Stress Test]]: Taiwan invasion/blockade scenario mispriced as -30% position risk when realistic downside is -85-95% permanent impairment (destroy-the-fabs protocol + Arizona is 5-8% of capacity through 2030). 8/9 assumptions rated 🔴 — conviction weakened: reassess medium→low pending Taiwan macro research + Arizona capacity re-quantification.
  ```
- Log append outcome: succeeded

## Recovery guidance

To undo this stress test's Log entry (e.g., the stress test was based on wrong
input and the Log entry misrepresents current conviction state):

  /rollback stress-test-TSM-2026-04-19-003529
  → Step 2.5d matches this manifest by batch ID
  → Presents the Log entry above for strikethrough annotation
  → User can choose: (1) leave as historical audit (Tier 2 append-only respected)
                     (2) strikethrough with `~~entry~~ → Reverted YYYY-MM-DD:
                        stress test was invalid because...`
                     (3) manually delete (violates Tier 2 — only for clearly
                        erroneous entries)

The research note at `Research/2026-04-19 - TSM - Stress Test.md` is NOT
deleted by rollback — it persists as historical record (same rule as scenario
research notes).
