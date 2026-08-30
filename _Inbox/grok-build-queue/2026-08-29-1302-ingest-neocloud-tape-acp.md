---
grok_build: true
skill: /ingest
vault: /Users/alexcohen/InvestmentVault
status: done
article_url: 'https://www.tipranks.com/news/neocloud-stocks-fall-as-nvidia-shelves-revenue-sharing-deals-heres-why'
---

# $ingest — Neocloud Tape on Nvidia ACP Pause Report (one article)

Source URL: https://www.tipranks.com/news/neocloud-stocks-fall-as-nvidia-shelves-revenue-sharing-deals-heres-why
Date: 2026-08-29
Access: free full text (fetched)

Do **not** batch. One article = this job.

## Staging (on this Mac)

- Inbox clip: `_Inbox/grok-build-queue/staging/tipranks-neocloud-nvidia-shelves-clip.md`
- Draft research note (verify against `/ingest`, then file to `Research/`): `_Inbox/grok-build-queue/staging/2026-08-29 - NBIS CRWV IREN - Neocloud Tape on Nvidia ACP Pause Report - news.md`

## Command

```
$ingest /Users/alexcohen/InvestmentVault/_Inbox/grok-build-queue/staging/tipranks-neocloud-nvidia-shelves-clip.md
```

If the draft note already satisfies ingest verification (`verify_note.py`), file it to `Research/` under that filename and treat as Mode B local-file ingest of the source (dedup on `source:` URL). Do not create a second note. Do not change conviction/status.

Mark this job `status: done` when the Research note exists.
