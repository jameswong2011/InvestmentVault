---
grok_build: true
skill: /queue
vault: /Users/alexcohen/InvestmentVault
status: queued
---

# Run the Vault Boss queue

You are Grok Build on this vault. Process every job in `_Inbox/grok-build-queue/` with `status: queued`. Do not batch several `$ingest` articles into one run.

## Order

1. Each `$ingest` job, one article at a time (use the staging clip + draft named in that job):
   - `2026-08-29-0924-ingest-photoncap-reading-list.md`
   - `2026-08-29-0924-ingest-jasons-hot-chips-day3.md`
   - `2026-08-29-1302-ingest-mrvl-q2-fy27.md`
   - `2026-08-29-1302-ingest-nbis-575b-convert.md`
   - `2026-08-29-1302-ingest-nvda-denies-acp-pause.md`
   - `2026-08-29-1302-ingest-neocloud-tape-acp.md`
   - `2026-08-29-1302-ingest-000660-indiana-hbm.md`
   - `2026-08-29-1302-ingest-samsung-8hi-nvhbm.md`
   - `2026-08-29-1302-ingest-ai-rack-density.md`
   - `2026-08-29-1302-ingest-avgo-70b-debt.md`
   - `2026-08-29-1302-ingest-iren-4b-arr.md`
2. One `$sync` for the notes just filed (those files only). Then mark both `2026-08-29-0924-sync.md` and `2026-08-29-1302-sync.md` done.
3. One `$graph last`. Then mark both graph jobs done.

After each job: set that file's frontmatter `status: done`. Do not change conviction/status. Skip README.md and this file.
