---
name: ingest
description: Ingest content into the vault as structured research notes. Accepts a URL, a local file path, or no arguments (batch-processes _Inbox/). Use when user shares a URL, says "clip this", "ingest", or "process inbox".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebFetch Bash(date * mv * mkdir * ls * find * defuddle *)
---

Ingest raw content into the vault as structured research notes. **This skill creates research notes only — it does NOT propagate insights to theses, sector notes, or macro notes. Run `/sync` after ingesting to propagate.**

## Input Mode Detection

Parse $ARGUMENTS to determine mode:
- **URL** (starts with `http`): Fetch and process a single web page
- **File path** (ends with `.md`, `.pdf`, `.csv`, `.txt`, or contains `/`): Read and process a single local file
- **No arguments / empty**: Batch-process all files in `_Inbox/`

---

## Mode A: URL Ingest

1. **Fetch and extract** the content from the URL. Use `defuddle` for web URLs when available, otherwise use WebFetch.
2. Proceed to **Processing Pipeline** (Step 1) with the extracted content.

## Mode B: Local File Ingest

1. **Read the file** at the given path:
   - `.md` files: Read directly
   - `.pdf` files: Read with the Read tool (it handles PDFs natively). For PDFs over 10 pages, read in chunks using the `pages` parameter (e.g., `pages: "1-10"`, then `pages: "11-20"`). Process all chunks, then combine insights into a single research note.
   - `.csv` files: Read and interpret the tabular data
   - Other formats: Attempt to read as text
2. Proceed to **Processing Pipeline** (Step 1) with the extracted content.

## Mode C: Batch Inbox Processing

1. **Scan `_Inbox/`** for all files (excluding `_Inbox/processed/` and hidden files):
   ```bash
   find _Inbox/ -maxdepth 1 -type f \( -name "*.md" -o -name "*.pdf" -o -name "*.csv" -o -name "*.txt" \) | sort
   ```
2. If no files found, report "Inbox empty — nothing to process" and stop.
3. **Prior-processing guard**: for each inbox file, check whether `_Inbox/processed/[filename]` already exists. If it does, the file is a re-drop of something already processed — do NOT reprocess. Report `ℹ️ Skipped [filename] — already in _Inbox/processed/ from a prior run. Delete from _Inbox/ manually if intended to re-ingest fresh.` Move to the next file.
4. **Process each remaining file** through the Processing Pipeline below (Steps 1–3).
5. **Post-write verification gate** — after the Processing Pipeline writes the research note, re-read it and verify (see `Post-write verification` section below). Only on verification success proceed to step 6.
6. **Move the original** to `_Inbox/processed/` (verification-gated):
   ```bash
   mkdir -p _Inbox/processed
   mv "_Inbox/[filename]" "_Inbox/processed/[filename]"
   ```
   If `mv` fails: report the failure clearly (`⚠️ Processing succeeded but mv failed for [filename] — research note [[Research/...]] exists. Move source manually: mv "_Inbox/[filename]" "_Inbox/processed/[filename]". Re-running /ingest will skip this file via dedup (source URL/path match) OR the prior-processing guard.`). The research note remains — re-running `/ingest` is safe because the source-URL/path dedup check in Step 1 of the Processing Pipeline will find the existing note and skip.
7. After all files are processed, provide a batch summary including verification failures and mv failures as separate counts.

### Post-write verification

Re-read the just-written research note and check:
1. YAML frontmatter parses (has opening `---` and closing `---`, valid key-value lines between).
2. Required frontmatter fields present: `date:`, `tags:`, `source:`, `source_type:`.
3. Body is non-empty and contains at least one `## ` section header.
4. Last non-empty line does not end mid-sentence (doesn't terminate in a conjunction, preposition, comma, or opening bracket).

If any check fails: do NOT move the source file. Report `⚠️ Partial-write detected for [[Research/filename]] — source [[_Inbox/filename]] left in place for reprocessing. Failure: [specific check that failed]. Delete the partial note and re-run /ingest, or complete the note manually.`

This verify-before-commit pattern keeps the source file in `_Inbox/` as the authoritative "needs processing" marker until a complete research note exists. Partial notes are surfaced rather than silently committed.

---

## Processing Pipeline

For each piece of content (regardless of input mode):

### Step 1: Analyse Content
- Identify the primary topic, ticker(s), and sector
- Determine the appropriate source_type: earnings | analyst-report | news | deep-dive | data | web-clip
- Check if a thesis already exists for this ticker — this determines the note's framing
- **Duplicate check**: Grep Research/ frontmatter for matching `source:` URL. If an existing note has the same source URL, skip this item and report: `⚠️ Duplicate source — already ingested as [[Research/existing-note]]`

### Step 2: Create Research Note
Save to `Research/YYYY-MM-DD - [Topic or Ticker] - [Source Type].md`:

```yaml
---
date: YYYY-MM-DD
tags: [research, SECTOR, TICKER(s)]
sector: [primary sector]
ticker: [primary ticker if applicable]
source: [URL, file path, or description]
source_type: [earnings|analyst-report|news|deep-dive|data|web-clip]
---
```

**Follow CLAUDE.md Writing Standards strictly.** Structure the body as:

- **Thesis Delta** (1-2 sentences: what this changes for the investment case. If no thesis exists, state the key question this raises. Do NOT re-describe the business — the thesis note already does that.)
- **Evidence** (data points only. Tables preferred. No narrative. Lead with numbers, not context.)
- **Contradiction Check** (does this support or challenge existing conviction? Name the specific assumption affected.)
- **Source Excerpts** (only quotes containing specific numbers or claims not captured above. Delete section if empty.)

### Step 3: Connect to Vault
- **Search /Theses** for matching tickers or topics
- **Read the relevant Sector Note** for context
- **Add wikilinks** within the research note body to every related thesis and macro note
- **Check for contradictions** — does this content challenge any existing thesis conviction?

### Step 4: Report
For each processed item, report:
- Research note created: `[[Research/filename]]`
- Contradictions found: [any insights that challenge existing convictions]
- **Theses requiring `/sync`**: [list tickers whose notes should be updated with this research]
- **Sector Notes requiring `/sync`**: [list sectors that should incorporate this research]

If batch mode, end with:
- Total items processed: X
- **Run `/sync` to propagate these insights to affected theses, sector notes, and macro notes.** `/sync` will also update `_graph.md` with the new research notes.
