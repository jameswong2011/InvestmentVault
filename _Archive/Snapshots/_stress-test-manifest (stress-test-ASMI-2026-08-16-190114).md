---
type: stress-test-manifest
batch: stress-test-ASMI-2026-08-16-190114
status: completed
ticker: ASMI
date: 2026-08-16
completed_date: 2026-08-16
---

# Stress Test Manifest

> **If `status: in-progress`**, `/stress-test` crashed between Phase 4.0 (skeleton)
> and Phase 4.6 (flip). The Log entry on `Theses/ASMI - ASM International.md` may or may not
> have landed; check the thesis `## Log` for today's date + `Stress test` prefix.
> Recovery: manually complete or strike through the entry, then flip this
> manifest's `status:` to `completed` or `rm` the manifest.
>
> **If `status: completed`**, Phase 4 finished cleanly. `/rollback` Step 2.5d
> can surface the recorded Log entry for strikethrough review.

## Research note created
- [[Research/2026-08-16 - ASMI - Stress Test]]

## Thesis Log entry appended (Tier B — no snapshot)
- Target: `Theses/ASMI - ASM International.md`
- Entry date: 2026-08-16
- Entry text: `Stress test [[Research/2026-08-16 - ASMI - Stress Test]]: "POR annuity" is the basket's thinnest service floor + 1.4nm POR unverified/rev 2028+ + Q2 order miss the note omits — 5/8 assumptions 🔴 — conviction weakened: reassess high→medium (matches thesis's own unreconciled Summary "medium pending 1.4nm").`
- Log append outcome: succeeded

## Recovery guidance

To undo this stress test's Log entry (e.g., the stress test was based on wrong
input and the Log entry misrepresents current conviction state):

  /rollback stress-test-ASMI-2026-08-16-190114
  → Step 2.5d matches this manifest by batch ID
  → Presents the Log entry above for strikethrough annotation
  → User can choose: (1) leave as historical audit (Tier 2 append-only respected)
                     (2) strikethrough with `~~entry~~ → Reverted YYYY-MM-DD:
                        stress test was invalid because...`
                     (3) manually delete (violates Tier 2 — only for clearly
                        erroneous entries)

The research note at `Research/2026-08-16 - ASMI - Stress Test.md` is NOT
deleted by rollback — it persists as historical record.
