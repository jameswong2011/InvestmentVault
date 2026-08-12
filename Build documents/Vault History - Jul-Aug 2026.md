# Vault History — One Month of Evolution (5 Jul → 7 Aug 2026)

34 days of vault activity: **11 git commits, 328 pre-edit snapshots, 12 new theses, 6 new skills, 8 multi-agent workflow scripts, 2 new macro frameworks, a 27-name conviction re-rate, and an automation pipeline that went from zero to twice-daily production.** The month splits into two alternating modes — research sprints and infrastructure sprints — and the pattern of alternation is itself the story: each infra sprint raised the throughput ceiling of the research sprint that followed.

All dates verified against git commit history, thesis `## Log` headers, snapshot filename timestamps, and [[_hot.md]] archives.

---

## The month at a glance

| Week | Infrastructure track | Research track | Snapshots |
|---|---|---|---|
| Jul 5–11 | Skill hardening (`verify_note.py`, `numbers_compute.py`, transcript extractor) | Research sprint (12+ notes); **vault-wide 27-name conviction re-rate (Jul 11)**; CBRS + CAMT initiated | 36 |
| Jul 12–18 | Codex dual-agent port (`.agents/`, `.codex/`, `AGENTS.md`); Claudian plugin rewrite (+10.8k lines) | **Mechanical batch peak**: `/numbers` ×78 theses ×2 passes, `/deepen --sync-metrics` ×25; 10 business breakdowns in one day (Jul 14); SE, TSEM, LYV, ONON initiated | 220 |
| Jul 19–25 | **Automation build-out**: n8n Daily Intel goes live (Jul 18), 8 portfolio workflows + 5 diagnostic skills (Jul 23), hooks + launchd schedule, `Website/` pipeline | Near-zero: TSM Q2 earnings (Jul 24) synced across ~12 semis theses — the only research note in 19 days | 31 |
| Jul 26–Aug 1 | Build documents reorganized; `n8n Automations.md` (2,354 lines); plugin rewrite #2 | [[Macro & Technology/Sustainability of AI Capex.md]] framework (854 lines); BE + ORCL initiated from hedge-sourcing doc | 12 |
| Aug 2–7 | **Portfolio tracker deploy** (Aug 4): `portfolio-snapshot` skill, [[Live Portfolio.md]] restructure | **Research sprint resumes**: 4 theses in one session (2454, GRND, HOOD, IREN); NBIS/CRWV Rubin-ROIC modeling; AI power-markets deep-dive → 10-file sync; UBER AV reassessment | 29 |

---

## Prologue (Jul 3–4)

The month's analytical foundation landed just before the window: `[[Lens - Automation & AI Readiness]]` and `[[Lens - Value Layer Monopoly]]` were added to `/Mental Models` (Jul 3) — both now mandatory pre-analysis reads per `CLAUDE.md` — alongside 8 new theses (036930, 2383, 3110, 6515, ARM, LPKF, ONTO, SOI) and [[Watchlist.md]]. Every conviction call made later in the month runs through these two lenses.

---

## Week by week

### Jul 5–11 — The re-rate

- **Jul 8–9** ("Big skills cleanup" + "Second round skill fix"): determinism push — `lint.py` extracted from prose spec into a 973-line standalone script; `/ingest` gains `verify_note.py` (329 lines), `/numbers` gains `numbers_compute.py` (250 lines), `/transcript` gains `extract_transcript_signals.py` (432 lines). Skill behavior moved from LLM-interpreted prose to executable code.
- **Jul 9–11 research sprint**: lens synthesis notes for both new Mental Models lenses, PLTR model-evolution deep-dive, NET stress test, MRVL-vs-AVGO and Murata-vs-MLCC comparisons, AI-adoption gating-thresholds framework. New macro note: DRAM Memory Cycle (duration, peak timing, second-order effects).
- **Jul 11 — vault-wide valuation scoreboard**: a multi-agent pass re-rated 27 of ~78 theses in one run (full ledger below). 27 `pre-status` snapshots fired at 06:32:11 — one batch, one timestamp.

### Jul 12–18 — Mechanical hygiene + the dual-agent port

- **Jul 12**: `/numbers` swept all ~78 theses **twice** in one day (156 snapshots — 79% of the week's total) and `/deepen --sync-metrics` propagated refreshed metrics into the prose of 25 theses. The entire book's quantitative layer was re-based in a single day.
- **Jul 12** ("Codex Install"): Claudian Obsidian plugin `main.js` grew +10,828 lines; old plugin archived.
- **Jul 14**: 10 business-breakdown deep-dives written in one day (AAPL succession, Citadel, DE Shaw, EDA primer ×2, GAW, ISRG, Intel Foveros-vs-CoWoS, LYV, MCO, MONC, ONON, RDDT, TTWO).
- **Jul 18** ("Pre-twitter API build"): the vault became **harness-agnostic** — `.agents/skills/` mirrors every skill for OpenAI/Codex agents via an 815-line `port_claude_skills.py` converter; `.codex/agents/` gains read-only and worker profiles; `AGENTS.md` (259 lines) created. Same commit: `followups-contract.md`, `provenance-tags.md`, `trigger-touch.md` shared contracts — [[_followups.md]] and [[_watchers.md]] become tracked state files.

### Jul 19–25 — The automation week

Research output stopped; the machine got built instead.

- **Jul 18–19**: n8n **Daily Intel** pipeline goes live — first raw X-dashboard dumps land Jul 18 (5 in one evening); `setup-vault.sh` rewritten; `Thesis Breakdowns/` + Breakdowns template introduced.
- **Jul 19–24**: automation iteration visible in the archive — 4–5 raw n8n test dumps per day, later swept to snapshots. Format stabilizes **Jul 25** as the twice-daily `News Brief` + `X Intel` pair that still runs today.
- **Jul 23** ("23 Jul Sync") — the single densest infra commit of the month:
	- **8 multi-agent workflow scripts** in `.claude/workflows/`: portfolio-conviction-audit, portfolio-correlation, portfolio-macro-exposure, portfolio-retro, portfolio-scenario, portfolio-stress-test, portfolio-supply-chain, vault-contradictions — plus the [[_workflows.md]] registry and its generator.
	- **5 new diagnostic skills** feeding them: `assumptions`, `conviction-audit`, `dependency-map`, `macro-exposure`, `value-chain`.
	- **Hooks**: `guard-protected.py` (Tier-1 file guard), `mark-graph-dirty.py`, `refresh-graph.py` — graph freshness became event-driven instead of manual.
	- **Scheduled jobs**: launchd plists for `/catalyst` and `/lint` — the first automated `Vault Health - lint` note appears in Daily Intel Jul 26.
	- **`Website/` publishing pipeline** live: 7 dated pieces Jul 22–29 (Laniakea Partners overview, semiconductor-cycle framework, SK Hynix, Nvidia, TSMC, Pricing the End of the Semiconductor Cycle, Sustainability of AI Capex).
- **Jul 24**: the week's one research act — TSM Q2 2026 earnings ingested and synced across ~12 semiconductor theses (000660, 2383, 3110, AMAT, ASMI, AVGO, INTC, KLA, LRCX, MRVL, AMD, TSM).

### Jul 26–Aug 1 — Frameworks and documentation

- **Jul 29** ("29 Jul 26"): `Build documents/` reorganized into its current form — README, Setup Guide, User Guide consolidated; **`n8n Automations.md` (2,354 lines)** documents the pipeline; plugin rewrite #2 (+2,219 lines).
- **Jul 29**: [[Macro & Technology/Sustainability of AI Capex.md]] created — 854 lines, now the load-bearing cross-thesis framework for CRWV, NBIS, BE, ORCL, IREN.
- **Jul 29**: BE and ORCL initiated — both sourced from the `Semiconductor bear market hedges` gap-analysis docs (archived in `_Archive/Docs/`), an explicit portfolio-construction motive rather than bottom-up discovery.

### Aug 2–7 — Research resumes on new rails

- **Aug 4** ("Portfolio tracker deploy"): `portfolio-snapshot` skill + `build_snapshot.py` (483 lines); first published snapshot (`Portfolio Snapshot/04-08-2026.md` + SVG chart); [[Live Portfolio.md]] restructured.
- **Aug 4, 16:00–20:30 — four theses in one session**: 2454 (MediaTek), GRND (Grindr), HOOD (Robinhood), IREN — with an NBIS-vs-CRWV `/compare` and a `/deepen NBIS` run sandwiched in. The throughput demonstrates the compounding: graph primer + templates + diagnostic skills make a thesis a ~1-hour object, not a weekend project.
- **Aug 4–5**: NBIS Rubin-generation ROIC modeling — rate-sensitivity model note, iterative `Refined:`/`Re-specced:` Log entries across two days.
- **Aug 5–6**: AI Data Center Power Markets deep-dive (nodal/LMP pricing framework) → `/sync all` propagated it to IREN, NBIS, VRT, CRWV, BE + 4 sector notes + 1 macro note in one pass — the cleanest demonstration of the ingest→propagate loop all month.
- **Aug 6**: `/deepen UBER` — AV-sentiment reassessment; Waymo direct-app plans fired an existing falsifier (see open items).

---

## Conviction ledger

### Jul 11 vault-wide re-rate (27 names, one run)

| Direction | Tickers |
|---|---|
| medium → **HIGH** | INTU, META, NFLX, PINS, UBER (+ monitoring→active), CSGP, CSU, PCOR, WTC |
| **HIGH → medium** | AMD, NET, PANW, 6981, MRVL, VICR, AEHR, AIXA, IQE, SNDK, BESI, TTWO, 000660, LNG, SPOT |
| medium → **LOW** | INTC, HIMS |
| Status only | SIVE active → monitoring |
| Held HIGH | TSM, NVDA, ASMI, KLA, PLTR, AMAT, GAW, LRCX, SHOP, LITE |

Sample verbatim reasoning (from thesis Logs):

- **HIMS → LOW**: "US revenue -8%, ARPU -6%, GAAP loss with GM at 65% (through the thesis's own bear line) — reported growth is now an acquired roll-up, not organic platform economics; the vertical-integration moat was falsified by the company's own US compounding exit."
- **NET → medium**: "AWS shipped the Act IV rail (x402) free in CloudFront GA two weeks before Cloudflare's own Monetization Gateway waitlist; zero Act IV revenue disclosed at 34x FY26 sales / ATH."
- **META → HIGH**: "~17-18x fwd P/E (cheapest Mag-7, fastest growth) embeds low-teens earnings growth versus delivered +30% op income; capex-ROIIC fear is the mispriced variable."

Three of the downgrades (NET, 6981, AEHR) actioned flags raised by earlier stress tests — the trigger discipline working as designed.

### New thesis initiations (12)

| Date | Ticker | Conviction | One-line rationale |
|---|---|---|---|
| Jul 9 | CBRS (Cerebras) | low | WSE interconnect economics unresolved |
| Jul 11 | CAMT (Camtek) | medium | Initiation |
| Jul 13 | SE (Sea Ltd) | medium | Shopee+Monee+Garena support case; TikTok pressure + unseasoned +71% loan book cap it |
| Jul 14 | TSEM (Tower Semi) | low | Contracted SiPho validates inflection but $25.5B ≈ 34x mgmt's 2028 target |
| Jul 14 | LYV (Live Nation) | medium | Value-layer ticketing flywheel real; ATH valuation + monopoly jury verdict cap it |
| Jul 15 | ONON (On Holding) | medium | Repriced ~$54→$37 on guide optics, not demand miss; seeds new sector note (Athletic Footwear & Apparel, added Jul 29) |
| Jul 29 | BE (Bloom Energy) | low | Q2 33.4% GAAP GM validates inflection but ~17.3x LTM rev prices multi-GW conversion pre-proof |
| Jul 29 | ORCL (Oracle) | medium | "Two-Oracles" frame: 16%-GM OpenAI-concentrated OCI vs mispriced 70%-GM multicloud-DB layer monopoly |
| Aug 4 | 2454 (MediaTek) | medium | Google-TPU ASIC option funded by mobile cash cow; ~55x already prices ASIC success |
| Aug 4 | GRND (Grindr) | low | Cheap but alleged undisclosed SEC probe on paying-user metric + withdrawn take-private floor |
| Aug 4 | HOOD (Robinhood) | medium | Platform-asset annuity building but ~40x prices flawless execution on 59%-cyclical revenue |
| Aug 4 | IREN (IREN Ltd) | medium | Owned 5.8GW power/land layer inverts "poor short" into convex long; ~$21B funding gap caps it |

Initiation conviction is deliberately conservative: 3 low / 8 medium / 0 high. High conviction has to be earned through the research loop, never assigned at creation.

---

## Skill-run activity (from 328 in-window snapshots)

| Trigger | Runs (snapshot count) | Concentration |
|---|---|---|
| `/numbers` | 155 | Single Jul 12 two-pass batch across ~78 theses |
| `/sync` | 37 | Jul 12/14/15/24, Jul 29, Aug 6 |
| `/status` | 27 | Single Jul 11 scoreboard batch |
| `/deepen --sync-metrics` | 25 | Single Jul 12 batch |
| `/deepen` (analytical) | ~19 | PLTR, SNDK, WTC, META, INTU, CBRS, SE (Jul) → NBIS, UBER (Aug) |
| `/thesis` | 12 | Matches the 12 initiations |
| `/compare` | 6 | MRVL/AVGO, MLCC set, NBIS/CRWV |
| `/stress-test` | 3 | NET (Jul 10), INTU (Jul 13) |
| `/catalyst` | 2 | Jul 17, Jul 26 (then scheduled via launchd) |
| n8n test artifacts | ~35 | Jul 18–27 iteration, swept to archive |

---

## What the month demonstrates

1. **Infra and research alternate in sprints — and infra pays back immediately.** Jul 15–Aug 3 produced exactly one research note while the automation layer was built; the week after produced 4 theses in one session, a multi-thesis quantitative model, and a 10-file propagation. The tooling investment converted directly into research throughput.
2. **Hygiene is batch-mechanical, not continuous.** Metrics refresh (78 theses ×2), metric-prose sync (25), and conviction re-rate (27) each ran as single-day sweeps with one snapshot timestamp — drift is eliminated in bulk, then the book stays coherent for weeks.
3. **Attention migrated up the stack.** Raw scanning went to n8n (twice-daily briefs + X dashboards), periodic hygiene went to launchd (`/catalyst`, `/lint`), portfolio-scale analysis went to workflow fan-outs. What stayed manual is exactly what should: thesis judgment and Tier-3 conviction calls.
4. **Every mutation stayed reversible and attributed.** 328 snapshots, every conviction change carrying a falsifiable reason in an append-only Log. The Jul 11 re-rate is fully reconstructible 27 days later from file evidence alone — which is how this document was written.
5. **The open loop is visible too.** [[_followups.md]] holds 30 open findings (all Jul 15) with zero resolved; INTU (stress test falsified 5/6 bull assumptions, Jul 13) and UBER (Waymo direct-app falsifier fired, Aug 6) both await their `/status` calls. The system surfaces its own unfinished business — next month's first actions are already written down.

---

## Standing state as of 7 Aug 2026 (uncommitted working tree)

- Theses 2454 / GRND / HOOD / IREN + all Aug 4–6 research notes (NBIS Rubin ROIC, NBIS-vs-CRWV, AI power markets, rate-sensitivity model, UBER AV) — created, not yet committed
- Daily Intel running current through Aug 7 (News Brief + X Intel)
- `Build documents/Vault Explainer.md` + presentation deck in progress (this session)
- 7 stale `_Inbox` n8n digests (Jul 17–20) staged for deletion
- Pending decisions: `/status INTU conviction high→medium`, `/status UBER` reassessment, `_followups.md` triage
