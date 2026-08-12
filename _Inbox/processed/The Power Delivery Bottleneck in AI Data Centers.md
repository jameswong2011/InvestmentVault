---
date: 2026-08-04
tags: [research, email-backfill, Damnang]
source: 'https://damnang2.substack.com/p/the-power-delivery-bottleneck-in'
source_type: web-clip
sender: damnang2+company-deep-dives@substack.com
---

# The Power Delivery Bottleneck in AI Data Centers

Power comes up in every conversation about AI infrastructure bottlenecks.

The problem is that it usually takes some engineering background to follow. I’ve written about power investing before, and the main thing I took away was that readers wanted the technical side explained much more simply.

### AI Datacenter Power Investment Map: From 765kV to 0.65V

### The Re-rating in AI Power Started Here

So this piece does that.

It walks through why the power delivery bottleneck exists, in the plainest terms I can manage, and then lays out how to think about the four companies closest to it: MPWR, Vicor, Murata and Samsung Electro-Mechanics. If you’ve been investing here without a clear picture of the mechanics, this should help.

> Note: There’s a whole other part of the delivery bottleneck around 800VDC distribution, where 800 volts of direct current runs all the way to the rack. That’s big enough to need its own article, so I’ve left it out. I’ll cover it next time.

Disclaimer

This article is for information only. It does not recommend buying or selling any security. Investment decisions and their outcomes are the reader’s own responsibility. Figures cited are based on public sources and may have changed since publication.

## Power at Three Scales, and Where It Gets Stuck

Power is measured in watts, written W. A kilowatt is a thousand watts, a megawatt is a thousand kilowatts, and a gigawatt is a thousand megawatts. For scale, the microwave in your kitchen pulls about a kilowatt.

AI infrastructure power is easiest to picture at three levels. A GPU accelerator, the part doing the computing, sits at roughly a kilowatt. A rack, the cabinet servers get stacked into, runs in the hundreds of kilowatts today and is heading toward a megawatt. A campus is measured in gigawatts. That’s what people mean when they say hyperscalers are building gigawatt data centers. A gigawatt is roughly what a million American homes use, and several AI campuses are due to hit that scale in 2026.

And the buildout keeps accelerating. When OpenAI announced Stargate, it committed to ten gigawatts of AI infrastructure by 2029. By April 2026 the company said it had already passed that, having added more than three gigawatts in the previous ninety days alone. Meta has said it will build tens of gigawatts this decade. AI data centers are about to consume a staggering amount of electricity.

So why has power become the next bottleneck? Two very different problems get bundled under that one word.

The first is getting the electricity in the first place.

Moving power from a plant to a data center means new transmission lines and new substations, and in the US the wait just to get an interconnection approved can run for years. That’s a grid and permitting problem, and it belongs to utilities and power equipment makers.

The second is getting that electricity to the chip without losing it on the way.

A GPU can be as fast as you like on paper, but it won’t hit those numbers if the power can’t reach it cleanly. That second problem, the power delivery bottleneck inside the data center, is what this article is about.

## Two Problems in Delivering Power

So what does delivering power well actually mean?

The easiest way to picture electricity, as you probably learned in school, is water moving through a pipe.

(If that’s gone fuzzy, no problem, here it is again)

Voltage is pressure.

Current is how much water is flowing.

Power is the two multiplied together, P (power) = V (voltage) × I (current).

Which means that for a fixed amount of power, higher pressure lets you move less water, and lower pressure forces you to move more.

Think about a water pipe.

To do the same job, high pressure gets by with a narrow pipe. Low pressure means pushing far more water through, and the pipe has to get much fatter to handle it.

Here’s the problem with a chip: it needs a lot of power but runs at almost no voltage.

A modern data center GPU pulls more than a thousand watts, while the voltage it actually accepts is under one volt. Pushing all that power through at rock bottom pressure sends the current into the thousands of amps. A typical home, for comparison, is served by around 200.

So what goes wrong once the current gets that high?

Back to the water. As it travels down a pipe it rubs against the walls, and in electricity we call that friction resistance. Pushing power through resistance costs you some of it, and the loss scales with the square of the current. Double the flow and the loss is four times. Triple it and it’s nine. Since the voltage can’t be raised at the chip, the only lever left is to make the path shorter and thicker.

Then there’s a second problem. So far we’ve assumed the water flows at a steady rate, but it doesn’t. Say you’re in the shower and the washing machine starts up while someone flushes the toilet. The amount of water being drawn jumps several times over in an instant. The water is coming from a main some distance away, so it can’t meet that demand right away, and your shower goes weak for a moment.

The same thing happens at the chip. When the compute load spikes, the current it needs jumps instantly, and a power source sitting some distance away can’t respond fast enough. The voltage sags briefly, and the chip throttles itself to avoid glitching.

Leave either problem unsolved and a good share of the power you brought onto the campus turns into heat before it ever reaches the chip. Buy all the high end GPUs you want; you won’t get the performance they were built for. That’s the power delivery bottleneck.

## Two Fixes

### Murata: The Stock You Missed If You Only Bought GPUs and HBM in the AI Rally

Friction losses come down when you shorten the path.

In the traditional setup, the 48 volts arriving at the rack gets stepped down to around 12 volts on the board, and a converter then drops it below one volt near the chip. Skip the 12 volt stage and go straight down from 48, and one conversion disappears. Move the converter to the underside of the board, directly beneath the chip, and the stretch carrying the enormous current gets much shorter.

The voltage sag comes down when you put capacitors right next to the chip, giving it something local to draw on when demand spikes. That’s the small water tank from earlier. Industry estimates put hundreds of thousands of them in a single NVL72 class cabinet.

Share

## Power Converters: Vicor and MPWR

Putting the converter around the edge of the chip is called LPD, lateral power delivery. Moving it to the underside of the board, right below the chip, is VPD, vertical power delivery. Both companies build both.

What differs is where their weight sits. MPWR built its business making power semiconductors cheaply at scale. Its designs are proven, they get designed in broadly, and the company earns on volume. Its parts are in most of what ships today.

Vicor has always sold modules rather than individual chips, packaging the converter, coil and capacitor together. So the question that matters for Vicor is how much current it can pull out of a given area and thickness, which is exactly why it leads in VPD. It has also wrapped the approach, and the circuit architecture inside it, in patents. Anyone heading the same way either designs around them or pays a licence. Its second quarter guidance raise reflected both higher product revenue and income from a newly signed licence.

So which one do you buy?

MPWR is already designed into the current generation broadly, shipping a wide range of power stages and modules in volume. Vicor’s strength is high density modules and the patents around vertical delivery. What matters for MPWR is that the dollar content of power components per accelerator keeps climbing while today’s layout holds. What matters for Vicor is that product and patent value rise together the moment the layout changes.

Which means the question isn’t which layout survives. It’s how fast the shift to vertical actually happens.

The consensus view is that LPD stays dominant for now. Products pushing more current through a single converter keep arriving, and they lift performance without forcing a redesign of the board and package. VPD still has open problems, starting with the fact that the heat from the chip and the heat from the converter end up in the same place.

So what ships today doesn’t drop LPD. It handles most of the power around the chip and moves only some stages underneath, a hybrid. Vicor’s management described the market moving exactly that way on its earnings call. My own view is that an LPD-centered hybrid holds for the next two to three years.

On that view MPWR is the steadier pick. As chip current and power climb, so does the dollar value of the power components going into each GPU. That might mean more power stages, or it might mean existing parts getting swapped for higher current, higher priced modules. Component count doesn’t necessarily track current one for one, but the direction is clear enough: MPWR captures more content per accelerator.

The second quarter bears that out. Enterprise data revenue came in around 2.6 times the year ago level, and management lifted the low end of its full year growth expectation for the segment from 85% to 130%. Even if vertical delivery arrives later than expected, rising chip power alone can carry MPWR’s results within the current generation. That’s the appeal.

There’s risk, of course. Suppliers get reconsidered every time the GPU generation turns, and a high share today doesn’t automatically carry forward. But given how broadly it’s designed in and how much it can manufacture, MPWR looks well positioned to hold what it has.

Vicor is a different proposition. It already earns money from its existing module business, but the share price isn’t explained by those numbers alone. What’s priced in is the expectation that as power delivery moves from beside the chip to underneath it, both the modules and the patents get more valuable.

That expectation gets more concrete as designs put several compute dies and memory into one large package. The bigger the package, the less room there is around the edge for converters, and the further the current has to travel from the outside to the center of the die. At that point the case for moving some converters underneath gets much stronger.

It comes down to thickness and current density. The space under the chip is very shallow, so an efficient part is useless if it’s too thick. Make it thinner and both heat removal and current handling get harder. Hit the height target and you fall short on current; hit the current target and the part won’t fit.

According to Vicor’s earnings call, large OEMs and some hyperscalers are asking for modules 3 mm or shorter. Vicor’s second generation part delivers the required current density at about 1.5 mm, half that, and it’s understood to be the only company that can do it today. Thin packaging and high current density at the same time is the company’s core technical moat.

The technology is already in use in wafer scale systems, where there’s simply no room around the chip for converters. The industry assumes that customer is Cerebras. Chips designed in house by hyperscalers are expected to head the same direction as they scale up, which is why the company named TPUs, GPUs and wafer scale engines together as targets for the second generation part. Go from one customer to two to three and revenue changes scale entirely. That’s the technical case for owning Vicor.

For now, though, the first fab is near capacity, so a record backlog isn’t converting into revenue. That waits on the second fab site being confirmed and its lines coming up. And the price already assumes a lot. Set the August 3 market cap against the company’s own revenue guidance for the year and you get roughly 17 times sales. That revenue includes licence income at higher margins than product, so it doesn’t compare cleanly with a typical power semiconductor multiple. What’s harder to argue is already in the price is the size and timing of the second fab, which makes the groundbreaking announcement the point where the math gets redone.

Share

## MLCC: Murata and Samsung Electro-Mechanics

The capacitors mentioned earlier, the ones sitting next to the chip to ride out the spike, are mostly MLCCs, multi-layer ceramic capacitors. They’re built by stacking hundreds of ceramic layers, and the top end of the market for the high capacitance, high reliability parts AI servers need is an oligopoly centered on Murata and Samsung Electro-Mechanics.

Capacitors sort themselves by distance from the chip. Out on the board, large polymer and tantalum parts handle the slow changes. Around the chip, MLCCs cover the middle. Directly underneath or inside the package, thinner and faster silicon capacitors go in. MLCCs are by far the biggest of the three by count and by value.

Investing here is a completely different exercise from the converter layer. That one was about guessing which layout wins and who takes the socket. None of that applies here. Whichever layout wins, more chip power means more capacitors, and the two companies taking most of that volume today are Murata and Samsung Electro-Mechanics.

What you watch instead is price and supply, since demand is already settled. The approach is to get in while prices are rising and get out before that phase turns. It’s closer to owning a cyclical component than waiting on a technology transition.

Right now the constraint isn’t price, it’s availability. Murata’s capacitor revenue rose 16.5% quarter on quarter while its backlog built to 617.8 billion yen, so orders keep running ahead of shipments. Channel checks suggest lead times on some high spec parts have stretched to as long as 30 weeks.

Customers have responded by locking in volume ahead of time. Instead of pushing prices down they’re asking for long term supply agreements, and Samsung Electro-Mechanics has closed agreements with about ten of them, including major hyperscalers and semiconductor firms. Only a handful of suppliers can build the very top of the range, parts above 100 microfarads or rated to 125 degrees, so the leverage sits on the supply side.

Where the two companies differ is when the price increase shows up in results. Murata raised first and the effect has already started coming through, and it lifted its full year data center revenue outlook to 370.6 billion yen, up roughly 110% year on year. Samsung Electro-Mechanics raised 30% from August shipments, so its effect starts in the third quarter. It has signed a run of AI server MLCC contracts centered on 2027 delivery, roughly 750 billion won among those disclosed, plus a 1.5 trillion won silicon capacitor agreement announced in May. Being one of the few companies commercializing MLCCs, silicon capacitors and package substrates together is a further edge.

The risk comes down to one question: when does this phase end. Component markets in a rising price cycle have always ended with capacity additions, and both companies are adding lines now. Watch for the point where those new lines start running and consumer demand comes back at the same time. In 2022 that’s exactly where the price increases were handed back.
