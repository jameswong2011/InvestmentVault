---
type: thesis-manifest
batch: thesis-CRWV-2026-05-15-233458
status: completed
ticker: CRWV
proposed_name: CoreWeave
proposed_path: Theses/CRWV - CoreWeave.md
sector: Neoclouds & GPU-as-a-Service
date: 2026-05-15
completed_date: 2026-05-15
---

# Thesis Transaction Manifest (completed)

Manifest written at Step 3.5 before any file modifications. All stages succeeded.

## Thesis file creation
- Target path: `Theses/CRWV - CoreWeave.md`
- Status: created
- Conviction at creation: medium
- Status at creation: draft

## Sector note update
- Sector resolution: exact (`Neoclouds & GPU-as-a-Service` → `Sectors/Neoclouds & GPU-as-a-Service.md`)
- Sector note path: `Sectors/Neoclouds & GPU-as-a-Service.md`
- Edit applied: skipped (draft status) — per Step 5 SKILL.md contract, draft theses are added to sector Active Theses only on `/status TICKER status draft→active` promotion. Sector note already references CRWV in the existing "Coverage candidates" line of `## Active Theses`.

## `_hot.md` updates
- Active Research Thread entry: added (CRWV new lead; Murata compressed to *Previous:* line; INTC retained as condensed *Previous:* line)
- Recent Conviction Changes entry: added (full CRWV entry; Murata / INTU / PINS compressed to one-liners per hot-md-contract drop-oldest)
- Open Questions entries: 3 added (items 28-30: second-cycle Hopper re-rent rate, Microsoft 2027-2028 renewal cut, OpenAI $22.4B serviceability)
- Pre-edit word count: 4,978; post-edit word count: 4,916 (under 5,000 hard cap)

## Orphan research integration
- Orphan research notes touched: `Research/2025-06-09 - CRWV - CoreWeave Deep Dive.md` (sole match — has `tags: [research, CRWV, GPU-cloud, data-centers, AI-infrastructure]`)
- Wikilinks added to Related Research: 14 total in `## Related Research`:
  - 5 research notes (CRWV Deep Dive, Jensen Huang Moat, Dylan Patel AI Token, AI Bubble Risk Canvas, Insight Surface Scan)
  - 5 sector + macro context links (Neoclouds, Compute & AI Compute, Data Center Power, Custom Silicon, AI Bubble Risk Macro)
  - 6 cross-thesis strong (NVDA, VRT, META, AVGO, NET, BTC-CRYPTO)
  - 2 cross-thesis weak (TSM, PSTG)

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none (Signals A/B/C/D all empty)
- User decision: n/a

## Graph-primer cross-thesis suggestions (Step 2.5 output)
- Strong (counterparty / factor): NVDA, VRT, META
- Medium (architecture / pricing power): NET, AVGO, BTC-CRYPTO
- Weak (shared macro / broader stack): TSM, PSTG
- Acceptance: all Strong + Medium + Weak wired into thesis Related Research per sector-note adjacency context (no explicit user-accept gate fired; user can prune in editing)

## Recovery guidance

All steps landed successfully. Manifest flipped to `status: completed` at Step 7.5. Manifest ages out via `/clean` Step 2a (90/180 day tiers); surfaces in `/lint #49` only if some future skill bug returns it to `in-progress`.
