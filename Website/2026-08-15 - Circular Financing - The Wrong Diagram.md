---
date: 2026-08-15
tags:
  - essay
  - laniakea-partners
  - artificial-intelligence
  - datacenters
  - financing
  - credit
  - capital-cycle
  - vendor-financing
  - circular-financing
status: draft
audience: intermediate
source_note:
  - "[[Macro & Technology/AI Datacenter Financing Mechanism Design]]"
  - "[[Macro & Technology/Sustainability of AI Capex]]"
  - "[[Website/2026-07-29 - Sustainability of AI Capex]]"
  - "[[Mental Models/Generalist - Overview]]"
source: internal synthesis
---

# Circular Financing: The Wrong Diagram

![[1843741-17601230201037135.webp]]

**The most shared chart of the AI cycle is a circle.** Nvidia puts $30 billion into OpenAI. OpenAI carries roughly $1.4 trillion of compute commitments across Oracle, CoreWeave, Broadcom and the rest of its supplier set. Oracle and CoreWeave buy Nvidia chips with borrowed money. The arrows close where they began, and the caption writes itself: the vendor is funding its own revenue, the boom is financing itself, the demand is not real.

The filings do not match that picture. Vendor credit that has actually been entered runs two orders of magnitude below the $500 billion headline. Most of what has closed is equity — a shareholding, not a purchase order. The next dollar of financing is coming from insurance accounts, private-credit funds, construction banks and bond buyers who do not sit in that loop.

Whilst consensus expects these bespoke vendor financing arrangements of inflating revenue we expect that initial capital that Nvidia provides to its clients, and the residual value guarantee, has the effect of reducing the overall financing rate and increasing the demand from external funding partners and increases the speed and total quantum of funding for Nvidia's products. Furthermore, it serves to protect Nvidia's market share as alternative chips are likely not sufficiently capitalised to provide these terms, nor are they willing to guarantee residual value in the way Nvidia is able to. 

The structures are still hard to read. Terms are negotiated deal by deal, so the clauses that decide who pays in a default are mostly private. None of those contracts has been through a downturn in which customers, chip values and vendor earnings all break together. That is a credit problem. It is not evidence that the revenue was invented. It is also, for anyone willing to read the next filing, a standing advantage.
## What the headlines got wrong

"Nvidia's $500 billion circular financing scheme" is a set of memoranda of understanding signed in August with six asset managers — Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR. The ambition is to mobilize more than $500 billion of third-party capital over time, each project underwritten on its own. No vehicle exists. No amount has been raised. Nvidia's 10-K says financing requests have been received and that none of the residual-value support it has offered has been entered. The vendor credit that is live is a $3.5 billion maximum of site-lease guarantees — land, power and shells, not chips — on five-to-seven-year terms.

| The headline | The public record |
|---|---|
| "Nvidia raised a $500B fund to finance its customers" | MOUs with six asset managers; project-by-project underwriting; zero committed tickets; 10-K: requests received, none entered |
| "Nvidia's $100B OpenAI deal funds chip purchases" | $30B of ordinary equity inside a $122B round, next to Amazon's $50B and SoftBank's $30B; no deployment gating; Huang has said the full $100B is "probably not in the cards" |
| "Broadcom guarantees Apollo's $35B" | A $29B *maximum* lease backstop that rises as racks deploy and falls as the customer pays — not a guarantee of the deal size |
| "Residual-value support worth $125B" | "Up to 25% of an opportunity," selected deals, no denominator, no legal form, no signed agreement |

The $100 billion letter of intent is the number the chart never updated. It was meant to fund one tranche per gigawatt deployed. It stalled, then shrank into a $30 billion equity ticket in a round where non-vendor capital put in nearly three times as much. Equity does not oblige the customer to buy the vendor's product. OpenAI took Nvidia's $30 billion and then committed six gigawatts to AMD — and AMD is paying OpenAI for that commitment in penny warrants. Money is fungible. A shareholding does not steer a purchase order.

Against the annual flow, those vendor seats are small. The build is spending roughly $850–900 billion a year. Add Nvidia's equity, the $3.5 billion of site guarantees, Broadcom's $29 billion maximum backstop and Google's lease backstop on a ~$35 billion TPU vehicle, and you can get to the low hundreds of billions of *maximum contingent* exposure. Most of that is equity or a backstop that has not been drawn. Drawn credit is in the single-digit billions.

The outside money is sitting in priced deals. Pimco took ~$18 billion of a single $27.3 billion Meta campus bond. Blackstone anchored CoreWeave's $8.5 billion GPU facility. Datacenter asset-backed securities outstanding have grown from $4 billion to $61 billion since 2020. Morgan Stanley's map of the ~$1.5 trillion external financing need through 2028 puts $800 billion of it in private credit.

Trace those financings to the end and you usually find a cash payment or a third-party lender with covenants. OpenAI pays Oracle cash under a consumption agreement. Oracle pays rent to a site venture and owns the GPUs inside it. The venture services construction debt. Meta's rent services long amortizing notes held by insurance accounts.

A few live arrangements do look more like the late-cycle vendor-finance books people have in mind. AMD's warrant is the cleanest: the vendor is paying its customer synthetic equity for demand. Nvidia's stake in Valor — a fund that buys Nvidia GPUs and leases them to xAI — puts the vendor one layer under its own product. Reported talks around OpenAI's Piketon campus — roughly $250 billion of lease guarantees and up to $350 billion of chip financing — would, if anything like that closed, make vendor first-loss a fact of the capital structure rather than a footnote. Those belong on a watchlist. They are small against the annual flow. The large vendor-funded versions have mostly died before signature, because third-party capital has been cheaper than the vendor's own balance sheet.

Lucent and Nortel booked equipment sales in 1999–2001 against unsecured loans they themselves made to startup carriers with no revenue. When the carriers died, the receivables were worthless and the revenue had never existed. Global Crossing swapped identical fiber with its peers and booked the exchanges as sales. That pattern is real. Almost none of the paper printing today is that pattern.

## Seven ways a campus gets paid for

The structures multiplied in 2026 because internal cash ran out. Hyperscaler bond issuance reached $194 billion by early July against $108 billion in all of 2025. Alphabet's quarterly capex crossed above its operating cash flow. Oracle's free cash flow ran near negative $24 billion. Once the next dollar is borrowed, someone has to decide who holds construction risk, who holds the long cash flows, who owns the building if the tenant leaves, and who owns a used GPU if the contract ends.

Every live deal is some mix of those answers. Seven templates cover almost everything that has printed.

**1. The company just pays.** Microsoft, Google, Amazon and Meta still fund most of their own build from operating cash flow, investment-grade bonds and ordinary leases. This is the cheapest capital in the stack. Utilization, residual value and customer credit all stay on the company. The constraint is the rating, not the project model. As capex crosses above cash flow, more of the next dollar leaves this bucket.

**2. A campus vehicle, short lease, residual-value guarantee.** Outside capital owns about 80% of a project company. The hyperscaler keeps 20%, builds the campus, and occupies all of it. The vehicle issues long amortizing notes — Meta's Louisiana campus sold $27.3 billion of A+ paper out to 2049, Pimco taking ~$18 billion of it. The tenant signs a four-year lease with options out to twenty years, plus a declining residual-value guarantee running the first sixteen operating years: if it walks and a marketed sale clears below a contractual floor, it pays the shortfall. That guarantee is what turns a four-year lease into twenty-five-year investment-grade debt. Meta gets the vehicle off its balance sheet only because it gave up remarketing, successor negotiation and the right to sell the property. A twin deal in El Paso priced about 40 basis points wider ten months later — same rating, same structure.

**3. A GPU loan that draws as racks go in.** A vehicle holds the chips and the customer contracts. Lenders commit a facility that funds as equipment deploys, and the loan amortizes inside the anchor contract. CoreWeave's $8.5 billion facility is the template: first investment-grade GPU-collateral loan, about 5.9%, non-recourse. The rating comes from the take-or-pay (OpenAI, Meta), not from a view on used-chip prices. Residual risk shows up elsewhere in the same capital structure: the unsecured notes yield 9.625%. That 370-basis-point gap is what the market is charging for a used GPU today.

**4. The customer pays first.** Microsoft put roughly $7 billion into Nebius against a $17–19 billion contract, released against deployment and availability rather than as a lump sum at signing. Meta has a $27 billion prepay line. $75 billion of Oracle's $638 billion remaining performance obligation is customer-prepaid or customer-supplied chips. The customer is senior to every external lender because the cash arrives before the asset exists. Nebius now says more than 70% of new deals carry an upfront payment, expected to cover about half of related capex. Rising prepay share means customers are funding the build. Falling prepay share means more leverage and more vendor support.

**5. The vendor writes some form of support.** Nvidia's live committed instrument is the $3.5 billion of site-lease guarantees above — land, power and shells. Residual-value support ("up to 25% of an opportunity") has been offered; the 10-K says none of it has been entered. The $500 billion platform is still an uncommitted set of MOUs. Broadcom's version is more concrete: a $29 billion *maximum* lease backstop on Apollo's rack vehicle, rising as racks go in and falling as the customer pays. The stock later sold off on a sell-side note that walked those already-filed terms out to the full gigawatt ambition.

**6. An infrastructure platform owns the box.** An infrastructure manager and a sovereign put up most of the equity — Macquarie and GIC at Theseus, with Anthropic as the tenant. A separate compute vehicle bought about a gigawatt of Google TPUs for ~$35 billion and leases them to Anthropic, with Google backstopping the lease payments. Stargate is the same idea stacked three deep: a Blue Owl / Crusoe venture owns the shell and borrows construction money from JPMorgan; Oracle leases the site for fifteen years and owns the GPUs; OpenAI consumes under a separate agreement. The end customer's credit never touches the building loan. When Oracle and OpenAI scrapped a ~600 megawatt Abilene expansion in March, the break was at the one decision nobody had locked in.

**7. The building is securitized; the chips are not.** Land, power and the shell already have a bond market. US datacenter ABS outstanding has gone from $4 billion to $61 billion since 2020, with settled conventions and published rating methodologies. No GPU- or compute-backed ABS has ever been publicly priced. That is why mega-projects go through campus vehicles and private credit, and why GPU residual risk still lives in delayed-draw loans and unsecured notes rather than in a public bond.

The same name can sit in several of these at once. Meta is the off-balance-sheet tenant in a campus vehicle, a $27 billion prepay customer at Nebius, and a $14 billion offtaker at CoreWeave — three projects, three funding channels. A large buyer using every tool on the table gets written up as a web of self-dealing.

## Who holds which piece

| The risk | Who holds it | Why that holder |
|---|---|---|
| Construction and completion | Bank construction loans; milestone-gated prepayments | Short, secured, monitorable. Payment starts at acceptance, so unfinished-build risk stays with sponsors and contractors. |
| Long cash flows out to the 2040s | Insurance and annuity capital (Pimco ~$18B of the $27.3B Beignet notes: A+, 1.12× coverage, amortizing to 2049) | A 25-year amortizing investment-grade note is what an annuity book is built to hold. Banks and equity holders do not want this duration. |
| The campus if the tenant leaves | The tenant, via a declining residual-value guarantee running 16 years | Meta knows more than anyone about whether it will still want the campus in 2033. It pays a capped shortfall after a sale rather than owning 100% of a possibly empty building for 25 years. |
| Used-GPU value | Private credit, in the 370bp gap between CoreWeave's contract-backed loan and its unsecured notes; vendors, where they have written a backstop | Either the mandate to price an unrated leftover, or the remarketing desk, the software stack and the customer list. |
| Delivery risk on a prepayment | The customer, released against milestones | The buyer writes its own completion protection into the payment schedule. |
| First loss | Project equity: infrastructure funds, sovereign wealth | Locked-up capital. The leftover claim after everyone senior has been paid. |
| The float while racks are being built | Taiwanese ODMs, on local bank credit | Trade finance against purchase orders. A finished, financed campus can still miss a quarter if a bank concentration limit binds two layers down. |

Railroad equipment trusts financed rolling stock for a century and a half on this logic: title, remarketing rights and payment priority written down in advance. Aircraft enhanced equipment trust certificates kept paying through airline bankruptcies for the same reason. Unsecured loans from a vendor to a startup customer are a different product. Most of what is printing today — covenants, escrow, draws matched to deployment — is closer to the equipment-trust family than to Lucent.

The holders are mostly term-locked and lightly levered next to banks: private-credit funds that draw over years, insurance accounts buying paper to hold to 2049, sovereign wealth in project equity. The Fed puts average bank AI exposure near 0.8% of assets; private credit is doing most of the work in the riskier layers. Post-Enron consolidation rules also make cosmetic transfer hard. Meta deconsolidates those campus vehicles only because it surrendered the powers that matter. A stranded campus in 2033 is a workout inside one non-recourse vehicle. It is not a margin call that travels back onto a dealer balance sheet overnight.

Jay Cooke failed in 1873 because a deposit-funded bank was sitting on long railroad paper it could not place. The long paper here has been placed, with buyers who intend to hold it for decades. The fragile corner that does exist — semi-liquid retail private-credit vehicles — has already been marked in public. Blue Owl gated 41% of redemptions at one fund. That is a funding-side problem in one product, not a description of how the campuses are financed.

Deals that transfer nothing do not get leverage. SpaceX sells compute on 90-day cancellation at $30–50 million per megawatt-year, the highest price in the market, and no one will lend against it. Ninety-day paper cannot service a ten-year loan. Duration you can underwrite is what the debt attaches to.

## What the documents still hide

The lien priority among the participants in Broadcom's Apollo vehicle is undisclosed. Reserve accounts, cash-trap triggers and cure procedures — the clauses that decide who absorbs a correlated failure — have no public print anywhere in this market. The legal form of Nvidia's offered residual-value support (guarantee, put, or repurchase) is unstated. Anthropic appears as a named partner in a press release and as "customer" in the corresponding 10-Q. Meta books a $2.92 billion recognized investment against a disclosed $46.03 billion maximum exposure. Roughly $120 billion of sector debt has moved into vehicles that a consolidated leverage screen never sees.

That opacity is what you get when every deal is bespoke. No GPU-backed security has been publicly priced. No rating agency has published a methodology for compute collateral. Accounting pushes in one direction: the cleaner the transfer, the less the sponsor's balance sheet shows, so a real deconsolidation and a decorative one look the same at the line-item level. The difference is in a variable-interest-entity footnote.

The market is already charging for the unreadability. 86% of hyperscaler bonds trade wider than where they were issued. The second Meta campus vehicle priced about 40 basis points wider than the first on the same structure and the same rating, with no tightening from price talk.

Splitting the risks also does not remove the fact that they move together. One AI demand shock raises the odds the customer defaults, cuts the recovery value of the chips and the campus, and arrives when exposure is highest — which is also when the vendor who wrote the backstop is having its own worst quarter. Broadcom's top five customers are roughly 45% of its revenue. These structures handle a single failed project reasonably well. A correlated break they handle only as well as the contracts are written, and none of those contracts has run even once. No vacated single-tenant hyperscale campus has sold at arm's length. No GPU fleet has been remarketed through a downturn.

## Why the opacity is useful

The same unreadability is what creates the edge. A market that prices this complex off a chart and a capex headline, while the actual state of the paper surfaces one 10-Q footnote, one rating action and one priced deal at a time, is paying a continuing rent to anyone doing the reading. You do not need a private data room. You need to know which template a new print belongs to, and which line in the filing would change your mind.

That rent is already being collected in public. Broadcom fell about 6% when a sell-side team walked a disclosed backstop out to its 20-gigawatt conclusion — about $370 billion of maximum residual-value exposure by 2029 — weeks after the terms were filed. The 40-basis-point gap between the two Meta campus bonds was visible to anyone tracking those prints and invisible to anyone reading capex guides. CoreWeave's 370-basis-point split between contract-backed and unsecured paper is a live GPU-residual quote most equity holders in the sector do not know exists. Nebius's disclosure that more than 70% of new deals carry upfront customer payments sits in an earnings deck and tells you, more directly than any leverage ratio, whether customers or lenders are funding the next gigawatt.

A handful of dated events will reset a lot of this paper at once, and each will be read first by people who already know which template they are looking at:

- The first closed ticket under the Nvidia platforms, with a disclosed spread and loan-to-value, turns an MOU into a price for whether a GPU can be redeployed.
- The quarter Nvidia's filings flip from "none entered" to entered, the vendor is in the loss stack.
- The first re-rental prints on aging Hopper fleets put a number under every residual assumption in the stack.
- Prepay share of new deals tracks whether customers or leverage are funding the next gigawatt.
- The third campus-vehicle print tells you whether the extra spread on this structure is still widening.

If a neocloud restructuring or a backstop draw shows the support disappearing at the moment it is needed — priorities disputed, recoveries near zero — then Lucent was the right comparison. Until that print arrives, the capital is mostly external. The remaining work is reading the next deal before the tape does.
