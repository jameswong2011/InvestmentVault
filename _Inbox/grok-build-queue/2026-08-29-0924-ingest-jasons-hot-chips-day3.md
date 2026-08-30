---
grok_build: true
skill: /ingest
vault: /Users/alexcohen/InvestmentVault
status: done
---

# $ingest — Jason's Chips Hot Chips Day 3 (one article)

Pub: Jason's Chips
Title: Hot Chips Day 3 - Spicy (Jalapeno) Chips
Source URL: https://www.jasonschips.ai/p/hot-chips-day-3-spicy-jalapeno-chips
Date: 2026-08-26
Access: free full post

Do **not** batch. One article = this job.

## Staging (on this Mac)

- Source: `_Inbox/grok-build-queue/staging/2026-08-26-jasons-hot-chips-day-3.md`
- Draft research note (use as starting point; verify against `/ingest`, then file to `Research/`): `_Inbox/grok-build-queue/staging/2026-08-26 - NVDA AVGO 000660 SNDK - Jasons Chips Hot Chips Day 3 Jalapeno - deep-dive.md`

## Command

```
$ingest /Users/alexcohen/InvestmentVault/_Inbox/grok-build-queue/staging/2026-08-26-jasons-hot-chips-day-3.md
```

If the draft note already satisfies ingest verification, file it to `Research/` under that filename and treat as Mode B local-file ingest of the source (dedup on `source:` URL). Do not create a second note. Wikilink existing Jalapeño news notes rather than duplicating them.

Mark this job `status: done` when the Research note exists.
