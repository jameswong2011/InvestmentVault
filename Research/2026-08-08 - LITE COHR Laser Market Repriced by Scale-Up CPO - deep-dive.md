---
publish: false
date: 2026-08-08
updated: 2026-08-14
tags: [research, Semiconductors, LITE, COHR, Optics]
sector: Custom Silicon & Networking Semiconductors
ticker: LITE
propagated_to: [LITE]
source: 'https://damnang2.substack.com/p/the-laser-market-repriced-by-scale'
source_type: deep-dive
---

# The Laser Market Repriced by Scale-Up CPO

## Thesis Delta

Consensus prices CPO as a pluggable/laser destroyer (NVIDIA's 4×-fewer-lasers slide; optics revenue per 800G port −39% on a CPO bill of materials) → Damnang's model implies the 2030 optics market stays $70–74B on any scale-out CPO mix and jumps to $113.8B once scale-up optics attaches (to $155.5B at 30% adoption), with CW-DFB laser dollars per port rising $8→$30 (to $60 on 8λ) rather than collapsing. Hypothesis to test: [[Theses/LITE - Lumentum]] §Outstanding Questions CPO-role/volume-vs-margin and [[Theses/NVDA - Nvidia]] Risk #10 are the live variables; [G-13] the mispriced operating lever is 2028 scale-up attachment, not scale-out CPO share; Semis #8/#18 and VLM high-power CW/ELS are the layers being repriced.

## Summary

Damnang's argument is that the market is running three stacked errors — treating scale-out and scale-up as one CPO story, reading NVIDIA's laser-count slide as a laser-TAM cut, and treating NPO as a brief bridge that dies when CPO yields. The piece is an author-built TAM model (not a primary-source data dump) whose claim scope is 2026–2030 optical-port and laser-die dollars under explicit mix and adoption assumptions. Pluggable stays the workhorse because a failed module is field-swappable and multi-sourced; its defect is electrical reach from switch ASIC to faceplate. A typical 800G module burns 15.5 W, of which 6–7 W is the DSP that restores a degraded waveform; adding the switch-side drive for the long board trace takes a port to ~30 W. CPO puts the optical engine in the same package as the switch chip, shortens the electrical path to microns, drops the DSP, cuts port power from 30 W to 9 W (>70%), and frees the faceplate so chassis port count is no longer cage-limited. The cost is assembly yield and a larger replace-on-fail unit. NPO is the socketed compromise: ASIC and optical engine sit on a common high-performance substrate, can be tested separately, and can be reworked at engine level. The electrical path is longer than CPO and far shorter than front-panel pluggable, so most of the power win is kept.

NPO is commonly sold as an interim step. Damnang treats it as a parallel architecture through 2030. The socket itself had to be invented — a 200G-per-lane, minimum-loss, multi-vendor connector did not exist — and Open CPX MSA (2026) is the spec effort, with Ciena, Coherent, [[Theses/MRVL - Marvell Technology]], Molex, Samtec, and TeraHop named. Three optical MSAs landing on 12 March 2026 is framed as the industry agreeing the AI physical layer must change now. The binding physics is lane rate: at 400G/lane the same trace strips more signal and connector reflections rise, so a single socket can fail the link. If OIF/Open CPX solve that, NPO carries a generation; if not, CPO without a socket wins. Once manufacturing, reliability, and serviceability are solved, raw performance favors CPO. In the current generation the NPO concession is small, so systems that must push power and bandwidth density go CPO and systems that need part separation, test yield, supply-chain flexibility, and serviceability keep NPO. The later TAM run uses that view: both methods still in the 2030 mix.

The first misconception is that CPO shrinks the optics market and ejects module vendors. On an 800G CPO-switch BOM, the optics vendor's recognized revenue falls from $520 (CW-DFB pluggable) to $317 (−39%). The market-level picture does not follow. Even a CPO switch still terminates the accelerator-side communication card on pluggables, so the two methods coexist by construction. Port volume in the model grows 36% a year from 44 million (2026) to 150.4 million (2030). The module SKU disappears; optical engines, fiber attach, external laser modules, and shuffle boxes take its place. Revenue changes form; it does not vanish.

The second misconception is that CPO cuts laser revenue. NVIDIA's "lasers fall to a quarter" is an EML-pluggable vs CPO comparison. An EML puts emitter and modulator on one InP die, so 800G as 200G × 4 needs four dies. Current CPO uses CW-DFB on silicon photonics: InP only emits, silicon modulates, and one high-power laser is split across lanes. On that basis pluggable is two CW-DFB dies per port and CPO is one — a halving, not a quartering. Die count is the wrong unit. CPO parks the source outside the package and needs much higher power, so dollars per die go from $4 to $30 and dollars per port from $8 to $30. Scale-up's eight-wavelength spec needs two dies again and can print $60 per port. NVIDIA's slide is not false; it is the wrong denominator for a CW-DFB P&L.

The third misconception is that calling the scale-out CPO year is the optics investment. Inside scale-out, 2030 market size stays $70–74B on any CPO share. A delayed scale-out transition is not even a vendor loss: bandwidth demand is unchanged, volume stays in pluggable longer, and pluggable is the highest optics-vendor revenue per port — a longer sold-out cycle on the current line. A delayed scale-up transition is a different object. Scale-out-only 2030 is $70–74B; with scale-up open it is $113.8B. That is the timing call.

Scale-up is the fabric that binds accelerators inside one tightly coupled compute domain into one resource. Bandwidth required per accelerator is at least 9× scale-out, and port count scales with it. The "explosive CPO TAM" in this piece is that segment. The model starts the scale-up optical transition in 2028 and puts 2030 adoption at 15–30%, with a 2030 architecture mix of 25% pluggable / 35% NPO / 40% CPO. Scale-out alone compounds ~30% a year over four years. Adding scale-up takes the path to 46%; 30% adoption prints $155.5B and 57%. Laser die moves more than the total: 24% a year on scale-out (below the 30% market) versus as high as 61% once scale-up opens (above the market). That is the stated reason InP and laser names get repriced.

On names the source is explicit and ranked. [[Theses/LITE - Lumentum]] leads the high-power band: OFC 2026 ELS with an 800 mW source and its largest ELS order to date. Coherent (no vault thesis) is scored slightly ahead of Lumentum for vertical integration — 6.4T socketed CPO with its own ELS and own high-power source, plus a move to a 6-inch line. [[Theses/AAOI - Applied Optoelectronics]] is the US-manufacturing sleeve: 400 mW class product, laser fab expanding 3× by Q3 2027, small enough that one hyperscaler adoption moves the P&L. [[Theses/SIVE - Sivers Semiconductors]] enters ELS through a consortium; the base is small enough that a single adoption is material, and the author treats it as a high-beta trading name at the right price. AXT is not a laser company; it makes the InP substrate. It is in the screen because modeled InP die-area demand tracks laser revenue and because, unlike engine vendors, it is not tied to one CPO implementation — the same InP-path logic the vault already runs on [[Theses/IQE - IQE]] at the epi layer.

The sizing rules are three: Lumentum and Coherent as the stable pair for anyone with CPO/optics conviction, Coherent slightly preferred on integration; AAOI only on confirmed, continuing hyperscaler orders and AXT only on conviction that an InP shortage persists despite Chinese regulation; Sivers only as a high-beta sleeve when the price is cheap. The bear the author grants is that new capacity could clear the top power band before volume arrives and erase the premium. Field color in the piece says that timing is hard to pull forward: 300–400 mW is not a process where yield follows new lines, and Lumentum's new fab is not meaningful until 2028 — the same year scale-up volume is assumed to arrive, so supply expansion and demand growth overlap. Until 2028 the three live checks are accelerator-vendor scale-up optical-interface announcements and dates, scale-up engine and laser-module orders in optics-vendor results, and high-power lasers as a share of revenue.

## Framework / Mental Model

Damnang's reusable object is a two-axis optics TAM, not a sell-side CPO-penetration S-curve.

**Axis 1 — architecture mix (parallel, not sequential).** Pluggable / NPO / CPO are assigned different optimal points by system character (serviceability and multi-sourcing vs power and bandwidth density). The 2030 working mix is 25% / 35% / 40%. NPO is not modeled as a 12–18 month bridge; it remains in the mix through 2030 unless 400G/lane socket physics fails, in which case CPO without a socket takes the next generation.

**Axis 2 — domain (scale-out vs scale-up).** Scale-out CPO share is almost a rounding error on 2030 dollars ($70–74B band). Scale-up attachment is the discontinuous variable ($113.8B base; $155.5B at 30% 2030 adoption). Laser-die CAGR is the more levered output (24% scale-out vs up to 61% with scale-up) because CPO CW-DFB raises dollars per port even as die count per port falls.

**Three-misconception screen** (the piece's named typology): (1) CPO shrinks pluggable TAM; (2) CPO cuts laser revenue; (3) scale-out CPO timing is the investable call. Each is inverted with a specific counter-metric (port volume, CW-DFB $/port, scale-up TAM gap).

**Positioning rules:** stable (LITE/COHR), conditional (AAOI on order continuity; AXT/IQE-class InP on shortage persistence), high-beta (SIVE at price). Kill-switch inside the model: high-power (300–800 mW) capacity clears the premium before 2028 scale-up volume.

## Evidence

All figures below are from Damnang's author model or in-piece BOM/physics statements, not third-party market research. Treat as [est.: Damnang model] unless tagged otherwise.

| Item | Figure | Tag |
|---|---|---|
| 800G module power | 15.5 W; DSP 6–7 W | [1×: Damnang The Optical Edge] |
| Port power, pluggable vs CPO | ~30 W → 9 W (>70% cut) | [1×: Damnang] |
| Optics vendor $/port, 800G CW-DFB pluggable → CPO | $520 → $317 (−39%) | [est.: Damnang 800G CPO-switch BOM] |
| Optical port volume 2026 → 2030 | 44.0M → 150.4M | [est.: Damnang] |
| Port-volume CAGR | ~36% | [est.: Damnang] |
| EML dies / 800G port (200G × 4) | 4 | [1×: Damnang] |
| CW-DFB dies / port, pluggable vs CPO | 2 → 1 | [1×: Damnang] |
| NVIDIA stated laser reduction | to 1/4 vs "legacy" (EML basis) | [1×: Damnang citing NVIDIA] |
| CW-DFB $/die, pluggable vs CPO high-power | $4 → $30 | [est.: Damnang] |
| CW-DFB $/port, pluggable vs CPO | $8 → $30 | [est.: Damnang] |
| CW-DFB $/port, scale-up 8λ (2 dies) | $60 | [est.: Damnang] |
| 2030 scale-out optics market (any CPO share) | $70–74B | [est.: Damnang] |
| 2030 with scale-up (15–30% adoption from 2028) | $113.8B | [est.: Damnang] |
| 2030 at 30% scale-up adoption | $155.5B | [est.: Damnang] |
| 4-year CAGR, scale-out only | ~30% | [est.: Damnang] |
| CAGR with scale-up / at 30% adoption | 46% / 57% | [est.: Damnang] |
| Laser-die CAGR, scale-out / with scale-up | 24% / up to 61% | [est.: Damnang] |
| Scale-up vs scale-out bandwidth per accelerator | ≥9× | [1×: Damnang] |
| 2030 architecture mix (author assumption) | 25% pluggable / 35% NPO / 40% CPO | [est.: Damnang] |
| Scale-up optical transition start | 2028 | [est.: Damnang] |
| Open CPX MSA participants | Ciena, Coherent, Marvell, Molex, Samtec, TeraHop | [1×: Damnang] |
| Triple optical-MSA date | 12 Mar 2026 | [1×: Damnang] |
| Lumentum high-power demo | 800 mW ELS, OFC 2026; largest ELS order to date | [1×: Damnang] |
| Coherent CPO demo | 6.4T socketed CPO + own ELS + own high-power source; 6-inch line | [1×: Damnang] |
| AAOI laser product / fab | 400 mW class; own laser fab 3× by Q3 2027 | [1×: Damnang] |
| High-power yield band that does not follow new lines | 300–400 mW | [1×: Damnang field color] |
| Lumentum new-fab meaningful output | not before 2028 | [1×: Damnang] |

| Misconception | Per-port or slide read | Market-level inversion |
|---|---|---|
| CPO shrinks optics TAM | −39% vendor $/port | Ports 44M→150.4M; pluggable remains on accelerator NIC; engine/ELS/shuffle replace the module SKU |
| CPO cuts laser revenue | NVIDIA 4× fewer lasers vs EML | CW-DFB dies 2→1; $/port $8→$30 ($60 @ 8λ) |
| Scale-out CPO year is the trade | Earlier CPO = more optics $ | 2030 scale-out $70–74B any mix; delay extends highest-$/port pluggable; scale-up is the $113.8B gap |

## Contradiction Check

[[Theses/LITE - Lumentum]] §Outstanding Questions ("How does Lumentum's role change under CPO, and does volume offset margin compression?") — source answers yes on dollars, not on die count: CW-DFB $/port $8→$30 and laser-die CAGR up to 61% if scale-up opens in 2028. Supports §Summary "arms dealer" / SiPh-paradox (every CPO engine still buys an external InP source) and §Business Model CW/UHP 800 mW ELS named into NVIDIA platforms. Challenges §Bear Case "CPO margin compression — CW DFB relatively standardized/commoditized": the source's $4→$30/die step is the opposite dollar path, but only inside the high-power band Lumentum is demonstrating (800 mW) and only if 300–400 mW yield stays inelastic through 2028 ([G-13] expectations; Semis #1/#2/#17). Tension, not confirmation: Damnang ranks Coherent slightly above Lumentum on vertical integration (6.4T socketed CPO + own ELS + 6-inch), which leans against the thesis's EML-monopoly-as-the-edge and toward the already-logged Semis #8 read that CPO migrates value from EML to contestable CW/ELS. LITE has no Conviction Triggers section; the source's three 2028 watches (accelerator scale-up IF announcements, engine/laser-module orders, high-power mix) are the closest operational stand-ins. [G-10] 61% laser-die CAGR is an inside-view outlier versus sustained-growth base rates — the thesis must beat that with 2028 scale-up attachment, not with scale-out CPO mix.

[[Theses/AAOI - Applied Optoelectronics]] §Conviction Triggers → LOW ("CPO captures ≥20% of NVIDIA + Broadcom hyperscale switch shipments in H2 2026") and → CLOSE ("Broadcom OR NVIDIA discloses pluggable transceiver demand stepping down in 2027–2028") — source says a faster scale-out CPO mix barely moves 2030 dollars ($70–74B band) and that pluggable remains structurally on the accelerator communication card, so those triggers fire on the wrong object if the model is right. Softens §Outstanding Questions "Does the CPO transition arrive before AAOI's 1.6T capex pays back?" for scale-out; does not soften it for scale-up, where AAOI is a 400 mW / US-fab sleeve, not an 800 mW ELS name. Supports the thesis's own conditional sizing: invest only if hyperscaler orders are confirmed and continue. VLM §2 layer-renter still applies — middle-assembly is not the layer being repriced.

[[Theses/NVDA - Nvidia]] Risk #10 (NVLink copper reach / SerDes plateau; scale-up CPO as the later TAM) — supported. The source's ≥9× scale-up vs scale-out bandwidth-per-accelerator and the $70–74B vs $113.8B gap are the same domain split as SemiAnalysis, with a laser-P&L overlay NVIDIA's "4× fewer lasers" slide does not contain. [G-14] Jevons: 39% $/port drop is more than offset by 44M→150.4M ports. NVIDIA here is the architecture setter and the source of the misread, not the equity being repriced.

[[Theses/IQE - IQE]] §Bull Case (CPO/SiPh inflection as structural InP demand) and Outstanding Question 4 (how much InP epi the buildout actually captures) — supported at the die-area layer. The source puts AXT on the screen because modeled InP die area tracks laser revenue and is implementation-agnostic; IQE is the vault's listed epi analogue of that same path. Does not speak to the dead M&A special-situation leg. Semis #1: InP area is the bottleneck proxy, not a named epi-vendor qualification gate.

[[Theses/SIVE - Sivers Semiconductors]] §Summary overflow-ELS / high-beta option and §Conviction Triggers → HIGH (named hyperscaler CPO ELS qualification + Photonics run-rate) — source agrees on shape (consortium ELS, small base, size only at an attractive price, treat as high-beta) and does not deliver the HIGH-trigger evidence (no named hyperscaler PO). Compresses the overflow window: Lumentum's new fab and scale-up volume are both dated 2028, the same year SIVE's 4-inch cost gap versus LITE Greensboro / Coherent 6-inch becomes binding. VLM: Sivers is a layer-renter on overflow ELS, not the layer owner.

Falsifiers the source itself names: scale-up optical transition slips past 2028; 300–800 mW capacity clears the premium before that volume; 400G/lane socket physics is solved and NPO takes share the model gave to CPO (mix error, not TAM death, inside scale-out). Cross-model agreement (G-13 + Semis #1 + VLM infrastructure-layer) is the cue to hunt the bear, not to raise conviction: the single disconfirming datapoint is a 2027 print where high-power laser mix and ELS/module orders are still absent while 6-inch CW capacity is already yielding.

## Source Excerpts

> "Revenue per port falls 39 percent, but port volume grows from 44 million in 2026 to 150.4 million in 2030, so the total market grows."

> "NVIDIA's four-times-fewer-lasers figure is measured against EML. Recalculated on the CW-DFB basis used today, the count halves but higher power is required, so the laser amount per port rises from $8 to $30."

> "Even within CW-DFB, CPO has the light source outside the package and must use a far higher-power laser, in which case the amount per die rises from $4 to $30 and the amount per port from $8 to $30. And under the eight-wavelength specification used in scale-up, two dies are required again, so it can rise to $60."

> "Whatever CPO share is assumed within scale-out, the 2030 market stays between $70 billion and $74 billion. The real variable is the scale-up optical transition, which takes it to $113.8 billion."

> "A delayed scale-out transition is not a loss either. If it is postponed because of integration difficulty, bandwidth demand is unchanged, so volume stays in pluggable longer, and pluggable is the structure with the highest optics vendor revenue per port."

> "On a scale-out basis, laser die grows 24 percent a year, below the 30 percent for the overall market, whereas with scale-up open it can reach as high as 61 percent and exceed the market's growth rate."

> "Against a growth rate of 30 percent a year calculated over four years on scale-out alone, adding scale-up brings it to 46 percent, and setting adoption at 30 percent brings it to $155.5 billion and 57 percent."

> "I view it as closer to a parallel structure than an interim step... the model calculated later is also set on this view, with both methods in use through 2030."

> "The 300 to 400mW band is not a process where yield follows immediately from adding lines, and Lumentum's new fab will not operate meaningfully until 2028. By around that time scale-up volume begins arriving in earnest, so supply expansion and demand growth overlap in the same year."
