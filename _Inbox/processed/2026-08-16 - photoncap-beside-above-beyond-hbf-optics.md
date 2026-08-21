---
title: "Beside, Above, or Beyond: The AI Memory Capacity Race and Where Optics Fits"
source: PhotonCap
url: "https://photoncap.net/p/beside-above-or-beyond-the-ai-memory"
date: 2026-08-16
publication: PhotonCap
gmail_id: 1a00850c578e3e4e
tags: [research, email-backfill, PhotonCap, SNDK, MU, HBF, HBM, NAND, optics]
source_type: web-clip
sender: photoncap@substack.com
gmail_full: true
---
# Beside, Above, or Beyond: The AI Memory Capacity Race and Where Optics Fits

On August 13, one slide was shared at the Sandisk Investor Day. The content was that Meta joined the HBF consortium following Google, and ten days earlier, the first HBF standard specification of up to 512GB and up to 3.0TB/s was published through OCP. Ironically, in the same week, Samsung brought out the zHBM concept that stacks memory vertically on top of the accelerator. Then the question, naturally, has a place it heads to. What about Micron? Micron is officially not putting its name in this game. However, the phrase “stacking NAND” points to a completely different structure at each company, and if you do not distinguish them, you end up drawing the beneficiary map wrong. So this article is going to try dividing the question into two. How to stack, and where to place the capacity made that way, relative to the processor. My interpretation is on the side of “whichever direction the stacking competition gets settled, wouldn’t a considerable part of the growth go not to the memory companies but to the optical interconnect layer?” The evidence has been prepared with job posting originals and physics arithmetic.

Contents

- August 13, One Slide at Investor Day
- Three Meanings of the Word “Stacking”
- Micron’s Public Stance and the Careers Site
- The Structure Micron’s Job Postings Draw
- Beside, Above, Beyond: Three Paths and Three Walls
- Microseconds and Meters: The Physical Reason NAND Is Allowed to Move Away
- The Optics Map: Which Layer It Falls On
- Stacking Equipment and Optical Links: The Related Names
- Conclusion

## 1. August 13, One Slide at Investor Day

Let me start with the $SNDK story. Sandisk stock rose 6% on August 12 alone and reached the mid $1,300 range (as of the 2026-08-12 close) [3], and on the 13th, the day of the Investor Day, it rose another 14% and closed at $1,528 (as of the 2026-08-13 close) [1][4]. In terms of the gain since the start of the year, it is over five times, remarkably [3][4]. It is true that the NAND shortage cycle made these numbers, but the place where my eyes stayed long that day was one slide on the technology roadmap side, rather than the financial targets page.

The “HBF Consortium Milestones” slide from the Sandisk 2026 Investor Day. The August 2026 milestone shows “Consortium Expands: Meta”

The timeline of the slide reads like this. In August 2025, Sandisk and SK hynix agreed on HBF (High Bandwidth Flash) standardization, and in February 2026, a consortium was formed under OCP (Open Compute Project, the body where hyperscalers turn hardware specifications into open standards). The ones that joined at that time were Google and Tenstorrent [5][7]. Until then there did not seem to be much reaction, but just recently, in August 2026, when the first standard spec was published and the Meta logo went up in the consortium expansion box [1], the mood really became one of wondering whether HBF is going to become the standard. In other words, to organize it again, two hyperscalers that design their own AI chips, namely Google and Meta, are now in a state of having put their names on a NAND-based memory standard.

What HBF is, I covered in January in HBF (High Bandwidth Flash) and Optics: The Missing Link in AI Infrastructure, and at that time, it was the article with the best response among the ones I had posted on my Substack.

To say it again in one line, it is a plan to transplant HBM’s stacking formula onto NAND and create a middle tier that is “much wider than SSD and much bigger than HBM.” At that time it was at the level of conference presentations and concepts. Now, a concrete spec document with 512GB capacity, three bandwidth grades from 0.4 to 3.0TB/s, and a UCIe interface is up on OCP [5][6], and it has come to the stage where the company states a schedule: samples in the second half of this year, inference devices in early 2027 [5]. At the Investor Day they went one step further, and it is said that the tape-out of the first HBF die (the state of having finished the design and handed it to the foundry) is complete and customer samples are next year [4].

So the material the market encountered this week is two things. On the surface there are the NAND price cycle, the contract backlog that has grown to the $90 billion range [4], and the Investor Day’s long-term financial targets [2], and below that there is the structural change that “NAND comes out of the storage box and climbs onto the memory bus.” This article intends to deal with the latter. And the question is one.

Everyone says they are stacking NAND, but are they stacking the same thing?

## 2. Three Meanings of the Word “Stacking”

Before the main body, it would be good to divide the axes first. The news of “stacking NAND” actually has two different questions mixed in it. One is the process question of how to stack and build, and the other is the placement question of where to put the capacity block made that way, relative to the processor. This section is the former question, and the beside, above, and beyond in the title are the latter question.

Starting from the process side, the word “stacking” in the industry right now points to three different processes. The three differ in purpose, and the direction the money flows is also different.

Concept diagram of the three kinds of stacking. Layer stacking, wafer bonding, and package-level TSV stacking compared in one view

The first is layer stacking. It stacks NAND cells vertically inside the die, and the “hundreds-of-layers NAND” we see in the news is all this story. It is said that Samsung V10 has passed 400 layers, Kioxia and Sandisk’s BiCS10 is 332 layers, and Micron G9 is 276 layers [8][9][10]. The purpose is simple. Extracting more bits from the same wafer and lowering the cost. It is the economics of storage devices, and it is a game that every NAND company is playing without exception.

The second is wafer bonding. It is a method of making the NAND cell array wafer and the peripheral circuit (CMOS) wafer separately, then attaching them whole to complete one die. Kioxia and Sandisk went first under the name CBA [9], and Samsung also announced that it is joining this column from V10 under the name BV-NAND [8]. Up to here, it is still a story about “how to make one die well.” Density increases and I/O gets faster, but the completed die still sits behind the SSD controller, behind the serial passage called PCIe.

The third is HBF. It is a structure that threads multiple completed NAND dies with TSV (Through-Silicon Via, vertical wiring that penetrates the die) like HBM, puts them on a logic base die, and connects them directly with a wide parallel bus from the seat beside the processor [5][6]. The first spec is 8-high or 16-high stacking, up to 512GB per stack, and bandwidth from 0.4 to 3.0TB/s depending on grade [6]. If the previous two stackings are the game of “cheaper,” this one is the game of “wider.” Since it is a matter of changing the interface itself from the storage kind (serial PCIe) to the memory kind (parallel wide bus), I see only this third one as a stacking of a different nature.

But here, one placement question cuts in ahead of time. It is the option of moving the stacking position onto the processor entirely. The zHBM that Samsung unveiled at FMS 2026 is a concept that stacks not NAND flash memory but HBM vertically right on top of the accelerator, and by the company’s claims, it speaks of 8 times the performance of HBM5 and more than 10 times the density [8]. Let me clearly attach the maturity label that it is still at the concept model stage. It is not a product, not a confirmed roadmap, and the figures are vendor claims. Still, the direction itself needs a serious look, because as covered in July in TSMC Is Ahead in CPO. Samsung Is Putting a Third Chip Next to HBM, Samsung keeps digging into the real estate problem inside the package from different angles. And that makes sense, because Samsung is a vertically integrated semiconductor company that can optimize the processor, memory, HBM, photonics, and process together, so it may well be making various attempts. I also think this point is their strength.

Concept diagram of the zHBM structure from the Samsung newsroom. A cross-section with the HBM stack placed on top of the processor

That was long, so to organize it a little: the layer-count competition and the bonding transition are the stacking of cost, HBF is the stacking of bandwidth, and zHBM is the stacking of position. The reason investors must not lump the three into one word is, as we will see later, that the physical limits each one hits are different.

## 3. Micron’s Public Stance and the Careers Site

Now it is Micron’s turn. In fact, Micron is not a member of the HBF consortium [7]. The award it received at FMS 2026 is also said to have been on the 245TB-class data center SSD side [11]. In early August at the Technology Leadership Forum, the remarks of CBO Sumit Sadana also stop at the level of “when DRAM is insufficient, KV cache spills over to the NAND side” [12].

To summarize, the Micron on public stages concentrates its firepower on HBM4 and sells NAND as fast SSDs. It stacks, but in the first and second meanings of stacking, that is, the stacking of cost.

Then is Micron really keeping its hands off the third game?

Actually, in January this year I made an inquiry to an acquaintance, and since it seemed difficult to talk in a public place about the answer I heard privately, only now have I found public materials and come to make it public.

If you open the careers site, the answer comes out somewhat different.

This part took some time to confirm. Nothing came up in news searches, so I went through Micron’s recruiting system directly, keyword by keyword, and the word “HBF” is 0 cases in all postings. Instead, two postings from the NAND design organization (NVEG) in Tokyo were caught. One was posted in April, one in July, a hiring that has continued for four months [13][14], and since postings can come down, I saved the originals as captures.

Please look at the highlighted phrase in the capture below. What structure of NAND this posting is hiring for, and why I crossed over to the optics-side conclusion after seeing it, is the content of the paid section.

Original Micron Tokyo NVEG job posting.

## 4. The Structure Micron’s Job Postings Draw

Let me carry over the posting wording as it is. The Tokyo NVEG Principal Design Engineer job description introduces itself as “design of datapath circuits for NAND flash memory,” and then writes this as the first responsibility. “Design and optimization of TSV interface circuits connecting memory die to logic die” [13][14].

Sentence by sentence, it points to the third stacking of the second section. NAND connected to a logic die through TSV is, in itself, not an SSD structure. In the requirements that follow, “TSV power integrity for highly parallel IO and array operations” and “energy-per-bit optimization in the context of 3D-stacked memory architectures” appear [13]. The decisive one is this phrase. “Column redundancy and lane repair schemes compatible with HBM-like highly parallel bus architecture” [13][14]. And in the preferred experience column, HBM3, HBM3E, HBM4 interface design experience is specified [13].

So, judging only by the hiring requirements, this is a posting that recruits “a person who threads NAND in the way HBM was made.” The Tokyo location also comes into view. It is a city where NAND design manpower of the Kioxia and Western Digital lineage is gathered, so the interpretation that it is a placement aimed at the talent pool is natural. However, this is my conjecture, and the company has never revealed the reason for the location.

Since I cannot always be right, let me first clearly write down the limits as well.

A job posting is a primary source that shows the direction of a development organization, but it is not confirmation of a product roadmap. However high the match between the posting wording and the HBF structure, one cannot jump to the assertion that “Micron is making an HBF rival product,” and this article will also go only as far as “circumstances of quietly preparing the same physical structure outside the standards consortium.” Even so, there is one thing that changes with these circumstances alone. The possibility that the composition of “HBF vs advanced NAND” is actually “TSV NAND inside the standard vs TSV NAND outside the standard.”

Weight is added to the side that the third stacking is a direction the whole industry is heading toward, and the exclusive property of no two companies.

In fact, Samsung also said in the same announcement that it is developing, under the name zNAND-O, a V-NAND based four- and eight-layer stacked NAND solution for edge AI [8], and at the FMS exhibition floor it even set up a model of this stack attached beside an NPU. There is no interface mention in the press release body, but on the exhibit model’s substrate a UCIe interface marking is visible (based on the exhibit labeling). Inside the standard or outside it, everyone is drawing the picture of putting NAND on the memory bus.

The V10 Bonding V-NAND model at Samsung’s FMS 2026 exhibit. A NAND stack connected beside an NPU over a UCIe interface

## 5. Beside, Above, Beyond: Three Paths and Three Walls

Now the placement question. The seats for attaching a capacity tier to a processor come down to only three. Place it beside, raise it above, or put it beyond. Beside is the on-package HBF seen earlier, above is zHBM, and beyond is the placement of putting the same HBF stack in a remote unit across an optical link. So beyond is, rather than a new memory, a different seat for the same thing, and optics is the means that makes that seat possible. And all three seats hit their own walls.

The three paths, beside, above, beyond, and their respective walls. A comparison diagram assigning shoreline, heat, and energy per bit to one axis each

The beside option is HBF’s basic form. The wall is real estate. The package edge, called the beachfront in industry terms, is already mostly occupied by HBM. A competition to increase the number of HBM stacks within interposer area and reticle limits is in progress, and here a 512GB NAND stack is asking for a few more seats. And the HBF stack is said to have been designed from the start to target the same footprint and pin layout as HBM4 [15]. Stacking 256Gb per die in 16-high for 512GB per stack, with a first-generation read bandwidth of up to 1.6TB/s as the company’s target [15]. So HBF receiving one seat means one HBM stack drops out as it is. It is trading a seat that gave 2TB/s-class bandwidth and tens of GB of capacity for 512GB of capacity, so neither side can easily yield a seat. Since it is a fight over seats, it is zero-sum. If capacity demand is faster than the speed at which the package grows, the seats beside run out quickly.

The above option is Samsung’s zHBM. The wall is heat. If you look at the cross-section in the capture above, the memory sits between the processor and the cold plate, and since the heat of a 1kW-class accelerator escapes almost entirely upward, it is a structure that inserts the memory into the middle of that path. This is the point where this placement becomes really difficult. Logic silicon endures up to around 105 degrees, but DRAM, past the usual 85 degrees, must double its refresh, and the retention margin deteriorates sharply.

The component most sensitive to temperature in the system sits in the hottest passage. It is not that there is no mass-production precedent, and the fact that AMD’s 3D V-Cache is the best-known case rather shows the limits. One low-power SRAM die on top of the comparatively cool cache region, with the early generation even lowering the clock: those were the conditions for it to hold, and AMD, in the second generation, flipped the cache under the cores entirely and went around the heat problem. It is a choice that shows how much the above placement loses on heat. Extending this to the combination of 12-high DRAM and a 1kW GPU is a completely different thermal budget problem. The part where Samsung claims to have reduced thermal resistance to less than half is a story about improving the bonding interfaces, and the placement itself, in which the accelerator’s heat must penetrate the memory, remains as it is [8]. I attach the concept-stage technology label once again.

The beyond option is disaggregation based on optical connection. The wall is energy per bit. The bit moved by electrical wiring inside the package is the cheapest. The moment you convert to optics, the EO/OE conversion loss of electrical to optical and optical to electrical, and the cost that follows it, attaches, and moving the same bit takes several times the energy. This is the reason it has been “memory must be close, unconditionally” until now.

But among the three walls, there is one whose nature is different. The shoreline is geometry and heat is thermodynamics, so they barely move even as time passes. You could call them physical limits. However, only energy per bit is on a technology curve. CPO (Co-Packaged Optics, packaging that pulls the optical engine into the processor package) keeps cutting this number down generation by generation, and the ladder of architecture options leading from DSP to LPO, NPO, and CPO is itself organized as a ladder of energy savings. The only wall that time and technology take the side of is the wall of the beyond option.

Let me add one personal story here. I am not a person who runs AI models, and I still feel this capacity problem every day. Semiconductor simulation is, in the end, giant matrix calculation, so I put it on a GPU, and if I increase the model size even a little, vRAM runs out first. When the compute units are idle and I am splitting the problem because memory is insufficient, you become convinced of why a capacity tier is needed, even without a paper. The inference-side story that KV cache has grown into a problem is an enlarged version of the problem on my desk. However much saving techniques like compression and quantization advance, this industry runs bigger models by as much as the savings made things cheaper, so capacity demand, paradoxically, keeps growing. That is how I see it, and I always emphasize this part.

## 6. Microseconds and Meters: The Physical Reason NAND Is Allowed to Move Away

For the beyond option to hold, one more thing is needed besides energy. A guarantee that performance does not die even if it is placed far away. And at this point, NAND’s weakness flips into a strength.

NAND is slow by nature. Read latency is in units of tens of microseconds, about a thousand times longer than nanosecond-unit DRAM. That is why it has been on the lower floor of the memory hierarchy until now, but when it comes to the distance problem, the story changes. An optical signal travels 1 meter in roughly 5 nanoseconds.

Even if you move an HBF stack from beside the processor to 2 meters away across the rack, and add all of the optical conversion, switches, and protocol delays on top, the added portion ends at the level of hundreds of nanoseconds. In front of an access latency of tens of microseconds, it is at the level of one hundredth.

On the other hand, if you move DRAM 2 meters away, access latency jumps several times. It is the obvious arithmetic that fast things are sensitive to distance and slow things are insensitive to distance, but the conclusion of this arithmetic is not obvious. It is hard for HBM to leave the processor’s side, but HBF is a tier that was allowed to leave from the beginning.

What is needed when leaving is bandwidth, and that is optics’ specialty. Extracting terabit-class from one strand of fiber with WDM, which loads wavelengths on top of each other, is the standard path of data center optics now, and the 3.0TB/s of the HBF grade table can be handled at rack distance with a bundle of a dozen or so fibers, depending on the WDM configuration. So my picture is this. The first generation of HBF will start in the UCIe seat beside the processor as the standard documents say, but from the moment capacity demand exceeds the package real estate, the growth accumulates on the HBF across the optical link, that is, on the optically connected flash appliance side. It is an extension of the hybrid tier seen in February in SK Hynix H³: Breaking the HBM Capacity Wall with ‘HBF Hybrid’, which covered SK hynix’s H³ structure, and it is also the same direction as the memory pooling picture drawn in The More Anthropic Buys Micron HBM, the Faster Optical Memory Pooling Arrives.

To be fair, let me also write down the opposite side where my claim or hypothesis could be wrong.

On-package electrical connection will always beat such distanced NAND (HBF plus optics) on energy per bit in the future too. So the realistic destination is more likely tiering than the victory of either side. Hot weights and KV cache are handled by HBM inside the package and a small amount of on-package HBF, and warm data is handled by optically connected capacity at rack distance, in that manner. My claim is not “on-package loses” but “the increment accumulates on the optics side,” and in the investment map this difference is quite large. If the former, you should sell the memory companies, but if the latter, it is a picture of holding the memory companies and the optics companies together.

## 7. The Optics Map: Which Layer It Falls On

So let me write down, layer by layer, which companies fall here. Prose instead of a table.

From the package boundary layer. That the HBF spec adopted UCIe (the open standard interface for connecting chiplets to each other) is [6], I think, an underestimated point from the optics standpoint. A UCIe socket does not discriminate between electrical chiplets and optical chiplets. If it is a seat where the NAND stack attaches over UCIe, then the friction of the design transition where an optical I/O chiplet attaches in the same seat is small.

Of course, it is an integration problem where packaging issues such as lasers, fiber attach, and thermal verification follow, so it is not a story that ends because the socket is the same, and this part is my inference rather than a fact of the standard. The name of this layer is Marvell. The Photonic Fabric secured through the Celestial AI acquisition is a plan in the direction of taking “memory over optics, out of the package” [16], and on the unlisted side, Ayar Labs’ TeraPHY aims at the same seat. For both companies, the maturity label of pre-mass-production stage is mandatory. It is the stage of samples and design win announcements, not the revenue stage.

The scale-up fabric layer. It is the layer of optical switching and optical engines that tie GPUs and the capacity tier together in and around the rack, and Broadcom’s CPO switch roadmap and the optical scale-up transition of the NVIDIA ecosystem hang here. The characteristic of this layer is the asymmetry that it grows without HBF and grows more with HBF. The moment the capacity tier comes outside, a new demand called “memory access” is added to East-West traffic.

The light source and components layer. Whichever architecture wins, lasers and optical engines are sold. The Coherent and Lumentum InP capacity story has been covered many times in this series, so here just one line. Optical disaggregation of the capacity tier is, for them, closer to an amplification of the existing SAM than a new SAM.

Lastly, let me look at one common counterargument and finish. If HBF puts large-capacity data right beside the processor, data has fewer reasons to travel the network, so isn’t that actually bad for optical communication demand? That is the question. It is a reasonable worry, and here is how I see it. These days, inference services do not finish inside a single GPU. Both the model and the conversation history (KV cache) have grown too large, so the work runs with multiple nodes holding pieces and passing them to each other [12]. So for the picture of “pack it all inside the package and remove the traffic” to hold, the data first has to fit inside the package, and right now data size is growing in exactly the opposite direction. What cannot be contained must be moved, and the moment it moves, optics demand appears again. The world where traffic really decreases is the world where models stop growing, and if that world comes, you would have to rethink the whole AI infrastructure investment before worrying about optics.

## 8. Stacking Equipment and Optical Links: The Related Names

Having talked about layers, now it is the turn to talk about actual stock names. Whichever of the three placements wins, there is one layer where work arises in common, and it is the equipment that goes into the act of stacking itself. The process chain of grinding dies thin, aligning them, and attaching them is volume that is relatively less shaken by the result of the placement fight. Of course, the equipment composition can change with stacking method and yield, so let me first set the premise that the mapping of this section is an inference descended from process structure.

First, the TSV stacking side. HBF-class stacks are highly likely to demand the process chain of die thinning (grinding), alignment, and the bonding that attaches the dies. This chain is demand already verified in HBM, and thermo-compression bonding (TCB, a method of pressing chips with heat and pressure) equipment is a composition where ASMPT, Hanmi Semiconductor, and Kulicke & Soffa are counted as the main suppliers, and BESI has also entered while receiving production orders. If HBF goes to 8-high and 16-high as the spec says, the number of joins per stack itself lands in the same digit range as one HBM stack. One caution here. Sandisk’s official wording is TSV and microbumps plus “proprietary stacking technology” [17], so the bonding method is not confirmed as TCB. The details of the production process (bonding method, underfill, stack thickness) are undisclosed, and I attach the maturity label that no equipment company has announced an HBF-related order.

The wafer bonding side must be viewed with maturity separated. Kioxia and Sandisk’s CBA is a process already in mass-produced products, and Samsung BV-NAND is at the announcement stage of having made official the bonding transition in the 400-layer range [8]. W2W bonding and alignment equipment, which attaches wafer to wafer, is a market where EV Group (unlisted) and SUSS MicroTec are representative and Tokyo Electron has also entered, and hybrid bonding, which attaches die to wafer, is a market where BESI is counted in the leading group. That Micron is also running bonding process development hiring that lists the integrated optimization of Wafer Bonding, Si Grinding, and Bevel Trimming [18] is a preceding development signal of this layer, and it is not evidence of equipment orders. The weight-class comparison and differentiation of these equipment companies were organized in May in 7 Bonding Equipment Companies Behind HBM4 and CPO: AI’s Real Bottleneck Lives in Assembly, and one more block, NAND stacking, is placed on the demand map drawn there with HBM4 and CPO.

For the optical link side, you can read section 7’s layer logic converted into stock names. Optical I/O at the package boundary is $MRVL (Photonic Fabric, with the first revenue contribution stated by the company in the second half of FY2028 [16]) and the unlisted Ayar Labs, scale-up optical switching is $AVGO (with CPO at the stage of being raised as an option in the switch lineup), and the light source side is $COHR and $LITE, whose roles differ somewhat across lasers, optical engines, and OCS. And the bigger the beyond placement grows, the stronger the volume logic of this layer. It is a structure where, when remote capacity units increase, the optical components at both ends of the link increase accordingly, though I attach the caveat that it is not exactly one-to-one depending on switch transit or wavelength multiplexing configurations.

If I reduce the picking criterion to one, it is this. Stacking equipment is the volume side that is relatively less sensitive to the winner of the placement fight, and optical links are the side that gets stronger as the beyond placement grows.

## 9. Conclusion

Conclusion. It was a week when stacking news for NAND and HBM poured out, but the three are different games. Layer count and bonding are the game of cost, HBF of the interface, zHBM of position, and Micron has been running the hiring of the third game outside the consortium for four months.

And among the walls the three paths hit, I see only one wall that time and technology can solve for us, and that is the optics wall. I stand on the side that the incremental value of this stacking competition flows to the optical interconnect layer. Capacity must grow, the package is narrow, zHBM’s heat does not cool, and NAND’s microseconds do not care about optics’ nanoseconds.

Let me also compare the past call here. In the January 26 article I wrote HBF down as a “candidate trigger for expanding the optical interconnect ecosystem,” and in half a year it came to an OCP standard spec, UCIe adoption, and Google and Meta joining the consortium, so it can be said the direction was right to some degree. However, among the companies listed together at that time as beneficiary candidates, there are names like POET that were shaken greatly in the meantime for other reasons, so I review the stock-level calls as half a grade. That article taught me that direction and stocks are different problems.

Let me also write down the conditions under which this judgment collapses. First, if the decline of CPO’s energy per bit stalls against the roadmap, that is, if the numbers of the next-generation optical engines stand still at next year’s OFC, the axis of this article, “time is on optics’ side,” collapses. Second, if panel-level packaging comes faster than expected and the shoreline widens greatly, the beside option lives on for a long time, and the blooming of optical disaggregation is pushed back. Third, if the first generation of on-package HBF absorbs most of the KV cache demand, I must fold the judgment that “the increment comes outside.” The checking dates are these. HBF sample shipment in the second half of this year and the customer samples said to be next year [4][5], the first inference devices said to be early 2027 [5], NAND-side new product mentions at Micron’s earnings call in late December, and the spec updates of OFC next March and FMS next August. I will open this article again on those dates and compare.

## References & Sources

[1] “2026 Sandisk Investor Day” - Sandisk IR, 2026-08-13. Investor Day event page with presentation PDF and webcast links
[2] “SanDisk unveils long-term growth strategy at 2026 Investor Day; Shares surge 12%” - Investing.com, 2026-08-13
[3] “Memory Stocks Rally Wednesday: SK Hynix, SanDisk, Micron All Jump. Here’s Why” - 24/7 Wall St., 2026-08-12
[4] “What SanDisk Stock’s 14% Investor Day Jump Means for a $93.9 Billion Backlog” - TIKR, 2026-08-13. Closing price $1,528, HBF tape-out and customer sample schedule, backlog figure
[5] “Sandisk and SK hynix Advance Global Standardization of High Bandwidth Flash with Release of First OCP Technical Specification” - Sandisk IR, 2026-08-03
[6] “SK hynix Unveils First HBF Standard Specifications with Sandisk, Presenting AI Memory Solutions at ‘FMS 2026’” - SK hynix Newsroom, 2026-08
[7] “SK hynix, SanDisk Debut HBF Standard to Challenge AI Memory Bottlenecks with Google, Tenstorrent Support” - TrendForce, 2026-08-04
[8] “Samsung Unveils Next-Gen 3D-Memory Vision at FMS 2026, Charting the Future of AI Infrastructure” - Samsung Newsroom, 2026-08
[9] “New 3D Flash Memory Technology from Kioxia and Sandisk Achieves Industry’s Highest Bit Density for QLC NAND” - Sandisk Newsroom, 2026-08-04. 332-layer BiCS10, the CBA (CMOS directly Bonded to Array) architecture, up to 60% QLC bit density gain
[10] “Micron Announces Volume Production of Ninth-Generation NAND Flash Technology” - TechPowerUp, republication of Micron’s announcement. G9 at 276 layers, 3.6GB/s interface
[11] “KIOXIA, Micron, and Samsung earn Best of Show awards at FMS 2026” - TweakTown, 2026-08
[12] “Micron at Technology Leadership Forum 2026: AI tightens memory market” - Investing.com transcript, 2026-08
[13] “Semiconductor Principal Design Engineer (JR106037)” - Micron Careers (Workday), posted 2026-07-21
[14] “Semiconductor Principal Design Engineer (JR94304)” - Micron Careers (Workday), posted 2026-04-13
[15] “Sandisk HBF Fact Sheet: Sandisk Unveils the Future of Memory Architecture for AI” - Sandisk official fact sheet. HBM4 footprint and pin compatible design, 256Gb per die, 16-high 512GB, first-generation read bandwidth up to 1.6TB/s
[16] “Marvell Completes Acquisition of Celestial AI” - Marvell Newsroom, 2026-02-02. Includes revenue contribution timing guidance
[17] “Sandisk Forms HBF Technical Advisory Board to Guide Development” - Sandisk IR. Source of the TSV, microbump, and proprietary stacking technology wording
[18] “Advanced Technology Japan Engineer, WoW Bonding (JR97682)” - Micron Careers (Workday), posted 2026-05-24. Source of the Wafer Bonding, Si Grinding, Bevel Trimming integrated optimization wording

Disclaimer: This article is an independent technical analysis published by PhotonCap, based on an engineering perspective. All content is derived from publicly available information and is intended solely for educational and informational purposes. In other words, nothing in this material should be construed as a recommendation to buy, sell, or hold any specific securities. Please note this carefully. The author may hold positions in the securities mentioned herein and reserves the right to trade such securities at any time without prior notice. Readers should conduct their own thorough review and research before making any investment decisions.
