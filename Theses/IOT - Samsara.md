---
date: 2026-04-15
tags: [thesis, enterprise-software, IoT, IOT, Samsara, connected-operations, physical-AI, data-flywheel]
status: active
conviction: medium
sector: Industrial IoT & Connected Operations
ticker: IOT
source: Vault research synthesis + web search (investor.samsara.com, G2, SaaStr, MIT News, IDC, Samsara Safety Report)
---

# IOT — Samsara

## Summary

$1.89B ARR (+30% YoY), 2M+ connected devices, $207M FCF — and the market prices Samsara as a fleet management company. Fleet management is the wedge, not the destination. Samsara's Connected Operations Cloud spans five product categories (telematics, AI video safety, equipment monitoring, site visibility, worker wearables), doing to physical operations what Salesforce did to sales. The moat is a self-reinforcing data flywheel: 25 trillion annual data points train AI models that improve with scale and cannot be replicated through capital investment alone. Founders Biswas and Bicket previously built Meraki (sold to Cisco for $1.2B, now Cisco's largest business unit) using an identical playbook. The profitability inflection (from -$191M to +$207M FCF in four years) confirms the business model is self-funding, but FY2027 guidance deceleration to 21-22% growth creates a potential entry window if the platform expansion thesis is correct.

---

## Key Non-consensus Insights

- **Samsara is not a fleet management company — it is building the operating system for the physical economy.** Five product categories with 95% of large customers using 2+ products and 69% using 3+. $1M+ ARR customers growing 56% YoY buy an expanding suite for construction sites, warehouse floors, and field operations. TAM is not $51B (fleet solutions) — it is $137B (connected operations).

- **A 10-20x technology spending gap between knowledge workers and frontline workers creates a multi-decade tailwind.** $5,000-10,000 annual SaaS spend per knowledge worker vs. $200-500 per frontline worker, despite physical operations representing >40% of global GDP. IDC-validated 815% average ROI, $2.02M average annual benefit. $1.89B ARR against $137B TAM = ~1.4% penetration.

- **The data flywheel is the durable moat, and Samsara's "Apple model" outcompetes Geotab's "Android model" in enterprise.** 25T annual data points train AI models that improve with scale. Geotab has more devices (4.6M) but its reseller model fragments data across partner ecosystems. Enterprise segment: 3,194 customers at $100K+ ARR (+37%), G2 99 vs. Geotab 56.2, 75B annual API calls embedding Samsara into external workflows.

- **Hardware-embedded 3-year contracts create physical switching costs pure SaaS cannot replicate.** Net retention 115-120% because customers expand, not churn. Samsara Wearable (September 2025) expands addressable units from ~30M US commercial vehicles to ~30M vehicles plus ~80M frontline workers. DHL, Werner, and City of New Orleans are early adopters.

- **The profitability inflection is structural proof, and the platform occupies a distinct layer complementary to Palantir and ServiceNow.** -$191M to +$207M FCF in four years — among the fastest SaaS profitability transitions in history. 30% growth with 21% FCF margins. Occupies a distinct "operational execution" layer (frontline safety, compliance, efficiency) complementary to [[Theses/PLTR - Palantir|Palantir]]'s strategic decision layer and [[Theses/NOW - ServiceNow|ServiceNow]]'s workflow governance.

---

## Outstanding Questions

1. **What is driving the FY2027 guidance deceleration from 30% to 21–22%?** Is this management conservatism (Samsara has beaten guidance every quarter), macro headwinds in physical operations spending, or genuine deceleration in net new customer acquisition? The answer determines whether the current stock price (~$29 vs $41+ analyst targets) is a buying opportunity or an appropriate discount.
2. **Can multi-product expansion sustain net retention above 115% as the base grows?** The 95% multi-product adoption among large customers is extraordinary, but it also means the easiest expansion opportunities are being consumed. Does Samsara have enough products in the pipeline (wearables, environmental compliance, AI-driven route optimization) to sustain expansion rates, or will NRR compress toward 110% as the installed base matures?
3. **International expansion trajectory** — At 85.6% US revenue, Samsara is unusually concentrated for a company of its scale. Management targets 18% international revenue (currently 14.4%). Can the US go-to-market model — direct sales, 3-year contracts, bundled hardware — translate to European and APAC markets where regulatory environments, fleet sizes, and buying behaviors differ?
4. **Wearable adoption curve** — Is the Samsara Wearable gaining traction? What is the per-unit economics (ARPU, gross margin, deployment friction)? Worker safety is the bull case for TAM expansion, but the product was only announced in September 2025.
5. **Insider selling cadence** — Biswas and Bicket plan to sell up to 5M shares each in 2026 under 10b5-1 plans, reducing combined ownership from ~34% to ~32.3%. This is routine founder diversification, but the cadence (~$3–7M per sale, multiple sales per month) creates persistent technical headwind. Does the selling pace increase or decrease?
6. **Competitive response from Motive** — Motive ($500M+ ARR, 120K+ customers) is Samsara's most direct rival, historically skewed toward smaller operators but clearly moving upmarket. If Motive achieves platform parity on AI safety and multi-product offerings, does Samsara's enterprise premium narrow?
7. **AI model differentiation sustainability** — As foundation models commoditize and open-source AI improves, can Samsara's proprietary AI models (trained on 25T data points) maintain differentiation, or will generic models applied to telematics data close the gap?

---

## Business Model & Product Description

Samsara's business model is "Salesforce for physical operations" — a cloud platform that digitizes the management of vehicles, equipment, sites, and workers through a hardware-embedded subscription model with structural switching costs. The Meraki playbook (co-founders Biswas and Bicket's previous company, sold to Cisco for $1.2B) is being re-executed against a vastly larger TAM: IoT hardware priced at or near cost serves as the on-ramp (77% Hardware-as-a-Service adoption), while the Connected Operations Cloud captures value through mandatory 3-year subscription contracts (98.1% subscription revenue). This creates a "razors and blades" dynamic where hardware installation physically embeds Samsara into customer operations — once gateways are installed in 500 vehicles and teams are trained on the platform, switching requires physically removing all devices, a disruption most enterprises will never undertake. Revenue per customer expands automatically: 95% of large customers use 2+ products, 69% use 3+, and net retention rates of 115-120% mean the installed base compounds without new sales. Revenue is 98.1% subscription across five integrated product categories:

### Fleet Telematics (Entry Wedge)

IoT vehicle gateways (plug into OBD-II/J1939 diagnostic port, install in minutes without professional technicians) providing:
- **Real-time GPS tracking and routing**: Live vehicle location, route history, geofencing, and AI-optimized route planning.
- **ELD compliance**: Electronic Logging Device functionality meeting the FMCSA mandate (Hours of Service recording, automated driver logs, roadside inspection mode).
- **DVIR (Driver Vehicle Inspection Reports)**: Digital pre-trip and post-trip inspections replacing paper workflows.
- **IFTA fuel tax reporting**: Automated fuel tax calculations based on GPS-tracked miles per jurisdiction.
- **Fuel management**: Fuel consumption monitoring, idle time tracking, and efficiency benchmarking.
- **Diagnostics**: Real-time engine fault code monitoring and maintenance alerts.

Hardware-as-a-Service model (77% adoption) bundles device costs into subscription pricing, minimizing upfront adoption friction — the same playbook founders Biswas and Bicket used at Meraki.

### AI Video-Based Safety

Dual-facing dash cameras (road-facing and driver-facing) powered by proprietary AI models:
- **Real-time unsafe behavior detection**: Distracted driving (phone use, eating), drowsiness, tailgating, rolling stops, lane departure, forward collision warnings.
- **Safety Coach**: Automated coaching workflow that detects incidents → generates coaching sessions with video evidence → delivers to fleet managers → tracks driver improvement over time. Evolving from analytical (flagging) toward agentic (autonomous intervention).
- **StreetSense**: Network-level intelligence combining footage from nearby Samsara-connected vehicles on the same network for enhanced incident reconstruction and context.
- **Collision detection and reconstruction**: Automatic crash detection with full video recording, G-force data, and incident reporting for insurance and liability.

IDC-validated ROI: full-suite adopters achieve 75% crash reduction over 30 months. NHTSA estimates commercial vehicle crashes cost $180B annually — the safety proposition pays for itself many times over.

### Equipment Monitoring

IoT sensors and gateways for non-vehicle physical assets:
- **Powered equipment**: Construction machinery (excavators, loaders, cranes), generators, pumps, compressors — tracking utilization, engine hours, fuel consumption, and GPS location.
- **Unpowered assets**: Trailers, containers, scaffolding, toolboxes — tracking location and movement.
- **Predictive maintenance**: AI analysis of equipment operating data (vibration, temperature, engine patterns) to predict failures before they occur, reducing unplanned downtime.
- **Utilization optimization**: Identifying underutilized assets across job sites to improve fleet efficiency and inform purchase/rental decisions.

### Site Visibility

Fixed cameras and environmental sensors for stationary locations:
- **Construction sites**: Real-time monitoring of site activity, progress tracking, unauthorized access detection, equipment movement.
- **Warehouses and yards**: Dock door monitoring, trailer tracking, yard management.
- **Environmental monitoring**: Temperature, humidity, and door-open sensors for cold chain compliance (food, pharmaceuticals), hazardous material storage, and environmental regulation.
- **Security**: Motion detection, time-lapse site documentation, and remote visual management.

### Worker Safety — Wearables (Launched September 2025)

Wearable devices extending the Connected Operations Cloud to frontline workers outside of vehicles:
- **Worker location tracking**: Real-time positioning on construction sites, warehouse floors, and field operations.
- **Environmental hazard monitoring**: Exposure to heat, noise, gas, and other occupational hazards.
- **Incident detection**: Fall detection, impact alerts, and man-down alarms.
- **Safety compliance**: Verification that workers are in designated safe zones, wearing required PPE, and following site protocols.

This product fundamentally expands the addressable unit count from ~30M US commercial vehicles to ~30M vehicles PLUS ~80M frontline workers. Early adopters: DHL, Werner Enterprises, City of New Orleans.

### Platform Layer (Cross-Product)

- **Weather Intelligence**: Real-time weather data integrated into fleet routing, safety risk assessment, and operational planning decisions.
- **Automated Coaching**: End-to-end AI-driven workflow from incident detection through coaching delivery to outcome tracking, operating without manual manager intervention.
- **API Platform**: 75B annual API calls enabling integration with ERP systems, TMS (transportation management systems), insurance providers, and operational partners (e.g., [[Theses/DE - John Deere|John Deere]] Operations Center). Open platform architecture ensures Samsara functions as the operational data layer feeding enterprise systems.
- **Reporting and analytics**: Customizable dashboards, benchmarking across the anonymized network, and operational KPI tracking.

### Key Platform Metrics

$1.89B ARR (+30% YoY), 2M+ connected devices generating 25T annual data points, 3,194 enterprise customers at $100K+ ARR (+37% YoY), $1M+ ARR cohort growing 56% YoY. 95% of large customers use 2+ products, 69% use 3+. NPS 75.6 (12-44 points above all competitors). Customer base spans transportation, construction, oil & gas, waste management, agriculture, food & beverage, government/municipal, and field services.

---

## Industry Context

### The Physical Operations Digitization Gap

The most important structural context for understanding Samsara is the *technology spending disparity* between knowledge workers and frontline workers. A typical enterprise spends $5,000–10,000 annually on SaaS tools per knowledge worker (CRM, ITSM, collaboration, analytics). The equivalent spend per frontline worker — truck driver, construction worker, warehouse associate, field technician — is $200–500. This 10–20x gap exists despite physical operations representing >40% of global GDP and employing the majority of the global workforce.

The gap exists not because the ROI isn't there — Samsara's IDC-validated data shows 815% average ROI and $2.02M average annual benefit per customer — but because the *technology didn't exist*. Legacy telematics and fleet management systems were expensive, difficult to install (professional installation required), fragmented (separate vendors for GPS, cameras, ELD compliance, fuel management), and lacked the AI/cloud capabilities to generate actionable insights from operational data. Samsara, Motive, and Geotab represent the first generation of cloud-native platforms purpose-built for this market. The physical operations digitization wave is structurally 15–20 years behind the knowledge worker SaaS wave, which means the adoption S-curve is still in early innings.

### Competitive Landscape

The physical operations platform market has consolidated around three meaningful competitors, each with a distinct strategic approach:

**Samsara (IOT)** — Vertically integrated "Apple model." Own hardware, own software, own data, direct sales. $1.89B ARR, 2M+ devices, 3,194 enterprise customers ($100K+ ARR). Strongest AI/platform capabilities, highest G2 scores (99 avg), highest NPS (75.6). 3-year mandatory contracts with bundled hardware. Weakness: smaller installed base than Geotab, higher price point, limited international footprint (14.4%).

**Geotab** — Open-platform "Android model." Hardware-agnostic, distributed through vast reseller network. 4.6M+ connected vehicles — largest installed base globally. ABI Research ranks #1 overall. Strength in mid-market and SMB through partner channel. Weakness: fragmented data (partners control customer relationships), lower customer satisfaction scores (G2: 56.2, customer sat: 76% vs Samsara's 84%), less integrated platform experience.

**Motive** — Direct competitor most similar to Samsara. $500M+ ARR, 120K+ customers. Historically strongest in trucking/SMB segment, now moving upmarket with AI Safety features. G2 score of 97.2 (close to Samsara's 99). Most credible competitive threat to Samsara's enterprise positioning because it combines similar platform ambition with a larger customer base in the mid-market.

**Legacy/fragmented players** — Verizon Connect (G2: 39.6), Lytx (G2: 62.6), Omnitracs, and dozens of point solutions. Losing share to platform players. The consolidation dynamic favors Samsara and Motive, who offer integrated platforms that replace 3–5 point solutions.

### The Meraki Precedent

Samsara's founders previously built Meraki (2006–2012), which applied a then-radical insight to enterprise networking: managed infrastructure hardware (routers, switches, access points) could be cloud-managed, radically simplifying deployment and administration. Cisco acquired Meraki for $1.2B in 2012. As of 2026, Cisco Meraki is Cisco's largest business unit by revenue and one of the most successful enterprise technology acquisitions in history.

The Meraki playbook has specific structural elements that Samsara replicates:
- **Hardware as on-ramp, cloud as value capture**: Meraki priced hardware accessibly and captured value through cloud management subscriptions. Samsara prices IoT hardware at or near cost (77% HaaS adoption) and captures value through the Connected Operations Cloud (98.1% subscription revenue).
- **Radical deployment simplicity**: Meraki access points self-configured via the cloud; Samsara vehicle gateways plug into diagnostic ports and install in minutes.
- **Direct sales in enterprise, self-serve in SMB**: Meraki built a direct enterprise sales force while offering self-serve for smaller customers. Samsara's direct sales force targets $100K+ ARR enterprises while mid-market customers can onboard more efficiently.
- **Platform expansion over time**: Meraki expanded from wireless to switching, security cameras, and MDM. Samsara expanded from fleet telematics to video safety, equipment monitoring, site visibility, and worker wearables.

The founders are not inventing a new playbook — they are executing a proven one against a market that is orders of magnitude larger.

### Safety as Regulatory and Economic Tailwind

Safety is both the primary customer value proposition and a regulatory tailwind. The FMCSA ELD mandate (2017, full enforcement 2019) required electronic logging devices in all commercial vehicles, creating a compliance floor that drove initial telematics adoption. Samsara's platform exceeds compliance — it uses AI to predict and prevent safety incidents. The economic case is compelling: the NHTSA estimates commercial vehicle crashes cost the US economy $180B annually. Samsara's data shows full-suite adopters achieve 75% crash reduction over 30 months, creating massive insurance, liability, and workers' compensation savings. This is not discretionary technology spending — it is risk management infrastructure that pays for itself many times over.

---

## Key Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Stock Price | ~$29–32 | Down ~40% from 52-wk highs |
| Market Cap | ~$16.8B | |
| FY2026 ARR | $1.89B | +30% YoY |
| FY2026 Revenue | $1.6B | +30% YoY |
| Q4 FY2026 Revenue | $444.3M | +28% YoY |
| FY2027 Revenue Guidance | $1.965–1.975B | +21–22% YoY (deceleration) |
| FY2026 FCF | $207M | 21% adjusted margin |
| GAAP EPS (Q4 FY2026) | $0.04 | Second consecutive GAAP-profitable quarter |
| $100K+ ARR Customers | 3,194 | +37% YoY |
| $100K+ ARR Contribution | $1.2B | 63% of total ARR |
| $1M+ ARR Customers | Growing 56% YoY | Highest-value segment accelerating |
| Net Retention Rate | 115% core / 120% large | |
| NPS | 75.6 | 12–44 points above competitors |
| G2 Score | 99 avg | vs Motive 97.2, Geotab 56.2 |
| Connected Devices | 2M+ | Generating 25T annual data points |
| API Calls | 75B annually | Platform extensibility proof |
| Multi-product Adoption | 95% (2+ products) | 69% use 3+ |
| Subscription % of Revenue | 98.1% | |
| US Revenue Share | 85.6% | International: 14.4% |
| Founder Ownership | ~32–34% combined | Biswas + Bicket |
| Analyst Consensus | Strong Buy (18 Buy / 5 Hold) | Avg target ~$41–44 |

---

## Bull Case

- **Platform expansion proves the "fleet management" label wrong**: Wearables, site visibility, and equipment monitoring drive multi-product adoption beyond the current 95% penetration. Samsara's $100K+ ARR customer count continues growing 35%+ as enterprises consolidate fragmented point solutions onto a single platform. NRR holds above 115% as new product categories provide fresh expansion vectors.
- **Data flywheel accelerates with AI advancement**: As AI models improve, the value extracted per data point increases — better predictions, more automated coaching, more accurate risk scoring. Samsara's 25T data point dataset becomes *more* valuable over time, not less. The AI Safety Coach evolves from analytical (flagging incidents) to agentic (autonomously intervening in workflows), deepening the platform's operational criticality.
- **International expansion unlocks the next growth phase**: 85.6% US concentration is a growth constraint *and* a massive opportunity. If international scales from 14.4% to 25%+ of revenue, it adds $400M+ in incremental ARR without saturating the US market. UK, France, Mexico, and a Bengaluru R&D hub signal the geographic expansion is underway.
- **Physical operations digitization wave follows the knowledge worker SaaS trajectory**: If per-worker technology spending in physical operations converges even partially toward knowledge worker levels ($200–500 → $1,000–2,000), the TAM doubles. Samsara's ~1.4% TAM penetration ($1.89B vs $137B) provides decades of compounding runway.
- **Self-funding growth engine enables aggressive investment**: With $207M FCF and growing, Samsara can invest heavily in R&D (AI, wearables, international) without dilution. The profitability inflection removes the "running out of cash" risk that caps many high-growth SaaS companies.
- **Founder-led execution continuity**: Biswas and Bicket's 32–34% combined ownership and prior Meraki success ($1.2B exit → Cisco's largest business unit) provide strategic continuity and aligned incentives. The "founder premium" is empirically justified: founder-led companies outperform professional-manager-led companies in long-term value creation.

## Bear Case

- **Growth deceleration is structural, not conservative guidance**: FY2027 guidance of 21–22% represents a meaningful step-down from 30% in FY2026. If growth continues decelerating toward 15–18% by FY2028, the growth premium in the valuation compresses severely. At 10x forward revenue and decelerating growth, the stock could trade flat or down for an extended period.
- **Motive closes the platform gap**: Motive ($500M+ ARR, 120K+ customers) is investing heavily in AI safety, multi-product expansion, and upmarket sales. If Motive achieves platform parity on AI capabilities and enterprise features, Samsara's premium positioning narrows, potentially compressing win rates and ASPs. Motive's G2 score of 97.2 (vs Samsara's 99) shows the gap is already narrow on customer satisfaction.
- **Hardware dependency creates margin headwinds**: Unlike pure SaaS companies, Samsara must manufacture, distribute, and install physical hardware. This creates logistics complexity, inventory risk, and gross margin pressure during hardware refreshes. The 77% HaaS adoption model defers hardware revenue recognition, but the capital intensity is real.
- **Insider selling creates persistent technical headwind**: Biswas and Bicket selling up to 10M combined shares in 2026 (~$290–320M at current prices) is routine founder diversification but creates steady supply pressure on a stock already 40% off highs.
- **Enterprise concentration risk**: 63% of ARR from $100K+ ARR customers means a small number of large customer losses would be material. The 3-year contract structure provides protection, but contract renewals become cliff events if competitors offer compelling alternatives.
- **International expansion may not transfer**: The US go-to-market model (direct sales, 3-year mandatory contracts, bundled hardware) may face friction in European markets with different regulatory regimes, data privacy requirements (GDPR), and purchasing norms. The Bengaluru R&D hub is a cost center, not a revenue driver.

---

## Catalysts

- **Q1 FY2027 earnings (June 2026)** — First quarter under new guidance framework. Will actual results beat the 21–22% revenue growth guide (as Samsara has historically beaten)? Any guidance raise would signal the deceleration is less severe than feared.
- **Wearable adoption metrics** — First quantitative disclosure on wearable device shipments, customer adoption, and unit economics. Worker safety is the key TAM expansion thesis — the market needs data to price it.
- **International revenue milestone** — Crossing 18% international revenue (management target) would validate the geographic expansion playbook and signal a second growth engine beyond the US.
- **$1M+ ARR customer milestones** — This fastest-growing cohort (56% YoY) is the leading indicator of platform vs. point-solution positioning. Continued acceleration validates the "system of record" thesis.
- **Strategic partnership or integration announcement** — A formal integration with Palantir, ServiceNow, or a major ERP vendor would validate the "operational data layer" positioning and expand the addressable enterprise market.
- **AI regulatory tailwinds** — FMCSA or OSHA mandating AI-powered safety monitoring (dash cams, driver coaching) would create a compliance-driven adoption wave, similar to the ELD mandate's effect on telematics.
- **Competitive M&A** — If Geotab or Motive is acquired by a larger platform company (Cisco, Microsoft, Salesforce), it would both validate the market and potentially create integration disruption that benefits Samsara.

---

## Risks

1. **Growth deceleration**: FY2027 guidance of 21–22% is a meaningful step-down from 30%. If this reflects genuine market maturation rather than conservative guidance, the growth premium in the valuation compresses. The stock at ~$29 vs $41+ analyst targets already reflects some deceleration concern — the risk is that consensus targets come down rather than the stock rising to meet them.
2. **Competitive convergence**: Motive's platform ambition and Geotab's installed base scale could compress Samsara's differentiation over time. The G2 gap (99 vs 97.2 for Motive) is narrow. If Motive achieves AI parity and moves upmarket effectively, Samsara's enterprise win rates could decline.
3. **Geographic concentration**: 85.6% US revenue creates single-market risk. A US recession, trucking downturn, or regulatory change impacting fleet spending would disproportionately affect Samsara vs. globally diversified competitors.
4. **Hardware obsolescence and refresh cycles**: IoT hardware has finite lifespans and requires periodic replacement. If technology cycles accelerate (new sensor types, connectivity standards), Samsara faces both capex for device refresh and customer friction during transitions.
5. **AI commoditization**: If open-source AI models become capable of processing telematics and video data at quality levels approaching Samsara's proprietary models, the AI differentiation layer erodes. The data moat (25T data points) provides protection, but the model layer is increasingly contestable.
6. **Founder transition risk**: Biswas and Bicket's gradual share sales (10M shares planned for 2026) are routine, but signal the beginning of founder transition planning. The "founder premium" is real — Meraki's success under Cisco ownership is the positive precedent, but eventual leadership transition creates uncertainty.
7. **Macro sensitivity**: Physical operations spending is tied to freight volumes, construction activity, and industrial production. A prolonged economic slowdown could extend sales cycles, reduce fleet sizes, and compress expansion rates — even if the long-term digitization thesis remains intact.

---

## Related Research

- [[Research/2026-04-15 - IOT - Samsara Business Deep Dive]] — $1.9B ARR, 2M+ devices, 25T data points, platform architecture, competitive positioning vs Geotab
- [[Theses/PLTR - Palantir]] — Adjacent operational intelligence thesis (strategic layer vs Samsara's operational execution layer)
- [[Theses/NOW - ServiceNow]] — Adjacent workflow automation thesis (IT/business process layer vs Samsara's physical operations layer)
- [[Theses/DE - John Deere]] — Samsara integration partner via Operations Center; overlapping physical operations / precision ag thesis
- [[@Industrial IoT & Connected Operations]] — Sector Note

---

## Log

### 2026-04-15
- [Thesis created]: Built from vault research + web search. Framing: Samsara as physical operations system-of-record mispriced as fleet mgmt. Q4 FY2026 integrated ($444.3M rev, $1.89B ARR, FY2027 guide $1.97B). Conviction medium — strong moat offset by growth deceleration and Motive convergence.

### 2026-04-15 (cross-thesis sync)
- [Deere cross-ref]: DE's Operations Center (500M+ acres) validates physical operations TAM; construction segment ($11.65B) overlaps Samsara's vertical. Deere's 10% recurring revenue target by 2030 validates subscription model — conviction unchanged.

### 2026-04-22
- Sector re-scoped: Enterprise Software → Industrial IoT & Connected Operations (vault-wide subsector taxonomy reorganization).
- Wikilink cleanup: Related Research `[[Sectors/Enterprise Software]]` → `[[Sectors/Industrial IoT & Connected Operations]]` (sector note body-filled 2026-04-22).
