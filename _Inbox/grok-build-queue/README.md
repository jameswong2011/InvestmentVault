# Grok Build queue

Vault Boss drops one job file per unit of work here. Run these in Obsidian Grok Build on this vault (`/Users/alexcohen/InvestmentVault`). Do not batch several `$ingest` articles into one run.

## File name

`YYYY-MM-DD-HHMM-<skill>-<slug>.md`

## Frontmatter

```yaml
---
grok_build: true
skill: /ingest   # or /sync /graph /surface /lint /numbers /catalyst /archive-callouts /portfolio-snapshot
vault: /Users/alexcohen/InvestmentVault
status: queued   # queued | done | skip
---
```

Body has the exact `$command`, staging paths, and inputs.

## Order

1. Each `$ingest` job (one article = one job)
2. One `$sync` (those files only)
3. One `$graph last`

Mark `status: done` when finished. Leave completed files; do not delete unless asked.
