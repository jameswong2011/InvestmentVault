---
grok_build: true
skill: /ingest
vault: /Users/alexcohen/InvestmentVault
status: done
article_url: 'https://nebius.com/newsroom/nebius-group-announces-closing-of-private-offering-of-convertible-senior-notes-with-aggregate-gross-proceeds-of-approximately-5-75-billion'
---

# $ingest — Nebius Closes $5.75B Convertible Notes (one article)

Source URL: https://nebius.com/newsroom/nebius-group-announces-closing-of-private-offering-of-convertible-senior-notes-with-aggregate-gross-proceeds-of-approximately-5-75-billion
Date: 2026-08-29
Access: free full text (fetched)

Do **not** batch. One article = this job.

## Staging (on this Mac)

- Inbox clip: `_Inbox/grok-build-queue/staging/nebius-575b-convertible-clip.md`
- Draft research note (verify against `/ingest`, then file to `Research/`): `_Inbox/grok-build-queue/staging/2026-08-29 - NBIS - 5.75B Convertible Notes Closing - news.md`

## Command

```
$ingest /Users/alexcohen/InvestmentVault/_Inbox/grok-build-queue/staging/nebius-575b-convertible-clip.md
```

If the draft note already satisfies ingest verification (`verify_note.py`), file it to `Research/` under that filename and treat as Mode B local-file ingest of the source (dedup on `source:` URL). Do not create a second note. Do not change conviction/status.

Mark this job `status: done` when the Research note exists.
