---
date: 2026-08-23
tags:
  - essay
  - research-process
  - laniakea-partners
  - llm-wiki
  - knowledge-systems
status: draft
audience: general-investor
source_note:
  - "[[Build documents/Vault Explainer]]"
  - "[[Build documents/User Guide]]"
  - "[[Build documents/INFRASTRUCTURE]]"
  - "[[Theses/000660 - SK Hynix]]"
source: internal synthesis
---

# Inside the vault: research as a compiled artefact

*Part one of three on the research system behind Laniakea Partners. This part covers the structure: what the system is and why it is built as a wiki rather than a chat. Part two covers the machinery that lets a language model maintain the book without breaking it. Part three covers the sensing and adversarial layers that make it argue back.*

**Nobody holds 95 investment theses in their head.** Our research book currently runs to 95 thesis notes (34 active, 31 monitoring, 30 draft), 53 sector maps, 11 macro frameworks and 376 research notes: roughly 1,500 plain-text files, of which 152 research notes carry a date from this month alone. At that scale the binding constraint on qualitative research is memory, in the specific sense of holding every prior claim, every pre-registered falsifier and every cross-holding dependency in a form the next incoming datapoint can be tested against within minutes of arriving.

The conventional solutions each give something up. Institutions solve scale with hierarchy and lose fidelity in the handoffs: evidence passes from analyst to sector head to portfolio manager, each transfer compressing the original observation and adding a layer of career incentive, so the person closest to the evidence holds the least authority (we covered this in *How Laniakea Partners Invests*). A solo analyst keeps fidelity and loses persistence: the conclusions survive, but the evidential chain that produced them decays, and two years in, a position is defended out of loyalty because the falsifiers that would have retired it were never written down. The obvious modern patch, a language-model chat window, fails a third way: each session is capable and amnesiac, so the same context is rebuilt every morning and discarded every night. Retrieval-augmented search does not repair this. It fetches fragments at query time, and nothing accumulates between queries.

The pattern we settled on is the one Andrej Karpathy sketched in April 2026 under the name 'LLM wiki': the model incrementally builds and maintains a persistent, interlinked body of markdown that sits between the analyst and the raw sources, so knowledge is compiled once, cross-referenced at write time, and thereafter kept current rather than re-derived on every question. His metaphor transfers directly onto our stack: Obsidian is the IDE, the language model is the programmer, and the wiki is the codebase. We choose the sources, ask the questions and make every final call. The model does the maintenance.

The system has three layers, and the discipline sits in who may write to which.

| Layer | Contents | Who writes it |
|---|---|---|
| Raw sources | Inbox deposits, overnight news and X sweeps, market-data feeds, our inline objections | The world and us; the model never modifies a source |
| The wiki | 95 theses, 53 sector maps, 11 macro notes, 376 research notes, plus the state files: session cache, dependency graph, follow-up register, catalyst calendar | The model, through 27 named procedures |
| The schema | A constitution file, four note templates, the procedure specifications | Us, rarely |

Sources are immutable, so provenance survives every rewrite above it. The wiki is regenerable, so a bad edit costs a restore rather than an argument about what a note used to say. The schema is the contract that keeps a thousand machine-written files structurally identical, and structural identity is what makes them queryable as a set rather than readable one at a time.

## The thesis is an adversarial contract

The unit of account is the thesis note: one file per name, fifteen fixed sections, identical across the book, from summary and business model through industry context, key metrics, bull and bear cases, catalysts and risks. The load-bearing sections are the ones designed to make the thesis attackable. Key Non-consensus Insights must each name the consensus they dispute, the first observable that should confirm the variant view, and the datapoint that would falsify it. Outstanding Questions are drafted as what a sceptical investment committee would ask before approving the position. Conviction Triggers are pre-registered if/then statements (raise if, cut if, close if) written down before the market has an opinion about them. And at the bottom of every thesis sits an append-only Log, two lines per entry, which no procedure may edit, reorder or delete.

The Log is where the format proves itself. Three entries from our SK Hynix note, trimmed:

> **2026-04-23** — Initial thesis created. Conviction: medium. Kill trigger: Samsung HBM4 captures >35% of Rubin allocation H2 2026.

> **2026-07-11** — Status change: conviction high → medium. ~6x forward earnings embeds true-cyclical mean reversion, but Q3 DRAM contract price growth is decelerating (~60% → 13–18% QoQ); the pricing second derivative has already turned against the bull case even as the multiple stays cheap.

> **2026-08-22** — [research note]: CMM-Ax is a CXL co-development, not a Rubin/HBM-share datapoint; HIGH/LOW/CLOSE no-touch. Conviction unchanged (medium).

The note was born carrying its own kill condition. The downgrade three months later cites a mechanism, the second derivative of contract pricing, rather than a mood. And the most recent entry records that a new datapoint was tested against the pre-registered triggers and touched none of them. That last habit is the one that matters most: negative results are logged, so 'nothing changed' is a recorded finding with a date on it rather than an absence.

Frontmatter does the same work in machine-readable form. Every note carries `status` (draft, active, monitoring, closed) and every thesis carries `conviction` (high, medium, low), which turns the book into a state machine: a watchlist tracker renders all 70 thesis tickers with trailing returns and forward multiples, coloured by whether the name is held or merely researched, and the colouring re-derives itself from the live holdings table on every refresh. Changing one of those fields is an investment decision, and the machinery treats it as one; part two covers the gate.

## Evidence flows one way

The folders form a pipeline. Raw material lands in an inbox. An ingestion procedure converts it into a structured research note. Synthesis accumulates in the thesis. Sector notes aggregate theses into maps of content covering industry history, competitive dynamics, product-level analysis and investor heuristics, so the industry view is a first-class document rather than an average of company views. Macro notes hold the cross-sector transitions (800-volt datacenter power distribution, panel-level packaging, stablecoin regulation as dollar infrastructure) with links back down into every thesis they touch.

Two rules give the pipeline its direction. Research notes are immutable once written: corrections go in a new note or a thesis Log entry, never in edits, so the evidence record cannot be quietly revised to fit the current view. And every research note leads with a Thesis Delta section stating what this source changes for the thesis, followed by a mandatory Contradiction Check, so a source is interrogated for what it breaks before it is filed for what it supports. A datapoint earns attention through its effect on a causal claim, never through novelty.

## The graph is compiled too

Wikilinks connect the layers, and a machine-built dependency graph compiles them: currently 1,887 edges across the book, one adjacency block per name listing its sectors, its macro exposures, the cross-thesis peers that share a mechanism with it, every research note that touches it, and the last three Log lines. The graph is rebuilt deterministically after every writing session (why deterministically is a story part two tells), and its use is governed by a rule that has its own automated check: the graph is a primer, never a filter. It orients which files to read; it is never permission to skip reading them. Asking 'what else in the book depends on HBM supply' returns an answer in seconds, with the file list to verify it against.

## Plain text is a strategic position

The whole system is markdown in a git repository: 115 commits since 17 April 2026, which also dates the system at four months old. Plain text keeps the book portable across models. The 27 procedures are auto-ported to a second vendor's agent CLI (OpenAI Codex) from the same source, so the wiki does not depend on one assistant surviving, and the publishable book compiles into three export tiers (a 54,000-word index, a 475,000-word core, a 1.2-million-word full dump) sized to whatever context window the next model brings. There is no database, no vendor schema and no retrieval infrastructure to migrate. The software is replaceable; the accumulated structure is the asset: fifteen-section theses, one-way evidence flow, pre-registered falsifiers, and 1,887 edges of compiled cross-reference.

Our own documentation states the compounding claim plainly: the benefit shows up around thesis five or six, when cross-thesis patterns first appear. At 95, portfolio-level questions (which names secretly rest on the same variable, where one thesis's bull premise is another thesis's bear premise) are answerable in minutes, because the reconciliation was done at write time. A book this size maintained by a probabilistic writer is also a standing liability, and an unguarded one would corrupt itself within a week. Part two covers the machinery that prevents that: the named procedures, the locks, the snapshots, and the health checks that let a language model be trusted near four months of accumulated work.
