---
date: 2025-11-27
tags: [research, semiconductors, HBM, memory]
status: active
sector: Semiconductors
source: ChatGPT conversation export
source_type: deep-dive
---
# HBM4 Breakthroughs and Yields

HBM4 is only just moving from samples into early production, so public data—especially on yields—is sparse and often indirect. Below is a synthesis of what is reasonably grounded in public sources plus an explicit, modelled revenue / share scenario.

---

## 1. HBM4 status and yields by vendor (late 2025)

### Technology baseline

- JEDEC’s HBM4 standard (JESD238) was finalized in April 2025. It targets up to ~2 TB/s per stack, higher capacities (up to 64 GB/stack) and major power‑efficiency gains vs HBM3E.citeturn0search9turn0search13  
- All three major suppliers (SK hynix, Samsung, Micron) are converging on 24 Gb DRAM dies, 12‑Hi and 16‑Hi stacks, and custom logic/base dies on advanced foundry nodes (TSMC 12FFC+/N5, Samsung 4 nm).citeturn8search2turn1search1  
- Industry roadmaps place HBM4 mass production in 2026, with HBM4E‑class parts becoming the dominant HBM generation around 2027–2028.citeturn5view0turn3news42  

#### A note on “yields”

Reported “yields” can mean:

- Front‑end DRAM die yield (per wafer)  
- Logic/base‑die yield  
- Final stacked HBM yield (all dies + TSV + packaging)

Stack yields are much lower than individual die yields; for example, one analysis shows that 95 % per‑die yield can still drop to ~44 % final yield on 16‑Hi stacks.citeturn6search6

---

### SK hynix

Position: Clear HBM leader, already into HBM4 production ramp.

Key HBM4 breakthroughs

- Announced completion of HBM4 development in 2025; specs include up to 10 Gb/s per pin and ≈40 % better power efficiency than HBM3E.citeturn3search10turn1search3  
- Shipped HBM4 samples from March 2025, completed internal certification, and is preparing full mass production; major supplier to NVIDIA.citeturn3news42turn1news41  
- Roadmap (2026‑2028) adds 16‑Hi HBM4 and multiple HBM4E variants (8/12/16‑Hi), including custom base‑die designs that integrate the memory controller to free GPU area and cut interface power.citeturn8search14  

Yields (publicly visible signals)

- For HBM3E, SK hynix has reported production yields around 80 %, enabled by its MR‑MUF (Mass Reflow Molded Underfill) stacking process, explicitly framed as paving the way for HBM4 scalability.citeturn2search14  
- SK hynix’s 1c‑node DRAM (for future HBM4E) has been reported with test yields averaging >80 % and up to 90 % on some lots; HBM4 itself initially uses the more mature 1b node.citeturn2search3turn2search8  
- Analysts and press commentary consistently state that SK hynix enjoys the best effective HBM yields among the big three (HBM is “margin‑accretive” for SK hynix), while Samsung’s are notably worse.citeturn6search14turn2search8  

Take‑away: SK hynix enters HBM4 with mature packaging, strong HBM3E yields, and first‑to‑market status. It is widely expected to retain the largest HBM4 share through at least 2027–2028.citeturn3news42turn2news41  

---

### Samsung

Position: Very large DRAM maker, but playing catch‑up in HBM yields and NVIDIA qualification.

Key HBM4 breakthroughs

- Samsung is delivering HBM4 samples to NVIDIA (Nov 2025) and aims for early‑2026 validation; volume production is targeted to align with next‑gen GPUs.citeturn1search4turn2search4turn1search0  
- Uses 1c‑node DRAM and a 4 nm logic/base die for HBM4, enabling tight integration and leveraging its foundry for custom logic dies.citeturn2search13turn2search5turn8search2  
- Reported to have significantly improved its AI‑memory competitiveness in 2025, with aggressive expansion plans for HBM3E and HBM4 capacity as AI demand continues to exceed supply.citeturn6news41turn1search2  

Yields

- 1c DRAM used for HBM4 reportedly has sample yields around 50 % for HBM4 dies, with DDR5 yields above 70 %. Industry sources say Samsung wants ≈70 % HBM4 wafer yield before full mass production.citeturn2search5turn2search9turn2search3  
- Samsung’s 4 nm HBM4 logic die reportedly exceeds 90 % yield, indicating the front‑end logic is not the bottleneck.citeturn2search13  
- Earlier, Samsung’s HBM3/HBM3E struggled to pass NVIDIA’s tests due to heat and power issues, highlighting that its effective stack yields and system‑level performance lagged SK hynix through 2024; that gap appears to be narrowing in late 2025.citeturn2search0turn2search4turn1search9  

Take‑away: Samsung’s HBM4 technology is competitive on paper, but effective yields and customer qualifications have trailed SK hynix. The trajectory in 2025 suggests improving yields, with room for share gains once HBM4 is in full volume.

---

### Micron

Position: Late to HBM3, now very aggressive on HBM3E and HBM4; strong with NVIDIA on HBM3E and positioning HBM4E for 2027.

Key HBM4 breakthroughs

- Micron announced shipment of HBM4 samples in mid‑2025: 2048‑bit interface, >2.0 TB/s bandwidth per stack, >60 % better performance vs its prior HBM, targeting next‑gen AI platforms.citeturn1search5turn6news40  
- Follow‑up disclosures and roadmaps show pin speeds above 11 Gb/s and bandwidth up to ≈2.8 TB/s per stack, exceeding the JEDEC baseline.citeturn1search1turn6search1turn6search5  
- Micron’s HBM4E (2027) will use custom base‑logic dies fabricated by TSMC, enabling customer‑specific variants with higher gross margins.citeturn5view0turn6search5turn6search8  

Yields

- Multiple analyses (SemiAnalysis, investor notes) characterize Micron’s HBM3E yields as competitive with or better than SK hynix and materially ahead of Samsung, enough that HBM is “margin‑accretive” despite lower absolute yields than commodity DRAM.citeturn6search14turn6search3  
- There are reports that Micron has had to redesign parts of its HBM4 due to yield/performance issues, potentially pushing some volume out toward 2027; this is framed as a temporary setback rather than a structural disadvantage.citeturn6search0turn6search13  
- No hard HBM4 yield numbers have been disclosed; based on HBM3E experience, it is reasonable to assume Micron aims for effective stack yields in the 50–70 % range once HBM4 is fully ramped.

Take‑away: Micron appears technologically competitive (fastest advertised HBM4 bandwidth today), but its HBM4 ramp is likely a bit later than SK hynix and Samsung. Its share gains are more visible in HBM3E, with HBM4/4E becoming a larger revenue driver from 2027 onward.

---

### Chinese vendors (CXMT, YMTC, Huawei ecosystem)

There are no public indications that any Chinese vendor will mass‑produce JEDEC‑compliant HBM4 in the 2026–2027 timeframe. Current efforts are focused on HBM3/HBM3E‑equivalent tech and in‑house/custom HBM for domestic AI accelerators.

Key points

- CXMT plans mass production of HBM3 around 2026 using MR‑MUF packaging, explicitly following SK hynix’s process, and is targeting HBM3E around 2027; it remains ~3–4 years behind the leaders.citeturn3search0turn3search6turn3search7  
- YMTC (primarily a NAND maker) is entering DRAM and HBM, developing TSV‑based stacking and exploring partnership with CXMT for HBM.citeturn3search3turn3search4turn0search15  
- Huawei has announced its own HiBL 1.0 HBM for the Ascend 950PR (2026), claiming 128 GB and up to 1.6 TB/s bandwidth and saying it is more cost‑effective than industry HBM3E/HBM4E; a second‑gen “HiZQ 2.0” is planned with 144 GB and up to 4 TB/s.citeturn3search2turn3search5turn3search8turn8search3turn8search15  
- Export controls on advanced tools and packaging are visibly constraining YMTC and other Chinese memory vendors; yields on leading‑edge products made with domestic tools are widely reported to be lower than international peers.citeturn8news40turn3search4  

Take‑away: Chinese players are unlikely to have material global HBM4 share before ~2028+, though they may play a growing role in the domestic China AI stack (Huawei Ascend, etc.). Their first volume products are more realistically HBM3/HBM3E‑class.

---

## 2. Expected revenue contribution and market share for HBM4

Because HBM4 is just ramping, any forward view has to be scenario‑based. The charts I generated above use a scenario primarily consistent with Yole Group’s aggressive HBM forecasts and TrendForce’s HBM4E adoption timeline.

### 2.1 Global HBM vs HBM4 revenue – scenario

Several recent forecasts:

- Some market studies put HBM revenue at only ~US$2.5–3 B in 2024, reaching ~US$5–6 B by 2030 (very conservative).citeturn0search2turn4search11turn0search14  
- Yole‑based work cited by multiple outlets instead projects HBM revenue growing from about US$17 B in 2024 to roughly US$98 B by 2030, a ~33 % CAGR.citeturn4search1turn4search3turn4search10turn4search12  

The table and plots here assume the *higher* Yole‑style trajectory:

| Year | Total HBM revenue (B$) | HBM4 family share of HBM | HBM4 revenue (B$) |
|------|------------------------|--------------------------|-------------------|
| 2024 | 17.0 | 0 % | 0.0 |
| 2025 | 34.0 | 0 % | 0.0 |
| 2026 | 42.0 | 15 % | 6.3 |
| 2027 | 51.9 | 60 % | 31.2 |
| 2028 | 64.2 | 80 % | 51.3 |
| 2029 | 79.3 | 90 % | 71.4 |
| 2030 | 98.0 | 95 % | 93.1 |

Assumptions:

- HBM4 (including HBM4E) begins meaningful volume in 2026, consistent with SK hynix and Samsung roadmaps.citeturn3news42turn1news41turn5view0  
- TrendForce’s estimate that HBM4E alone is ~40 % of HBM demand by 2027 implies that HBM4 + HBM4E together dominate (>60 %) from 2027 onward.citeturn5view0  

If instead you adopt the more conservative “HBM ~US$6 B in 2030” forecasts, you can roughly divide all HBM4 revenue numbers above by ~15–16; the vendor *shares* below would be similar, but absolute dollars far smaller.

---

### 2.2 Vendor‑level HBM4 revenue and share – scenario

The two plots I generated show:

1. HBM4 revenue by vendor (2026–2030)  
2. HBM4 market share by vendor (2026–2030)

The underlying numerical scenario (USD billions):

| Year | HBM4 total | SK hynix | Samsung | Micron | China‑based vendors |
|------|------------|----------|---------|--------|---------------------|
| 2026 | 6.3 | 3.18 | 1.56 | 1.50 | 0.06 |
| 2027 | 31.2 | 15.27 | 7.63 | 7.63 | 0.62 |
| 2028 | 51.3 | 23.41 | 13.45 | 12.95 | 1.54 |
| 2029 | 71.4 | 30.15 | 19.18 | 19.18 | 2.85 |
| 2030 | 93.1 | 37.15 | 26.53 | 24.76 | 4.66 |

Implied HBM4 market‑share paths:

- 2026: SK hynix ≈50 %, Samsung ≈25 %, Micron ≈24 %, China ≈1 %  
- 2027: SK hynix ≈49 %, Samsung ≈24.5 %, Micron ≈24.5 %, China ≈2 %  
- 2028: SK hynix ≈46 %, Samsung ≈26 %, Micron ≈25 %, China ≈3 %  
- 2029: SK hynix ≈42 %, Samsung ≈27 %, Micron ≈27 %, China ≈4 %  
- 2030: SK hynix ≈40 %, Samsung ≈28.5 %, Micron ≈26.5 %, China ≈5 %  

How this was constructed:

- 2025–2026 share anchors come from published HBM share data and a Deutsche Bank forecast: SK hynix 62 % of HBM in Q2‑25, Micron overtaking Samsung; 2026 HBM forecast: SK hynix 51 %, Samsung 25 %, Micron 24 %.citeturn2search1turn1search3turn1search9turn0search12  
- From 2027 onward, I slowly converge toward a somewhat more balanced market while keeping SK hynix as leader, reflecting Micron’s more competitive roadmap and Samsung’s catch‑up, but no data today suggests SK hynix’s dominance collapses.citeturn1search1turn2news41turn6news40turn6news41  
- Chinese vendors remain constrained to low‑single‑digit global share through 2030 due to sanctions, lagging process technology, and a mainly domestic customer base.citeturn3search0turn3search6turn3search7turn3search4turn8news40  

---

### 2.3 Revenue contribution relative to DRAM businesses

- Yole projects HBM’s share of DRAM revenue rising from ~18 % in 2024 to >50 % by 2030.citeturn4search1turn8search5turn4search3  
- SK hynix has already disclosed that HBM accounts for roughly 40 % of its DRAM revenue as of late 2024/early 2025, and plans to double HBM sales again, implying HBM4 will be the *single largest* product line in its DRAM portfolio by the late 2020s.citeturn2news40turn2news41turn8search12  
- Under the high‑growth scenario above, by 2030 HBM4 alone could represent on the order of:
  - SK hynix: ≈US$35–40 B/year  
  - Samsung: ≈US$25–27 B/year  
  - Micron: ≈US$25 B/year  
  which would make HBM4 the dominant profit engine for all three memory vendors.

---

### How to interpret this

- The *direction* is robust:  
  - HBM4/HBM4E becomes the dominant HBM generation by 2027–2028.  
  - HBM itself grows from a niche to a very large part of the DRAM market (approaching ~50 % of DRAM revenue by 2030 in aggressive scenarios).  
  - SK hynix stays in the lead, but Samsung and Micron both gain share vs their HBM3E positions.  
  - Chinese vendors grow but remain small globally through 2030.

- The *absolute dollar values* are highly uncertain; published 2030 HBM revenue forecasts span roughly an order of magnitude. If you want a conservative range, scale all absolute numbers above down by a factor of ~3–5 while keeping the share structure.

---

navlistSelected recent HBM4 / HBM market sourcesturn3news42,turn1search5,turn1search1,turn5view0,turn4search1,turn4search3,turn2news41,turn3search0,turn3search4,turn8news40

---

import matplotlib.pyplot as plt
import pandas as pd

# Scenario data (USD billions), based primarily on Yole Group / Yole-cited forecasts for total HBM
years = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
total_hbm = [17.0, 34.0, 42.0, 51.9, 64.2, 79.3, 98.0]  # total HBM market
hbm4_total = [0.0, 0.0, 6.3, 31.16, 51.34, 71.37, 93.1]  # HBM4 + HBM4E family (scenario)

# Vendor-level HBM4 revenue (scenario) in USD billions
skh =   [0.0, 0.0, 3.18, 15.27, 23.41, 30.15, 37.15]
samsung = [0.0, 0.0, 1.56, 7.63, 13.45, 19.18, 26.53]
micron =  [0.0, 0.0, 1.50, 7.63, 12.95, 19.18, 24.76]
china =   [0.0, 0.0, 0.06, 0.62, 1.54, 2.85, 4.66]

df = pd.DataFrame({
    "Year": years,
    "Total_HBM": total_hbm,
    "HBM4_total": hbm4_total,
    "HBM4_SK_hynix": skh,
    "HBM4_Samsung": samsung,
    "HBM4_Micron": micron,
    "HBM4_China": china,
})

# Filter for years where HBM4 meaningfully exists
df_hbm4 = df[df["Year"] >= 2026].copy()

# Plot 1: HBM4 revenue by vendor
plt.figure()
plt.plot(df_hbm4["Year"], df_hbm4["HBM4_SK_hynix"], marker="o", label="SK hynix")
plt.plot(df_hbm4["Year"], df_hbm4["HBM4_Samsung"], marker="o", label="Samsung")
plt.plot(df_hbm4["Year"], df_hbm4["HBM4_Micron"], marker="o", label="Micron")
plt.plot(df_hbm4["Year"], df_hbm4["HBM4_China"], marker="o", label="China-based vendors")
plt.xlabel("Year")
plt.ylabel("HBM4 revenue (USD billions)")
plt.title("Scenario: HBM4 / HBM4E Revenue by Vendor")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: HBM4 market share by vendor
for vendor in ["HBM4_SK_hynix", "HBM4_Samsung", "HBM4_Micron", "HBM4_China"]:
    df_hbm4[vendor.replace("HBM4_", "") + "_share"] = df_hbm4[vendor] / df_hbm4["HBM4_total"] * 100

plt.figure()
plt.plot(df_hbm4["Year"], df_hbm4["SK_hynix_share"], marker="o", label="SK hynix")
plt.plot(df_hbm4["Year"], df_hbm4["Samsung_share"], marker="o", label="Samsung")
plt.plot(df_hbm4["Year"], df_hbm4["Micron_share"], marker="o", label="Micron")
plt.plot(df_hbm4["Year"], df_hbm4["China_share"], marker="o", label="China-based vendors")
plt.xlabel("Year")
plt.ylabel("HBM4 market share (%)")
plt.title("Scenario: HBM4 / HBM4E Market Share by Vendor")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

df
```

## Related Sectors
- [[Sectors/GPU & AI Compute Accelerators]] — Back-reference: cited in sector fill under Macro shifts (HBM4 supply pivot — SK Hynix ~62% share, Samsung ~50% yield targeting 70% before mass production, Micron 2026 sold out; 16-Hi stack yields gate Rubin/MI450 production volume) and Key industry questions (HBM4 integration for Vera Rubin is the binding constraint on 2026 Nvidia volume).