---
grok_build: true
skill: /ingest
vault: /Users/alexcohen/InvestmentVault
status: done
article_url: 'https://247wallst.com/investing/2026/08/28/iren-just-locked-in-4-billion-in-arr-wall-street-still-sees-only-losses/'
---

# $ingest — IREN $4B Contracted ARR vs Earnings Miss (one article)

Source URL: https://247wallst.com/investing/2026/08/28/iren-just-locked-in-4-billion-in-arr-wall-street-still-sees-only-losses/
Date: 2026-08-29
Access: free full text (fetched)

Do **not** batch. One article = this job.

## Staging (on this Mac)

- Inbox clip: `_Inbox/grok-build-queue/staging/247-iren-4b-arr-clip.md`
- Draft research note (verify against `/ingest`, then file to `Research/`): `_Inbox/grok-build-queue/staging/2026-08-29 - IREN NBIS - IREN 4B Contracted ARR vs Earnings Miss - news.md`

## Command

```
$ingest /Users/alexcohen/InvestmentVault/_Inbox/grok-build-queue/staging/247-iren-4b-arr-clip.md
```

If the draft note already satisfies ingest verification (`verify_note.py`), file it to `Research/` under that filename and treat as Mode B local-file ingest of the source (dedup on `source:` URL). Do not create a second note. Do not change conviction/status.

Mark this job `status: done` when the Research note exists.
