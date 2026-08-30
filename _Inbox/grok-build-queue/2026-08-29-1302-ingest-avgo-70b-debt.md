---
grok_build: true
skill: /ingest
vault: /Users/alexcohen/InvestmentVault
status: done
article_url: 'https://finance.yahoo.com/technology/ai/articles/broadcom-avgo-nears-70b-debt-164236440.html'
---

# $ingest — Broadcom ~$70B AI Chip SPV Debt Talks (one article)

Source URL: https://finance.yahoo.com/technology/ai/articles/broadcom-avgo-nears-70b-debt-164236440.html
Date: 2026-08-29
Access: free full text (fetched)

Do **not** batch. One article = this job.

## Staging (on this Mac)

- Inbox clip: `_Inbox/grok-build-queue/staging/broadcom-70b-debt-clip.md`
- Draft research note (verify against `/ingest`, then file to `Research/`): `_Inbox/grok-build-queue/staging/2026-08-29 - AVGO - 70B AI Chip SPV Debt Talks Anthropic - news.md`

## Command

```
$ingest /Users/alexcohen/InvestmentVault/_Inbox/grok-build-queue/staging/broadcom-70b-debt-clip.md
```

If the draft note already satisfies ingest verification (`verify_note.py`), file it to `Research/` under that filename and treat as Mode B local-file ingest of the source (dedup on `source:` URL). Do not create a second note. Do not change conviction/status.

Mark this job `status: done` when the Research note exists.
