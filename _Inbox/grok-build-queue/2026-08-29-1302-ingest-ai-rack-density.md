---
grok_build: true
skill: /ingest
vault: /Users/alexcohen/InvestmentVault
status: done
article_url: 'https://www.datacenterknowledge.com/ai-data-centers/ai-rack-density-s-real-limits-power-cooling-failure-risk'
---

# $ingest — AI Rack Density Power Cooling Limits (one article)

Source URL: https://www.datacenterknowledge.com/ai-data-centers/ai-rack-density-s-real-limits-power-cooling-failure-risk
Date: 2026-08-29
Access: free full text (fetched)

Do **not** batch. One article = this job.

## Staging (on this Mac)

- Inbox clip: `_Inbox/grok-build-queue/staging/dck-ai-rack-density-clip.md`
- Draft research note (verify against `/ingest`, then file to `Research/`): `_Inbox/grok-build-queue/staging/2026-08-29 - NVDA NBIS - AI Rack Density Power Cooling Limits - news.md`

## Command

```
$ingest /Users/alexcohen/InvestmentVault/_Inbox/grok-build-queue/staging/dck-ai-rack-density-clip.md
```

If the draft note already satisfies ingest verification (`verify_note.py`), file it to `Research/` under that filename and treat as Mode B local-file ingest of the source (dedup on `source:` URL). Do not create a second note. Do not change conviction/status.

Mark this job `status: done` when the Research note exists.
