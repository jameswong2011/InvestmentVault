---
grok_build: true
skill: /ingest
vault: /Users/alexcohen/InvestmentVault
status: done
---

# $ingest — PhotonCap reading list (one article)

Pub: PhotonCap
Title: AI Infrastructure Value Chain: The PhotonCap Reading List (8/27/2026)
Source URL: https://photoncap.net/p/ai-infrastructure-value-chain-the
Date: 2026-08-27
Access: full paid-subscriber article

Do **not** batch. One article = this job.

## Staging (on this Mac)

- Source: `_Inbox/grok-build-queue/staging/2026-08-27-photoncap-ai-infrastructure-value-chain.md`
- Draft research note (use as starting point; verify against `/ingest`, then file to `Research/`): `_Inbox/grok-build-queue/staging/2026-08-27 - NVDA AVGO MRVL 000660 - PhotonCap AI Infrastructure Value Chain Reading List - deep-dive.md`

## Command

```
$ingest /Users/alexcohen/InvestmentVault/_Inbox/grok-build-queue/staging/2026-08-27-photoncap-ai-infrastructure-value-chain.md
```

If the draft note already satisfies ingest verification, file it to `Research/` under that filename and treat as Mode B local-file ingest of the source (dedup on `source:` URL). Do not create a second note.

Mark this job `status: done` when the Research note exists.
