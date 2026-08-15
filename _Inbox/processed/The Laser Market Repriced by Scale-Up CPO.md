---
publish: false
date: 2026-08-08
tags: [research, email-backfill, Damnang]
source: 'https://damnang2.substack.com/p/the-laser-market-repriced-by-scale'
source_type: web-clip
sender: damnang2+the-optical-edge@substack.com
---

# The Laser Market Repriced by Scale-Up CPO

TL;DR

- Pluggable does not shrink because CPO arrives. Revenue per port falls 39 percent, but port volume grows from 44 million in 2026 to 150.4 million in 2030, so the total market grows.

- NVIDIA’s four-times-fewer-lasers figure is measured against EML. Recalculated on the CW-DFB basis used today, the count halves but higher power is required, so the laser amount per port rises from $8 to $30.

- Whatever CPO share is assumed within scale-out, the 2030 market stays between $70 billion and $74 billion. The real variable is the scale-up optical transition, which takes it to $113.8 billion.

- Laser die grows 24 percent a year on a scale-out basis, below the overall market, but reaches as high as 61 percent once scale-up opens. That is where the room for repricing sits.

- On names, Lumentum and Coherent are the most stable, and among the two I view Coherent slightly more favorably for its vertically integrated structure. AAOI and AXT are conditional positions sized to their respective logic, and Sivers is approached at the right price in the way a high-beta name should be.

- All figures in this piece follow the assumptions of the model I built.

The biggest confusion in discussions of CPO is that scale-out and scale-up are used without distinction. With NPO added to the picture, the market’s misreadings have grown further.

I have written several articles on CPO so far. In this one I want to start by resolving this structural confusion. From there I will use my own model to examine how much room the scale-up CPO market has to be repriced, and analyze the laser names that would be repriced along with it.

Let us begin.

Contents

- Pluggable, CPO, and NPO

- How Long Will NPO Last

- Three Misconceptions About CPO

- The Real Variable Is Scale-Up

- Which Laser Companies Get Repriced

### Why CPO Is Becoming Inevitable? [CPO Special Part 1]

### CPO, Fully Dissected [CPO Special Part 2]

### The Illusion of CPO [CPO Special Final]

### The Market Doesn’t Know CPO Yet

Disclaimer

This material is written for informational purposes and does not recommend the purchase or sale of any security. The author may hold positions in the names mentioned, and scenario results depend on assumptions and may differ from actual outcomes.

Responsibility for investment decisions and their outcomes rests with the investor. Conduct your own research and invest on that basis.

## 1. Pluggable, CPO, and NPO

The method mainly used in optical communications today is pluggable.

Because the structure plugs an optical module into a cage on the front of the switch chassis, a failed module can be pulled and replaced in place, and the same form factor can be purchased from multiple suppliers.

The problem with pluggable, as shown in the figure, is the distance from the switch chip to the faceplate. Electrical signals become harder to maintain in waveform as they travel further, and this can lead to signal loss.

So at this stage a DSP (digital signal processor) that restores the signal is essential. Of the 15.5 watts a typical 800G module uses, 6 to 7 watts are consumed by this DSP chip, and adding the share used by the transmit circuitry on the switch chip side to drive the long board section brings the power on a single port to around 30 watts.

What is being developed to solve this power consumption is CPO (co-packaged optics),

which puts the optical components in the same package as the switch chip.

As the electrical path shortens to microns, the DSP can be removed. Power per port falls more than 70 percent versus pluggable, from 30 watts to 9 watts, and emptying the front cages also removes the limit on how many ports a single chassis can hold.

However, the disadvantages of CPO are also clear.

Because the optical engine must be attached in the same package as the switch chip, manufacturing difficulty rises sharply, and the more tightly the optical engine is integrated into the package, the larger the replacement unit becomes on failure.

To reduce this manufacturing, yield, and service burden of CPO,

the compromise that took shape alongside CPO is NPO (Near-packaged optics).

NPO places the packaged switch ASIC and the optical engine close together on a common high-performance substrate, with the optical engine configured as a separate part or a socketed module.

This allows the ASIC and the optical engine to be tested separately and then joined, and depending on the implementation, rework or replacement at the optical engine level is also possible.

The electrical path is longer than CPO but far shorter than conventional front-panel pluggable, so a significant portion of the power benefit can be secured.

## 2. How Long Will NPO Last

From the explanation so far, NPO looks technically better than CPO. It secures a significant portion of the power saving versus pluggable while allowing the switch chip and optical engine to be tested separately and then joined, and depending on the design, replacement at the optical engine level is also possible. It is easy to keep away from the heat source, and once a standard is established, optical engines can be chosen from multiple suppliers. So why not have every company go with NPO instead of CPO?

The obstacle lay in the fact that the socket itself is a part that had to be newly created. A high-density connector of the NPO type that sends 200G on a single lane while holding loss to a minimum did not exist before, and putting optical engines from different companies into the same socket requires agreeing on a specification first. For this, a number of suppliers launched the Open CPX MSA in 2026 to develop a common specification. Participating companies include Ciena, Coherent, Marvell, Molex, Samtec, and TeraHop.

## The War of Light Has Begun

On March 12, 2026, three separate optical-related MSAs dropped on the same day. That does not happen by coincidence. It means the entire industry has converged on the same conclusion: the physical layer of AI infrastructure needs to change, and it needs to change now. Call it the opening shot of the Optical War.

The larger constraint is the speed the socket can withstand. When the rate carried on a single lane doubles from 200G to 400G, more signal is stripped over the same trace, and the amount reflected back at surfaces where parts meet also increases. It means a point arrives where inserting a single socket is enough for the signal to fail. The OIF (Optical Internetworking Forum) and the Open CPX MSA have this on their roadmap.

If it is solved, NPO carries into the next generation.

If not, CPO without the socket has to be used.

To summarize, once manufacturing difficulty, reliability, and serviceability are solved, performance itself favors CPO.

But in the current generation the gap NPO concedes is small, so a trade holds in which it is exchanged for assembly yield, supply chain flexibility, and serviceability. In systems where power and bandwidth density must be pushed to the limit, CPO leads; in systems where part separation, test yield, supply chain, and serviceability matter more, NPO is retained.

NPO is commonly thought of as an interim step before CPO.

But given that the two methods have different optimal points and that this optimum is divided by the character of the system, I view it as closer to a parallel structure than an interim step. For reference, the industry movement I hear from optical specialists in the field points in the same direction. The model calculated later is also set on this view, with both methods in use through 2030.

## 3. Three Misconceptions About CPO

### First, CPO shrinks the pluggable market and pushes optics vendors out?

This misconception starts from the idea that once the pluggable module disappears as a product unit, CPO takes over existing volume and the market contracts accordingly. Viewed only from a per-port revenue perspective, it can be correct. For example, converting a CPO switch bill of materials on an 800G basis, the revenue an optics vendor recognizes falls from $520 for CW-DFB pluggable to $317, a decline of 39 percent.

But calculating the market as a whole gives a different picture.

First, pluggable is not a market that disappears because CPO arrives. Even in systems using CPO switches, the ports on the communication card next to the accelerator remain pluggable, so the two methods coexist by structure.

The same holds when looking at total market size. Optics follows the pace of data center expansion, so the prevailing view is that market size continues to grow. Models differ, of course, but in the model I use, total optical port volume grows 36 percent a year from 44 million in 2026 to 150.4 million in 2030, which shows that everything else grows while CPO grows.

Also, the module disappears in the transition to CPO, but the optical engine, fiber attach, external laser module, and shuffle box fill that place. What the optics vendor sells changes from the module to these parts; the revenue itself does not disappear.

### Second, CPO cuts laser revenue?

The source of this misconception is NVIDIA. When it unveiled its CPO switches, it stated that lasers are reduced to a quarter compared with legacy designs, and investors read this as meaning the number of lasers a laser company sells becomes a quarter.

The problem is that this figure is a simple comparison between EML pluggable and CPO. EML builds the light-emitting section and the data-modulating section on a single InP chip, so one chip is required per signal lane. For example, configuring 800G as 200G × 4 requires four dies.

The laser used in current CPO technology, however, is CW-DFB, a silicon photonics based laser. In this method InP only emits light (CW laser) and data is carried through the adjacent silicon chip, so a single high-power laser is divided across several lanes. CW-DFB in pluggable requires two dies per port and CPO requires one, so the reduction is precisely not to a quarter but to a half.

The more important point here is that counting laser dies alone is not enough. Even within CW-DFB, CPO has the light source outside the package and must use a far higher-power laser, in which case the amount per die rises from $4 to $30 and the amount per port from $8 to $30. And under the eight-wavelength specification used in scale-up, two dies are required again, so it can rise to $60.

To restate, NVIDIA’s figure is not wrong. But recalculating on a CW-DFB laser basis for an accurate reading shows that the misconception that laser revenue falls under CPO is incorrect, and that the structure instead points to an increase rather than a decrease.

### Third, timing the CPO transition is the most important thing in optics investing?

This is the view that optics earnings diverge sharply depending on whether the transition arrives a few years earlier or later. But within scale-out, the size of the market does not change much regardless of what CPO share is assumed. The 2030 scale-out market stays between $70 billion and $74 billion on any CPO share.

A delayed scale-out transition is not a loss either. If it is postponed because of integration difficulty, bandwidth demand is unchanged, so volume stays in pluggable longer, and pluggable is the structure with the highest optics vendor revenue per port. It means a longer cycle for a line that is currently sold out.

But not all delays are the same. A delay in the scale-up transition is a different matter. Whatever mix is assumed within scale-out, the 2030 market is between $70 billion and $74 billion, but with scale-up open it becomes $113.8 billion. The timing that needs to be called is this one, not scale-out CPO.

Share

## 4. The Real Variable Is Scale-Up

Why does scale-up matter? If scale-out is the network that connects multiple nodes and racks to widen cluster scale, scale-up is the fabric that binds multiple accelerators within a single tightly coupled compute domain into what functions as one large compute resource. The bandwidth required per accelerator is at least nine times higher, and port count is required in proportion. In other words, what is called the explosive market potential of CPO refers to this scale-up segment.

What do the market projections look like with scale-up reflected? The chart below is calculated with my own model, assuming the scale-up optical transition begins in 2028 and estimating 2030 adoption at 15 to 30 percent. For architecture mix, I assume NPO is retained as a parallel structure for the reasons seen in section 2, and set 2030 at 25 percent pluggable, 35 percent NPO, and 40 percent CPO.

Against a growth rate of 30 percent a year calculated over four years on scale-out alone, adding scale-up brings it to 46 percent, and setting adoption at 30 percent brings it to $155.5 billion and 57 percent.

What deserves attention here is that the laser side moves more than the total. On a scale-out basis, laser die grows 24 percent a year, below the 30 percent for the overall market, whereas with scale-up open it can reach as high as 61 percent and exceed the market’s growth rate. This is why I have continued to emphasize the importance of InP and the laser companies across several articles.

Share

## 5. Which Laser Companies Get Repriced

Lumentum leads in the high-power band. At OFC 2026 it demonstrated an ELS module carrying an 800mW light source, and it has taken its largest ELS order to date.

Coherent’s strengths are scale and vertical integration. It demonstrated a 6.4T socketed CPO combined with its own ELS and its own high-power light source, and has moved to a 6-inch line.

AAOI holds the position of manufacturing within the United States. It has released a 400mW class product and is expanding its own laser fab threefold by the third quarter of 2027. Its scale is far smaller than the two companies above, so a single hyperscaler adoption materially changes results.

Sivers has entered the ELS module market through a consortium. The base is small enough that a single adoption moves it significantly.

AXT is not a laser company. It makes the InP substrate underneath. The reason for including it is that the InP die area demand calculated earlier moves along nearly the same path as laser revenue. Unlike optical engine vendors, its exposure to any particular CPO implementation is relatively low, which is also an advantage.

As mentioned across several articles, my laser investment approach to date follows the rules below.

First, for those with strong conviction on CPO and optics, Lumentum and Coherent would be the most stable names. Among the two, I view Coherent slightly more favorably because of its vertically integrated structure.

Second, AAOI and AXT are also attractive, but it is better to size them conditionally according to their respective logic. AAOI is a name to invest in on the logic that hyperscaler orders are confirmed and will continue, and AXT on the logic of strong conviction in an InP shortage persisting despite Chinese regulation.

Third, Sivers is worth an aggressive position on the premise that the price is attractive. As I always argue, take an approach suited to a high-beta name. In my own case I watch this name for short-term trading purposes.

### What to Watch

The other view on lasers is the argument that if new capacity clears the top power band faster than expected, the price premium disappears before volume arrives.

That is correct in theory, but taking together what I hear from the field to date, there seems little room for that timing to be pulled forward. The 300 to 400mW band is not a process where yield follows immediately from adding lines, and Lumentum’s new fab will not operate meaningfully until 2028. By around that time scale-up volume begins arriving in earnest, so supply expansion and demand growth overlap in the same year.

That said, this calculation rests on the premise that scale-up opens from 2028. Until then, there are three things an optics investor should keep checking.

1. Announcements from accelerator companies on adoption of scale-up optical interfaces and their timing

2. Scale-up optical engine and laser module orders appearing in optics vendor results

3. The share of high-power lasers in revenue
