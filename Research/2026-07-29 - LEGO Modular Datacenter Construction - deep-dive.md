---
publish: false
date: 2026-07-29
updated: 2026-08-14
tags: [research, Semiconductors]
sector: Semiconductors
source: 'https://newsletter.semianalysis.com/p/the-wild-wild-west-of-lego-datacenters'
source_type: deep-dive
---

# The Wild Wild West Of LEGO Datacenters

## Thesis Delta
Consensus prices “modular datacenter” as marketing around an unchanged stick-build labor bottleneck, and prices [[Theses/VRT - Vertiv Holdings]] as a capacity-constrained industrial whose discrete ~$3.5M/MW power-plus-cooling content is the TAM → SemiAnalysis’s Modular Tracker (61GW+ / 1,000+ sites / 80+ vendors) rebuilds vendor speed and cost claims to a ~36% construction-window cut (~7–9 months) and ~8% cheaper Capex/MW, while OEM-led full-stack modules (OneCore) can lift Vertiv content toward ~$7M/MW and move the binding constraint from licensed electricians to factory slots, heavy-haul logistics, and on-site L5 commissioning — with go-live still the latest of building / power / GPUs. [G-4] Perez-frenzy factory overbuild, [G-13] street underwriting backlog not content-per-MW, semis #1 bottleneck-migration, VLM OEM-led layer-ownership vs hyperscaler insourcing — all held as hypotheses, not verdicts.

## Summary
Datacenter construction no longer resembles the industry’s historical stick-build sequence. Finished wall panels, pre-wired mechanical and electrical rooms, and occasionally entire halls arrive by truck; hyperscalers, colos, and now AI labs treat some form of modularization or prefabrication as the default playbook for speed. SemiAnalysis’s Modular Tracker, inside the Industrials Model, counts over 61GW of modular capacity and 1,000+ sites using some modular or prefab strategy, and estimates modular penetration at 30%+ of live capacity by end-2028. The motive is a labor constraint capitalist incentives cannot rapidly close: electricians are 30–40% of construction man-hours; Crusoe paid +30% wages to staff Abilene’s peak 9,000-worker site; a new Labor Model (state-by-state hours vs reachable supply, ex-modular, labor-per-GW held flat) shows an electrician shortage emerging in 2027, most acute in Texas and Ohio. Prior SemiAnalysis pieces argued most 2026 US capacity-cancellation talk is misunderstood and solvable ([[Research/2026-08-13 - Datacenter Capacity Cancellation Myth - deep-dive]]); trade labor is the named exception.

The analytical spine is a taxonomy, not a vendor pitch. Prefabrication is any work done offsite; modular is the narrower class of self-contained rooms, boxes, or blocks that ship complete and bolt together. A datacenter is three stacks — Site (cannot be modularized), Shell, Systems — and systems themselves climb a ladder from component → skid → enclosed module → ISO container → prefab facility block. Shell modularization itself has three phases: precast/tilt-up of a conventional building, simplified single-story steel/PEMB halls, then purpose-built rapid-deployment enclosures (Meta fabric “tents,” AWS narrower SAMDC halls). Integration ownership splits three ways: operator-led (AWS Project Houdini, Aligned owner-furnished gear), EPC/SI-led (Comfort Systems TAS/EAS, Quanta/Cupertino Electric, Sterling IMS), and OEM-led (Vertiv OneCore, Schneider EcoStruxure family). The same public names (Vertiv, Schneider, Eaton) appear in every column because they sell skids, CDUs, white-space pods, and whole blocks at once; depth sits in crowded power-room and cooling-skid markets.

SemiAnalysis rebuilt vendor claims against a 50MW liquid-cooled US AI-hall baseline in the Industrials Model. Full modular compresses the construction window ~36% (18–24 months stick-build → 12–18; permitting is a separate 12–13 months that cannot overlap), and is ~8% cheaper on all-in Capex/MW ($13.5M vs $14.6M, ~$1.1M/MW). Hardware unit cost barely moves; savings are factory labor throughput plus shorter field general conditions, offset by a double-margin penalty and chassis/transport premium. Speed is the economic prize: owner-operators value an earlier month at ~$500k/MW (GPU depreciation on a $30M/MW Nvidia cluster over five years), implying ~$4M/MW or ~$200M undiscounted across a 50MW hall for an eight-month lead — but only if the building, not interconnect or GPU delivery, is the date that binds. Factory first-pass quality is marketed at 95%+ vs 60–70% field; operators and MEP contractors counter that modular reliability failures erase the schedule gain and put hardware at risk. Site commissioning (3–8 months; L2–L5 cannot leave the site because utility, generators, and BESS only meet there) is the cycle’s largest residual gap.

Operator strategies do not converge. AWS re-cuts a standard hall map into ~45-foot Houdini white-space skids (15 weeks → 2–3 weeks, >50,000 on-site electrician hours removed per module). Meta encloses Prometheus with aluminum-framed fabric halls (~125,000 sf; eight standing by April 2026 after a July 2025 announcement) without accelerating utility, power, cooling, or commissioning. Crusoe dries-in Abilene shells in <8 weeks with 672 factory panels per building and sells 1MW Spark whole-facility boxes; Hut 8 buys Vertiv OneCore end-to-end for a 704MW IT lease at Beacon Point on Nvidia DSX. [[Theses/NBIS - Nebius Group]] pairs precast shell with [[Theses/BE - Bloom Energy]] behind-the-meter fuel cells in New Jersey (phased to 300MW) and reuses a Bridgestone plant at Béthune. Compass industrializes 70–85% of each building offsite; QTS warehouses ~7 million sf of long-lead gear in Kansas and scales Freedom pods in 1.5MW increments; Aligned keeps a common chilled-water loop while halls swing from Delta³ air (~50 kW/rack) to DeltaFlow liquid (>350 kW/rack). On the supplier side, Vertiv is scored the strongest public modular position (OneCore as the March 2026 Vera Rubin DSX building block; BMarko expected to lift regional modular manufacturing ~7×; some modular SKUs sold out >12 months). Schneider is the second-broadest portfolio but captures via configurable blocks plus operator partnerships (Compass $3B, 105,000-sf plant beside Red Oak). Comfort Systems, Quanta, and Sterling win as factory-plus-field integrators that let hyperscalers keep their own BOM. Claim scope is US/AI-hall construction economics plus a public-and-private vendor map; it does not claim modular solves grid interconnect ([[Research/2026-08-13 - BE VRT - US Grid Constraints 40GW BTM Datacenter 2028 - deep-dive]]), and the inbox clip ends in the private-integrator roster with no closing synthesis.

## Framework / Mental Model
**SemiAnalysis modular universe (named typology).** Classify every offering before accepting MW or timeline marketing. Two words that get mixed: *prefabrication* = where the work happened (any offsite manufacture delivered ready to install); *modular* = self-contained units that ship complete and bolt together. Every modular unit is prefabricated; prefabrication is not always modular.

**Datacenter anatomy (three stacks).** Site (grading, wiring, foundations — cannot be modularized). Shell (structure, skin, roof). Systems (mechanical, electrical, white space). Prefab strategies apply only to shell and systems.

**Shell phases (design simplification, not just offsite concrete).** Phase One: precast or tilt-up of a still-conventional, often multistory building (Northern Virginia labor already forced this; CloudHQ LC-2 Ashburn still ~18–20 months). Phase Two: simplify the building — regular bays, single-story steel, PEMB (primary frame / secondary purlins / metal skin) or heavier structural steel + insulated metal panels; land-for-speed trade (acceptable where AI land is cheap). Phase Three: purpose-built rapid-deployment enclosures — narrower halls, less building per MW, fabric-clad tents; durability and layout flexibility are the explicit give-up.

**Systems ladder (factory integration 1→5).** Component (single factory box) → Skid (open-frame pre-arranged package) → Module (skid plus walls and roof) → Container (ISO-dimension module, permit-free haul) → Prefab datacenter block (stitched modules as an end-to-end hall). Levels 1–4 are subsystem modularization (still must connect into a facility). Level 4–5 approach whole-facility modularization (containerized edge boxes vs all-in-one blocks such as Vertiv MegaMod that break into heavy-haul sections).

**Integration ownership (who modularizes).** Operator-led: owner specifies and owner-furnishes gear, integrator only assembles (confined to hyperscalers that can carry transformer/switchgear allocation risk). EPC/SI-led: vendor-agnostic factory conversion of third-party lineups (Comfort TAS/EAS, Quanta CEI, Sterling IMS, PCX, Nautilus, DXN, Infra Partners, BladeRoom). OEM-led: vendor sells its own stack as a finished product (Vertiv OneCore; Schneider EcoStruxure family). OEM-led raises content/MW and lead times; sold-out OEM slots push smaller buyers to SIs.

**Modularization cycle (five stages).** (1) Facility-level design and simulation first — SLD, short-circuit, protection-coordination, arc-flash in ETAP/PSSE cannot be closed on an isolated skid; 415/480VAC is templated, 800VDC is not ([[Macro & Technology/800VDC Adoption]]). (2) Documentation packages: IFF (factory), IFC (field), permitting/commissioning — generated from one model when Stage 1 is automated. (3) Assembly + FAT; 1-10-100 defect-cost rule. (4) Transport, crane, set — federal no-permit envelope 102 inches / 80,000 lb; superload reviews 7–21 days/state; insurance can force one-to-two high-value racks per trailer. (5) Site commissioning, six-level ladder (L1 factory red-tag; L2–L5 on site; L5 IST white-tag is the only step that must wait for the full set). Two recovery levers: parallelize L2–L4 as modules land; reuse plant BESS/power as the load bank.

**Vendor-claim rebuild (three marketed pillars).** Speed, quality/safety, TCO. Scope discipline: Vertiv SmartRun 85% is overhead busway/containment; MegaMod 50% is module deployment vs on-site build; Schneider 60%/13% is power-and-cooling modules — none is end-to-end groundbreaking-to-IT-ready.

## Evidence

### Tracker, labor, and the 50MW rebuild
| Metric | Figure | Tag |
|---|---|---|
| Modular capacity tracked | >61GW | [1×: SemiAnalysis Industrials Model] |
| Sites using some modular/prefab | 1,000+ | [1×: SemiAnalysis] |
| Vendor universe mapped | >80 players | [1×: SemiAnalysis] |
| Modular share of live capacity, YE2028 | 30%+ | [est.: SemiAnalysis] |
| Electrician share of DC construction man-hours | 30–40% | [1×: SemiAnalysis Labor Model] |
| Ex-modular electrician shortage | Emerges 2027; worst TX, OH | [est.: SemiAnalysis Labor Model] |
| Crusoe Abilene wage / peak headcount | +30% wages; >9,000 workers | [1×: SemiAnalysis] |
| Construction-window compression, full modular vs stick | ~36% (7–9 months); 18–24 mo → 12–18 mo | [1×: SemiAnalysis bottom-up, 50MW US liquid hall] |
| MEP-skids-only schedule | ~17 months | [1×: SemiAnalysis] |
| All-in-one block / containerized window | ~12 months (some vendor claims <12) | [1×: SemiAnalysis] |
| Permitting (cannot overlap construction) | +12–13 months; all-in ~30–35+ stick vs ~24–30 modular | [1×: SemiAnalysis] |
| Groundworks / shell / MEP fit-out / commissioning midpoints | ~5 / ~3.5 / 7–11 / ~4.5 months (commissioning range 3–8) | [1×: SemiAnalysis] |
| Field man-hours per MW (AI hall) | ~12,000; 50MW = 600,000 hours, ~300 craft at peak | [1×: SemiAnalysis] |
| On-site hours after relocating MEP to factory | ~4,500/MW (−63%); licensed-electrician hours ~−85% | [1×: SemiAnalysis] |
| Power-block-only move (~26% of build content) | Hall IT-ready ~22% faster (~13 vs ~16.7 mo); ~5% cheaper/MW; MEP fit-out ~5.5 → ~2.5 mo | [est.: SemiAnalysis] |
| Electrical fit-out range, 50MW power hall | 5.5–16.7 months | [1×: SemiAnalysis] |
| All-in Capex/MW, full modular vs stick | ~$13.5M vs ~$14.6M; ~$1.1M/MW; ~8% | [1×: SemiAnalysis] |
| Capex save split | ~$0.6M/MW construction services + ~$0.5M/MW installation | [est.: SemiAnalysis] |
| Field vs factory wage | BLS $34/hr field vs $33/hr factory; effective field electrician ~$63/hr with OT/site premium | [web: BLS via SemiAnalysis] |
| Factory first-pass quality vs field | 95%+ marketed vs 60–70% field | [1×: vendor/Flex framing via SemiAnalysis] |
| Operator/MEP counter on quality | Modular reliability issues erase schedule gain and put hardware at risk | [1×: SemiAnalysis channel checks] |

### Speed unit economics (only if the building is the binding date)
| Item | Figure | Tag |
|---|---|---|
| CSP revenue / IT MW | ~$12–15M/year ≈ $1–1.25M/MW/month | [est.: SemiAnalysis] |
| Disclosed high-end pays (SpaceX–Anthropic; Meta post) | ~$50M per IT MW; Anthropic/OpenAI API >$50M/MW | [1×: SemiAnalysis; [[Theses/SPCX - SpaceX]]] |
| GPU depreciation / MW / month | $30M/MW Nvidia cluster ÷ 5 years ≈ $500k/MW/month | [est.: SemiAnalysis] |
| Wholesale colo value of an earlier month | ~$190k/MW/month ≈ $190/kW-mo | [est.: SemiAnalysis] |
| 8-month lead, owner-operator, 50MW hall | ~$200M undiscounted ≈ $4M/MW | [est.: SemiAnalysis] |
| Go-live identity | Latest of building-ready, power-available, GPUs-delivered | [1×: SemiAnalysis] |

Vendor advertised vs rebuilt scope:

| Claim | Scope as rebuilt | Tag |
|---|---|---|
| Vertiv MegaMod “up to 50% faster” | Module deployment vs on-site build, not groundbreaking-to-IT-ready | [1×: Vertiv via SemiAnalysis] |
| Vertiv SmartRun “up to 85%” | Overhead busway and containment | [1×: Vertiv via SemiAnalysis] |
| Schneider “60% faster / 13% lower first cost” | Power and cooling modules; WP163 puts module hardware ~40% above traditional, nets −13% after design/install labor | [1×: Schneider WP163 via SemiAnalysis] |
| Flex “30%+” on whole projects | Closest published floor to SA’s ~36% end-to-end | [1×: Flex via SemiAnalysis] |
| Eaton/Flexnode “~35%” schedule cut | Flexnode modular halls 3.5–35MW | [1×: Eaton via SemiAnalysis] |

### Shell, systems, and platform reference designs
| Example | What actually ships | Outcome / constraint | Tag |
|---|---|---|---|
| CloudHQ LC-2 Ashburn | Load-bearing precast, two-story, roof mechanicals | Still ~18–20 months | [1×: SemiAnalysis] |
| QTS Cedar Rapids | ~28,000 tons structural steel; 420MW phase; ~2.8M sf | Groundbreaking → topping-out ~5 months; building ~11 months | [1×: SemiAnalysis / QTS] |
| Crusoe Stargate Abilene shell | ~672 factory insulated metal panels/building | Fab <40 days; install 15–20/day; dried-in shell <8 weeks | [1×: SemiAnalysis] |
| Meta Prometheus tents | Aluminum frame + tensioned fabric; ~125,000 sf each | Eight standing by Apr 2026 after Jul 2025 announce; first five permanent buildings took 2–3 years; tents do not pull utility/power/cooling/commissioning | [1×: SemiAnalysis satellite] |
| AWS SAMDC / narrower halls | Purpose-built shell around installed systems | Less building per MW, shorter spans, fewer field interfaces | [1×: SemiAnalysis] |
| Flex Anord Mardix | Power skid or enclosed power-module pod + busway/CRAH/fire | Grey-space power train as a factory room | [1×: SemiAnalysis] |
| DG Matrix | Software-defined multi-port power routing (grid / gen / storage / DC load) | Replaces portions of transformer+switchgear+UPS+battery chain | [1×: SemiAnalysis] |
| Airedale by Modine CDU | 2MW-class skid: loop, buffer tanks, leak detection | Site work = two loop connections + power feed | [1×: SemiAnalysis] |
| QTS yard piping | Prefabricated secondary-loop / outdoor piping | Civil/piping/controls pulled offsite; more valuable as liquid-cooled pipe counts rise | [1×: SemiAnalysis] |
| Karman Industries HPU | CO2 heat-processing NEMA skid; SiC + PM motors + aerospace turbomachinery | 4–5× conventional power density; yard footprint −60–80% | [1×: SemiAnalysis] |
| Schneider EcoStruxure Pod | Up to 40 racks; overhead busway, containment, TCS loop, cabling | 30+ Nvidia reference designs | [1×: SemiAnalysis] |
| Vertiv MegaMod 1MW ref | IT in center; perimeter power/cooling; ~26.5×24×4 m (Plus ~31 m wide) | Ships as heavy-haul sections, commissioned as one | [1×: SemiAnalysis] |
| Nvidia DSX | Omniverse twin (GTC Washington Oct 2025) → Vera Rubin DSX (Mar 2026) → full DSX platform; Max-Q (tokens/watt) + Flex (grid services / hybrid onsite gen) | Civil/structural/architectural in the validated set; CoreWeave on DSX Air twins; Vertiv OneCore as 12.5MW pods | [1×: SemiAnalysis; [[Theses/NVDA - Nvidia]]; [[Theses/CRWV - CoreWeave]]] |
| EdgeConneX on common design | 30–60% permit set before site-specific localization | Off-site work starts earlier | [1×: EdgeConneX via SemiAnalysis] |
| Aran Industries design software | Plugs into ETAP, PSCAD, PSSE, Revit | Multi-month (>2 months) multi-engineer electrical design → hours of compute + one reviewing engineer | [1×: SemiAnalysis] |
| 800VDC facility design | “A handful of reference designs, none well baked” | Architecture still design-by-design vs templated 415/480VAC | [1×: SemiAnalysis] |
| Long-lead electrical | Switchgear/transformers 12–18 months; customization reopens engineering ~8 weeks | Inventory and allocation sit with whoever owns the buy | [1×: SemiAnalysis] |

### Logistics, crane, commissioning
| Constraint | Figure | Tag |
|---|---|---|
| Federal no-permit envelope | 102 in wide, 80,000 lb gross ≈ 24 tons payload on a standard deck | [web: US DOT via SemiAnalysis] |
| ISO-container products (Azure Modular DC; Schneider Easy Modular) | 40-ft ISO, 96 in wide — any state line or C-17, permit-free | [1×: SemiAnalysis] |
| Oversize permit cost | $15–100 per state; line-haul $12–14/loaded mile → 500 miles ≈ $6–7k/trailer | [1×: SemiAnalysis] |
| Superload trigger | Past ~16 ft: bridge review 7–21 days/state, stacks toward months; escorts + restricted windows | [1×: SemiAnalysis] |
| State threshold mismatch | VA superload 18 ft or 250,000 lb vs OH 14 ft / 120,000 lb | [1×: SemiAnalysis] |
| Transit validation | Aligned shipped a 3MW module Utah → Omaha → Utah with force loggers | [1×: SemiAnalysis] |
| Insurance / loss | High-value AI racks often 1–2 per trailer; UPS module tipped in West Virginia en route to Northern Virginia | [1×: SemiAnalysis channel] |
| Design-around-the-haul | AWS Houdini on low double-drop trailers; Nautilus barged 50 miles to Port of Stockton; Compass put a Schneider factory next to Red Oak; DXN ships smaller containers Perth → US | [1×: SemiAnalysis] |
| Crane physics | Manitowoc 18000: ~600 tons at 7.3 m vs ~10 tons at 104 m; $5,000–$25,000/day | [1×: SemiAnalysis] |
| Schneider 500kW power module | 50,000 lb; six lift points; load distribution unknown until built | [1×: SemiAnalysis] |
| Site commissioning duration | 3–8 months end-to-end; “single biggest gap”; energy sources only meet on site | [1×: SemiAnalysis] |
| Commissioning ladder | L1 FAT red-tag (factory) → L2 receive/set → L3 green-tag startup → L4 blue-tag functional → L5 white-tag IST | [1×: industry via SemiAnalysis] |
| Binding L3 work | Point-to-point: every PDU/panel/device wired, addressed, named, verified to BMS | [1×: SemiAnalysis] |
| 6–9 month advertised schedules | Partly achieved by compressing commissioning; risk shifts into operations | [1×: SemiAnalysis] |
| 1-10-100 rule | $1 design/assembly defect → $10 in production → $100 after ship | [1×: industry via SemiAnalysis] |

### Operator playbooks
| Operator | Modular layer | Concrete numbers | Tag |
|---|---|---|---|
| AWS | Factory-built white space (Houdini); SAMDC shell | +~3.9GW capacity through end-2025; skid ~45 ft / ~2,000 lb; 15 weeks → 2–3 weeks; >50,000 electrician hours removed per module; factories Houston, Salt Lake City, Topeka; early sites Texas, South Bend; ~25 weeks construction-start → first server room; Cupertino Electric = physical-build partner | [1×: SemiAnalysis] |
| Meta | Phase-Three shell (tents) at Prometheus / New Albany | Six RDS built in-text; eight standing by Apr 2026; ~125,000 sf each; permanent halls 2–3 years | [1×: SemiAnalysis; [[Theses/META - Meta]]] |
| Crusoe | Phase-Two shell + whole-facility Spark | Easter-Owens acquired 2022; Spark factory Brighton, CO; ~1MW/unit; Redwood Materials NV: 4 Spark + 12MW microgrid → 24 units | [1×: SemiAnalysis] |
| Hut 8 | OEM-led full stack | Vertiv OneCore at Beacon Point; 704MW IT lease; Nvidia DSX; AEP utility; Jacobs EPCM (also River Bend) | [1×: SemiAnalysis] |
| Nebius | Selected MEP + precast shell; BTM power | NJ with DataOne, expandable 300MW, Bloom fuel cells; Béthune reuses Bridgestone plant, Azur Datacenter on land/utility/plant | [1×: SemiAnalysis; [[Theses/NBIS - Nebius Group]]; [[Theses/BE - Bloom Energy]]] |
| Compass | Whole-facility kit of parts | 70–85% manufactured offsite; frame+roof 18–21 days; rebar-free fiber-reinforced precast from on-site batch plants; Schneider EcoStruxure white space; ~1.25MW Schneider power center (Galaxy VX, Li-ion, QED-2); Siemens deal up to 1,500 MV skids / 5 years; Red Oak up to 360MW; Goodyear 8 buildings / 1.8M sf | [1×: SemiAnalysis] |
| QTS | Early design lock + owner-furnished inventory | ~7M sf Kansas warehouse; Freedom pod = 1.5MW UPS/switchgear + 2.25MW generator, scales 1.5MW; Freedom LC+ air or liquid; Rapids 60MW hall blocks; labor inflation ~+20–30%/MW; two major AI companies on Rapids | [1×: QTS via SemiAnalysis] |
| Aligned | Operator-led spec, partner factories; Adaptive Modular Infrastructure | 2MW UPS container + distribution; Delta³ ≤~50 kW/rack air; DeltaFlow >350 kW/rack liquid; same chilled-water interfaces; Project Caprock TX 540MW / 6 buildings / 1.65M sf | [1×: SemiAnalysis] |

### Public-supplier content, backlog, factory
| Supplier | Modular position | Content / backlog / factory | Tag |
|---|---|---|---|
| Vertiv (VRT) | Strongest public OEM span: SmartMod → OneCore; OneCore = Vera Rubin DSX block (Mar 2026) | Discrete ~$3.5M/MW → full-stack ~$7M/MW; some modular units sold out >12 months; YE2025 backlog $15.0B, Q4 B2B 2.9×; Apr 2026 BMarko deal expected ~7× regional modular manufacturing | [1×: SemiAnalysis; [[Theses/VRT - Vertiv Holdings]]] |
| Schneider (SU) | Second-broadest; EcoStruxure configurable blocks + AVEVA, not a single turnkey box | Secure Power ~32% of Data Center & Networks; Compass $3B multi-year + 105,000-sf plant beside Red Oak; management content ~$1.2–3.3M/MW; group backlog >€25B; 18–24 months DC visibility | [1×: SemiAnalysis] |
| Comfort Systems (FIX) | EPC/SI volumetric at TAS Houston + EAS Greensboro | 3.5M+ sf shop (pre-expansion); CY26 modular capex > prior 12 years combined; modular floor → 5M sf by late summer 2027; modular 17% of H1 2026 rev ≈ $2B annualized; backlog $14.1B +73% YoY; modular ≈ one-third of sequential backlog add; Q OCF $1.14B; advance billings +$1.11B over 6 months to $3.23B; pilots with frontier labs + colos beyond Google/Meta | [1×: SemiAnalysis / FIX Q2 2026] |
| Quanta (PWR) / Cupertino Electric | Houdini electrical integrator; factory + field retained | Houdini designs targeting May 2026, first skid Sep; tech end-market <5% → ~10% of backlog (Mar), growing >100%; ~7M sf under roof incl. transformers; ~$700M factory/MEP fab commit; CEI ~$1.5B DC backlog, >50% since acquisition; management frames DC construction opp ~$13M/MW | [1×: SemiAnalysis] |
| Sterling (STRL) | Site-development incumbent + CEC; IMS; duct-bank into site package | Texas lease ~triples modular capacity; throughput ~doubled; addressable DC 3.8GW → 14GW (TX, PNW, Midwest); 2× content/MW from CEC attach at Meta Cheyenne/El Paso | [1×: SemiAnalysis] |
| IES (IESC) | Communications + C&I electrical + Infrastructure Solutions enclosures | Prefab as extension of contracting, not a separate product line | [1×: SemiAnalysis] |
| Flex (FLEX) | Anord Mardix complete power system; Crown / JetCool / EP² stack | Anord claims onsite testing −70%; Cloud and Power Infrastructure $6.6B FY26, Power +61%; separation to make economics visible | [1×: SemiAnalysis] |
| nVent (NVT) | Trachte structure + Avail EPG switchgear/bus | Trachte ~$688M; Avail EPG ~$980M; ~$1M/MW across DC portfolio | [1×: SemiAnalysis] |
| Eaton (ETN) | NordicEPOD + Fibrebond + Flexnode + Beam Rubin DSX + Boyd liquid | Addressable ~$2.9M/MW → ~$3.4M/MW with liquid cooling; NordicEPOD ~1.7–2.0MW (to 3.1MW); Flexnode halls ~3.5–35MW | [1×: SemiAnalysis] |
| Siemens (SIE) | MV switchgear; IEC + UL for Rubin DSX | Up to 1,500 modular MV skids / 5 years (SemiAnalysis believes Compass); Smart Infrastructure DC rev ~€2.9B FY25 +40%; orders €1.8B Q1 FY26 / €1.9B Q2 | [1×: SemiAnalysis] |
| ABB | HiPerGuard electrical block; VoltaGrid eHouses + sync condensers | 2.5 MVA units combine to 25MW; 34.5 kV version −20–25% electrical footprint; Applied Digital 400MW ND; first two VoltaGrid phases 62 sync condensers; electrification orders +60% Q2 2026 to $7.2B; backlog $13.7B; +~$200M European MV capacity | [1×: SemiAnalysis] |
| Modine (MOD) | Airedale skid CDUs 400kW–>2MW | Cooling package ~$0.6M/MW → ~$0.7M/MW more integrated; >$4B cooling capacity reserved 2027–29 + $165M upfront (SA suspects Google) | [1×: SemiAnalysis] |
| Foxconn (2317) | ODM racks → modular DC + TECO electromechanical + Schneider power | Unveiled Modular Data Center at GTC 2026; claims >1GW deployed modular; ~1,000 AI racks/week; Houston 242,000 sf scaling toward ~2,000 racks/week; +$569M Wisconsin | [1×: SemiAnalysis] |
| Jacobs (J) | DSX EPCM (with Bechtel); Hut 8 River Bend + Beacon Point | Traditional design ~$2–5M on a 50MW-class job; some full-program engagements “two orders of magnitude larger” | [1×: SemiAnalysis] |
| EMCOR (EME) | Internal fab (not a third-party module vendor) | ~35,000 trades; ~95% of fab supports own projects; +400–450k sf / 18 months; 3-year payback hurdle; four large hyperscalers sharing plans through 2031; performance obligations $4.5B vs $4.1B 2025 rev; AI halls ~1.2× electrical and 1.4–1.8× mechanical content vs traditional cloud | [1×: SemiAnalysis] |
| MYR Group | Electrical prefab (Sturgeon, Huen); Valley Electric + Comet | C&I margins 8.1% vs 4.7% YoY, management-linked to prefab; Valley+Comet ~$328M | [1×: SemiAnalysis] |

### Private integrators (inbox ends here)
| Firm | Position | Scale | Tag |
|---|---|---|---|
| InfraPartners | Comprehensive portfolio closest to Vertiv’s; RapidNode / RapidHub / RapidFrame on a Standard Reference Design (Mar 2026); partners DG Matrix, Nvidia, EPRI, Prologis | Nscale Glomfjord (billed first fully modular AI DC); ~1.2GW nameplate annual deployment; 150,000 sf Houston; Romania factory doubling | [1×: SemiAnalysis] |
| BladeRoom (BRG) | Factory-built mission-critical; US via Rosendin Modular Power Solutions JV, Michigan | 30+ DCs Europe/Asia/Africa in as little as 20 weeks; hyperscale designs in 30MW+ blocks | [1×: SemiAnalysis] |
| Faith Technologies / Excellerate | Pure-play on the electrical-labor bottleneck; complete modular electrical buildings, assembled and tested | Beyond Appleton + 438,000 sf Olathe; +$79M Alabama; 500,000 sf Indiana; further El Paso — roughly 3× footprint | [1×: SemiAnalysis] |
| Also named | Cadolto, Flexnode (also in Eaton’s hall stack), PCX, Nautilus, DXN | Fill OEM/SI sold-out slots | [1×: SemiAnalysis] |

DSX ecosystem names listed by SemiAnalysis: Cadence, Dassault, Eaton, Jacobs, Nscale, Phaidra, Procore, PTC, Schneider, Siemens, Switch, Trane, Vertiv. [[Theses/PCOR - Procore Technologies]] appears as a construction-software seat on the digital-twin path, not as a module OEM.

## Contradiction Check
**Supports [[Theses/VRT - Vertiv Holdings]] §Key Non-consensus Insights “Power+cooling vertical integration premium” and the MegaMod/OneCore content claim; challenges the street’s discrete-SKU TAM.** Source’s $3.5M → $7M/MW OneCore math is the same mechanism the thesis already uses for bundled 360AI/SmartMod/MegaMod (~35–40% of FY26E revenue uplift). It adds a factory-constraint qualifier the thesis’s capacity narrative under-weights: modular lead times >12 months, OEM slot allocation with capacity minimums, BMarko as a ~7× manufacturing response. Held as [G-7] ROIIC × runway on incremental content/MW, not as proof the multiple is cheap.

**Partially supports [[Theses/VRT - Vertiv Holdings]] §Key Non-consensus Insights “The real chokepoint is grid interconnect… modular/prefab… Vertiv-favorable.”** Modularization is the construction-labor workaround; it does not move interconnect. Source is explicit that accelerating the building earns nothing if power-available or GPU delivery is later. That is the same caution already logged from [[Research/2026-08-13 - BE VRT - US Grid Constraints 40GW BTM Datacenter 2028 - deep-dive]] and [[Research/2026-08-05 - AI Data Center Power Markets and Electricity Pricing - deep-dive]]: density/prefab can be bullish for content/MW and still fail to guarantee vendor return if nodal deliverability binds. Semis #1 / #18: the bottleneck *migrates* (site electricians → factory throughput + heavy-haul + L5 IST + grid), it does not disappear.

**Challenges [[Theses/VRT - Vertiv Holdings]] §Outstanding Questions “Can Vertiv’s liquid cooling IP lead survive a hyperscaler insourcing push?” and the → LOW trigger (hyperscaler proprietary liquid-cooling reference vs 360AI).** Operator-led modular (AWS Houdini with owner-furnished gear and Cupertino as assembler; Aligned’s architecture with external factories) is the insourcing path for *white space and power rooms*, not only CDUs. OEM-led OneCore wins Hut 8–class buyers who want a finished stack; hyperscalers with in-house engineering keep the BOM and buy factory hours from FIX/PWR. VLM hypothesis: OneCore is an attempt to own the integration layer; Houdini is the layer-renter inversion — Vertiv can still sell boxes into Houdini and lose the $7M/MW stack. Google Project Deschutes already hit the thesis’s standards-authorship insight; this source adds a second, construction-shaped insourcing surface.

**Supports [[Theses/NBIS - Nebius Group]] §Conviction Triggers → HIGH (energize ≥600MW by Q3 / 800MW–1GW YE2026) as a construction-method datapoint, not a confirmation.** NJ precast + Bloom BTM and Béthune brownfield reuse are the source’s evidence that NBIS modularizes *selected* MEP and avoids greenfield shell where it can. That is consistent with an execution bet, not a de-risking of the >4× power ramp. The source does not disclose MW energized or a factory-slot reservation that would fire HIGH.

**Supports [[Theses/BE - Bloom Energy]] §Summary “time-to-power arbitrage, not a layer monopoly” at the NBIS NJ pairing; does not move §Conviction Triggers (audited RPO / repeat Tier-IV primary-power).** Bloom appears as a behind-the-meter module riding a precast hall — exactly the 50–90-day deployment product sitting next to a factory-built shell. VLM WEAK FIT on Bloom is unchanged: the source’s scarce layer here is *factory electrical/cooling integration*, not SOFC chemistry. Automation lens energy/industrials overlay remains Anti-fit/bounded for Bloom.

**Supports [[Theses/CRWV - CoreWeave]] only on the DSX/Omniverse execution path, not on §Conviction Triggers (MSFT renewal, Hopper re-rent, DDTL).** CoreWeave is named as already using DSX Air to twin AI factories. That is a construction-standardization input to time-to-power; it does not speak to counterparty credit or second-cycle rental rates.

**Challenges the miner-pivot “buy a finished stack” as a durable model versus [[Theses/IREN - IREN Limited]] §Key Non-consensus Insights “the durable asset is the power stack, not the GPU fleet.”** Hut 8 is the source’s worked example of a former miner purchasing Vertiv OneCore + Jacobs EPCM + AEP to commercialize a 704MW IT lease. That path rents the integration layer and pays OEM double-margin; IREN’s thesis claims the mispriced layer is owned, interconnected power + shell. Source implication: the buy-OneCore shortcut wins speed-to-lease and loses content/control — a live test of IREN’s owner-vs-renter split (VLM §2). IREN is not named in the article.

**Adds a revenue/MW datapoint to [[Theses/SPCX - SpaceX]] §Summary / §Key Non-consensus Insights on AI capital recovery, without touching → HIGH/LOW GW or CSA-duration triggers.** SemiAnalysis’s CSP rule of thumb is $12–15M per IT MW-year; it cites the SpaceX–Anthropic deal (and a Meta post) at ~$50M/MW, with Anthropic/OpenAI API also >$50M/MW. That is a *tenant willingness-to-pay* print, not evidence CSA duration covers GPU/turbine D&A — the variable the SPCX thesis isolates.

**Supports [[Theses/NVDA - Nvidia]] §Summary software/simulation stack (Omniverse, DSX) as facility-level lock-in; NVDA has no Conviction Triggers section to target.** DSX pulls civil, structural, architectural, power, cooling, and controls into a validated AI-factory architecture; Vertiv 12.5MW OneCore pods and Eaton Beam Rubin DSX are the physical attach. Hypothesis [G-6]/VLM interface-control: Nvidia is attempting to own the *reference-design interface* for the hall, not only the GPU. 800VDC “not well templated” in Stage-1 design is a near-term execution tax on that interface ([[Macro & Technology/800VDC Adoption]]).

**Supports [[Theses/META - Meta]] only as a capex-execution / enclosure tactic; META has no Conviction Triggers section.** Tents pull dried-in date forward and do not pull energized-MW date. That weakens any read that satellite hall-counts equal commissioned AI capacity, and it is consistent with the thesis’s ROIIC question on incremental infrastructure dollars ([G-7]).

**[[Theses/VICR - Vicor Corporation]] adjacency only.** Source discusses 800VDC as an untemplated facility-design problem and names Flex/Eaton/Siemens as modular-power attach; it does not mention Vicor, VPD, or socket share. Do not treat this as a Conviction Trigger print.

**Sector notes.** [[Sectors/Data Center Power & Cooling]] key question on prefab-at-density IP vs insourcing: source says both coexist — OEM-led stack for Hut 8/colo, operator-led for AWS/Aligned. [[Sectors/Neoclouds & GPU-as-a-Service]] construction question: modular is how Crusoe/Hut 8/Nebius try to convert power positions into leasable MW; it does not convert a GPU-rental business into a layer monopoly.

**Base-rate / outside view [G-10].** Factory-built construction (precast, PEMB, volumetric hotels/prisons) has a long reference class of schedule claims that die at site interfaces. SA’s own quality channel-check (reliability issues eating the time save) is the disconfirm already inside the source. Agreement across [G-4] frenzy factory capex, semis #17 (assuming factory capacity arrives in line with demand), and VLM OEM-layer hopes is the cue to hunt the bear: sold-out 12-month modular lead times plus L5 commissioning that cannot leave the site plus interconnect that modular never touches. Single falsifier for the “modular solves the labor ceiling” claim: 2027 electrician shortage still binds *after* 30%+ modular penetration because L2–L5 and utility work do not factory-ize.

## Source Excerpts
> "Our Modular Tracker, included in our SemiAnalysis Industrials Model, tracks over 61GW of modular capacity and 1,000+ sites using some form of modularization or prefabrication strategy."

> "We estimate that modular penetration will reach 30%+ of total live capacity by the end of 2028."

> "We rebuilt the modular case bottom-up against some of the speed and cost claims made by vendors like Vertiv or Schneider, finding that modular construction can compress the construction window by ~36%, or 7-9 months, and is ~8% cheaper on a Capex/MW basis."

> "We also analyze how vendors like Vertiv are able to expand their value capture per project by offering the full stack solution, going from their historical ~$3.5M/MW content to ~$7M/MW with the modular solutions."

> "A megawatt of IT load generates on the order of $12M to 15M of revenue a year, or about $1-1.25M per IT MW per month. That said, in such a capacity constrained market, we are seeing new deals being made on much higher disclosed pays, see SpaceX and Anthropic deal, or as we recently covered in our Meta newsletter post, revenues of $50M per IT MW."

> "Go-live is the latest of three dates, building ready, power available, and GPUs delivered, and accelerating the building earns nothing if it was not the date that bound."

> "When considering all the implications of the 800VDC transition, it is not as well-templated. A handful of reference designs exist, but none are well baked yet."

> "Operators consistently call this the single biggest gap in the modular cycle, with a full site commissioning running 3 to 8 months end to end."

> "We estimate Vertiv’s content can increase from roughly $3.5 million per MW for discrete power and cooling equipment toward approximately $7 million per MW under a full OneCore deployment."
