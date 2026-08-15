---
publish: false
date: 2026-08-12
tags: [research, email-backfill, IrrationalAnalysis]
source: 'https://irrationalanalysis.substack.com/p/lumentum-q4-fy26-earnings'
source_type: web-clip
sender: irrationalanalysis@substack.com
---

# Lumentum Q4 FY26 Earnings

- Irrational Analysis is heavily invested in the semiconductor industry.Positions will change over time and are regularly updated.

- Opinions are authors own and do not represent past, present, and/or future employers.

- All content published on this newsletter is based on public information and independent research conducted since 2011.

- This newsletter is not financial advice and readers should always do their own research before investing in any security.

- Feel free to contact me via email at: irrational_analysis@proton.me

There is a huge amount of alpha on the Lumentum earnings call that was not explained well by management.

To do this properly, let me break out the InP model again.

Suppose you have a ring-modulated, single-wavelength PIC design that expects the laser source to be split 6 times before hitting the rings.

To close the link, you need around 2 mW of power entering each ring.

Your two options are:

- Place lasers in an external module. (ELSFP/ELS)

- Integrate the lasers directly into the optical engine assembly.

The external option requires 400mW lasers while the internal option can run with 250 mW lasers. We know that…

- InP/lasers are in a critical supply crunch.

- The area efficiency (light per unit area of InP) for 400mW lasers is 65% when compared to 250mW lasers. (more power per laser =  less area efficient)

So why has everyone been so focused on the high-power stuff? The answer is with regards to reliability in terms of mode hopping (laser unstable and flicker) and death. (laser catastrophic failure)

https://www.rp-photonics.com/mode_hopping.html

Intuitively, a laser mode hop is a “flicker”. This means your link goes down and has to be re-trained. Link-flap.

Mode hops are extremely bad and need to be avoided at all costs. The region in which a laser is “mode hop free” depends on the quality of the laser and is typically defined as a drive current and temperature range. A portion of the LIVT curve.

Keeping the laser drive current clean (very low RMS ripple) is much more difficult if it is co-integrated with the optical engine.

Keeping the laser at a stable temperature is far more difficult when you have an optical engine with heaters and heavy IO electrical circuits kicking out dynamic noise.

Preventing mode-hops on lasers integrated with the OE is way way way more difficult than if you just disaggregate the lasers.

Additionally, if any laser dies, your entire optical engine is dead and so is whatever it is soldered to. Dead lasers in ELSFP is easy to deal with. Just swap the damn module.

In summary, integrated lasers with optical engines (NPO, CPO, whatever) is a terrible idea. The only reason people are going for this path is there is a crippling photon/InP shortage.

My view was that nobody would actually do this integration strategy. Apparently several big fish are. This is hilariously bullish for Lumentum.

Have any of you fools seen real LIV curves across temperature for different lasers alongside the mode-hop free regions?

Lumentum kicks ass in this metric. This stuff does not show up on a datasheet. It only shows up if you take 1K production samples and stress test them in rigorous qualification process.

Historically, mid-power lasers were used in transceiver form-factor where thermal density and PCB real-estate (for mitigating electrical crosstalk of HSIO and laser driver circuits) were manageable. Co-integrating mid-power lasers with NPO optical engines makes reliability (mode-hop free operation and wide range) much more important!

Wupen what the hell. Talk about mode-hops and wider range in LIV curve across temperature where laser is stable.

CUSTOMER YEILDS ARE BETTER BECAUSE OF WIDER MODE-HOP-FREE RANGE OF LUMENTUM CW LASERS.

SO CLOSE BUT YOU DID NOT SAY THE RIGHT KEY PHRASE.

Wupen and Michael, you two need to have a meeting together and go over this from a messaging/strategy perspective. You have differentiation but catastrophically failed to explain why.

Reading this transcript is legit painful. Management failing to explain a home run and sell-side clueless as to the epic alpha that is right in front of them.

UHP laser gross margin is 80-90%.

ELS module margin is 50-60%.

I have extensive BOM modeling at both InP and ELSFP module level. The range is only because I am unsure on ASP. AKA how fast Lumentum is hiking prices on their kickass products with no real competition. (Broadcom also sold out).

THEY REDUCED CAVITY LENGTH AGAIN WHILE MEETING SAME LINEWIDTH REQUIRMENT.

This entire call is so damn bullish lol.

lasers go pew pew pew

Share
