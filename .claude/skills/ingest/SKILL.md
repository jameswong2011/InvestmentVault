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
- **Batch inbox mode**: acquire a `vault-wide` scope lock. Timeout budget: 15 minutes (batch can be slow). All modes: capture the token at Step 0.1, verify ownership (Procedure 1.5) at every subsequent Bash block, release explicitly in the final reporting Bash block.

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

**Domain-specific content validators (T1.1 — NEW — BLOCKING for URL/PDF, advisory for manual local files)**:

These validators catch content that passes generic structural checks (#1-7) but is semantically wrong for the declared `source_type`. Examples: an "earnings" note that passed word-count but contains no period/currency tokens (likely a JS-rendered placeholder); an "analyst-report" note with no rating or target (likely a disclaimer page). The domain validators encode minimum domain-vocabulary signatures; absence signals that the fetch returned wrong content.

8. **`source_type: earnings` signature (BLOCKING)**:
   - MUST contain at least one quarterly-period token (case-insensitive): `Q1`, `Q2`, `Q3`, `Q4`, `1Q`, `2Q`, `3Q`, `4Q`, `H1`, `H2`, `FY2` followed by digits (e.g., `FY2026`), `fiscal year`, `full year`.
   - MUST contain at least two numeric currency figures: any of `$[digit]`, `[digit] million`, `[digit] billion`, `[digit]M `, `[digit]B `, `revenue of`, `EPS of`, `operating income`, `net income` each followed by or preceded by a numeric value.
   - MUST contain a ticker-shaped token (1-5 uppercase letters) OR a company-name frontmatter value matching any thesis in `Theses/`.

9. **`source_type: analyst-report` signature (BLOCKING)**:
   - MUST contain at least one rating token (case-insensitive): `Buy`, `Sell`, `Hold`, `Neutral`, `Overweight`, `Underweight`, `Outperform`, `Underperform`, `Market Perform`, `Strong Buy`, `Reduce`, `Accumulate`.
   - MUST contain at least one price-target token: `price target`, `PT`, `target price`, `fair value`, `12-month target`, OR a `$[digit]` figure within 200 characters of the word `target`.
   - MUST contain a ticker-shaped token or company-name reference.

10. **`source_type: news` signature (BLOCKING)**:
    - MUST contain a company/ticker reference (ticker-shaped token OR known-company token per thesis/sector notes).
    - MUST contain a dated event reference — at least one of: an absolute date (`YYYY-MM-DD`, `Month DD, YYYY`, `DD Month YYYY`), a relative temporal token (`today`, `yesterday`, `last week`, `this morning`, `announced`, `reported`, `disclosed`, `released`, `filed`), or a weekday reference (`Monday`, `Tuesday`, etc. in capitalized form).
    - Purpose: news articles without temporal grounding are usually boilerplate / about / contact pages disguised as content.

11. **`source_type: deep-dive` signature (BLOCKING)**:
    - Higher word-count floor: MUST have ≥500 words body content (overrides #5's 150-word threshold).
    - MUST have ≥3 substantive sections (non-empty `##` headings with body content below).
    - Purpose: deep-dives are substantive synthesis; structural shallowness signals extraction failure or wrong-article.

12. **Numerical integrity probe (BLOCKING — all source types)**: detect OCR-style corruption that passes word-count:
    - **Capital-O as zero**: regex `\b[A-Za-z]*[O0]{1,}[A-Za-z]*\b` where a numeric context is adjacent (e.g., `2O26`, `$1OO`, `Q2O26`). Count matches; if >3 occurrences OR any near a currency/year token, treat as OCR-corrupt and fail.
    - **Lowercase-l / capital-I as 1**: `\b[Il]{2,}\b` where surrounding context suggests a number (e.g., `II.5%`, `IO million`). Count matches; if >3, fail.
    - **Decimal-dropped currency**: `\$\d{2,}\s+\d{1,2}\b` patterns where the space likely replaces a decimal (e.g., `$1 5B` → `$1.5B`). Two or more occurrences flag corruption.
    - If ANY of the above thresholds trip, report `#12 numerical integrity FAILED: [specific pattern, count]`.

13. **Title-URL consistency (BLOCKING for Mode A URL ingest only)**: compare the research note's first `# Heading` (or frontmatter `title:` if present) against the URL's path/slug segments. Extract alphabetic words ≥4 chars from both; require at least 50% overlap (Jaccard similarity on token sets). If the title says "NVIDIA Q3 2026 Earnings" but the URL path is `/subscribe/signup`, the title-URL mismatch signals a redirect to a wrong page. Below 50% overlap, fail.
    - Mode B (local file) skips #13 — local files don't have a canonical URL-to-title expectation.
    - If the URL uses an opaque slug (UUID, short ID) with <3 alphabetic tokens ≥4 chars, skip #13 gracefully and log advisory (not enough signal to validate).

**Failure handling**:
- **Structural failure (1-4)**: do NOT move the source file. Report `⚠️ Partial-write detected for [[Research/filename]] — source [[_Inbox/filename]] left in place for reprocessing. Failure: [specific check that failed]. Delete the partial note and re-run /ingest, or complete the note manually.`

- **Content-quality failure (5-7) OR domain validator failure (8-13)** for URL ingest (Mode A) or PDF ingest (Mode B): do NOT move the source file. **DELETE the just-written research note** (it's contaminated, not partial — re-running with the same source would repeat the failure). Report:
  ```
  ⚠️ Content-quality gate FAILED for [URL or path]
    Triggered check: [specific check identifier + evidence]
    Category: [generic 5-7 | domain 8-13]
  Diagnostics:
    - Body length captured: [N] words
    - source_type declared: [value]
    - Domain tokens found: [list relevant tokens detected/missing per #8-11]
    - First 200 chars of body: [excerpt for user to verify the fetch contents]
  Action taken:
    - Research note NOT created (would propagate corrupted content via /sync).
    - Source [_Inbox/filename or URL] retained — re-run /ingest after resolving
      the underlying issue (login, alternate URL, manual download, or correcting
      the source_type if the content truly is a different type).
  ```

- **Content-quality / domain validator failure** for local manual files (Mode B for `.md`/`.csv`/`.txt` sources, where the user explicitly created the source): write the research note as-is, but flag advisory for EACH failing check: `ℹ️ Content-quality threshold not met (#[N]: [details]). Note created because source is a manually-curated local file, but body may be sparse or domain-mismatched — review before /sync propagates.` Do not block.

- **source_type: web-clip or data**: skip checks #8-11 (no domain vocabulary expected — clips and raw data can be anything). Still run #12 (numerical integrity) and #13 (for Mode A) — these catch universal corruption.

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

### Step 3.5: Graph-primer propagation fanout

Per `.claude/skills/_shared/graph-primer.md` Mode C.

Read `_graph.md` once (parallel to any remaining Reads in Step 3). Parse `adjacency_index`, `sector_reverse`, `macro_reverse`.

For each just-created research note, with:
- `T` = note's primary `ticker:` (if any)
- `S` = note's `sector:` (if any)
- `M` = `Macro/` references in note body (if any)

Compute:
- `direct_targets` = theses already matched in Step 3 (ticker/topic grep hits)
- `sector_candidates` = `sector_reverse[S] - direct_targets` (if S resolved via sector-resolution contract)
- `macro_candidates` = union over each referenced `m ∈ M` of `macro_reverse[m] - direct_targets - sector_candidates`

Record `direct_targets`, `sector_candidates`, `macro_candidates` for Step 4 reporting.

**Orientation not filter** (contract §Anti-patterns): the graph is a known-minimum. `sector_candidates` and `macro_candidates` are weak-match suggestions, advisory only — user decides whether to wikilink.

**Batch mode** (Mode C): Read `_graph.md` ONCE across all inbox files. Cache `adjacency_index`, `sector_reverse`, `macro_reverse` in memory through the batch — do NOT re-read per file.

**Missing-graph fallback**: per `.claude/skills/_shared/graph-primer.md` §Missing-graph fallback. Skip this step with `ℹ️` advisory. Step 3 strong-match set still reports in Step 4.

### Step 4: Report
For each processed item, report:
- Research note created: `[[Research/filename]]` OR **`❌ rejected — content-quality gate failed (see triggered check)`** for blocked URL/PDF ingests
- Contradictions found: [any insights that challenge existing convictions]
- **Strong-match theses** (explicit ticker/topic — `/sync` will propagate): [list from Step 3, or "none"]
- **Weak-match via shared sector** (graph primer — review before `/sync`): [list from Step 3.5 `sector_candidates`, or "none"]. If any are analytically relevant, add `[[Theses/...]]` wikilinks to the research note body before `/sync`, or `/sync` will not propagate to them.
- **Weak-match via shared macro** (graph primer — review before `/sync`): [list from Step 3.5 `macro_candidates`, or "none"]. Same action note.
- **Sector Notes requiring `/sync`**: [list sectors that should incorporate this research]
- **Content-quality advisories** (if any non-blocking failures from #5–#8 fired on local files): list the specific check + advisory message

If batch mode, end with:
- Total items processed: X
- **Content-quality blocks** (URL/PDF only): Y items rejected before write — see per-item details above. Re-run `/ingest` after resolving the access issue.
- **Source-type advisories**: Z items had signature mismatch (#8) — content may be off-topic for the declared `source_type`. Review before `/sync`.
- **Run `/sync` to propagate these insights to affected theses, sector notes, and macro notes.** Run `/graph last` afterward to register any new research notes in the dependency map — `/sync` does NOT write to `_graph.md` directly (owned exclusively by `/graph`).

### Step 5: Release lock

After Step 4's report is complete, release the vault lock per `.claude/skills/_shared/preflight.md` §1.7 as the skill's FINAL Bash block. Lock scope depends on mode acquired in Step 0.1:
- Batch mode → `.vault-lock`
- Single URL/file mode → `.vault-lock` (current implementation) or `.vault-lock.TICKER` if single-file resolution bound the ticker

Runs unconditionally — whether all inbox items processed cleanly, some were rejected by content-quality gates, or the skill hit a non-fatal error.

```bash
# Lock release — verify ownership before rm (preflight §1.5)
LOCK_FILE="<paste-from-Step-0.1>"                # e.g., .vault-lock
EXPECTED_TOKEN="<paste-token-captured-from-Step-0.1>"
if [ -f "$LOCK_FILE" ] && grep -q "token: $EXPECTED_TOKEN" "$LOCK_FILE"; then
  rm -f "$LOCK_FILE" && echo "=== LOCK RELEASED ($LOCK_FILE) ==="
else
  echo "⚠️ Lock ownership check failed at release ($LOCK_FILE) — skipping rm to avoid stealing another skill's lock."
fi
```
