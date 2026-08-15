---
publish: false
date: 2026-05-24
tags: [meta, briefing, web-ui]
status: active
source: hand-authored briefing pack for a web-based LLM tasked with building an interactive explainer UI
---

# Web UI Build Brief — Claudian Investment Vault Explainer

> **You are receiving this file together with four companions:**
> 1. `CLAUDE.md` — the vault's system prompt / behavioral contract for Claude Code (26 KB)
> 2. `User Guide.md` — the user-facing reference manual (76 KB) — **PRIMARY SOURCE**
> 3. `INFRASTRUCTURE.md` — the deep-mechanics spec for skill authors (82 KB) — **PRIMARY SOURCE**
> 4. `Canvas/New User Orientation.canvas` — a JSON-Canvas visual orientation map (36 KB)
>
> **This brief is the orientation layer that sits on top of all four.** Read it first, then read `User Guide.md` and `INFRASTRUCTURE.md` in full — they are not optional.

---

## 0. Your Mission

Build a **single-page interactive web UI** that lets a complete newcomer understand the Claudian Investment Vault — **with context engineering and the vault's context files as the centerpiece** — in 10-15 minutes of exploration. Every other section (architecture, workflows, skills, note anatomy, safety) exists to support and demonstrate this central insight.

**Output**: A self-contained HTML file (embedded CSS + JS, no build step, no backend, no API calls). One CDN-loaded framework is fine (React via esm.sh, Vue via CDN, Alpine.js, or vanilla JS).

**Audience**: A finance-literate but Obsidian/Claude-Code-naive professional. They know what a thesis is; they don't know what a wikilink, YAML frontmatter, or MOC is.

**Mandatory citation requirement**: The UI MUST contain explicit, inline references to specific sections of `User Guide.md` and `INFRASTRUCTURE.md` throughout. Every concept card, every workflow chain, every skill description, every context-file panel should have visible "→ Read: User Guide §X" and/or "→ Deep mechanics: INFRASTRUCTURE.md §Y" pointers. Use the source-file headings as canonical reference targets. Treat these two files as the source-of-truth that the UI summarizes; newcomers should know exactly where to dig deeper for every topic the UI surfaces. Aim for ≥2 such citations per major section.

**Success criterion**: After 10 minutes the user can answer:
1. **What are the 6 context files** (`CLAUDE.md`, `_hot.md`, `_graph.md`, `_catalyst.md`, `.last_sync`, `_Archive/Snapshots/`) and what role does each play in making a stateless LLM behave as if it has persistent memory?
2. **What are the 10 prompt-engineering patterns** the vault implements (system prompt as durable memory, context cache, dependency graph priming, snapshot rollback, subagent forking, watermark incrementality, pre-flight contract, append-only audit logs, provenance immutability, deterministic skill specs)?
3. What is this vault for, and why isn't ChatGPT enough?
4. What's the difference between a "skill" and a "prompt"?
5. What are the main workflows day-to-day?
6. How would I start using or building something like this myself, and **where in `User Guide.md` / `INFRASTRUCTURE.md` should I dig deeper**?

---

## 1. How to Use the Source Files

| File | Trust for | Role in the UI |
|---|---|---|
| **This brief** | Build directive · UI/UX spec · pedagogical priorities | Read first; defines what to build |
| **CLAUDE.md** | Vault structure, safety rules, writing standards, conventions | Cite when explaining "Safety", "Note Anatomy", "Architecture", "Writing Standards" |
| **`User Guide.md`** | **PRIMARY**: Workflow chains, skill arguments, cadence, gotchas, "I Want To..." index, callout lifecycle, prompt library | **Cite explicitly in every Workflow, Skill, Callout, and Get-Started panel.** Use exact section anchors (e.g., "User Guide §3.1 New position — full build", "User Guide §5 Skill Reference", "User Guide §6 Inline callouts", "User Guide §11 Prompt Library", "User Guide §12 Cadence Guide", "User Guide §13 Caveats & Gotchas") |
| **`INFRASTRUCTURE.md`** | **PRIMARY**: Deep mechanics — locks, snapshots, manifests, propagation gates, `_hot.md` compression contract, graph-primer pattern, pre-flight contract, log-prefix classification, lifecycle of every metadata file | **Cite explicitly in every Context File, Prompt-Engineering Pattern, and Skill Internals panel.** Use exact section anchors. **This file is non-optional** — the prompt-engineering centerpiece of the UI is impossible to build accurately without reading it in full. |
| **`Canvas/New User Orientation.canvas`** | Pre-distilled information architecture | Read the JSON to extract the 10-zone scaffold and color palette; mirrors §3-§11 of this brief |

**Conflict resolution**: This brief ≻ CLAUDE.md ≻ User Guide ≻ INFRASTRUCTURE. If they disagree, prefer the higher-trust source. **For deep mechanics where this brief is silent or vague, INFRASTRUCTURE.md is authoritative.**

**Don't**: Try to surface every skill, every workflow, every gotcha. The UI is an explainer, not a manual.

**Do**: Build deep affordances for context engineering specifically; for everything else, summarize crisply and cite the User Guide / INFRASTRUCTURE.md section the user should read next.

### Inline-citation pattern (use throughout)

Every concept card / panel / interactive element should end with a citation strip. Examples:

```
[ Context-file: _hot.md ]
... your interactive content ...
─────────────────────────────────────────
→ User Guide §14 "How the Vault Stays Consistent"
→ INFRASTRUCTURE.md §_hot.md compression contract
→ CLAUDE.md Operational Rule 9
```

```
[ Workflow: Earnings reaction ]
... your interactive content ...
─────────────────────────────────────────
→ User Guide §3.2 Earnings reaction
→ User Guide §5 /ingest, /sync, /status
→ INFRASTRUCTURE.md §sync lifecycle
```

Render citation strips visibly (small caps, monospace, muted color is fine — but not hidden behind a hover). The reader should never wonder "where do I read more?"

---

## 2. The System in 60 Seconds

The Claudian Investment Vault is, fundamentally, **an experiment in context engineering** — using a small set of structured "context files" (`CLAUDE.md`, `_hot.md`, `_graph.md`, `_catalyst.md`, `.last_sync`, `_Archive/Snapshots/`) to give a stateless LLM the appearance of long-term memory, the discipline of deterministic workflows, and the safety of pre-edit snapshots. **Equity research is the showcase domain; the architectural pattern generalizes to any LLM-augmented knowledge work.**

Concretely: a personal knowledge base for equity research stored in Obsidian (Markdown files in folders), augmented by **Claude Code** (a CLI running Claude Sonnet/Opus locally with tool-use) configured with **custom skills** — deterministic, spec-driven, multi-step workflows defined in Markdown.

Imagine if:
- ChatGPT had **persistent memory** of your research, coordinated through a handful of structured files the LLM reads on every session
- Typing `/sync` propagated a new earnings note across every related thesis via a pre-computed dependency graph
- Every destructive action created a snapshot you could roll back
- The LLM was opinionated about how a thesis should be structured (14 sections, structured frontmatter) and enforced it
- Heavy-read operations forked into a subagent so your main conversation context stayed clean

That's Claudian. **The vault is the agent's substrate. The context files are its short-term memory and routing table. The skills are its motor functions.** The context files are where the prompt-engineering magic actually lives.

The investment edge: built for **qualitative, non-consensus research** — technology shifts, management quality, competitive dynamics, pricing power, investor bias. The dimensions traditional financial modeling misses.

→ Read: `User Guide.md` §0–§1 (First Run, Core Loop) · `INFRASTRUCTURE.md` §1 (Architecture Overview) · `CLAUDE.md` Approach & Core Purpose

---

## 3. The Six Must-Convey Concepts

The UI succeeds if these six ideas land. **Order them in this priority** — they build on each other, and #1 and #2 are the centerpiece the rest orbits.

### 3.1 ⭐ Context engineering IS the system (THE THESIS)
The vault is, at its core, a context-engineering pattern: a set of structured files that prime a stateless LLM with persistent memory, dependency awareness, audit history, and recovery state. Strip the context files away and Claude becomes a generic LLM with some Markdown notes nearby; layer them in and the LLM behaves as an agent with long-term memory, deterministic workflows, and rollback. **This is the architectural insight the UI is teaching.** Every other concept below exists to make this one tangible.

→ Read: `INFRASTRUCTURE.md` §1 Architecture Overview · `User Guide.md` §14 How the Vault Stays Consistent

### 3.2 ⭐ The 6 context files, one by one
Each file implements a specific prompt-engineering pattern. Surface all six in the UI with equal weight:

| File | Pattern | Read by | Written by |
|---|---|---|---|
| `CLAUDE.md` | System prompt as durable memory | Every skill, every session | Manually (Tier 1 protected) |
| `_hot.md` | Cross-session context cache | Every skill (on read) + user (session start) | 13 skills (shared writer pool with compression contract) |
| `_graph.md` | Dependency-graph priming | `/sync`, `/surface`, `/prune`, `/compare`, etc. | `/graph` exclusively (3 modes) |
| `_catalyst.md` | Materialized view (event calendar) | User, `/sync` | `/catalyst` exclusively |
| `.last_sync` | Watermark for incremental processing | `/sync` default + all modes | `/sync` default + all modes |
| `_Archive/Snapshots/` | Snapshot-based rollback | `/rollback` | Every destructive skill (pre-edit) |

→ Read: `INFRASTRUCTURE.md` §14 (full spec per file) · `User Guide.md` §14 (short reference table)

### 3.3 The vault IS the agent's accumulated memory
40+ thesis notes, 133+ research notes, 13 sector overviews, 6 macro frameworks. The context files are how Claude *coordinates* against this body of knowledge; the body of knowledge itself is what makes Claude useful as a research analyst rather than a generic LLM. **Vault content + context files = stateful agent.**

### 3.4 Skills are deterministic specs, not "prompts"
A "skill" is a Markdown spec at `.claude/skills/<name>/SKILL.md` defining a multi-step procedure: pre-flight checks → mutations → exit conditions. The LLM follows the spec literally. Same input → same output regardless of model temperature. **This is the key distinction from ChatGPT.** Skills are the motor functions that read and write the context files.

→ Read: `INFRASTRUCTURE.md` §Skill specifications · `User Guide.md` §5 Skill Reference

### 3.5 The core loop is forward + backward
Two cycles drive every session:
- **Forward** (new info in): `_Inbox drop → /ingest → /sync → /graph last`
- **Backward** (thinking vs market): `/retro → review → /status·/deepen·/stress-test → /sync → /graph last`

Periodic maintenance (`/surface`, `/catalyst`, `/lint`, `/prune`, `/clean`) keeps the substrate healthy. Each loop step mutates specific context files — surface this in the UI's loop animation.

→ Read: `User Guide.md` §1 The Core Loop · §3 Workflow Chains · §12 Cadence Guide

### 3.6 Safety is baked in via tiers + snapshots
Three-tier change model:
- **Tier 1 Protected**: `CLAUDE.md`, `Templates/` — never modify without explicit ask
- **Tier 2 Append-only**: thesis `## Log` sections, `_hot.md` archive — add at end, never edit
- **Tier 3 Confirmation required**: conviction changes, status transitions, file deletion

Every destructive skill snapshots before editing. `/rollback` restores any snapshot. **Mistakes are cheap → enables aggressive automation.**

→ Read: `CLAUDE.md` Change Safety Rules · `User Guide.md` §10 Vault Maintenance · `INFRASTRUCTURE.md` §pre-flight contract

### 3.7 The system is opinionated about methodology
The vault enforces a specific research methodology: qualitative, non-consensus, critical (not always positive). The 14-section thesis template is rigid. The writing standards forbid hedge words ("importantly", "notably", "significantly"). Tables over prose for comparative content. Every Log entry max 2 lines. This opinionation is a **feature** — it produces consistent output across hundreds of notes over years.

→ Read: `CLAUDE.md` Approach & Core Purpose, Writing Standards · `User Guide.md` §6 Anatomy of Vault Content

---

## 4. Architecture (canonical reference)

```
Vault Root
├── _Inbox/                Raw drop zone — web clips, PDFs, CSVs
│   └── processed/         Auto-archive after /ingest consumes the source
├── Theses/                40+ files: TICKER - Name.md (14 sections each)
├── Research/              133+ files: YYYY-MM-DD - Topic - Type.md (4 sections)
├── Sectors/               13 sector Maps-of-Content (10 sections each)
├── Macro & Technology/    6 macro framework notes (freeform)
├── Templates/             Note skeletons (Tier 1 protected)
├── _Archive/              Closed theses + Snapshots/ for version control
├── Canvas/                Visual relationship maps (.canvas JSON files)
├── CLAUDE.md              System prompt loaded every session
├── User Guide.md          User-facing reference manual
├── INFRASTRUCTURE.md      Deep mechanics spec for skill authors
├── _hot.md                Session cache (shared writer pool — 13 skills)
├── _graph.md              Dependency map (owned by /graph)
├── _catalyst.md           Forward event calendar (owned by /catalyst)
├── .last_sync             Watermark (mtime = last sync timestamp)
├── .graph_invalidations   Append-only queue of deferred adjacency updates
├── .rename_incomplete.*   Failure markers; hard-block ticker-scoped skills
└── .claude/skills/        Skill definitions (SKILL.md per skill)
```

---

## 5. Workflows to Showcase

Pick 3-5 of these for the UI's workflow demo section. The first three are the highest priority.

### 5.1 New position — full build (Priority 1)
```
/thesis TICKER                                      # creates draft 14-section thesis
/status TICKER status draft→active [rationale]      # promotes; updates sector
/stress-test TICKER                                 # adversarial review
/sync TICKER                                        # propagates to sector + macro
```

### 5.2 Earnings reaction (Priority 1)
```
/ingest [transcript URL]                            # creates Research note
/sync TICKER                                        # propagates to thesis
/status TICKER conviction old→new [if needed]       # if conviction shifted
```

### 5.3 Conviction drift response (Priority 1)
After a few weeks of edits, `/sync` flags `⚠️ Conviction drift`. The user:
```
/stress-test TICKER                                 # investigate
/status TICKER conviction high→medium [rationale]   # OR /status reaffirm
/sync TICKER
```

### 5.4 Macro shock
```
/scenario Fed cuts 150bps by year-end               # propagates through portfolio
/status TICKER conviction old→new [channel]         # most-affected positions
/compare [exposed] vs [beneficiary]                 # competitive shift
/sync
```

### 5.5 Monthly maintenance chain
```
/sync all → /graph → /lint → /prune → /clean → /surface → /catalyst → /graph last
```
Forked subagents (`/lint`, `/prune`, `/surface`, `/retro`) keep main context clean even on a 41-thesis vault.

### 5.6 Recovery — undo a bad sync
```
/rollback TICKER                                    # pick (pre-sync) snapshot
/sync TICKER                                        # OR /sync all if cascade
/graph                                              # full rebuild after closure
```

---

## 6. Skills Catalog (21 skills, 4 categories)

### Core (4) — Daily-driver loop
| Skill | One-liner |
|---|---|
| `/ingest` | URL/file/batch → structured Research notes; same-source dedup |
| `/sync` | Propagate research to theses/sectors/macro/`_hot.md` (3 modes: default, TICKER, all) |
| `/status` | Conviction/status changes with Tier-3 confirmation gate |
| `/graph` | Rebuild dependency map (3 modes: full, `last`, catch-up N days) |

### Analytical (7) — Generate insight
| Skill | One-liner |
|---|---|
| `/surface` | Find new ideas + blind spots (forks to subagent; 4 scopes) |
| `/stress-test` | Adversarial short-seller review |
| `/scenario` | "What if X" propagated through portfolio with impact tagging |
| `/compare` | Side-by-side competitive analysis (2+ tickers) |
| `/catalyst` | Refresh `_catalyst.md` with web-searched earnings dates |
| `/retro` | 1w/1m/1q backward review; narrative-price gap ranking |
| `/transcript` | Pull earnings transcript; extract thesis-delta-first Research note |

### Building (4) — Create / improve content
| Skill | One-liner |
|---|---|
| `/thesis` | New thesis (draft, 14 sections, archive-collision detection) |
| `/deepen` | Surgical section enhancement (NOT full rewrite) |
| `/brief` | 1-page IC memo (read-only on thesis) |
| `/numbers` | Refresh Key Metrics table from financial data API |

### Maintenance (6) — Keep vault healthy
| Skill | One-liner |
|---|---|
| `/lint` | Health check: structural, freshness, analytical (forks to subagent) |
| `/prune` | Evaluate weak theses for upgrade/monitor/close (forks to subagent) |
| `/clean` | Purge old snapshots with safety nets (orphan, closure 30d floor, modified-source) |
| `/archive-callouts` | Sweep ≥180d addressed callouts to `## Legacy Callouts` |
| `/rollback` | Restore from snapshot; cascade detection for multi-file syncs |
| `/rename` | Company name change; atomic across all wikilinks + graph + sector + snapshots |

---

## 7. Note Anatomy

### Thesis Note (14 sections)
Path: `Theses/TICKER - Company Name.md`

1. Summary
2. Key Non-consensus Insights (3-5 paragraphs of what market is missing)
3. Outstanding Questions (3-10 IC-style questions)
4. Business Model & Product Description
5. Industry Context
6. Key Metrics (table)
7. Bull Case
8. Bear Case
9. Catalysts
10. Risks
11. Conviction Triggers (falsifiable `→ HIGH if` / `→ LOW if` / `→ CLOSE if`)
12. Related Research (wikilinks)
13. Legacy Callouts (auto-managed by `/archive-callouts`)
14. Log (append-only dated entries, max 2 lines each)

Frontmatter: `date, tags, status, conviction, sector, ticker, source`

### Research Note (4 required + optional)
Path: `Research/YYYY-MM-DD - Topic - SourceType.md`

1. **Thesis Delta** — what this changes for the case
2. **Summary** — 1-4 paragraphs capturing source's argument
3. **Evidence** — data points, tables (no narrative)
4. **Contradiction Check** — challenges which assumption?

Optional: Source Excerpts, Framework, Key Segments (>15K words). Body length scales with source word count.

### Sector Note (10 sections)
Path: `Sectors/Name.md`. Map-of-Content. Active Theses list at top doubles as routing table for sector-scoped skills.

### Macro Note (freeform)
Path: `Macro & Technology/Name.md`. Geo / rates / commodities / tech-trend frameworks. Cross-sector reach.

---

## 8. Context Engineering & Prompt Patterns — THE CENTERPIECE OF THE UI

⭐ **This is the thesis of the UI.** Every other section (architecture, workflows, skills, note anatomy, safety, callouts) exists to make these patterns concrete. A newcomer who understands the 10 patterns below has gotten the value; everything else is supporting context. **Build the deepest interactivity, the most prominent visual real estate, and the most explicit source-file citations here.**

The patterns generalize beyond finance — they apply to any LLM-augmented knowledge system. A web developer, scientific researcher, or journalist could implement variants of all 10 in their own domain. **Make this transferability explicit in the UI** — each pattern should have a "where else does this apply?" hint.

**Required UI treatment**: each pattern below maps to a dedicated affordance (expandable card, animated diagram, or before/after comparison). Each card must:
1. Name the pattern and the file(s) it operates on
2. Show a synthetic concrete example (file snippet, skill output, etc.)
3. Explain *why* it works (the prompt-engineering rationale)
4. Cite the exact `INFRASTRUCTURE.md` and/or `User Guide.md` section as "Read more" pointers
5. Hint at the cross-domain generalization

### 8.1 System prompt as durable memory
`CLAUDE.md` is loaded as the system prompt every session. Stable behavioral contract — no fine-tuning needed. Update conventions once → all skills + manual prompts inherit them automatically. **The vault is configurable without ML.**

→ Read: `CLAUDE.md` (the file itself) · `INFRASTRUCTURE.md` §System prompt loading

### 8.2 Context cache pattern (`_hot.md`)
Custom short-term memory for the stateless LLM. Skills write deltas after every operation; users read on session start. 6 sections, soft cap 4K words. Compression rules ensure it never overflows. **A general pattern for any agent that needs cross-session continuity.**

→ Read: `INFRASTRUCTURE.md` §_hot.md compression contract · `CLAUDE.md` Operational Rule 9 · `User Guide.md` §2 Session Start

### 8.3 Dependency graph priming (`_graph.md`)
Tells skills which 3-5 thesis files matter for a given research note. Without it, `/sync` would re-read all 40 theses every time. **Avoids cold-context re-reads at scale.** See the graph-primer contract: research skills consume `_graph.md` for cross-ticker context but never replace content reads of target files.

→ Read: `INFRASTRUCTURE.md` §_graph.md ownership & graph-primer pattern · `CLAUDE.md` Workflow Rule 8 · `User Guide.md` §5 /graph

### 8.4 Snapshot-based rollback
Every destructive skill copies the file before editing: `_Archive/Snapshots/TICKER (pre-sync 2026-05-23-2114).md`. `/rollback` restores. **Enables aggressive automation — mistakes cost a snapshot, not real data.**

→ Read: `INFRASTRUCTURE.md` §Snapshot lifecycle & cascade detection · `User Guide.md` §3.4 Recovery — undo a bad sync · §5 /rollback

### 8.5 Subagent forking for context isolation
Heavy-read skills (`/lint`, `/prune`, `/surface`, `/retro`) spawn a subagent. The subagent reads hundreds of files; only the final report returns to main. **Main conversation context stays clean** — this is what keeps the system usable at scale.

→ Read: `INFRASTRUCTURE.md` §Skill execution matrix (Forked subagent column) · `User Guide.md` §14 Skill execution matrix · §3.4 Monthly maintenance

### 8.6 Watermark-based incrementality
`.last_sync` mtime = the watermark. `find -newer .last_sync` returns only modified files. 30 seconds incremental vs 5 minutes full read. **Same pattern for `/graph last`** (uses thesis mtimes + `.graph_invalidations`).

→ Read: `INFRASTRUCTURE.md` §.last_sync & watermark mechanics · `User Guide.md` §13 .last_sync deletion · §5 /sync modes

### 8.7 Pre-flight contract (locks + markers + probes)
Four checks before any write: vault lock acquisition, rename-marker check, name sanitization, section existence probe. **Prevents concurrent races and cascading failures** — the spec at `.claude/skills/_shared/preflight.md` is short and reusable.

→ Read: `INFRASTRUCTURE.md` §pre-flight contract (full procedure spec) · `CLAUDE.md` Operational Rule 10 · `User Guide.md` §13 Concurrency

### 8.8 Append-only audit logs with prefix classification
Thesis `## Log` sections are append-only with prefixed entries (`Stress test:`, `Manual edit:`, `Addressed user callouts:`, `Retro insight:`). `/sync` reads the prefix to decide whether to propagate downstream. **The log IS the source-of-truth for what changed when**, and the prefix grammar IS the routing table.

→ Read: `INFRASTRUCTURE.md` §Log-prefix classification (`_shared/log-prefixes.md`) · `CLAUDE.md` Workflow Rule 6 · `User Guide.md` §2 Manual edit protocol · §6 Propagation contract

### 8.9 Provenance immutability
`source:` frontmatter never changes. Research note bodies are immutable after creation. **The vault is its own court of record** — defend a thesis 90 days later by walking the audit trail.

→ Read: `CLAUDE.md` Operational Rule 3, Tier 2 Append-Only Zones · `User Guide.md` §6 Research note (immutability)

### 8.10 Deterministic skill specifications
`.claude/skills/<name>/SKILL.md` is a self-contained, reproducible procedure with pre-flight, steps, and exit conditions. Long skills include a truncation safeguard ("if your skill content has truncation markers, Read full SKILL.md before mutating"). **Same skill produces same behavior regardless of model temperature or context window pressure.**

→ Read: `INFRASTRUCTURE.md` §Skill spec structure & truncation safeguard · `CLAUDE.md` Operational Rule 11 · `User Guide.md` §5 Skill Reference (canonical entries)

### 8.11 Citation table (use this as a UI affordance)

Build a sortable table in the UI mapping each pattern → primary file → exact section. Lets a curious newcomer drill straight to authoritative sources.

| # | Pattern | Primary file | Section anchor |
|---|---|---|---|
| 1 | System prompt as durable memory | CLAUDE.md | (whole file) |
| 2 | Context cache (`_hot.md`) | INFRASTRUCTURE.md | _hot.md compression contract |
| 3 | Dependency-graph priming (`_graph.md`) | INFRASTRUCTURE.md | _graph.md ownership |
| 4 | Snapshot-based rollback | INFRASTRUCTURE.md | Snapshot lifecycle |
| 5 | Subagent forking | INFRASTRUCTURE.md | Skill execution matrix |
| 6 | Watermark incrementality (`.last_sync`) | INFRASTRUCTURE.md | .last_sync mechanics |
| 7 | Pre-flight contract | INFRASTRUCTURE.md | pre-flight contract (4 procedures) |
| 8 | Append-only audit logs | INFRASTRUCTURE.md | Log-prefix classification |
| 9 | Provenance immutability | CLAUDE.md | Tier 2 Append-Only Zones |
| 10 | Deterministic skill specs | INFRASTRUCTURE.md | Skill spec structure |

---

## 9. Safety Model

### Tier 1 — Protected (never modify without explicit ask)
- `CLAUDE.md` — system instructions
- `Templates/*.md` — define vault consistency; changing them alters ALL future output
- `.obsidian/` — Obsidian config
- `.claude/skills/` — skill definitions

### Tier 2 — Append-Only
- Thesis `## Log` sections — add dated entries at the end
- `_hot.md ## Sync Archive` — prepend new, never remove old
- Research notes — body immutable after creation; corrections via new note or thesis log

### Tier 3 — Confirmation Required (investment decisions)
- `conviction:` frontmatter changes (high → medium etc.)
- `status:` transitions (active → monitoring, active → closed)
- Moving a thesis to `/_Archive`
- Removing any wikilink from thesis/sector/macro
- Deleting or renaming any file

### Operational rules (selected)
- Read before write
- Archive don't delete (preserves log history + link traceability)
- `source:` frontmatter immutable
- New files to canonical directory (never vault root)
- Follow naming conventions exactly
- Wikilinks are additive (adding free; removing requires explicit instruction)

---

## 10. User Feedback Channel — Inline Callouts

A lightweight feedback mechanism for the user to comment on LLM-generated content without breaking flow.

| Callout | Hotkey | Use when |
|---|---|---|
| `> [!question]` | Mod+Alt+1 | Ask a question |
| `> [!error]` | Mod+Alt+2 | Flag disagreement |
| `> [!tip]` | Mod+Alt+3 | Suggest a change |
| `> [!todo]` | Mod+Alt+4 | Specify an action |

**Lifecycle**: Fresh → Addressed (with `**Prompt:** *...*` + `**Response:**` blocks) → Pinned (`[[pinned]]` marker exempts from sweep) → Legacy (swept by `/archive-callouts` after 180d to per-thesis archive).

**Workflow**:
1. Drop callout inline next to LLM output via hotkey
2. Continue writing — callout is a flag, not a blocker
3. Ask Claude: *"Address fresh callouts in [[Theses/TICKER]]"*
4. Claude edits sections in-place, marks as Addressed, writes Log entry prefixed `Addressed user callouts:`
5. `/sync TICKER → /graph last`

**Body-is-deliverable rule**: full analysis goes in the body section; the callout's `Response:` is a 1-3 sentence ledger + pointer to body. **Callouts are an audit trail of the user-Claude exchange, not appendix storage.**

---

## 11. UI/UX Build Specification

### 11.1 Recommended Layout — Single-Page Vertical Scroll

Sticky left nav (or top tabs for mobile/compact). **Context Engineering sits at slot #2, right after the hero — before workflows, before skills, before everything.** Architecture follows so newcomers understand where the context files live. Everything else orbits.

```
[ HERO ]                            TL;DR framed around context engineering;
                                    answers "why isn't ChatGPT enough?" in 2 sentences

[ ⭐ CONTEXT ENGINEERING ]          THE CENTERPIECE — half the UI's depth lives here
                                    ├─ The 6 context files (interactive inspector — MANDATORY)
                                    ├─ The 10 prompt-engineering patterns (expandable cards)
                                    ├─ Context-flow animator (session lifecycle)
                                    └─ Citation table (pattern → source-file section)

[ ARCHITECTURE ]                    Interactive directory tree;
                                    context files visually distinguished (color, badge)

[ ANIMATED CORE LOOP ]              Forward & Backward loops, animated;
                                    EACH step highlights which context files it reads/writes

[ WORKFLOWS ]                       Scrollable cards with terminal-style chains;
                                    EACH chain shows which context files mutate at each step
                                    + cites User Guide §3 chain

[ SKILLS CATALOG ]                  4-column grid;
                                    EACH skill card shows context-file reads/writes
                                    + cites User Guide §5 entry + INFRASTRUCTURE.md spec

[ NOTE ANATOMY ]                    Tabbed view (Thesis / Research / Sector / Macro)
                                    + cites CLAUDE.md Conventions and User Guide §6

[ SAFETY ]                          3-tier visual + operational rules
                                    + cites CLAUDE.md Change Safety Rules

[ INLINE CALLOUTS ]                 Live demo of dropping a callout
                                    + cites User Guide §6 Inline callouts

[ FAQ ]                             Common misconceptions

[ GET STARTED ]                     Concrete next steps with explicit pointers to:
                                    User Guide §0 First Run, §4 "I Want To..." decision guide,
                                    INFRASTRUCTURE.md §1 Architecture Overview
```

**Visual emphasis allocation**: the Context Engineering section should occupy roughly 35-45% of total scroll height and reading time. Workflows + Skills together should occupy ~25%. Everything else <10% each. **If the user remembers only one section, it must be Context Engineering.**

### 11.2 Required Interactions

1. **⭐ Context-file inspector (MANDATORY, hero interaction)** — Detailed, interactive visualization of all 6 context files (`CLAUDE.md`, `_hot.md`, `_graph.md`, `_catalyst.md`, `.last_sync`, `_Archive/Snapshots/`). For each file, show:
   - **Synthetic content** — a realistic excerpt (~10-30 lines)
   - **Skills that READ this file** — clickable list; clicking jumps to the skill's card
   - **Skills that WRITE this file** — clickable list with write-mode (append-only, overwrite, mtime-touch, snapshot)
   - **The prompt-engineering pattern it implements** — short explanation
   - **Citation strip** — links to the exact `INFRASTRUCTURE.md` and `User Guide.md` sections
   - **"What breaks if you delete this file?"** — concrete failure mode
   - **"Cross-domain analogy"** — how this pattern would apply outside finance

   **This is the heart of the UI.** Allocate the most design polish here. Treat the inspector as a six-tab panel or a six-column dashboard, not as a list.

2. **Context-flow animator (MANDATORY)** — Animate one full session lifecycle so a newcomer sees the context files "in motion":
   - (a) User types `/sync NVDA` in a terminal pane
   - (b) Skill reads `CLAUDE.md` (highlight) + `_hot.md` (highlight) + `_graph.md` (highlight; show adjacency lookup for NVDA)
   - (c) Skill does pre-flight checks (lock acquisition animation; show `.locks/` dir)
   - (d) Skill makes Edits to `Theses/NVDA - Nvidia.md` (show snapshot pre-edit copy being created)
   - (e) Skill writes deltas to `_hot.md` (compression contract reference)
   - (f) Skill exits; user runs `/graph last`; `.graph_invalidations` is consumed and cleared

   Pause/play, step controls, speed slider. Every animation frame should show which files are being read/written.

3. **Animated Core Loop diagram** — Show data flowing from `_Inbox/` → `/ingest` → `/sync` → thesis updates. Step-through mode highlights what each skill modifies. **Each step labels the context files it touches.**

4. **Live thesis note browser** — Embed 1-2 synthetic thesis notes; user explores 14 sections via accordion or tabs. Show frontmatter, body, Log entries. Annotate which sections are append-only (Tier 2) and which trigger downstream propagation when edited.

5. **Skill simulator** — Clickable terminal. User "types" a skill (`/sync TICKER`); see simulated output (pre-canned, deterministic). Minimum implementations: `/ingest`, `/sync`, `/status`, `/thesis`, `/stress-test`. **Output should explicitly name every context file the skill read/wrote**, mirroring real skill behavior.

6. **Workflow chain runner** — Pick a scenario ("new earnings", "macro shock") → watch the chain animate step-by-step with each skill's output appearing. **Show context-file mutations at each step** (e.g. "`_hot.md` updated", "snapshot created", "`.graph_invalidations` appended").

7. **Callout demo** — Inline next to a paragraph, click "Drop a Question" → show Claude's `**Response:**` materialize → show the lifecycle progression (Fresh → Addressed → Pinned → Legacy).

### 11.3 Visual Style

- **Dark mode default** (matches Obsidian's typical theme); allow toggle
- **Monospace** for code/terminals (JetBrains Mono, IBM Plex Mono, or system mono)
- **Sans body** (Inter, system-ui)
- **Color palette** (mirrors the canvas):
  - **Purple** — meta/foundation (purpose, context files, prompt engineering)
  - **Orange** — structure (architecture)
  - **Yellow** — content artifacts (note anatomy)
  - **Cyan** — flow/process (loop, workflows)
  - **Green** — actions (skills, callouts)
  - **Red** — safety/warnings
- **Iconography**: Lucide icons via inline SVG; no icon-font dependencies
- **Diagrams**: prefer hand-coded SVG over Mermaid for full control

### 11.4 Sample User Journeys

Build affordances for these. Journey C ("Why is this novel?") is the marquee journey — the rest support it.

| Journey | Duration | Path through UI |
|---|---|---|
| **A — "What is this?"** | 30 sec | Hero (TL;DR framed around context engineering) + glance at Context File inspector |
| **B — "How would I use it day-to-day?"** | 3 min | Workflows section → pick one → step through chain → see notes + context files mutate → cite-out to User Guide §3 chain |
| **⭐ C — "Why is this novel?" (MARQUEE)** | 5-7 min | Context Engineering section → inspect each of the 6 context files → step through context-flow animator → expand each of the 10 prompt-engineering patterns → before/after vs raw ChatGPT comparison → cite-out to INFRASTRUCTURE.md sections |
| **D — "How would I build this myself?"** | 10 min | Context File inspector (the patterns to copy) + Architecture deep-dive + Skills catalog + sample SKILL.md + explicit links to INFRASTRUCTURE.md §pre-flight contract, §_hot.md compression contract, §Skill spec structure |
| **E — "I'm sold; where do I dig deeper?"** | 2 min | Get-Started section with curated reading order: User Guide §0 First Run → User Guide §3 Workflow Chains → INFRASTRUCTURE.md §1 Architecture Overview → INFRASTRUCTURE.md §pre-flight contract |

### 11.5 What NOT to Build

- ❌ Live Anthropic API calls (this is an explainer, not a live demo)
- ❌ Login / auth / user state (one-page educational tool)
- ❌ Backend (everything client-side)
- ❌ Investment advice or any reference to real tickers in synthetic content
- ❌ Full skill spec listings (link out to the source files for depth)
- ❌ Replication of the entire `User Guide.md` or `INFRASTRUCTURE.md` — the UI is a launchpad INTO those files, not a replacement for them. Every section must include explicit citations back; resist the urge to inline-copy long passages.

### 11.6 Tech Stack Suggestions (non-binding)

- Single HTML file, no build step
- Tailwind CSS via CDN OR scoped vanilla CSS
- React via esm.sh (`https://esm.sh/react@18`) OR Alpine.js OR vanilla JS — pick one
- Lucide icons via inline SVG
- Hand-coded SVG for diagrams (not Mermaid — gives finer control)
- LocalStorage for dark/light toggle persistence

---

## 12. Pedagogical Priorities

### 12.1 What MUST come through (in this priority order)

1. **⭐ Context engineering is the architectural insight.** The 6 context files (`CLAUDE.md`, `_hot.md`, `_graph.md`, `_catalyst.md`, `.last_sync`, `_Archive/Snapshots/`) are the secret sauce. Without them, the system is "Claude with some Markdown files nearby"; with them, it has persistence, incrementality, propagation, rollback, and concurrency safety. **This is the centerpiece of the UI.** If the user remembers nothing else, they should remember this.

2. **⭐ The 10 prompt-engineering patterns generalize.** System prompt as durable memory, context cache, dependency-graph priming, snapshot-based rollback, subagent forking, watermark incrementality, pre-flight contract, append-only audit logs, provenance immutability, deterministic skill specs. Each is a transferable building block for any LLM-augmented knowledge system. The UI should make the transferability explicit.

3. **The vault IS the agent's accumulated memory** — the substrate the context files coordinate against. Without vault content, the context files are empty machinery.

4. **Skills are deterministic specs, not "prompts".** The key distinction from ChatGPT.

5. **Safety is baked in.** Snapshot before every destructive op + 3-tier change model.

6. **This is a knowledge base, not a portfolio tracker.** No live prices, no PnL, no position sizing.
7. **The system is opinionated.** Enforced 14-section thesis structure, no hedge words, tables over prose. Opinionation produces consistency across hundreds of notes over years.

### 12.2 Common misconceptions to head off

- **"Isn't this just RAG?"** No. RAG = retrieval-augmented generation against a static index. This is **stateful, structured, mutually-aware** notes that the LLM both reads AND writes through deterministic workflows. The vault grows; the LLM acts on its own prior output.

- **"Why not just use ChatGPT with file uploads?"** ChatGPT has no persistent memory of your vault, no skill enforcement, no rollback, no propagation. You'd re-explain your context every session. The deterministic-skill layer doesn't exist.

- **"Why Obsidian specifically?"** Obsidian gives you Markdown files in folders (LLM-readable), wikilinks (LLM-traversable), and a graph view (LLM-extractable). It's the lowest-friction substrate for human + LLM collaboration. Any plain-text editor would work; Obsidian's affordances make the human side ergonomic.

- **"Is this only for finance?"** The investment-research instantiation is one use case. The architectural patterns — skills, context files, snapshots, propagation, append-only audit logs, subagent forking — generalize to any LLM-augmented knowledge work (legal research, scientific literature review, software architecture documentation, journalism).

- **"Doesn't this just make the LLM produce average analysis faster?"** The opinionated writing standards + non-consensus mandate + critical perspective requirement push output toward *better* analysis, not just faster. The 14-section thesis structure forces consideration of Outstanding Questions, Bear Case, and Conviction Triggers — sections that consensus analysis often skips.

### 12.3 Glossary (define on first use in the UI)

- **Context engineering** — Architecting a stateless LLM into a stateful agent through structured files (system prompts, caches, dependency maps, snapshots) that the LLM reads on every session and writes back to as it operates. The architectural pattern this entire UI is teaching.
- **Context file** — One of the 6 structured files (`CLAUDE.md`, `_hot.md`, `_graph.md`, `_catalyst.md`, `.last_sync`, `_Archive/Snapshots/`) that coordinate the vault's agent behavior.
- **Wikilink** — `[[note-name]]` syntax for internal cross-reference in Obsidian
- **Frontmatter** — YAML metadata block at the top of a Markdown file
- **Markdown** — Plain-text formatting standard (`# Heading`, `**bold**`, `[link](url)`)
- **MOC** — Map of Content (Obsidian convention for an index/hub note)
- **Subagent** — A child Claude instance spawned for an isolated subtask (used by `/lint`, `/prune`, `/surface`, `/retro`)
- **Snapshot** — A pre-edit backup copy of a file written by every destructive skill
- **Skill** — A Markdown-spec multi-step workflow callable as `/skill-name`
- **Watermark** — A timestamp marker used to identify what's changed since the last operation (e.g. `.last_sync`)
- **Adjacency** — In `_graph.md`, the per-thesis list of related theses/research/sectors
- **Pre-flight contract** — The 4-procedure check (vault lock, rename marker, name sanitization, section probe) every write-skill runs at Step 0

---

## 13. Pre-Distilled Reference

### Vault statistics (as of 2026-05-24)
- 40+ Thesis notes
- 133+ Research notes
- 13 Sector notes
- 6 Macro notes
- 5 existing Canvas files
- 21 Skills
- 4 Templates

### Writing standards (from CLAUDE.md)
- Lead with the insight or the number; never with context the reader already has
- No hedge words: "importantly", "notably", "significantly", "it's worth noting", "interestingly", "crucially"
- Every sentence earns its place with a data point, insight, or specific claim
- Tables over prose for comparative or quantitative content
- Thesis Log entries: max 2 lines
- Research notes for existing theses: lead with what changed, not a business description

These standards apply to the vault's internal writing. **The UI itself should also follow them** in any inline copy (descriptions, tooltips, FAQ answers).

### The two complementary loops (canonical diagram)
```
FORWARD LOOP                                    BACKWARD LOOP
─────────────                                   ─────────────
_Inbox drop                                     /retro [1w|1m|1q]
    ↓                                                 ↓
/ingest        ← raw → Research notes           [review window]
    ↓                                                 ↓
/sync          ← propagate to theses            /status · /deepen · /stress-test
    ↓                                                 ↓
[work]         ← analysis, callouts             /sync
    ↓                                                 ↓
/sync          ← propagate additions            /graph last
    ↓
/graph last    ← reconcile dependency map
```

---

## 14. Synthetic Sample Data

Use these synthetic examples in the live thesis browser and skill simulator. **Do not use real ticker names or real positions** — invent fictional companies clearly.

### Sample Thesis (truncated)
```markdown
---
date: 2026-05-23
ticker: ACME
status: active
conviction: medium
sector: Industrial Automation
source: synthetic-demo
---

# ACME - Acme Robotics

## Summary
ACME makes industrial humanoid robots for warehouse picking, undercutting human
labor cost by ~60% at scale via a vertically-integrated hardware/software stack.
2026 unit shipments tracking 4,800 vs guide 4,000 (+20% beat), with ASP holding
above $75K. Conviction: medium pending sustained gross-margin trajectory through
the SF2 manufacturing node ramp in Q3.

## Key Non-consensus Insights
1. **Hardware-software disaggregation enables an Apple-vs-PC strategy.** Most
   competitors sell either the robot or the software; ACME bundles a closed
   stack that hits 94% picking accuracy vs 81% sector median...

2. **EU labor regulation forces adoption.** The 2026 Düsseldorf Accord caps
   warehouse shift length at 6 hours and mandates a 1.4× wage uplift...

## Outstanding Questions
1. Can SF2 manufacturing achieve >65% yield by Q3 2026? Current 51% requires
   a Q2 process inflection that has slipped twice...

## Key Metrics
| Metric | Value | Notes |
|---|---|---|
| Market Cap | $18.2B | -22% from 52-wk high |
| EV/Revenue (NTM) | 8.4× | vs sector median 5.1× |
| Revenue Growth (YoY) | +85% | accelerating from +71% in 2025 |
| Gross Margin | 38% | guide 42-45% post SF2 ramp |
| FCF Yield | -2.1% | reinvestment phase through 2027 |

## Conviction Triggers
- **→ HIGH if** SF2 yield exceeds 65% AND Q3 GM > 42%
- **→ LOW if** Q3 unit shipments miss guide by >15% OR competitor breakthrough on hardware-software unbundling
- **→ CLOSE if** EU Accord challenged in court AND labor cost arbitrage compresses below 30%

## Log
### 2026-05-23
- Ingested: Q1 transcript — units beat by 33%, GM flat; strengthened, scaling pathway intact

### 2026-05-15
- Stress test: identified SF2 yield risk; conviction unchanged, added to Outstanding Questions
```

### Sample Research Note (truncated)
```markdown
---
date: 2026-05-15
source_type: earnings
ticker: ACME
sector: Industrial Automation
source: synthetic-demo
---

# 2026-05-15 - ACME - Q1 2026 Earnings

## Thesis Delta
Q1 unit shipments 1,200 vs guide 800-1,000 (+33% beat). Strengthens Bull Case
bullet #1 (scaling pathway). ASP -15% YoY but ABOVE the bear-case floor of $70K.
Conviction unchanged; SF2 yield commentary still vague.

## Summary
ACME reported Q1 2026 results with revenue +85% YoY to $124M. Management
emphasized the SF2 process ramp will deliver "structural margin inflection"
in H2, declining to commit to a specific yield number...

## Evidence
| Metric | Q1 25 | Q1 26 | Delta |
|---|---|---|---|
| Units shipped | 320 | 1,200 | +275% |
| ASP ($K) | 89 | 76 | -15% |
| Revenue ($M) | 67 | 124 | +85% |
| Gross Margin | 31% | 38% | +700 bps |
| Backlog (units) | 1,800 | 6,200 | +244% |

## Contradiction Check
The +700 bps GM expansion partially contradicts Bear Case bullet 2 ("ACME's
margin trajectory will stall as competitors flood the mid-tier"). Hold the
contradiction in tension — competitor pressure is concentrated at the <$50K
ASP tier, which ACME doesn't serve. Bear case more accurately re-framed as
TAM-ceiling, not margin-compression risk.
```

### Sample skill output: `/sync TICKER` (simulated)
```
$ /sync ACME

[Step 0] Pre-flight: ticker:ACME lock acquired
[Step 1] Reading recent activity since .last_sync (2026-05-22 18:42)
[Step 2] Graph-assisted scope: 3 Research notes, 1 thesis, 1 sector
         - Research/2026-05-15 - ACME - Q1 2026 Earnings.md (new)
         - Research/2026-05-12 - Industrial Automation - Düsseldorf Accord Update.md (new)
         - Theses/ACME - Acme Robotics.md (adjacent)
         - Sectors/Industrial Automation.md (sector parent)

[Step 3] Propagation gates:
         ✓ Research notes have non-skill-origin prefixes
         ✓ Thesis has Log entries from research
         → Sector propagation: ENABLED

[Step 4] Edits:
         - Theses/ACME: appended Log entry, updated Catalysts (SF2 Q3 yield call)
         - Sectors/Industrial Automation: updated Macro shifts (Düsseldorf Accord)
         - _hot.md: added Active Research Thread entry, updated Conviction Changes section

[Step 5] Snapshot pre-edit copies created:
         - _Archive/Snapshots/ACME - Acme Robotics (pre-sync 2026-05-23-2214).md
         - _Archive/Snapshots/Industrial Automation (pre-sync 2026-05-23-2214).md

[Step 6] Drift check: 3/5 recent ACME updates flagged headwinds
         ⚠️  Conviction drift signal — consider /status ACME conviction medium→low
         OR /status ACME reaffirm

[Exit] Sync complete. 2 files modified, 2 snapshots created.
       Suggested next: /graph last
```

---

## 15. Output Checklist

Before declaring the UI done, verify:

**Structural**
- [ ] Single self-contained HTML file (no external assets except CDN-loaded JS/CSS)
- [ ] Dark mode default with light toggle, persisted to LocalStorage
- [ ] Mobile-responsive (collapsible nav, stacked cards)
- [ ] No external API calls; everything client-side

**Context engineering centrality (highest priority)**
- [ ] **Context Engineering section is the centerpiece** — appears at slot #2 (right after hero), occupies ~35-45% of total scroll height
- [ ] **Context-file inspector implemented for all 6 files** with synthetic content, READ/WRITE skill lists, pattern explanation, citation strip, failure mode, cross-domain analogy
- [ ] **Context-flow animator implemented** — animates a full session lifecycle showing context-file reads/writes
- [ ] **Citation table (§8.11) rendered in the UI** mapping each pattern → source-file section
- [ ] **All 10 prompt-engineering patterns surfaced as expandable cards**
- [ ] Architecture section visually distinguishes context files from regular vault content

**Citation requirement (mandatory)**
- [ ] **Every major section has explicit `User Guide.md` and/or `INFRASTRUCTURE.md` citations** with exact section anchors
- [ ] Each Workflow card cites the User Guide §3 chain it implements
- [ ] Each Skill card cites the User Guide §5 entry AND the INFRASTRUCTURE.md spec
- [ ] Each Context File card cites both source files with exact anchors
- [ ] "Get Started" section curates a reading order across both source files
- [ ] No major section is missing a citation strip

**Content quality**
- [ ] All 7 must-convey concepts present (per §12.1)
- [ ] Animated Core Loop diagram works (forward + backward); each step labels context files touched
- [ ] At least 4 of the 7 recommended interactions implemented (inspector + animator are mandatory)
- [ ] No real ticker names or investment advice
- [ ] Glossary defines context engineering, context file, wikilink, frontmatter, MOC, skill, subagent on first use
- [ ] Honors the vault writing style in inline copy (no hedge words, lead with insight)
- [ ] Common misconceptions section explicitly addresses "isn't this RAG?" and "why not ChatGPT?"

---

## 16. Final Notes for the Receiving LLM

- **The centerpiece is context engineering.** If you build only one section well, build the Context File inspector + the 10-pattern explorer. Workflows and skills are supporting material; the context-engineering insight is what makes the UI worth building. Treat any time-pressure trade-off as "cut depth elsewhere, never here".

- **Read `User Guide.md` and `INFRASTRUCTURE.md` in full before writing code.** They are not optional reference material — they are the source-of-truth for the deep mechanics the UI is summarizing. The brief you're reading is an orientation layer that points at them; the substance lives in those files. **Build the citations into the UI as a first-class affordance, not an afterthought.**

- **Stylistically**, match the vault's writing standards even in your UI copy. The vault forbids hedge words ("importantly", "notably", "significantly", "interestingly", "crucially"). Apply the same discipline in tooltips, descriptions, FAQ answers. **Lead with the insight; never with context the reader already has.**

- **Pedagogically**, the goal is *understanding*, not enumeration. A user who understands the 6 context files + 10 prompt-engineering patterns is better served than one who has read every skill description. Build for the former.

- **Aesthetically**, the system is precise and opinionated. The UI should feel the same: clean, dense, mono-typeset for code, no decorative chrome. Reference Linear, Stripe Docs, or Anthropic's own documentation for tone.

- **Architecturally**, you're explaining a system that demonstrates how to make LLMs reliable through external structure. **The medium IS the message** — your UI itself should be reliable, predictable, and free of LLM-generated bloat. Cut every paragraph that doesn't earn its place.

End of brief. Build a UI that makes a finance-literate, Obsidian-naive newcomer say *"so context engineering is the trick — and here's exactly where to read more"* within 10 minutes.
