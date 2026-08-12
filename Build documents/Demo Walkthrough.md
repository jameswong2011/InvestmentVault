# Demo Walkthrough — End-to-End Vault Session (3–4 hours)

A scripted runbook demonstrating every layer of the vault in one sitting: the wiki, the core loop, the analytical engines, portfolio-scale orchestration, the sensory pipeline, the safety machinery, and the publishing stack. Written 2026-08-07 against live vault state; re-verify the **Pre-flight** section on demo day since state moves daily.

**Design principle — demo as real work.** Every mutation in this script is genuine vault progress, not throwaway: the ingest processes a real `_Inbox` item, the callout pass addresses a real question, the Tier-3 demo executes a conviction change the vault has *already flagged as pending*. Nothing needs undoing afterward — and if anything goes wrong, that's the `/rollback` demo.

---

## Timing overview

| Act | Content | Duration |
|---|---|---|
| 0 | Pre-flight (before audience arrives) | 30 min prior |
| 1 | The idea + orientation tour | 25 min |
| 2 | The core loop, live: ingest → sync → graph | 40 min |
| 3 | Callouts — the disagreement channel | 15 min |
| — | *Break* | 10 min |
| 4 | Analytical engines: conviction-audit → live Tier-3 status change | 35 min |
| 5 | Portfolio-scale workflow (+ sensory-layer tour while it runs) | 30 min |
| — | *Break* | 10 min |
| 6 | Safety machinery: hooks, snapshots, rollback, locks | 15 min |
| 7 | Publishing layer + the evolution story + Q&A | 25 min |
| | **Total** | **~3 h 45** |

Cut-for-time order if running long: Act 7 publishing detail → Act 5 workflow (fall back to walking a prior output) → Act 3 (fold into Act 2).

---

## Act 0 · Pre-flight

**The day before:**

1. **Commit the working tree.** ~15 files are currently uncommitted (Aug 4–6 theses and research notes, Daily Intel, this document set). A clean git state means the entire demo is additionally reversible at the repo level.
2. **Verify no stale runtime state:** no `.vault-lock*` or `.rename_incomplete.*` files at vault root; `.claude/.graph_dirty` absent.
3. **Pick the ingest source** (Act 2) from `_Inbox/`. Current candidates (12 unprocessed): Samsung zHBM, SMIC N+3, Unitree robotics, neocloud economics, US grid constraints, CXMT/DRAM. Prefer a mid-size item (~2–8k words) — ingest completes in minutes. Avoid the Neel Somani *Power 2026* file as primary: it is 173KB (slow path) and its content overlaps the Aug 5 power-markets deep-dive — though if `/ingest` fires its **same-source dedup block**, that is itself worth showing (safety gate working).
4. **Smoke-test the data layer:** open [[Live Portfolio.md]] → Refresh. Confirms the FMP key before Acts 2/7 depend on it.
5. **Dry-run the workflow choice** (Act 5) once to know its real wall-clock on your machine, or save its output note as the fallback exhibit.
6. Skim `_hot.md` and today's thesis Logs so nothing in the live state surprises you.

**30 minutes before:**

7. Confirm this morning's n8n run: today's `News Brief` and `X Intel` exist in `Daily Intel/`; Telegram alerts visible on phone.
8. **Obsidian tab layout** (left→right): [[_hot.md]] · `Daily Intel/<today> - News Brief` · [[Theses/ORCL - Oracle Corporation.md]] · [[Theses/INTU - Intuit.md]] · [[_watchers.md]] · [[Live Portfolio.md]] · Claudian chat pane open.
9. Keep `Build documents/` docs one click away: [[Vault Explainer]], [[Vault History - Jul-Aug 2026]], [[User Guide]].

**Session-discipline rules for the driver:**
- One skill at a time — the vault is single-session by design (locks serialize; parallel `_hot.md` writes race).
- Never `/sync all` live (minutes-long). Scoped `/sync` or `/sync TICKER` only.
- Never `portfolio-stress-test` live (the heaviest sweep). Read-only workflows only.
- Anything Tier-3 will pause for confirmation — that pause is a feature; narrate it.

---

## Act 1 · The idea + orientation tour (25 min)

**Goal:** the audience understands *what kind of thing this is* before seeing it move.

1. **The one-liner** (2 min): "An LLM-maintained research wiki — Karpathy's compilation-not-retrieval pattern applied to equity research. The model doesn't answer questions about my documents; it *maintains a persistent artifact* that compounds." Show Explainer §1–§2; land the numbers table: **88 theses, 51 sectors, 209 research notes, 27 skills, 8 workflows, 5 automation pipelines.**
2. **`_hot.md`** (4 min): "This is session memory." Walk the six sections — active thread (UBER AV work), latest sync (Aug 6 power-markets propagation into 5 theses + 4 sectors), Recent Conviction Changes (the Jul 11 vault-wide re-rate), Open Questions (numbered to #162), portfolio snapshot line.
3. **One thesis end-to-end** (8 min): open **ORCL**. Walk the 15 sections quickly, dwelling on three: **Key Non-consensus Insights** (the "Two-Oracles" frame — 16%-GM OpenAI-concentrated OCI vs the mispriced 70%-GM multicloud-DB layer monopoly), **Conviction Triggers** (pre-committed falsifiable if-thens — "I wrote down today what changes my mind, so future-me can't renegotiate"), and **Log** (append-only; the audit trail everything else reads).
4. **The connective tissue** (6 min): the ORCL `sector:` → sector note (Active Theses routing table first); the ORCL block in `_graph.md` (adjacencies + log-tail cache — "how a skill finds the right 5 files instead of re-reading 88"); 30 seconds on `Mental Models/Generalist - Overview` — the READING PROTOCOL: "models are lenses, never conclusions; when every model agrees, that's the signal to hunt the bear case."
5. **Rules of the game** (5 min): CLAUDE.md scroll-through — writing standards (no hedge words, tables over prose, 2-line log entries), the three safety tiers. "Tier 3 is the line: the machine never changes conviction, status, or kills a file without my explicit confirmation. You'll see that gate live in Act 4."

---

## Act 2 · The core loop, live (40 min)

**Goal:** raw source → structured research → propagated wiki, in real time. This is the heart of the demo.

1. **Show the raw input** (2 min): open the chosen `_Inbox/` file. "Unstructured — a clipped article/PDF dump. Watch what the vault does with it."
2. **`/ingest`** (8 min incl. run time). Narrate while it works: source extraction → vault context check (does a thesis exist? prior research?) → 4-section note authored (**Thesis Delta first** — "what does this change, not what does this company do") → `verify_note.py` quality gate (blocks structurally deficient output) → original archived to `_Inbox/processed/`, `source:` locked as provenance.
3. **Read the output** (5 min): the new `Research/2026-08-XX - … .md`. Point at: Thesis Delta naming specific theses; **Contradiction Check** ("the anti-confirmation-bias section — mandatory"); provenance tags on figures (`[FMP]`, `[1×: source]`, `[est.]`).
4. **`/sync`** (10 min incl. run time): watch it read the graph to target files, snapshot before editing, then propagate — thesis Log entries appended, sector/macro sections updated where touched, `_hot.md` refreshed. Call out the **drift check** if it fires ("N of last 5 updates pushed against the Bull Case — consider `/status`").
5. **The invisible follow-through** (5 min): at turn end, the Stop hook sees the dirty flag and regenerates `_graph.md` automatically — show its `date:`/counts just updated. "Nobody ran `/graph`. Freshness is event-driven."
6. **The automated variant** (5 min): open today's News Brief — the funnel line ("~6,500 fetched → ~350 admitted → ~240 stories"). "Same loop, machine-sourced: `/ingest --from-brief` promotes stories from this brief straight into what you just watched. The Aug 5 power-markets deep-dive that synced into five theses entered exactly this way — see [[Vault History - Jul-Aug 2026]]."
7. **Beat to land** (2 min): "Ten minutes ago this was a clipping. Now every relevant thesis knows about it, the graph routes to it, and two months from now `/retro` will check whether the market agreed."

---

## Act 3 · Callouts — the disagreement channel (15 min)

**Goal:** show that pushback is a first-class, durable object — not chat scroll.

1. In the thesis `/sync` just touched, find a claim worth probing. Hit **⌘⌥1** → type a real question against that claim (2 min).
2. "Address fresh callouts in [[the thesis]]" (5 min). Narrate the contract while Claude works: **body is the deliverable, callout is the ledger** — the full analysis integrates into the note's spine; the callout becomes a Prompt/Response pair (your words verbatim in italics) with a pointer.
3. Show the result + the Log entry (`Addressed user callouts: …` — a non-skill prefix, so the next `/sync` treats it as research-driven) (4 min).
4. Show lifecycle depth (4 min): a `[[pinned]]` callout somewhere in the book ("a question I re-ask every quarter — exempt from archival"); a `## Legacy Callouts` section ("addressed exchanges auto-swept after 180 days — the full history of everywhere I pushed back, per note"). Line: "Four `[!error]` callouts on one name in a month *is* conviction drift — and the system says so."

---

## Act 4 · Analytical engines → a live Tier-3 decision (35 min)

**Goal:** the vault as adversary, ending in a real investment decision executed on stage.

**Context to narrate first** (3 min): "On Jul 13 a stress test falsified 5 of 6 INTU bull assumptions. The vault has been carrying a pending `high→medium` downgrade ever since — it's sitting in `_hot.md` and `_followups.md`. Today we action it."

1. **`/conviction-audit INTU`** (12 min incl. run time): read-only, no locks. While it runs: "Five of these diagnostic skills exist — assumptions, dependencies, macro bets, value chain, this one. Each is a lens the portfolio workflows can fan across all 88 names." Read the output: evidence-vs-conviction mismatch, whether triggers silently fired.
2. **`/status INTU conviction high→medium [rationale]`** (10 min): the **Tier-3 gate appears — stop and let the audience read it**: trigger-alignment line, mental-model-basis line, explicit confirm. Confirm. Show what one confirmation cascaded: frontmatter, sector table, `_hot.md` Recent Conviction Changes, Log entry, `_followups` resolution, pre-edit snapshot.
3. **The adversarial engine behind it** (10 min): open the Jul 13 INTU stress-test note (or Jul 10 NET). Point at the anti-anchoring design ("the short case is drafted *before* reading my Bull Case"), the `[consensus]` vs `[vault-blind-spot]` tags, the external-evidence mandate at high conviction. "Both of July's stress tests preceded downgrades. The system attacks my positions so the market doesn't get the first punch."

*Stretch (if ahead of schedule): fire `/stress-test HOOD` or `IREN` — a fresh Aug 4 draft — and read results in Act 7.*

---

## Act 5 · Portfolio scale + the sensory layer (30 min)

**Goal:** one question asked of all 88 theses at once — and the machine that reads the news before you wake.

1. **Launch** (3 min): request the **portfolio-macro-exposure** workflow (read-only; natural-language invocation — workflows aren't slash commands; show `_workflows.md` as the registry). Narrate the architecture as agents spawn: "One read-only agent per thesis, each literally following the `/macro-exposure` skill's method; an aggregator ranks concentration; nothing writes; nothing can touch conviction."
2. **While it fans out — sensory-layer tour** (15 min):
	- `_watchers.md`: "The control surface. These markdown tables — queries, RSS outlets, price-tripwire levels, X terms, even which model runs each pipeline stage — *are* the n8n configuration. Retargeting the machine is a table edit."
	- Today's **X Intel**: the theme table and **thesis-divergence flags** ("crowd narrative vs vault view — this UBER flag became a real `/deepen` reassessment this week").
	- Telegram: tripwire/catalyst alert examples — "a tripwire cites my own trigger block: a signal to read the thesis, not to act."
	- The governance line: "n8n only creates new files in `Daily Intel/` and `.data/`. It can never touch a thesis, never change conviction. Acquisition is automated; judgment is not."
3. **Results** (10 min): read the ranked concentration output — which macro variable the book is most levered to, which names share it. Close: "This is the question a 40-position PM can't answer from memory and a spreadsheet can't answer at all."

**Fallback** if the run is slow/erratic: keep it running in background and walk a saved prior workflow output (or the `vault-contradictions` registry entry) instead; return to live results whenever they land.

---

## Act 6 · Safety machinery (15 min)

**Goal:** why aggressive automation is safe here.

1. **The guard hook, live** (4 min): ask Claude to edit `CLAUDE.md` (any trivial change). The PreToolUse hook **blocks the write before it executes**. "Tier-1 protection isn't an instruction the model follows — it's machinery the model can't bypass. The escape hatch exists and re-arms itself every turn."
2. **Snapshots** (4 min): `_Archive/Snapshots/` — 394 files, `TICKER (pre-<trigger> <timestamp>).md`. Find today's `pre-status` INTU snapshot from Act 4. "Every destructive act pre-images itself. Closure snapshots carry a 30-day floor no cleanup flag can override."
3. **`/rollback`** (4 min): run list mode (read-only) — show it grouping by batch with manifests; "one command restores Act 4 wholesale, and cascade detection knows which sibling files belonged to the same transaction." Don't execute.
4. **Locks + weekly self-audit** (3 min): mention token-based scoped locks (why the demo runs one skill at a time), then open the latest `Vault Health - lint` note in Daily Intel: "Sunday 20:00, unattended, ~67 checks, publishes its own report. The vault tells me when it's decaying."

---

## Act 7 · Publishing layer + the evolution story (25 min)

**Goal:** research flows out, and the system visibly compounds.

1. **Live Portfolio → snapshot** (8 min): refresh [[Live Portfolio.md]] (34 holdings, FMP, tables persist into the note). Run `/portfolio-snapshot` — fast, mechanical — and show the stripped dated export with baked SVG chart in `Portfolio Snapshot/`.
2. **Outbound surfaces** (7 min): `Website/` essays (Jul 22–29, each tracing to vault notes via `source_note:`); `Thesis Breakdowns/` (bilingual 15-episode video scripts with the Evidence Ledger grading every claim VF→AI — "research integrity surviving translation into content"); the `publish: true` GitHub→website sync on every thesis/sector/macro note.
3. **The evolution close** (10 min): open [[Vault History - Jul-Aug 2026]]. Walk the month-at-a-glance table: the Jul 11 27-name re-rate, the Jul 12 mechanical sweeps, the Jul 23 automation commit, the Aug 4 four-theses-in-a-session sprint. Land the compounding argument: "Infra sprints and research sprints alternate — and each infra sprint raised the ceiling of the research sprint that followed. A thesis is now a ~1-hour object. That's the compound interest of the wiki."
4. **Q&A** — Explainer §17 FAQ covers the hard ones (RAG? hallucination? cost? off-script?).

---

## Contingency table

| Failure | Response |
|---|---|
| FMP down / key invalid | Skip live refresh; show Aug 4 snapshot in `Portfolio Snapshot/` and cached tables in the tracker; `/numbers` has a web-search fallback if needed |
| `/ingest` blocks on same-source dedup | Demo gold — show the block message, explain provenance dedup, pick the backup `_Inbox` item |
| Workflow too slow | Background it; walk a saved output or `_workflows.md`; return when it lands |
| n8n didn't run this morning | Use yesterday's News Brief / X Intel — content is dated, mechanics identical |
| Lock conflict (`.vault-lock` present) | A prior run died: show the lock file (teachable), verify no live session, remove per `_shared/preflight.md`, continue |
| Skill misbehaves mid-write | That's the Act 6 story early: `/rollback` list → restore, live |
| Running >30 min behind | Cut order: Act 7 detail → Act 5 live run → fold Act 3 into Act 2 |

## After the session

Nothing to reset — every mutation was real work (one source ingested and propagated, one callout addressed, one pending conviction change executed, one portfolio snapshot published). Optional hygiene: commit (`git add -A && git commit -m "Demo session <date>"`), confirm `_graph.md` refreshed, and add a Log entry to any thesis whose body you hand-edited during Q&A discussion (Workflow Rule 6 — so the next `/sync` propagates it).
