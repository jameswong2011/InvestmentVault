---
publish: false
date: 2026-08-05
tags: [research, email-backfill, NuttyCLD]
source: 'https://nuttycld.substack.com/p/public-serdes-part-1-the-technology'
source_type: web-clip
sender: nuttycld@substack.com
---

# SerDes Part 1 The Technology You Should Know Before CPO

> An analysis of industry and technology structure, not investment advice · The author may hold positions in securities mentioned

I work in Silicon Valley as an analog IC design engineer. Lately my LinkedIn inbox has been filling up with messages like the one below, all about SerDes (Serializer and Deserializer) engineer positions.

Most of you are probably familiar with CPO, but I suspect SerDes (Serializer-and-Deserializer) is new to many. Today I want to walk through just how deeply this technology is embedded in the current interconnection era. For the record, the message below came from a recruiter at one of the companies that will appear in this article. In the age of CPO, the emblem of the digital and optical era, the person this company is desperately hunting for is, ironically, an analog designer.

## I Know Analog and Digital

We lived through the age of analog communication and now live in a thoroughly digital one. As with computing, communication is a field digital has won outright. The reason is the noise tolerance of digital signals. By the nature of communication, data is attenuated as it crosses a transmission line and distorted by outside factors. Since delivering data exactly as sent is the highest virtue in communication, these factors are weeds: things to be removed or suppressed by any means available. In an analog signal, every level carries meaning, so faithfully reconstructing the transmitted level at the receiver is tricky. Digital only has to tell 0 from 1, so even with some noise mixed in, recovery is comparatively easy. Which is why communication has always been digital, and always will be.

But as AI training and inference put ever more GPUs, CPUs, and memory to work, and the volume of data to move kept climbing, digital communication began running into limits. You know HBM: High-Bandwidth Memory, that is, memory with large bandwidth. Conceptually, you can read bandwidth here as the number of transmission lines. In other words, it solves the problem of moving lots of data by sending it in parallel over many lines. But not every application can raise bandwidth through this kind of parallelization, because laying more lines is itself a cost. The next idea, then, is to serialize the data and send it fast. And that is exactly what a SerDes circuit does.

## Now I Know SerDes as Well

What a SerDes (Serializer and Deserializer) does is the same whether the link is electrical or optical. That is a question about the material of the transmission line, and has nothing to do with the methodology of sending more data faster. So SerDes has existed from the early days until now, and will keep existing even after optical links become the norm inside a rack. That does not mean it sits outside today’s datacenter communication revolution. On the contrary, its importance keeps rising. The biggest reason of all: the amount of data the AI industry creates and moves has exploded.

Inside a chip, data travels in parallel along thousands, tens of thousands of wires. The trouble starts the moment it has to leave the chip. To build transmission lines matched to that data volume, the number of physical wires would have to grow with it. Look inside a datacenter linking tens of thousands of GPUs, or a rack inside one, and the wires and optical cables are already packed about as tight as they could possibly be.

If we tried to send data off-chip in parallel, the wires and optical cables would end up occupying more volume than the chips themselves. Physically and economically, that is not a viable path.

So at the chip boundary, where transmission begins, a special circuit is attached. It serializes the parallel data on the way out (transmit side), or parallelizes the serial data on the way in (receive side). The Serializer does the former, the Deserializer the latter. As in the picture below, think of goods carried by many trucks being loaded onto one very fast express train, then split back across many trucks on the receiving end.

Naturally, the serialized data has to move faster than the parallel data did. If ten trucks each deliver one package per second, the train must carry ten packages per second to avoid a bottleneck. It has to run ten times faster. The numbers the industry throws around, 112G and 224G, mean exactly this transfer speed. One lane, meaning one path the data travels along, carrying 112 billion bits per second, is what we call 112G/lane. The industry is now crossing over to 224G/lane, and the next generation, 448G/lane, is under continuous development.

How far this speed can be pushed is one of the key technical metrics of a SerDes. Of course cost cannot be ignored, and here the cost is power. So the metric that matters most is how fast you can carry data within a limited power budget. Improving that metric is what circuit designers like me stay up all night wrestling with. To add one number for a sense of scale: by an NVIDIA ($NVDA) estimate, in the same 100K-server-class datacenter, the transceivers (optical modules) draw 2.3 MW in a traditional cloud and 40 MW in an AI factory. The electricity spent just carrying data now rivals a decent-sized power plant.

NVIDIA’s fiscal 2026 annual report shows computing chip revenue up 59%, while revenue from networking, the business of connecting those chips, grew 142%. These numbers are proof of why this is the age of communication, and of how much this technology matters.

## The Age of Interconnection

✍️ It’s a long one, so I hope you take your time with it, perhaps with a cup of coffee or a glass of wine by your side. - Nutty

## PAM4? I Think I’ve Heard That Somewhere

If you follow this field a bit more closely, you have probably run into the term PAM4 (Pulse Amplitude Modulation, 4-level). The digital communication we usually think of uses NRZ (Non-Return-to-Zero); there is also RZ, Return-to-Zero, which I will skip here. As the figure below shows, NRZ is a signaling scheme with two levels, 0 and 1, PAM4 with four, and PAM6 with six.

More bits per level (NRZ carries 1 bit; PAM4 carries 2) means more information loaded onto each carrier. To send the pattern 01, NRZ has to transmit twice, a 0 and then a 1, while PAM4 sends one symbol at the level that means 01 and delivers the same information in one shot. Think of it as raising the payload per shipment. Obviously favorable for moving data. Today’s 112G and 224G links all use PAM4.

So why not PAM6 or PAM8? A perfectly sensible question. And it is true that the bigger the number, the more favorable the transmission becomes. But this is where we need to recall the history of analog signals ceding their place in communication to digital.

As you may have noticed, this is digital taking a step back toward analog. The most important line dividing analog from digital is the continuity of levels, so the more levels you slice the transmission into, the more analog-like the communication becomes. And that makes it vulnerable to exactly the attenuation and distortion we discussed earlier. In the figure above, you can see the width of the bands marked ‘margin’ shrink as the PAM number grows. Within that margin, a certain amount of distortion can be recovered at the receiver, but as the margin narrows, the allowance for recoverable attenuation and distortion shrinks with it. Pile on levels recklessly and the receiver can no longer tell them apart, which wrecks the essential purpose of communication: sending and receiving data accurately.

The standards body OIF calculates that, holding the same error rate, PAM6 requires 3.6 dB more noise margin than PAM4, and PAM8 requires 6.1 dB more. PAM8 needs 4x the SNR (Signal-to-Noise Ratio) of PAM4. To get there you either double the signal or halve the noise. Boosting the signal means raising the voltage, which burns additional power, and noise has physical floors that make it even harder to reduce. Even so, the industry keeps probing PAM6 for the next generation, 448G, and ISSCC, the field’s flagship conference, publishes research on higher level counts every year. It is a door that will have to be passed through someday, so people keep knocking.

## Now I Understand Why Analog Design Matters

Now the recruiter messages from the opening make sense. Why, in the age of digital, in a field digital has conquered, analog designers of all people are becoming so necessary.

The circuit that gathers data and converts it into a multi-level signal like PAM4 is the Serializer; to add technical precision, a DAC (Digital-to-Analog Converter)-based Serializer. The receive side, in turn, is called an ADC (Analog-to-Digital Converter)-based Deserializer. These data converters are among the main IPs that keep many analog designers fed. Not that digital designers are going hungry; on the contrary, their side keeps gaining importance too. Analog designers focus strictly on the conversion. The converted digital signals then run complex algorithms back in the digital world. The flagship example: at the receiver, digital algorithms strip out the distortion and attenuation picked up along the way and reconstruct the original signal. And that work is genuinely expensive. It is not rare for the receive-side DSP to consume more than 50% of the link’s total power.

Still, the bottleneck remains the analog circuitry. Ever-climbing speeds, circuit noise, the non-ideal behavior of transmission lines, jitter in the clocks driving the data converters: the problems that have tormented analog designers all along keep escalating in difficulty, making the design ever harder.

Analog’s troubles do not end there; they spread beyond the chip. The public datasheet for Panasonic’s Megtron 6, a material widely used in high-speed boards, specifies material properties only up to 10GHz, because beyond that you are in RF (Radio Frequency) territory, where complicated frequency behavior starts to matter. Yet the fundamental frequency of a 224G signal already sits near 56GHz. Once a signal’s fundamental crosses 50GHz, every trace, via, and connector contact in the package and board starts acting like an antenna and a filter that distorts the signal. In short, from 224G on, ‘a good circuit, a good SerDes IP’ is not enough. Chip, package, and board have to be designed together as one system, and the gap between teams that have done this and teams that have not is stark.

So as demand for high-speed communication grows, analog design has become a core technology again, and companies are out pounding the pavement for those designers. Look closely at this job market, though, and one feature jumps out. On the career boards of NVIDIA, Marvell ($MRVL), Intel ($INTC), Cadence ($CDNS), and the like, the SerDes and analog postings are almost entirely Senior, Staff, and Principal; the ranks below are rare. It is a market with no time to train juniors and wait, where companies poach seasoned designers from one another. This leads to outcomes like Qualcomm ($QCOM) acquiring the SerDes IP company Alphawave. Buy the company, restock the roster overnight.

Share

## Okay, I Understand SerDes Is a Sophisticated Technology, but Why Should I Know This?

Time to bring up optical communication again, the topic that set the market on fire this year.

## An Investor’s Handbook I - AI Optics

Information Needs No Mass

That copper keeps losing territory to optics is self-evident. Yet copper is still in use, and will remain so. Which is why it matters to know how far copper can physically go. Copper attenuates a signal more as frequency rises. The copper-cable reach objectives OIF has set by speed generation run about 2 m at 112G and 1 m at 224G. A server rack today stands 2 m tall, so at just 224G, spanning even a single rack on copper alone becomes difficult. Distance is not the only problem. By OIF’s system power targets, the energy to send one bit is about 0.7 pJ inside a package (a few cm) but climbs steeply to about 3.5 pJ over a board path of about 1 m.

The generational shift in optical modules we all know is the result of light filling the ground that copper has surrendered. It runs from pluggables in the equipment faceplate, to LPO with the module DSP removed, to CPO, the hottest topic of the moment, with the optics attached right beside the switch chip. Light keeps replacing copper and moving toward the chip.

If you have followed along this far, you can now spot at a glance, in each of those diagrams, the SerDes circuit and the electrical-optical converter that never leave the picture. Whichever generation the optical module belongs to, those two do not disappear. However far audio equipment advances, microphones and speakers do not go away.

LPO removed the DSP to cut power consumption, and handed the duty of signal recovery to the SerDes. The recovery here is not about distortion inside the optical fiber; it is about distortion arising on the electrical stretch leading to the optical module. Fiber has almost no loss at these distances. The problem is the 20 cm or so of copper running across the board from the switch chip to the faceplate module, and CPO shrinks that stretch to millimeters by attaching the optical engine right next to the chip. With fewer problems arising, a simple DSP implemented inside the SerDes can stand in for the heavy module-side DSP. Per NVIDIA’s materials, of the 30W that one pluggable draws, 20W is the module DSP’s share, while CPO does the same job in 9W.

The chip the industry calls an ‘optical DSP’ is the DSP that sits inside an optical module and restores the electrical signal on both sides of the electrical-optical conversion. Beyond reviving the electrical signal that arrived at the module, it also corrects the distortion created by the bandwidth limits of the laser, the modulator, and the receiving devices. It is ultimately the same family of technology as the DSP inside a host SerDes, and that is why the companies that are good at SerDes become the stars of the optical DSP market.

A SerDes must sit at both ends of the link whether the transmission medium is electrical or optical, so it will remain in place even when optical communication becomes mainstream. DSP is a little different. The DSP that has moved inside the SerDes will still be needed, but the DSP inside the optical module that corrects signal distortion from the chip-to-module path is likely to disappear as that path grows shorter. When you look at the companies in this space, you can only forecast properly by matching what each company actually focuses on to the future expected for that focus.

NVIDIA’s published spec for its 102.4-terabit-class CPO switch explicitly lists 512 lanes. The high-speed electrical lanes did not disappear; they only moved from outside the package to inside. The standard-bearer of the farthest-out camp, optical I/O, is Ayar Labs, which introduces its product TeraPHY as ‘a retimer that cleans up the electrical signal and hands it over to the optical link.’ A retimer takes a signal weakened along the way, restores it to a clean state, and sends it on: a role much like an EV charging station on a long route. To do this, a SerDes circuit has to go inside the retimer. In effect, Ayar Labs has put forward ‘the SerDes in front of the optical link’ as its flagship product.

A sharp reader will surely ask this question:

> An optical fiber can carry several beams of light at different wavelengths on a single strand (wavelength-division multiplexing, WDM), so why bother serializing at all?

A fair point, and that is exactly what the industry does. The next-generation IEEE standard specifies 800 gigabits carried on four wavelengths over a single fiber. But what each of those four wavelengths carries is data serialized at the 224G class (200 billion bits per second) we saw earlier. The approach is not ‘stop using SerDes’; it is ‘multiply the SerDes lanes here.’ In this respect, fiber is undeniably attractive. But physical constraints exist here too. WDM does not come free. Parallelizing light means adding an entire set of laser, modulator, and receiver components for every wavelength, and that, too, is a cost. The next-generation spec stopping at four wavelengths is a compromise struck around exactly this cost (come to think of it, the number 4 seems to have something magical about it. PAM4, too..).

## So, Should I Just Buy the Best SerDes Company?

Whichever architecture wins, demand for high-speed electrical design skill is not going away; that much is now well understood. That is the technology side of the story. As investors, we arrive at the one-dimensional conclusion: “Fine, then I should invest in the companies that are good at SerDes.” Unfortunately, companies that make money by putting this IP front and center are hard to find. If today is the first time you have encountered this term, that in itself is evidence of the technology’s low visibility. Take cars as an analogy: the engine is the heart of the car, but companies that made big money selling pure ‘engine blueprints’ are rare. The big money is made on the finished car that carries the engine (with EVs as the exception, of course).

We need to sharpen the question beyond ‘who is best at SerDes.’ ‘Who is converting SerDes skill into money, and how: in systems, in products, in components?’ In Part 2, I will connect the flow of technology to the flow of money. We will look at how 13 key companies put this skill to work from the component, product, and system angles, and we will also look at one more inventive use of it, perhaps the most valuable one of all.

### Key Sources

- Standards and industry documents: OIF (copper reach and power targets, PAM signal analysis), IEEE 802.3 (next-generation optical specifications)

- Company technical materials: NVIDIA (datacenter power, CPO switch specifications), Ayar Labs, Panasonic (board material datasheet)

- Job postings: NVIDIA, Marvell, Intel, and Cadence career boards (viewed 2026-08)

- Press releases and filings: Qualcomm (Alphawave acquisition)

Disclaimer: This article is intended as a reference for understanding the industry and its underlying technology and was not written as investment advice. The figures and information used in this article are based on publicly available materials. The author may hold shares in companies mentioned in the article. All investment decisions and their outcomes are the reader’s own responsibility.

Copyright: This article is available free of charge. You are welcome to share or redistribute it, provided that you credit Nutty’s Research and include a link to the original article.

Share

Nutty's Article Atlas
