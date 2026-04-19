---
name: ingest
description: Ingest content into the vault as structured research notes. Accepts a URL, a local file path, or no arguments (batch-processes _Inbox/). Use when user shares a URL, says "clip this", "ingest", or "process inbox".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebFetch Bash(date * mv * mkdir * ls * find * defuddle *)
---

Ingest raw content into the vault as structured research notes. **This skill creates research notes only — it does NOT propagate insights to theses, sector notes, or macro notes. Run `/sync` after ingesting to propagate.**

## Step 0: Pre-flight (MANDATORY)

### 0.1: Acquire vault lock
- **URL or single-file mode**: acquire a `vault-wide` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 5 minutes. (Locks vault-wide because the research note's wikilink targeting may touch multiple tickers before `/sync` runs.)
- **Batch inbox mode**: acquire a `vault-wide` scope lock. Timeout budget: 15 minutes (batch can be slow). Release via `trap` on exit in all modes.

### 0.2: Rename-marker advisory check
Glob `.rename_incomplete.*` at vault root. If any marker exists, emit a non-blocking advisory: `⚠️ In-flight rename repair(s) detected: [markers]. New research notes will wikilink to current thesis filenames. If an ingested note targets a still-mid-rename ticker, run /rename TICKER "[new_name]" to resolve before /sync.` Ingest proceeds — the research note creation itself is safe; the split-name risk materializes only at `/sync` time.

### 0.3: Source dedup check (5.5 fix — URL and single-file modes)

**Applies to Mode A (URL) and Mode B (single local file). Batch Mode C uses the per-file Prior-processing guard instead** (Mode C already handles `_Inbox/processed/` dedup correctly).

Purpose: prevent duplicate research notes from ingesting the same URL twice (same day or across days with materially identical content). Without this check, a forgetful user who ingests the same article twice produces two research notes with identical `source:` URLs; `/sync` then propagates BOTH to downstream theses, writing duplicate Log entries (mitigated by T6 6.11 wikilink idempotency for the second sync, but the first one still spams).

Procedure:

1. **Compute source key**:
   - **Mode A (URL)**: use the raw URL as-is. Do NOT normalize (query params, fragments, path trailing slashes can be semantically meaningful — e.g., `?v=1234` on YouTube, `#section` anchors in documentation).
   - **Mode B (local file)**: use the absolute file path.

2. **Grep `Research/*.md` frontmatter** for a `source:` value matching the key. Match rule: exact string equality after frontmatter parse (tolerate wrapping whitespace). Use `Grep` with `-F` equivalent for literal match.

3. **Branch on match**:

   **No match** → proceed to Processing Pipeline normally.

   **One or more matches — same calendar day** (match's `date:` frontmatter equals today's date): HARD BLOCK with:
   ```
   ⚠️ Source already ingested today: [[Research/matched-note]]
     source: [URL or path]
     date:   [today]
   
   Duplicate ingest blocked. The existing note will propagate via /sync.
   
   If you actually want to re-process (source content materially changed since
   this morning's ingest), delete the existing note first:
     rm "Research/[matched-note].md"
   Then re-run /ingest [source].
   ```
   Exit without writing a new note. No vault state changes.

   **One or more matches — older than today**: WARN + confirm:
   ```
   ⚠️ Source previously ingested: [[Research/matched-note]]
     source: [URL or path]
     previous date: [YYYY-MM-DD] ([N] days ago)
   
   Options:
     (a) Skip — the existing note covers this source. /sync can re-propagate from it
         if /sync hasn't yet picked it up. No new note written.
     (b) Re-ingest — useful if the source URL serves materially updated content
         (e.g., a live earnings page that has been revised, a tracker URL with
         new data). Creates a NEW note at Research/YYYY-MM-DD - ... with today's
         date. Existing note is preserved. Note: /sync's wikilink-idempotency
         (T6 6.11 fix) means both notes can coexist cleanly — each is a
         separate propagation event to affected theses.
     (c) Cancel — investigate manually.
   
   Confirm (a/b/c):
   ```
   **Branch behavior**:
   - **(a)**: exit without writing. Log `ℹ️ Ingest skipped — existing note [[Research/matched-note]] covers source.`
   - **(b)**: proceed to Processing Pipeline. The new note's body will describe the update context in the Summary section.
   - **(c)**: exit without writing.

**Why not canonical URL normalization**: tempting to normalize (strip trailing slashes, sort query params alphabetically, downcase hostname) for stricter dedup. Rejected because: (a) URL semantics are provider-specific — YouTube's `?v=` is meaningful, a blog's `?utm_source=` often isn't, and the skill can't reliably distinguish; (b) over-normalization produces false dedup matches (two truly distinct articles collapsed as "same"); (c) strict exact match with user-facing confirmation for cross-day cases is auditable and recoverable, while silent canonical dedup is neither.

## Input Mode Detection

Parse $ARGUMENTS to determine mode:
- **URL** (starts with `http`): Fetch and process a single web page
- **File path** (ends with `.md`, `.pdf`, `.csv`, `.txt`, or contains `/`): Read and process a single local file
- **No arguments / empty**: Batch-process all files in `_Inbox/`

---

## Mode A: URL Ingest

1. **Fetch and extract** the content from the URL. Use `defuddle` for web URLs when available, otherwise use WebFetch.
2. Proceed to **Processing Pipeline** (Step 1) with the extracted content.
3. **Post-write verification gate** (mandatory): after Processing Pipeline writes the research note, re-read it and apply the verification checks listed under `Post-write verification` below. URL ingest is HIGH-RISK for silent content corruption (paywalls, CAPTCHAs, anti-bot pages return non-error content that looks valid until you read it) — content-quality checks block on failure for this mode.

## Mode B: Local File Ingest

1. **Read the file** at the given path:
   - `.md` files: Read directly
   - `.pdf` files: Read with the Read tool (it handles PDFs natively). For PDFs over 10 pages, read in chunks using the `pages` parameter (e.g., `pages: "1-10"`, then `pages: "11-20"`). Process all chunks, then combine insights into a single research note.
   - `.csv` files: Read and interpret the tabular data
   - Other formats: Attempt to read as text
2. Proceed to **Processing Pipeline** (Step 1) with the extracted content.
3. **Post-write verification gate** (mandatory): after Processing Pipeline writes the research note, re-read it and apply the verification checks listed under `Post-write verification` below. PDFs block on content-quality failure (PDF extraction can return image-only or scan-only content that has no text). Manual `.md`/`.csv`/`.txt` sources receive advisory-only content-quality logs (the user created the source, so they own the content quality).

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

Re-read the just-written research note and check, in order:

**Structural checks (block on failure)**:
1. YAML frontmatter parses (has opening `---` and closing `---`, valid key-value lines between).
2. Required frontmatter fields present: `date:`, `tags:`, `source:`, `source_type:`.
3. Body is non-empty and contains at least one `## ` section header.
4. Last non-empty line does not end mid-sentence (doesn't terminate in a conjunction, preposition, comma, or opening bracket).

**Content-quality checks** (NEW — block on failure for URL/PDF source types; advisory for manual local files):

5. **Minimum body word count**: body (excluding frontmatter, fenced code blocks, and section headers) is at least **150 words**. Below that threshold, the fetch likely captured a paywall, error page, or near-empty redirect rather than substantive content. Most legitimate articles, transcripts, and reports easily clear this floor.

6. **Anti-bot / paywall sentinel detection**: scan the body for any of the following case-insensitive token sequences. Match indicates the fetch hit a wall, not the article:
   - `subscribe to continue`, `subscribers only`, `become a member`, `paywall`
   - `please enable javascript`, `enable javascript to view`
   - `verify you are a human`, `verify you are human`, `complete the captcha`, `cloudflare protection`, `prove you're not a robot`
   - `access denied`, `403 forbidden`, `404 not found`, `page not found`
   - `sign in to read`, `log in to continue`, `register to read`, `create a free account to`
   - `cookie consent required`, `accept cookies to continue`
   - body contains ONLY a single line of generic site navigation (e.g., `Home  About  Contact`) — heuristic: <50 words AND no `## ` section beyond frontmatter

7. **Section structural minimum**: at least 2 of the 4 expected body sections (`## Thesis Delta`, `## Evidence`, `## Contradiction Check`, `## Source Excerpts`) must contain non-empty content. A note with only stub headers is structurally complete but analytically empty — extraction failed.

8. **Source-type signature mismatch** (advisory):
   - `source_type: earnings` should contain at least one quarterly-period token (`Q1`, `Q2`, `Q3`, `Q4`, or `FY20XX`) AND a numeric currency token (e.g., `$`, `revenue of`, `million`, `billion`). If absent, log advisory: `ℹ️ Earnings note lacks period/financial tokens — content may be off-topic.`
   - `source_type: analyst-report` should contain a price target or rating token (`PT`, `target price`, `Buy`, `Sell`, `Hold`, `Overweight`, `Underweight`). If absent, log advisory.

**Failure handling**:
- **Structural failure (1-4)**: do NOT move the source file. Report `⚠️ Partial-write detected for [[Research/filename]] — source [[_Inbox/filename]] left in place for reprocessing. Failure: [specific check that failed]. Delete the partial note and re-run /ingest, or complete the note manually.`

- **Content-quality failure (5-7)** for URL ingest (Mode A) or PDF ingest (Mode B): do NOT move the source file. **DELETE the just-written research note** (it's contaminated, not partial — re-running with the same source would repeat the failure). Report:
  ```
  ⚠️ Content-quality gate FAILED for [URL or path] — fetch likely returned [paywall | CAPTCHA | empty page | wrong content].
    Triggered check: [specific check, e.g., "#5 body word count = 47 (< 150)" or "#6 detected sentinel: 'subscribe to continue'"]
  Action taken:
    - Research note NOT created (would propagate corrupted content via /sync).
    - Source [_Inbox/filename or URL] retained — re-run /ingest after resolving access (login, alternate URL, manual download).
  Diagnostics:
    - Body length captured: [N] words
    - First 200 chars of body: [excerpt for user to verify the fetch contents]
  ```

- **Content-quality failure (5-7)** for local manual files (Mode B for `.md`/`.csv`/`.txt` sources, where the user explicitly created the source): write the research note as-is, but flag advisory: `ℹ️ Content-quality threshold not met (#[N]: [details]). Note created because source is a manually-curated local file, but body may be sparse — review before /sync propagates.` Do not block.

- **Source-type signature mismatch (#8)**: never blocks; always advisory. Logged in the report.

This verify-before-commit pattern keeps the source file in `_Inbox/` as the authoritative "needs processing" marker until a complete research note exists. Content-quality checks specifically protect against silent semantic corruption — the most damaging failure mode because corrupt research propagates through `/sync` into thesis Log entries before any human reviews it.

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
- Research note created: `[[Research/filename]]` OR **`❌ rejected — content-quality gate failed (see triggered check)`** for blocked URL/PDF ingests
- Contradictions found: [any insights that challenge existing convictions]
- **Theses requiring `/sync`**: [list tickers whose notes should be updated with this research]
- **Sector Notes requiring `/sync`**: [list sectors that should incorporate this research]
- **Content-quality advisories** (if any non-blocking failures from #5–#8 fired on local files): list the specific check + advisory message

If batch mode, end with:
- Total items processed: X
- **Content-quality blocks** (URL/PDF only): Y items rejected before write — see per-item details above. Re-run `/ingest` after resolving the access issue.
- **Source-type advisories**: Z items had signature mismatch (#8) — content may be off-topic for the declared `source_type`. Review before `/sync`.
- **Run `/sync` to propagate these insights to affected theses, sector notes, and macro notes.** `/sync` will also update `_graph.md` with the new research notes.
