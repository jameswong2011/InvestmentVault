---
publish: false
date: 2026-08-11
tags: [research, email-backfill, SuperpositionV]
source: 'https://superpositionv.substack.com/p/nvidia-special-series-part-2-how'
source_type: web-clip
sender: superpositionv@substack.com
---

# Nvidia Special Series Part 2 How Do You Underwrite an AI Factory

Fact cutoff: August 11, 2026

> Evidence policyThis essay distinguishes among confirmed facts from official filings and announcements, company claims about technologies and transactions, analytical inferences drawn from public evidence, and testable predictions that remain to be observed.

An AI factory is not financed on chip collateral alone. In normal operation, lenders ask whether customer contracts and market revenue can cover debt service. After failure, they ask how much can be recovered from equipment, contracts, and vendor support—and which party absorbs the loss first.

Imagine a lender walking through an AI data center. Thousands of accelerators are installed, and the benchmarks look exceptional. But the credit decision does not end with the question, “Which chip is fastest?” Is power and cooling secured on time? When do the customer’s payment obligations begin? Who bears the cost if the facility fails its performance-acceptance tests? If the customer leaves, how long will it take to find another buyer and return the capacity to a billable state? During that interval, who absorbs the downtime and price decline: equity investors, the customer, the silicon vendor, or the lender?

Two financing initiatives announced in 2026 appear, at first, to offer different answers. On August 10, 2026, NVIDIA announced plans with six financial institutions to establish independent compute-financing platforms, foregrounding the redeployability of its compute across customers and workloads, software-enabled life extension, and residual value. On June 9, 2026, Broadcom, Apollo, and Blackstone announced the AI XPV Platform, foregrounding Anthropic’s large-scale capacity expansion, multiyear capital commitments, and contracted cash flows. Yet the filings show that neither case is a pure type. NVIDIA already guarantees certain facility lease obligations, while Broadcom is backstopping five years of customer lease obligations with maximum exposure of $29 billion.

The central claim is this:

> The financing of an AI factory is not a choice between general-purpose chips and long-term contracts. It is the task of combining normal-state cash flow, default-state net recovery, and the loss waterfall among customers, vendors, sponsors, equity, and lenders into a single structure.

This essay does not address the full corporate-credit profile of hyperscalers or their general bond issuance. It focuses on structures built around specific AI compute assets and customer contracts: special-purpose vehicles, leasing, project finance, and object finance. Much as the Basel specialized-lending framework distinguishes project finance supported by a project’s own revenues from object finance supported by the cash flows of a specific physical asset, actual AI-factory financing is likely to combine facilities, equipment, customer contracts, corporate credit, and vendor support.

## The central map: how a technical asset becomes a credit asset

In this map, offtake or contracted-cash-flow underwriting and fungibility or residual-value underwriting are not mutually exclusive legal categories. They are analytical ideal types used to interpret real transactions.

# 1. The $500 Billion Announcement Is a Proposal to Build a Market, Not Completed Financing

On August 10, 2026, NVIDIA announced strategic partnerships with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs, and KKR to establish independent compute-financing platforms. The agreements are memoranda of understanding. Their stated objective is to mobilize more than $500 billion of third-party capital over time for AI infrastructure.

The announcement describes multiple dedicated capital pools and independent platforms. It does not describe a single funded vehicle, a closed fund, or a committed amount for one customer.

Three formulations should therefore be avoided.

It is not yet accurate to say that NVIDIA has raised $500 billion. It is also inaccurate to say that a single $500 billion fund has been launched. And there is no basis for saying that NVIDIA has guaranteed the entire amount.

What is publicly confirmed is narrower. NVIDIA and the six financial institutions intend to build platforms capable of mobilizing more than $500 billion of third-party capital over an extended period. The financial institutions are expected to underwrite individual projects independently, assessing the customer, demand, utilization, cash flow, and residual value. According to Jensen Huang’s description, NVIDIA provides the compute platform and ecosystem; the capital providers make the financing decisions.

But the announcement should not be read as NVIDIA withdrawing entirely from vendor-level risk support.

NVIDIA’s FY2026 Form 10-K states that the company had received requests to provide financing for customers’ and partners’ data-center development, but had not, at that time, entered into such financing arrangements. The same filing separately discloses guarantees of certain partners’ facility lease obligations.

The maximum aggregate exposure under those guarantees was $3.5 billion. The terms run for five to seven years, and partners had placed $712 million in escrow. NVIDIA states that if a partner defaults, it may take over the underlying lease, use the facility itself, or sublease it to a third party. The guaranteed layer principally concerns land, power, and the building shell—the site layer rather than the compute equipment itself.

The August platform is therefore better understood not as a replacement of vendor finance by independent finance, but as an attempt to institutionalize project-level underwriting by independent capital providers at a much larger and more repeatable scale—while preserving the option to use limited vendor credit support where needed.

There is no public evidence that the existing $3.5 billion facility guarantees are part of the August platform. Nor should those guarantees be treated as the same instrument as the residual-value support NVIDIA says it may offer for selected future opportunities.

The two forms of support sit at different layers. The existing guarantees concern land, power, and shell. The potential residual-value support concerns the recoverability of the compute asset. They should not be combined or treated as one program.

The headline number matters less than whether this architecture can become a repeatable credit market.

To move beyond bespoke negotiations, the market will need common definitions of the asset boundary, performance, customer contracts, collateral value, vendor support, and post-default redeployment procedures.

What has been confirmed so far is a proposal to create such a market. Actual commitments, capital raised, capital deployed, spreads, loan-to-value ratios, maturities, and final financing costs have not yet been disclosed. It would therefore be premature to claim that NVIDIA customers have already obtained a lower weighted average cost of capital.

# 2. Before Cash Flow: Completion and Performance Acceptance

Neither contracted cash flow nor redeployability becomes a repayment source until the AI factory is completed and enters commercial operation.

For a new project, the first risk may not be customer attrition. Land and grid connections may be delayed. Cooling and networking may not be ready. Rack delivery and systems integration may fall behind schedule. The equipment may be installed but fail to meet the throughput, reliability, or acceptance criteria required by the customer.

In its quarterly filing for the period ending April 26, 2026, NVIDIA identified access to data-center capacity, energy, and capital as critical to customers’ and partners’ ability to deploy AI infrastructure. It described energy expansion as a multiyear process involving regulatory, technical, and construction complexity, and warned that shortages of data-center capacity or power could delay or reduce deployments.

Broadcom similarly warns that customers may underestimate the amount of data-center, power, and water capacity required, and that a bottleneck in one component of a data-center project can affect the project as a whole.

This is why an AI factory cannot be analyzed as a single block of “GPU collateral.”

The first layer is the site-fixed layer: land, building shell, grid interconnection, substations, and cooling. These assets may have long physical lives, but they are tied to one location and one regional power market.

Above that sits the relatively movable equipment layer: accelerators, servers, racks, and some networking equipment. These assets can theoretically be relocated. But relocation requires more than packing and shipping. The destination must have adequate power, cooling, networking, and physical compatibility. The system must then be reintegrated and requalified.

The third layer is the intangible operating layer: software licenses, model support, monitoring, security certifications, maintenance, and the operating organization. Legal title to the hardware may transfer without the software, support rights, or operational capability needed to use it at the same level.

The final layer is the contract and credit-support layer: customer leases, capacity-purchase agreements, service-level obligations, escrow, guarantees, vendor backstops, and residual-value support. This layer determines how the physical asset becomes normal-state cash flow and post-default recovery.

A lender is therefore not asking one question—“What is the residual value of this AI factory?”—but several.

Which assets can actually be moved? Who holds legal ownership and control? Can the customer contract be assigned after default? Do the software, warranty, and maintenance rights travel with the equipment? Is there another site with enough power and cooling to receive the racks?

Technical versatility becomes a financeable recovery path only when all of these layers connect.

# 3. What Does a Lender Actually Underwrite?

AI-factory credit analysis must separate the performing state from the default state.

In the performing state, the lender examines cash flow available for debt service, or CFADS. This is the cash left from customer lease payments, long-term capacity contracts, and merchant revenue after power, operations, maintenance, required reinvestment, and other necessary outflows.

A common measure is the debt service coverage ratio, or DSCR. The name is technical; the question is simple:

> Under normal and stressed conditions, how many times can the project’s available cash flow cover scheduled principal and interest?

After default, the question changes:

> If the customer contract fails, how much can be recovered through re-leasing, redeployment, or sale of the equipment and facility?

The relevant figure is not the headline secondhand price of the hardware. It is the net amount remaining after downtime, dismantling, transport, porting, requalification, legal enforcement, maintenance, and price discounts.

Within this broader credit framework, two underwriting logics are especially useful.

The first is fungibility / residual-value underwriting.

This logic assumes that if the current customer leaves, the AI factory can be reassigned to other customers and workloads, restoring market revenue. If necessary, the equipment can be re-leased or sold to reduce loss severity.

The second is offtake / contracted-cash-flow underwriting.

This logic assumes that the current customer remains obligated to pay under a long-term contract or lease, allowing debt service to continue without immediately finding another buyer.

These are not pure opposites.

A long-term contract still requires analysis of collateral value after customer default. A broadly redeployable asset still needs paying customers and current cash flow to service its debt. Real transactions place guarantees, backstops, escrow, and vendor support between these two logics to allocate losses.

The governing questions are not reducible to benchmark performance.

> In the performing state, how reliably does cash flow cover debt service? In the default state, how much can be recovered after customer credit and collateral value deteriorate together? And who bears the losses, in what order?

# 4. The Logic NVIDIA Publicly Foregrounds: Fungibility and Residual Value

The company logic NVIDIA publicly foregrounded in its August 2026 announcement is redeployability and residual value.

NVIDIA argues that its AI factories can run a broad range of models and workloads, can be reused across customers, clouds, and operators, and can receive CUDA software updates that improve the performance and economics of already-installed infrastructure. The company’s claim is that its large developer and customer ecosystem deepens the pool of potential users and offtakers, supporting residual value.

That is a company claim. It is not independent evidence that every NVIDIA-based AI factory can be immediately redeployed at a high price after default.

Three concepts must be separated.

Technical versatility means that one system can run many models and workloads.

Operational redeployability means that the system can move from one customer or workload to another without excessive downtime, reconfiguration, requalification, or additional investment.

Bankable redeployability is narrower still.

> The asset must return to a billable state within a bounded time and cost, and the resulting cash flow or sale proceeds must be material to the lender’s recovery.

Technical compatibility does not guarantee bankable redeployability. A rack may be capable of running multiple models, yet no replacement customer may exist. A customer may exist, but data sovereignty, security, networking, or software-license restrictions may delay the transition. If the entire industry is overbuilt, many assets may pursue the same replacement customers at once, driving prices sharply lower.

The lender’s ultimate question is therefore:

> If the current customer disappears, who will use this asset next, when will they begin paying, and at what price?

## What does support of “up to 25% of an opportunity” mean?

Jensen Huang wrote that, in some cases and subject to opportunity-by-opportunity review, NVIDIA may provide residual-value support of up to 25% of the relevant opportunity. He also stated that such support is limited and intended to supplement, not replace, independent underwriting by financial institutions.

This does not mean that NVIDIA has guaranteed 25% of the entire $500 billion.

The public language does not define the denominator of “the opportunity.” It could refer to equipment cost, total project cost, loan principal, or another measure. The legal form is also undisclosed. It could be a guarantee, put option, repurchase arrangement, equipment exchange, or something else.

The valuation date, trigger conditions, duration of support, and priority relative to other creditors are also unknown.

The evidence should therefore be divided carefully.

Confirmed fact: NVIDIA has stated that it may offer limited residual-value support for selected projects.

Company claim: The breadth of NVIDIA compute, software upgrades, and redeployability allows limited support to catalyze financing.

Analytical inference: If the support is legally enforceable and genuinely reduces a defined post-default loss layer, lenders may be willing to consider a higher LTV, longer maturity, or lower debt spread.

Not yet demonstrated: That the platform has already reduced WACC for NVIDIA customers.

NVIDIA’s existing facility guarantees show that the company is not categorically opposed to retaining some infrastructure risk. But those guarantees should not be treated as part of the August platform or the proposed “up to 25%” residual-value support. They concern different asset layers and appear in different disclosures.

# 5. The Logic Broadcom Publicly Foregrounds: Contracted Cash Flow and a Vendor Backstop

Broadcom’s case is more specific—and more hybrid—than it first appears.

On June 9, 2026, Broadcom announced the AI XPV Platform with Apollo and Blackstone Credit & Insurance as initial core capital partners. The platform is intended to support more than 20 gigawatts of potential AI compute capacity by 2028 using Broadcom custom XPUs and networking.

The initial $35 billion capital solution is led by Apollo alongside Blackstone and global banks. Broadcom’s announcement connects it to more than one gigawatt of training and inference infrastructure for Anthropic, with deployment beginning in mid-2026 at Fluidstack-operated sites. Apollo described the structure as providing committed capital on a multiyear draw schedule and emphasized contracted cash flows as a defining feature of the asset class.

At that level, the transaction appears to be a straightforward example of contracted-cash-flow underwriting.

Broadcom’s Form 10-Q for the quarter ended May 3, 2026, however, discloses a more consequential structure in its subsequent-events section.

Broadcom states that, on June 8, 2026, Apollo assumed purchase agreements for AI racks based on Broadcom-designed custom accelerators, together with the related customer lease agreements. Broadcom will backstop the customer’s lease obligations for five years.

Broadcom’s exposure increases as the racks are deployed and declines as the customer makes lease payments. The maximum exposure is $29 billion. If the customer defaults, Broadcom may assume the leases or seek to sell the AI racks to reduce its exposure.

The official announcement links the initial $35 billion transaction to Anthropic’s expansion. The 10-Q refers to Apollo and a “customer” but does not name that customer. It is reasonable to read the two disclosures as describing the same initial architecture, but it would be inaccurate to say that the SEC filing itself names Anthropic.

The $29 billion figure must also not be described as an unconditional guarantee of the full $35 billion transaction. It is Broadcom’s maximum exposure, dynamically increasing with rack deployment and declining with customer lease payments.

The structure is therefore not just contracted cash flow.

It is:

> five years of customer lease obligations→ a Broadcom backstop of up to $29 billion→ and, after customer default, the option to assume the leases or sell the racks.

The initial Broadcom transaction is thus a hybrid: contracted lease cash flow serves as the first repayment logic, while the vendor retains a significant portion of customer-credit risk.

Broadcom’s backstop should not be treated as identical to NVIDIA’s proposed residual-value support. The disclosed instrument is a backstop of customer lease obligations, accompanied by post-default remedies. The eventual sale value of the racks affects Broadcom’s ultimate loss, but the public filing does not describe a guaranteed residual value.

Important terms remain undisclosed.

The public documents do not reveal whether the customer has broad termination rights, whether the lease is effectively take-or-pay, whether performance shortfalls reduce payments or permit termination, how liens and creditor priorities are structured, or how losses are allocated among Apollo, the banks, Blackstone, and Broadcom. The detailed claim, cure, and enforcement procedures for the backstop are also not public.

But the earlier claim that guarantees and post-default remedies were undisclosed can no longer be maintained. The duration, maximum exposure, and some remedies are confirmed in the official filing.

# 6. NVIDIA and Broadcom Are Not Pure Opposites

The difference between NVIDIA and Broadcom is not as simple as asset value versus contract.

NVIDIA does not ignore contracted cash flow. Jensen Huang explicitly states that financial institutions will underwrite the customer, demand, utilization, cash flow, and residual value. NVIDIA’s fungibility thesis is therefore not collateral-only financing without customer contracts. The customer and current cash flow remain the first repayment source; redeployability and residual value become additional recovery paths if the contract fails.

Broadcom, in turn, is not financing a contract without regard to the physical asset. Its filing states that, after customer default, Broadcom may take over the leases or sell the racks. Control rights and recoverable equipment value are embedded in the structure. At the same time, the backstop transfers part of the customer-credit risk from capital providers back to the vendor, reducing the need for lenders to rely solely on the residual value of custom racks.

The real difference is which underwriting logic is publicly foregrounded, and where the vendor’s credit enters the asset stack and the loss waterfall.

NVIDIA’s August MOU foregrounds redeployability across customers and workloads, along with residual value. NVIDIA has previously supported the site layer through guarantees related to land, power, and shell, and has stated that it may provide limited residual-value support for selected future opportunities.

Broadcom’s initial XPV transaction foregrounds five years of lease cash flow from a large customer. Yet the structure also places up to $29 billion of lease backstop exposure on Broadcom and provides post-default remedies through lease assumption or rack sales.

Between the two underwriting logics sits a third layer:

> Guarantees, backstops, escrow, lease assumption, and residual-value support allocate the loss interval between contract failure and asset recovery.

This is not a third underwriting ideal type. It is the credit-support layer that turns the two ideal types into actual transactions.

Financial institutions are not loyal to one architecture. Apollo and Blackstone appear in both the Broadcom platform and NVIDIA’s announced financing initiative. Capital providers can finance NVIDIA, Broadcom, and other silicon architectures simultaneously, depending on project cash flow, contracts, collateral, vendor support, and risk-adjusted return.

# 7. Open Weights Affect Both Underwriting Logics

Part 1 argued that open weights can create two opposing infrastructure effects.

The first is demand-side fungibility: a broader set of customers and workloads may be able to use the same AI-factory capacity.

The second is silicon portability: the same model may become easier to qualify for production on alternative accelerators.

The July 2026 letter Open Weights and American AI Leadership argues that open-weight models expand organizations’ ability to deploy and control models on their own infrastructure, while increasing competition across model, cloud, chip, application, and service layers. This is a policy and industry claim made by the signatories, including NVIDIA. It is not independent evidence that open weights have already improved loan pricing or residual values.

## The effect on fungibility underwriting

Open weights can increase the number of customers willing to deploy models on infrastructure they control rather than rely on one closed API provider.

Organizations that cannot use external APIs because of regulation, security, data sovereignty, or control requirements may become independent buyers of compute capacity. A model may also remain operable even if its original provider changes strategy.

If this effect actually deepens the pool of replacement customers and reduces the time required to re-contract capacity, the fungibility thesis becomes stronger.

But greater persistence of demand for a model does not automatically imply greater persistence of demand for NVIDIA silicon.

## The countervailing effect of silicon portability

If weights and related artifacts are accessible and the license permits their use, more third parties can build porting, optimization, and validation paths for alternative backends.

The same model may eventually be qualified on AMD GPUs, TPUs, Trainium, or customer-specific XPU environments that the user can actually access.

Open weights alone are not sufficient. Production migration still requires compiler and kernel support, memory and networking optimization, numerical and model-quality validation, throughput and latency testing, security approval, and operational reliability.

The lender’s governing variable is not simply whether the weights are open.

> How long does it take to qualify the workload on an alternative backend at the same quality, functionality, scale, and service level? What does the migration cost, and is the post-migration cost per task acceptable?

As that time and cost fall, customers gain greater leverage at renewal, expansion, and new-deployment decisions. That can pressure renewal rates and architecture-specific residual values for NVIDIA-based assets.

## The effect on contracted-cash-flow underwriting

A long-term contract can absorb the near-term impact of silicon portability. Even if the customer could technically migrate, the existing lease obligation may continue to protect debt cash flow during the contract period.

The picture changes after contract expiry.

If alternative silicon has become economically superior, the customer may decline to renew. A lender may assign high value to cash flow during the committed term but a lower value to renewal probability and post-maturity collateral.

The opposite outcome is also possible. If a custom XPU delivers a sufficiently large cost-per-task advantage, customer-specific optimization may support a stronger long-term contract and compensate for lower general-purpose redeployability. But if that customer fails, the pool of replacement users may be shallower.

Open weights therefore do not unambiguously favor one underwriting logic.

> Open weights can increase the persistence of demand for a model while reducing the persistence of demand attached to a particular silicon architecture.

The governing variable between those effects is the time and total cost required to qualify an alternative backend for production.

# 8. How Technical Architecture Becomes Credit Terms

Technology does not become WACC directly.

Between the two lie cost per task, utilization, contractual continuity, cash flow available for debt service, and post-default net recovery.

## Cost per task and utilization

Nominal FLOPS and a low cost per task are not the same thing.

What matters to the customer is the cost of reaching the required model quality, latency, and throughput. If the same workload can be processed with fewer racks and less power, the customer’s unit economics improve. Better customer margins may increase the probability of continued usage and renewal.

Conversely, a system may have high nominal performance yet produce weak cash flow because of software bottlenecks, low utilization, or network instability.

The first translation path is:

> performance and power efficiency→ cost per task and sellable throughput→ customer margins and utilization→ cash flow available for debt service→ debt spread and leverage.

## Power, completion, and operational reliability

Power efficiency changes not only operating costs, but also the probability of completion and the number of sites to which the equipment can be moved.

If the same revenue can be generated with less power, the project is less sensitive to electricity prices and can sell more compute within a constrained power envelope. If the equipment’s power and cooling requirements are unusually demanding, the number of viable deployment and replacement sites shrinks.

Operational reliability also connects directly to contracted cash flow. If the customer contract requires uptime, throughput, or latency, failures and performance shortfalls may trigger lost revenue, service credits, payment reductions, or termination rights.

The second translation path is:

> power, cooling, networking, and reliability→ completion and performance acceptance→ contractual performance obligations→ utilization and cash-flow volatility→ maturity, reserves, and debt pricing.

## Software, portability, and redeployment

Software can extend or shorten the economic life of hardware.

NVIDIA argues that CUDA updates improve the throughput and efficiency of already-installed infrastructure, extending its economic life. If this is repeatedly demonstrated across material production workloads, depreciation in economic value may be slower than the hardware-generation cycle alone would suggest.

But software cannot eliminate every physical constraint. New models may exceed the memory, precision, or networking capabilities of older systems. Common compilers and serving layers may also reduce the cost of moving workloads to competing silicon, weakening renewal rates and residual value for the incumbent architecture.

The third translation path is:

> software support and silicon portability→ supported workload range and switching cost→ renewal probability and depth of replacement demand→ remarketing time and price discount→ net recovery, LTV, and maturity.

The financial terms also need precise placement.

A spread is not simply the price of expected credit loss and cash-flow volatility. It may also reflect maturity, liquidity, capital usage, embedded options, structural complexity, and market supply and demand.

LTV is not merely a percentage of purchase price. It reflects how much leverage can be supported by the asset’s recoverable value after enforcement, relocation, downtime, and other stress costs.

Maturity should be aligned not with physical life alone, but with the customer contract, economic competitiveness, vendor-support period, and redeployability.

WACC is not a term set by one lender. It is the combined result of debt cost, equity cost, and capital structure.

The central conclusion is therefore:

> AI chip competition is not moving from FLOPS to WACC. FLOPS, power efficiency, software, networking, and operational reliability are translated into cost per task, utilization, cash flow, and net recovery. Those outcomes shape spreads, LTV, maturity, residual value, and ultimately WACC.

Finance is not replacing technical competition. Technical advantage is reflected in financing terms only when it produces defensible normal-state cash flow and recoverable default-state value.

# 9. Five Ways an AI Factory Can Fail

## 1. Completion and performance-acceptance failure

The first failure may occur before the customer leaves: the factory may not enter commercial operation on time.

Grid connection, permits, cooling, rack and network delivery, integration, and commissioning may be delayed. If performance does not meet the customer’s acceptance conditions, lease or capacity-payment obligations may not begin as scheduled.

The key question is who bears cost overruns and interest during delay. If the customer’s obligations begin only after commercial operation, pre-completion risk remains with sponsors, vendors, contractors, and capital providers.

Both NVIDIA and Broadcom disclose data-center capacity, power, water, capital availability, and component bottlenecks as real constraints on large-scale AI deployment.

## 2. Oversupply

Redeployability depends on market conditions.

When demand is strong, replacing one customer may be easy. But if the industry has overestimated demand, many AI factories may bring the same generation of capacity to market at once. Even technically versatile equipment can suffer sharp rental and resale-price declines if replacement demand is smaller than available supply.

The versatility of one machine and the resilience of the portfolio are not the same thing. Customers may appear independent while all being exposed to the same AI capital-expenditure cycle.

## 3. Technological obsolescence

Accounting life, physical life, and economic life are different.

Equipment may function normally while losing market competitiveness because a new generation delivers much more useful work per unit of power. New models may also require more memory, different precision formats, or more advanced networking than older racks can provide.

Software updates can improve the efficiency of legacy assets, but they cannot remove every physical constraint. High utilization or rental pricing today does not prove stressed residual value at financial maturity.

## 4. Correlated exposure

Contracts and collateral may not be independent protections.

If the customer’s business depends on AI demand and model economics, while the collateral’s value depends on the same demand, a downturn may simultaneously raise customer default probability and the asset’s loss severity.

The contract deteriorates precisely when replacement demand and secondhand prices weaken.

Broadcom estimates that its five largest end customers represented approximately 45% of net revenue in the first half and second quarter of fiscal 2026. This does not measure the default probability of the XPV transaction or Anthropic. It does show that Broadcom’s broader business and the custom-AI supply chain are sensitive to the investment decisions of a small number of large customers.

A financial institution may invest in several nominally separate projects and still be concentrated in the same silicon generation, frontier-model demand, power markets, and AI investment cycle.

## 5. Silicon portability

Portability means different things to the customer, lender, and owner of the incumbent asset.

For the customer, it is an exit option at renewal or expansion.

For the lender, it can enlarge the set of models and customers that might use the asset.

For the owner of the incumbent silicon, it is a risk to renewal and residual value if the customer can preserve the model and data while moving to a more efficient accelerator.

Low portability is not inherently safe either. It may bind the current customer more tightly, but if that customer fails, replacement demand may be limited.

> Portability is an exit option for the customer, a potential source of replacement demand for the lender, and a renewal and residual-value risk for the incumbent silicon.

# 10. What Matters—and What Does Not

What matters is not the $500 billion headline.What matters is how many final transactions are signed, how much capital is actually committed, raised, and deployed, and what the project-level terms look like.

NVIDIA’s announcement currently reveals a market-building ambition and a company underwriting thesis. Actual spreads, LTVs, maturities, and vendor-support terms have not been disclosed.

What matters is not whether a rack can theoretically run many models.What matters is what percentage of capacity can be requalified for production after a customer change, and how much time and money are required to make it billable again.

Technical compatibility and bankable redeployability are not the same thing.

What matters is not whether current GPU rental prices are high.What matters is the time required to re-contract, re-lease, or sell the asset—and the net recovery—when customer attrition and oversupply occur together.

Current prices can be evidence of current demand. They are not proof of collateral value at maturity.

What matters is not the nominal amount of vendor support.What matters is its trigger, duration, valuation method, priority, enforceability, and the support provider’s ability to pay under stress.

Broadcom’s maximum $29 billion backstop is not a fixed, unconditional payout. Exposure rises with rack deployment and falls with customer lease payments; lease assumption or rack sales may reduce the amount after default.

What matters is not the simple claim that NVIDIA is general-purpose and Broadcom is custom.What matters is which layer fixes normal-state cash flow, and which party holds the first loss and the last loss.

NVIDIA structures still require customer contracts and may include vendor support. Broadcom’s structure still depends on control over the equipment and post-default recovery.

Four criteria should come first when evaluating AI-factory financing.

The first is completion and performance acceptance. When will power, cooling, racks, and networking enter commercial operation, and who bears delay and cost overruns?

The second is the first normal-state repayment source. Is it a long-term contract, diversified market revenue, or a combination? How reliably does that cash flow cover debt service?

The third is bankable redeployability and net recovery. After customer loss, how long will re-leasing, redeployment, or sale take? What remains after price discounts, requalification, relocation, enforcement, and downtime?

The fourth is duration alignment and the loss waterfall. Do the customer contract, vendor-support period, loan maturity, and economic life of the technology align? Which losses are borne by equity, the customer, the vendor, junior capital, and senior lenders?

# Conclusion: Technical Architecture Is Being Translated into Credit Architecture

For NVIDIA’s August 10, 2026 initiative to succeed, NVIDIA compute must become more than a popular chip platform. It must become an asset that capital providers can underwrite repeatedly.

That does not mean every NVIDIA system has the same collateral value. It means that the site and power, hardware generation, networking, software, operator, customer contracts, and vendor support must be measured separately.

NVIDIA foregrounds independent underwriting and the thesis of redeployable compute. Yet the company already guarantees some facility lease obligations and says it may provide limited residual-value support for selected opportunities. NVIDIA’s credit does not disappear. It may be inserted selectively into particular asset layers and loss intervals.

Broadcom’s AI XPV Platform foregrounds contracted cash flow. Yet Broadcom’s five-year backstop of customer lease obligations—up to a maximum exposure of $29 billion—and its ability to assume leases or sell racks after default show that it, too, retains material customer-credit and recovery risk.

The two cases therefore do not represent a simple collateral contest between general-purpose GPUs and custom XPUs.

> They represent a competition to design who supplies normal-state cash flow and who owns default-state losses.

Other things equal, an asset with both a strong contract and a broad remarketing path may support more debt. But the two protections cannot simply be added if both are exposed to the same AI demand cycle. The customer may fail at precisely the moment replacement demand and secondhand prices collapse.

The self-reinforcing effect of finance on technical competition is also conditional.

If demand persists, oversupply remains limited, and the technology’s economic life exceeds the financing maturity, better financing can accelerate deployment. A larger installed base may attract more developers, workloads, and potential replacement customers, which could further improve financing terms.

But if capital expands faster than real demand, the same mechanism amplifies oversupply. Assets that appear highly redeployable during the boom may all pursue the same replacement customers when the cycle turns.

The financialization of AI compute is therefore not merely a story about more money entering AI.

> AI chip competition is not moving from FLOPS to WACC. FLOPS, power efficiency, software, networking, and operational reliability are translated into cost per task, utilization, cash flow, and net recovery. Those outcomes shape spreads, LTV, maturity, residual value, and ultimately WACC.

Whether AI compute becomes a distinct infrastructure asset class will not depend on capital volume alone.

Before commercial operation, the market must define who bears power, completion, and performance-acceptance risk. During operation, it must measure whether contracts and market revenue cover debt service. After contract failure, it must determine how quickly and at what price the equipment can be monetized again.

The unresolved question is not whether lenders will prefer NVIDIA or Broadcom.

> When the same AI demand shock simultaneously weakens the customer’s ability to pay and the rack’s remarketing value, who among the customer, vendor, sponsor, equity investor, and lender absorbs the first loss—and who absorbs the last?

AI factories will become a genuine infrastructure asset class only if the market can turn that loss waterfall, along with completion conditions, collateral rights, performance measurement, secondary-market pricing, and vendor support, into repeatable standards.

# Appendix

## Assumptions

### The two underwriting logics are not legal transaction categories

Fungibility or residual-value underwriting and contracted-cash-flow underwriting are analytical ideal types. Actual transactions may combine project finance, equipment finance, leasing, corporate credit, vendor guarantees, and equity cushions.

### The $500 billion is not a fully funded single vehicle

As of August 10, 2026, the confirmed facts are the memoranda of understanding with six financial institutions and the objective of mobilizing more than $500 billion of third-party capital over time. Actual commitments, capital raised, capital deployed, and transaction terms must be verified separately.

### NVIDIA’s two forms of support are separate

The maximum $3.5 billion of facility lease guarantees disclosed in NVIDIA’s FY2026 10-K principally relate to land, power, and shell. Jensen Huang’s statement that NVIDIA may support up to 25% of selected opportunities refers to a separate potential residual-value mechanism. No linkage or aggregation between the two has been disclosed.

### Broadcom’s $29 billion is a dynamic maximum exposure

Broadcom’s backstop exposure rises as racks are deployed and falls as the customer makes lease payments. It should not be interpreted as an unconditional guarantee of the full $35 billion initial transaction.

## Mechanism Details

### Performing state

In the performing state, the lender examines revenue from contracts, leases, and merchant customers after subtracting power, operations, maintenance, taxes, and required reinvestment.

The remainder can be described conceptually as cash flow available for debt service, or CFADS.

DSCR compares that cash flow with scheduled principal and interest.

Strong contracted revenue is not enough if the customer is weak or has broad termination rights. Diversified market revenue is not enough if pricing and utilization are unstable.

### Default state

After default, the following should be analyzed by state rather than simply added together:

- enforceable vendor and sponsor support;

- the assignable value of customer contracts or leases;

- revenue from re-leasing, redeployment, or equipment sale;

- dismantling, transport, porting, and requalification costs;

- downtime and legal-enforcement costs;

- the separate value of fixed-site assets.

Vendor support should not be added to recovery at its headline amount. Its value depends on triggers, duration, enforceability, valuation method, priority, and the support provider’s own credit risk.

### Expected loss

At an expert level, expected loss can be expressed heuristically as:

Where:

- PD is probability of default;

- LGD is loss given default;

- EAD is exposure at default.

The distinctive problem in AI-factory finance is that these variables may not be independent.

A decline in AI demand may raise the customer’s PD while simultaneously reducing rack remarketing values and increasing LGD. Immediately after rapid deployment, EAD may also be high. Broadcom’s structure—in which exposure rises with deployment and falls with customer payments—makes that time dimension visible.

## Variables to Verify

- Whether NVIDIA and the six financial institutions sign final platform agreements

- The amount of third-party capital actually committed, raised, and deployed

- Project-level debt spreads, LTVs, and maturities

- The precise denominator and legal form of NVIDIA’s residual-value support

- The relationship, if any, between NVIDIA’s existing facility guarantees and the new platforms

- Payment obligations, termination rights, and performance conditions under the Broadcom customer lease

- Claim, cure, and priority provisions of Broadcom’s backstop

- Loss allocation among Apollo, banks, Blackstone, and Broadcom

- The link between completion, performance acceptance, and commencement of customer payments

- Actual time required to re-lease or redeploy capacity after customer loss

- Porting, requalification, relocation costs, and utilization loss during redeployment

- Stressed secondhand prices and net recovery rates by hardware generation

- Availability of alternative sites with sufficient power, cooling, and networking

- Production-qualification time for major open-weight models across silicon architectures

- Customer, silicon, and regional power concentration within lender portfolios

## Open Questions

- Can standardized collateral valuation and an observable secondary market emerge for NVIDIA compute?

- Will vendor support remain a limited market-formation tool, or will silicon vendors increasingly retain customer-credit and technological-obsolescence risk?

- Can the cost-per-task advantage of Broadcom’s custom XPUs support contracts strong enough to compensate for lower redeployability?

- Will open weights deepen the pool of replacement customers faster than they weaken renewal rates for any one silicon architecture?

- Will the eventual financing standard be secured by a specific silicon asset, or by architecture-neutral contracted compute capacity?

- Does financing NVIDIA-based and Broadcom-based assets provide true technological diversification, or merely duplicate exposure to the same AI investment cycle?

## Reference

- https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx “NVIDIA Corporation - NVIDIA Partners With Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR to Establish AI Compute Infrastructure Financing Platforms to Mobilize Over $500 Billion of Third-Party Capital”

- https://www.bis.org/basel_framework/chapter/CRE/20.htm?utm_source=chatgpt.com “CRE20 - Standardised approach: individual exposures”

- https://www.linkedin.com/pulse/nvidia-ai-factory-compute-becoming-investable-asset-class-huang-4ju6c “NVIDIA AI Factory Compute Is Becoming an Investable Asset Class”

- https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm “nvda-20260125”

- https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm “nvda-20260426”

- https://investors.broadcom.com/news-releases/news-release-details/broadcom-apollo-and-blackstone-establish-landmark-strategic “Broadcom, Apollo, and Blackstone Establish Landmark Strategic Platform to Accelerate More Than 20 Gigawatts of Global AI Deployments | Broadcom Inc.”

- https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm “avgo-20260503”

- https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/ “Open Weights and American AI Leadership”
