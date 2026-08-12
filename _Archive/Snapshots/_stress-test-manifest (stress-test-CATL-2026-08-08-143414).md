---
type: stress-test-manifest
batch: stress-test-CATL-2026-08-08-143414
status: completed
ticker: CATL
date: 2026-08-08
completed_date: 2026-08-08
---

# Stress Test Manifest

> **If `status: in-progress`**, `/stress-test` crashed between Phase 4.0 (skeleton)
> and Phase 4.6 (flip). The Log entry on `Theses/CATL - Contemporary Amperex Technology.md` may or may not
> have landed; check the thesis `## Log` for today's date + `Stress test` prefix.
> Recovery: manually complete or strike through the entry, then flip this
> manifest's `status:` to `completed` or `rm` the manifest.
>
> **If `status: completed`**, Phase 4 finished cleanly. `/rollback` Step 2.5d
> can surface the recorded Log entry for strikethrough review.

## Research note created
- [[Research/2026-08-08 - CATL - Stress Test]]

## Thesis Log entry appended (Tier B — no snapshot)
- Target: `Theses/CATL - Contemporary Amperex Technology.md`
- Entry date: 2026-08-08
- Entry text: `- Stress test [[Research/2026-08-08 - CATL - Stress Test]]: top vulnerability = ESS margin-premium engine (insight #1) inverting in live H1'26 data (blended GM −1.09pp→23.93%; fixed-price ESS contracts compressing on lithium reflation) + unmodeled VAT export-rebate abolition (→0% Jan'27) vs the 29.97% overseas margin engine; 3/6 bull assumptions 🔴 — conviction weakened: reassess medium→low (both core mispricing pillars under live attack; multiple de-rating now — JPM H-share cut to Neutral, record HK shorts — not re-rating up as thesis assumes).`
- Log append outcome: succeeded

## Recovery guidance

To undo this stress test's Log entry (e.g., the stress test was based on wrong
input and the Log entry misrepresents current conviction state):

  /rollback stress-test-CATL-2026-08-08-143414
  → Step 2.5d matches this manifest by batch ID
  → Presents the Log entry above for strikethrough annotation
  → User can choose: (1) leave as historical audit (Tier 2 append-only respected)
                     (2) strikethrough with `~~entry~~ → Reverted YYYY-MM-DD:
                        stress test was invalid because...`
                     (3) manually delete (violates Tier 2 — only for clearly
                        erroneous entries)

The research note at `Research/2026-08-08 - CATL - Stress Test.md` is NOT
deleted by rollback — it persists as historical record (same rule as scenario
research notes).
