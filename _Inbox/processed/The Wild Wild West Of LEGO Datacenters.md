---
publish: false
date: 2026-07-29
tags: [research, email-backfill, SemiAnalysis]
source: 'https://newsletter.semianalysis.com/p/the-wild-wild-west-of-lego-datacenters'
source_type: web-clip
sender: semianalysis@substack.com
---

# The Wild Wild West Of LEGO Datacenters

# The Labor Problem and Modularization to the Rescue

Today we dig into the world of datacenter construction, because how datacenters are built now bears little resemblance to how the industry has historically done it. Concrete walls arrive as finished panels, mechanical and electrical rooms arrive wired, and sometimes even entire data halls arrive on the back of a truck. Some of the largest datacenters in the world are increasingly assembled the same way you assemble your new Spider-Man LEGO set, only that the bricks weigh 50,000 pounds and are a tiny bit more complex. This is the world of modular construction.

From Hyperscaler to Colos to now even the AI labs, modular construction has become the default playbook for building fast. Our Modular Tracker, included in our SemiAnalysis Industrials Model, tracks over 61GW of modular capacity and 1,000+ sites using some form of modularization or prefabrication strategy. Full breakdown by modular category and equipment type is included in the Industrials Model. We estimate that modular penetration will reach 30%+ of total live capacity by the end of 2028.

Ultra-fast modular designs are increasingly the norm. Over a year ago, we were the first to call out Meta’s drastic change to using “tent” buildings. As shown below, AWS is now rolling out at very large scale their own modular design codenamed “SAMDC”.

To understand the reason, we need to start looking at one of the structural bottlenecks that capitalist incentives alone cannot build past: labor.

Our recent articles have been a journey toward that bottleneck. In “The Case for Space Datacenters”, we showed the ceiling on terrestrial capacity. Last month, in “Stop Saying Half of 2026 US Datacenter Capacity Is Canceled”, we argued that most bottlenecks are misunderstood and solvable. Trade labor is an exception here, as you cannot quickly solve for a shortage of electricians and pipefitters. The race for that talent became a true constraint long ago, visible when operators like Crusoe pumped wages by 30% to bring talent to Abilene’s site, which required over 9,000 workers at its peak.

Aiming to size the labor shortage trade by trade, we now also include the Labor Model as part of the Industrials Model. It translates the state-by-state buildout from our Datacenter Model into hours of demand for every trade and sets them against reachable labor supply. To frame the problem before modularization enters the picture, the chart below is ex-modular construction, with labor demand curve assuming labor per GW stays roughly flat over the forecast period and doesn't yet reflect the benefits we'll cover later in this article. Reachable labor supply in each state, on the other hand, is affected by how much capacity is being built, and how much labor is being pulled, in other US states.

Electricians are a clear case, as they represent 30-40% over the total construction man hours in a datacenter project. The chart below shows an estimated electrician shortage emerging in 2027 driven by the huge mission-critical demand. On a state-by-state basis, the shortage is most acute where the buildout concentrates, like Texas and Ohio.

The response is that every operator and vendor are now racing toward modularization, which essentially means pulling repeatable work off-site and into factories, where everything from wall panels to power rooms and cooling skids are built in parallel with the site and delivered as finished units. Besides, it does more than ease the labor crunch, promising large speed and time-to-build gains. And today, speed is revenue.

The shift is already underway, with Compass and Switch being the first operators to move parts of their datacenter builds offsite. Using some form of skidded solution for electrical equipment is now pretty standard for every operator. AWS’s Project Houdini prefabricates the white-space buildout and collapses the time before servers go in from months to weeks. Meta is standing up fabric-clad “Tent”-like halls. And a wave of new entrants, both in the OEM and the System Integrator space, are building specifically around modular.

In this deep dive we rebuilt the modular case bottom-up against some of the speed and cost claims made by vendors like Vertiv or Schneider, finding that modular construction can compress the construction window by ~36%, or 7-9 months, and is ~8% cheaper on a Capex/MW basis. We also analyze how vendors like Vertiv are able to expand their value capture per project by offering the full stack solution, going from their historical ~$3.5M/MW content to ~$7M/MW with the modular solutions.

The problem, though, is that today everything seems to be modular and vendors, EPCs and Colocation providers many cases are describing entirely different things. To bring some order to this wild west, this article unpacks what modular actually means. We map the vendor landscape building a modular universe of more than 80 players and test whether the vendor claims hold up.

For subscribers, we focus on the main beneficiaries and break down how each player is positioned,  from the public names (FIX, STRL, PWR, VRT, SU, FLEX…) to private challengers such as Infra Partners, Bladeroom, and Faith Technologies, distilling the key insights from our recent Core Research subscriber notes on Comfort Systems: “Modular Capex Is The Moat” and Sterling Infrastructure: “Winning Where It Counts: Quadrupled TAM via Texas, Pacific Northwest, and the Midwest; 2X Content per MW from CEC Attach; ~$6B Run-Rate In View”.

To start off, we’d like to thank QTS, EdgeConneX, Aligned Data Centers, Schneider Electric, Applied Digital, DG Matrix, Aran Industries, Karman Industries, Radiant, and Rajat Bhagat for their contributions and insights during the preparation of this deep dive.

# The Modular Taxonomy

Before we go into the detail taxonomy, let’s start with the basic definitions, because two words concepts often get mixed up: prefabrication and modularization.

- Prefabrication is the broader concept: any part of the build manufactured offsite and delivered ready to install. It is a statement about where the work happened, not about the shape of the thing.

- Modular is narrower. It refers to the actual self-contained units (rooms, boxes, blocks) that ship complete and get bolted together on site. Every modular unit is prefabricated, but prefabrication may not be directly modular.

Hold onto that distinction, because it is the spine of everything below. From here on, we will walk through the landscape the way a datacenter is actually built up, then we will go into details on the taxonomy that makes up the modular market starting from the ground up.

## Understanding The Datacenter Anatomy

At a high level, a datacenter can be seen as simple three stacks of layers: Site, Shell, and Systems.

At the bottom we have the site, or the physical land of the datacenter buildout. This is where grading, wiring, and foundation building take place. This layer cannot be modularized because you have to physically break ground on a parcel of land and pour foundations into it on the set up.

Above that sits the shell, which means the structure, skin, and roof that serve as the backbone and weatherproof the entire datacenter buildout. Inside the shell is where all the equipment and subsystem, including all the mechanical and electrical systems, sit.

Considering that the site itself can not physically be moved, prefabrication strategies are focused on the other two layers, and we take them in that order, working from the outside in.

## Modularizing the Datacenter Shell

The shell is the structure, walls, and roof that hold the datacenter up and keep the weather out. It generally follows either a frame-and-skin design, where the structure and cladding are separate, or a load-bearing panel design that combines both.

In a traditional build, both the skin and the frame need to go up on site. Crews break ground, pour the foundation, then form and cure concrete right where the building stands, one piece at a time. A modular shell starts the same way, on a poured foundation, but from there the structure and panels arrive as finished pieces from a factory, craned and bolted into position once arrived.

The time saving is evident from the graphic above. In the traditional cast-in-place buildout, each pour has to reach roughly 75% of its design strength before the next can go on top. Prefabricated structure sidesteps that wait.

However, the evolution did not stop with prefabricating the same conventional building. The larger gains now come from simplifying the building itself: moving from complex multistory facilities toward repeatable single-story halls, and then toward narrower, purpose-built structures.

### Phase One: Precast Industrialized the Conventional Shell

The first phase is precast concrete described above. Instead of forming and curing the full structure in the field, panels are manufactured under controlled conditions, transported to the site, and craned onto a prepared foundation.

This is not new. Northern Virginia has used precast extensively for years because construction labor was already constrained. CloudHQ’s two-story LC-2 facility in Ashburn is a representative example: its load-bearing shell supports long, column-free spans and enough structural load to place mechanical equipment on the roof.

Nevertheless, the building still took roughly 18 to 20 months to deliver. Precast reduced field forming and curing, yet the underlying facility remained a large, multistory structure facility.

Tilt-up concrete follows a similar logic but casts the panels on the building slab rather than in a remote factory.

This method avoids long-haul transportation and can be the lowest-cost route for a large single-story box, although quality and schedule remain more exposed to site conditions and weather.

### Phase Two: Simplifying the Building

The second phase is where design changes happen. In order to further speed up the time, the industry turn towards alternating the design for simplicity. These buildings use regular structural bays, fewer architectural features, and standardized exterior panels. Steel is often favored because the frame can be fabricated off site, shipped efficiently, and bolted together quickly across a large flat campus.

At the light end is the pre-engineered metal building, or PEMB built in three parts:

- The primary frame serving as the structural skeleton

- The secondary frame tying the main frames together, these are lighter steel member like roof purlins that span between the primary frames.

- The skin, keep in mind this is different from the frame. They are the thin light weighted metal panel whose job is to protect the interior from extreme weather conditions

This is the fastest option since all parts arrive cut, punched, and labeled, a crew simply need to bolt them together on the site. Furthermore, a light steel structure needs far less material than concrete.

More demanding halls use structural steel - heavier, hot-rolled beams and columns fabricated off site and bolted into a rigid frame. It costs more than a light PEMB but supports wider spans, heavier loads, and more complex layouts.

QTS’s Cedar Rapids campus shows the speed and scale this approach can unlock. The current 420 MW phase spans approximately 2.8 million square feet and uses roughly 28,000 tons of structural steel. QTS moved from groundbreaking to topping out in about five months, with the broader building delivered in approximately 11 months.

The exterior is then closed with prefabricated cladding, most commonly insulated metal panels. Similarly, we see this approach with Crusoe’s Stargate campus in Abilene, each building used roughly 672 factory-made panels. The panels were fabricated in under 40 days and installed at approximately 15 to 20 per day, helping bring each building to a dried-in shell in under eight weeks.

The speed advantage therefore comes less from steel itself than from what it enables: simple single-story halls, repeatable structural bays, fewer field interfaces, and a supply chain that can be reproduced across markets. It can also reduce labor and structural material per MW compared with a dense multistory design.

The main trade-off is land. Single-story campuses require more acreage, but that is often acceptable in newer AI markets where land is cheaper and deployment speed matters more than maximizing MW per acre.

### Phase Three: Purpose-Built Rapid-Deployment Shells

The third phase pushes simplification further by designing the enclosure around a more specific deployment model. Narrower, lighter structures can reduce the amount of conventional shell work and support faster repetition, although tighter optimization may leave less flexibility for future equipment or layout changes.

Meta’s rapid-deployment structures at Prometheus campus in New Albany are the most visible extreme. The aluminum-framed, fabric-clad halls provide enclosure and weather protection without constructing a conventional permanent shell. Each structure is roughly 125,000 square feet, and satellite tracking showed eight standing by April 2026 after the buildout was announced in July 2025.

That does not mean Meta completed a full datacenter in nine months. The tents accelerate the enclosure, not utility interconnection, power, cooling, or commissioning. They also trade away some of the durability and long-term flexibility of a permanent concrete or steel building.

AWS is moving in a similar direction with its newest modular builds. Rather than treating the shell as a large generic warehouse, AWS is using narrower and more repeatable structures organized around the systems installed inside. The result is less building per MW, shorter structural spans, and fewer interfaces for field crews to assemble.

The common thread is that shell modularity is increasingly about design simplification, not just prefabrication. Precast moved concrete production off site but largely preserved the conventional building. Standardized steel made single-story halls easier to repeat across markets. Purpose-built structures go further by reducing the size and complexity of the shell itself.

The cost savings thus come from removing floors, reducing structural complexity, decreasing labor on site, and repeating the same enclosure / supply chain across the campus. Once the shell is dried in, the larger modularization opportunity moves inside, to the power, cooling, and white-space systems that turn the enclosure into an operating datacenter.

## Modularizing the Equipment and Subsystems

Equipment and subsystems are where most of the real modularization is happening, and the offerings span an enormous range, from a single piece of equipment all the way up to an entire building delivered ready to switch on. Previous deep dives already covered in big depth the anatomy of Mechanical and Electrical systems. Besides, before we start naming categories, it helps to fix some vocabularies:

- Component: The lowest level of form factor. It is a single piece of equipment manufactured in a factory.

- Skid: First common modular form. It is a group of components mounted on an open frame. Instead of shipping each piece separately, the equipment is pre-arranged, configured, and shipped together as one package.

- Module: A skid but in an enclosed space. It can go anywhere from a simple power room to a prefab mechanical/electrical room similar to a skid, but only it will become a module if you put walls and roof on top of it.

- Container: A specific form of module using ISO container for packaging. An ISO container is built specifically for standard shipping dimension, which means it can travel anywhere on normal transport with a truck without limitation.

- Prefab Datacenter block: Facility scale buildout that stitches multiple factory-built module into a much larger facility block. The intent of these block is to serve as an end-to-end datacenter buildout

This is like a ladder, from 1-5 increasingly factory integration and scope. If you look carefully, you may also be able to realize the first 4 levels are better known as the subsystem modularization. This is where the supplier delivers one part of the datacenter as a factory-built unit. That unit is arrived assembled and tested, but still has to be connected into the broader facility before it becomes useful.

The last level and sometimes the fourth level, moves closer to a whole facility modularization. Here, the supplier is delivering a much larger portion of datacenter as an integrated product.

## Subsystem Modularization

With the vocabulary in hand, we can now start climbing the ladder, and the natural place to begin is at the bottom, with subsystem modularization. This is the larger of the two families and where most of the market lives today. We start off with the grey space, and modular power block is where most people think of when discussing modular design.

### Modular Power Blocks

A power module is a factory-built electrical room or power block that packages the major electrical equipment into a containerized box. Among all subsystem modules, power is one of the most natural areas to modularized because the equipment lineup is well defined and lots of different pieces are needed to assemble the units. The electrical fit-out and commissioning take on average 5.5 - 16.7 months on a 50MW power hall.

To illustrate with an example, let’s see Flex’s modular power solution, built through the Anord Mardix unit below:

Flex sells this in two versions, the power skid and the power module pod, which is the same lineup wrapped in a secure enclosure. Inside the room, you will find major electrical components laid out like a power train.

As you may have noticed, the module also contains the busway system like the IBAR feed above the building which bridges the power pod to the data hall. The CRAH units, or computer room air handler and fire protection system, also exist to help manage the air temperature inside the enclosed shell and protection against unexpected conditions.

By our own estimate, the power block is where the schedule payoff concentrates. Moving just the power scope into the factory, roughly ~26% of the build by content, gets a hall to IT-ready ~22% faster, ~13 months against ~16.7 for stick-build, and around ~5% cheaper per MW, largely by compressing the mechanical-and-electrical fit-out from ~5.5 months to ~2.5.

Lastly, within modular power blocks, a new subcategory is emerging, which we can define as “software defined” power routing blocks. Instead of packaging the conventional transformer+switchgear+UPS+battery chain into a box, companies like DG Matrix replace portions of that chain with power-electronics-based multi-port routing. These systems can connect grid, generation, storage, and DC loads through a common controlled power platform.

### Modular Cooling Blocks and Prefabricated Cooling Infrastructure

Similar to a power module, the cooling block packages the datacenter’s cooling loop into one integrated subsystem. At first glance, the case for modularizing cooling is weaker than for power, since there are simply fewer pieces to pre-assemble. But as primary and secondary loops grow more complex, the ability to add cooling capacity in repeatable, modular increments becomes far more attractive to operators.

Focusing on the TCS loop, the majority of modular efforts are centered on skids for CDUs. Airedale by Modine’s skid-based CDU (for more on cooling systems, read our Cooling deep dive here) is an example of this category.

The Airedale by Modine skid-based CDU is a 2 MW-class unit arrives on a pre-manufactured skid with everything included, from the red-and-silver cooling loop to the buffer tanks on the top right, and even the leak detection system built into the end of the skid. On site, all the crew needs to do is hook up the two loop connections and a power feed.

On the other hand, the value proposition for prefabricated cooling systems is stronger when looking at the secondary loop and the outdoor mechanical yard, where piping and other outdoor cooling infrastructure is prefabricated, significantly reducing the civil, piping, and controls work completed onsite.

When thinking about cooling equipment, keep in mind that much of it was originally designed for hospitals, campuses, and industrial process cooling rather than GW-scale datacenters. At that scale, large footprints and hundreds of co-located units can create issues such as hot-air recirculation and heat islanding.

The Vertiv installation above shows a conventional mechanical yard. The cooling plant sits outside the data hall as a separate piece of infrastructure, with chillers, pumps, piping, and supporting steel assembled around the building.

Some datacenter developers, like QTS, are now prefabricating most of the piping infrastructure, which allows for faster installation while maintaining high quality. That becomes especially valuable today, given the increasing piping requirements of dense liquid-cooled deployments.

A handful of new entrants are now even attacking the whole yard. Karman Industries’ CO2-based Heat Processing Unit (HPU) is a purpose-built unit borrowing SiC power electronics and permanent-magnet motors from EVs, and compact turbomachinery and advanced heat exchangers from aerospace. The HPU, which is configurable to each site, ships as an outdoor-rated NEMA skid at 4 to 5 times conventional power density and cuts yard footprint by 60 to 80%.

## Other Modularized Options

Power and cooling are not the only parts of the datacenter that can be move into the factory. The same concept can be apply across the gray space such has the energy storage (BESS) system, water treatment skids, Fire safety system, and many more.

Many are not on the critical path for construction timeline, or they are small enough to be able to build on site. Moreover, where these systems do get modularized, they often ride along inside a large unit rather than shipping separately. For example, the Schneider EcoStruxure for example was built in with the fire protection system.

### Factory Built White Space

The intention of the factory built white space module is to replace hand-built data hall and manual on-site wiring with a unit made factory product. This means operator can directly put compute in place without the need to figure out wiring and connection.

The whole package comes ready for the rack frames, and all the last mile connection points the rack need to operate. Think of it like a prepared envelope for compute, its organized where racks go, provide the cable and connection to how they receive power and extract heat, and include prefabricated power busway and technical water loop situated above the rack.

Take Schneider’s EcoStruxure Pod as an example. The image above shows the black cabinets forming the IT rack rows where products like Nvidia GPU servers would be installed, a total of up to 40 racks can be placed in this one system. Above the racks, the gray overhead infrastructure is the distribution layer. It carries the busway that delivers power to each rack, containment to capture hot air as some of the solution will still be air cooled, technical water loop to distribute liquid cooling that extracts heat, and cabling that connects each servers.

The interesting thing about this is the product design behind it. A factory white space must be able to serve different custom needs and therefore, suppliers like Schneider work with Nvidia to support more than 30+ reference designs. The buyer can essentially pick the specs that matches the chips it wants and gets a hall that is pre-coordinated with the matching required power and cooling module. In the coming section we will study in more detail how the design process takes place.

## Whole Facility Modularization

Whole Facility modularization is the literal datacenter-in-a-box model. Instead of delivering individual parts, the supplier delivers a complete or near-complete datacenter block.

### Containerized Datacenters

Starting with a containerized datacenters, this is the 4th part of the form factor design where the datacenter itself is packaged into an ISO-style container or purpose-built weatherproof enclosure. Like we had discussed, the reason why this option exist is for the ease of transportation.

As the image shown above, you can see almost everything inside the box: the IT racks, the power equipment, the batteries, and even the cooling system.

These types of design are commonly used in edge computing, industrial environments, remote or unused spaces, and the product is most useful when the buyer needs a smaller datacenter quickly. For AI workloads, the buyer is usually not a compute startup chasing scale but an asset owner that needs low-latency inference at a fixed physical location.

The main limitation of this buildout is density. The same form factor that makes the unit portable and fast to deploy also fixes the layout. That’s why suppliers are pushing beyond the containerized model toward all-in-one prefab datacenter blocks.

### All-in-One Prefab Datacenter Block

The all-in-one prefab datacenter block is the more ambitious version of whole-facility modularization. Here the supplier delivers a larger facility block with more of the datacenter already integrated before delivery.

Vertiv MegaMod shows what this can looks like in practice. The structure effectively is a modular datacenter with the major systems packaged into one enclosure. The center of the block contains the IT racks, where servers are installed. Above and around the racks runs the fiber optics and cable-management pathways, along the perimeter are all the supporting infrastructure systems like cooling and power units.

The system’s 1 MW reference design can stretch to approximately 26.5 meters long, 24 meters wide, and 4 meters high in dimensions. While the MegaMod plus version can extend to as much as 31 meters wide. You may be wondering, if it’s this big how can it be ship to the site? In reality, the structure needs to be broken into transportable prefabricated sections, shipped through a standard heavy-haul logistics truck, and then connected and commissioned as one.

## Platform Modularization and Reference Designs

The last step in whole-facility modularization moves beyond any single vendor’s block into a standardized reference design for the facility itself. In the same fashion the industry has reference designs for rack systems and CDUs, Nvidia now publishes one for the entire AI factory: Nvidia DSX. It was first unveiled as an Omniverse digital-twin blueprint at GTC Washington in October 2025, formalized as the Vera Rubin DSX reference design in March 2026, and more recently expanded into the full DSX platform.

The DSX reference designs are validated AI factory architectures covering compute, networking, storage, hardware cluster design, and also the facilities side, including power, cooling and controls. Even civil, structural, and architectural design. The value proposition behind is that Nvidia’s DSX Max-Q maximizes token per watt within a fixed power budget, and DSX Flex facilitates the connection the facility to grid services, dynamically adjusting power draw and orchestrating demand with hybrid onsite generation.

When deploying a DSX facility, through the Omniverse DSX Blueprint, an operator first builds a digital twin of the facility, simulates layouts, power topologies, thermal behavior, and operational policies in real time, and optimizes the design before construction begins, then reuses the same validated architecture across sites. For example, CoreWeave is already using DSX Air to build and test digital twins of its AI factories.

Besides, the whole DSX ecosystem includes pretty much all the supply chain: Cadence, Dassault Systemes, Eaton, Jacobs, Nscale, Phaidra, Procore, PTC, Schneider Electric, Siemens, Switch, Trane or Vertiv. Vertiv’s OneCore, for example, packages power and cooling into standardized 12.5 MW pods that can be combined into larger AI-factory deployments

EdgeConneX estimates that a common design can advance a project to roughly a 30% to 60% permit set before site-specific localization is complete, allowing substantial off-site work to begin earlier.

# Vendor landscape

If you have made it this far, you should have a working feel for the categories. You should also, maybe be a little buried in names. We have put a power module from Flex, a CDU from Airedale, a data-hall pod from Schneider, and an all-in-one datacenter from Vertiv all in front of you. So before going further, it helps to step back and lay the whole market out on a single map.

Our universe runs to over 80 players, and laying them out this way is useful because two patterns jump out right away.

- The depth is in the subsystems. The power-room and cooling modular are by far the most crowded

- The same names keep showing up across columns, because a vendor like Vertiv, Schneider, or Eaton sells a power module, a CDU, a white-space pod, and a whole block all at once.

## Owning the Integration: Who actually does the modularization?

The vendor landscape above maps who builds each piece, but not how those pieces become a module or who is on the hook when they do. From the solution provider’s point of view it has three answers:

- At one end the operator holds both rights: it specifies the equipment, buys it directly, and hands it to an integrator purely for assembly.

- In the middle sits the EPC- or integrator-led buildout, where the operator still sets the performance requirements but hires an EPC or integrator to source, coordinate, and build.

- At the far end is the OEM-led model, where a vendor like Vertiv designs and sells its own stack as one finished product, as it does with the OneCore portfolio

### Operator-Led Modularization

This is where the operator engineers the specification themself, procures the equipment directly as owner-furnished gear, and hands it to an integrator purely for assembly.

This model requires the operator to have a deep in-house engineering and procurement team to specify and source every component, and the willingness to carry all of the cost, inventory, and lead-time risk.

In a supply-constrained market that risk is sharp, since the operator is competing for scarce transformers and switchgear without a vendor’s allocation leverage, unless it buys at enough scale to have that leverage of its own.

That is why operator-led modular is effectively confined to the largest hyperscalers. AWS, for example, engineers its own prefabricated data-hall skids under Project Houdini and procures the equipment directly, using Cupertino Electric as design partner.

Aligned is another example of operator-led modularization, although it relies on external integration partners for manufacturing capacity. Aligned defines the architecture, owner-furnishes the major components, and controls the commissioning and quality program, while its integration partners receive, store, assemble, and test the equipment across multiple factory locations. The partner provides the production footprint, but the modular system remains Aligned’s design.

### System-Integrator or EPC-Led Modularization

The EPC-led modularization includes system integrators or construction companies that take mostly third party equipment and convert it into a skid/module. The integrator does the assembly, installation, factory testing, enclosure, and is the party in charge of delivering the finished skid to the end customer.

The companies acting an integrators are both construction companies that have the footprint and capabilities to do the integration, like Comfort Systems, Sterling Infrastructure or Quanta’s Cupertino Electric, and specialized modular integrators, like PCX, Nautilus, DXN, Infra Partners, Bladeroom, etc.

This type of modularization is vendor agnostic, which means that the customer keeps more control over the datacenter design, while the contractor moves part of the construction sequence into a prefab shop. The EPC buys the equipment, assembles it, wires it, pipes it, tests it, and ships it as completed construction scope.

Take Comfort Systems as an example. It is a MEP contractor, not an equipment maker, so it acts as the layer that procures and assembles the gear on the operator’s behalf. The operator decides what equipment it wants and Comfort Systems does everything else. It runs that work through Environmental Air Systems and TAS Energy across 3.5+ million square feet of shop floor in Texas and North Carolina.

That concept is particularly attractive to hyperscalers. A big operator usually already knows exactly what equipment and design it wants, so it has no interest in buying someone else’s fixed system. Working with EPC integrators like the kind for Comfort System, the operator keeps its own design and its own gear, and simply hands the building of it to a factory instead of a jobsite.

### OEM-Led Modularization

Here the equipment vendor turns its own datacenter infrastructure stack into a repeatable module or platform. Although the product can still be configured for a specific site, the starting point is usually an off-the-shelf module using OEM’s own architecture.

Vertiv OneCore is a clear example. Instead of selling single equipment devices, Vertiv combines all the layers into a single modular platform. This platform integrates Vertiv’s power, thermal, cooling, and IT infrastructure technologies inside a Vertiv’s supplied steel shell.

That is what makes it OEM-led, the customer is buying into Vertiv’s entire integrated stack rather than asking an EPC integrator to assemble equipment line ups. This also allows Vertiv to capture higher content by selling the entire stack end to end, with the TAM expanding up to ~$7M/MW for some of their full-stack solutions.

The tradeoff is capacity and execution risk. Besides the fact that these companies are going up the value-chain toward market segments they were not previously involved in, OEM-led modularization can only scale as fast as the OEM’s factory capacity, supplier base, and integration teams can support. Vertiv’s modular solutions run lead times of over 12 months today. This is also pushing big OEMs, not only Vertiv but also companies like Schneider and Siemens, to be selective with capacity slot allocation, requiring certain capacity minimums and favoring bigger projects. As a result, operators or developers looking for smaller scale capacity are increasingly working with the System Integrators.

# The Modularization Cycle

By now our readers should be familiar with the different forms of modular solutions and the players leading this transformation. They will also have noticed how different this looks compared to traditional datacenter construction, and will have many questions about the operational implications. Those are the topics we address in this section.

## Stage 1: Solution Design and Simulation

Engineering the solution is the first step. In a field build, some of these decisions can change while construction is underway. In a modular build however, they need to be predetermined, frozen early, and repeatable since the box itself must come in a finish block.

The most important engineering at this stage happens at the facility level. Before a module can be finalized, the design team must define the load, select the equipment, develop the single-line diagram (SLD) and layout, and complete the short-circuit, protection-coordination, and arc-flash studies in tools like ETAP and PSSE. These analyses determine how the system is sized and which components can be used. Because they depend on the full electrical path from the utility connection through the downstream equipment, they cannot be completed on an isolated skid. The facility design therefore has to come first, with the module designed as part of that broader system.

Source: Aran Industries

For 415/480VAC this work is well templated and repeatable. When considering all the implications of the 800VDC transition, it is not as well-templated. A handful of reference designs exist, but none are well baked yet, so the facility-level architecture is still being worked out design by design. This is also the part of the cycle now being automated. Companies like Aran Industries are building build custom software that plugs into ETAP, PSCAD, PSSE, Revit and the other design tools, compressing what is otherwise a multi-month (>2 months), multi-engineer electrical design process into hours of compute plus a single engineer reviewing the output.

### Ownership of the Buildout

Once the design is set, ownership comes down to two questions:

- Who chooses the equipment;

- Who carries the cost, the inventory, and the lead-time risk of the buildout.

Those decisions do not always sit with the same party. An operator may specify a component directly, or an integrator may select it and seek approval.

Colocation operators are a clean exception. A wholesale colo is not bound to any single end-user’s specification, and often does not even know who the tenant will be, so it is free to choose the equipment it wants and commit to it early, without waiting on anyone’s sign-off.

Even then, local availability matters, because switchgear and transformers may carry 12 to 18-month lead times, while generators can require market-specific emissions controls. Customization can also reopen engineering and add roughly eight weeks.

## Stage 2: Packages and Documentation

Once the design is frozen in Stage 1, what leaves the design stage is not a single drawing but a set of documentation packages, produced by different parties in different tools:

- An issued-for-fabrication (IFF) package with the shop drawings telling the factory how to build the skid

- An issued-for-construction (IFC) package telling the site how to receive, place and connect it

- A separate permitting and commissioning documentation set, proving the design will pass code and testing.

This stage is largely a documentation and paperwork exercise. Automating the Stage-1 design model lets these packages be generated from one source rather than be recreated by hand, removing the manual redrawing between parties (IFF and IFC serve different audiences, the factory and the field, and are issued separately; they are not the same document and do not drift against one another).

## Stage 3: Assembling the module and Factory Testing

Once all the prework is completed, the module still has to be physically built. Think of this step as the production line, but in a much bigger scale of a datacenter. The assembly process starts with a base, a skid, or a frame that sets the foundation of the module. From there, equipments are layered in sequence, with each component placed into its designated area like how you will assemble a LEGO building.

What runs alongside the assembly is the factory acceptance test, or better known as “FAT”. Testing happens at two levels. The first is at each station as the module is assembled, an inspection gate where the work is checked before the module advances. The second comes once the module is complete: the whole unit is powered up and run the way it will run on site to confirm its rated load and everything is in place properly. By the time it leaves the line, the module is cabled, labeled, sealed, and proven to work on its own.

Factory testing is critical. The industry often describes this through the 1-10-100 rule: a defect that costs $1 to fix during design or assembly may cost $10 once production begins and $100 after the product has shipped. Furthermore, standardization also makes testing repeatable, so same FAT procedures can be run multiple times across production.

## Stage 4: Delivering and installing the modules

Now, the module leaves the factory’s controlled environment and runs into the uncontrolled area of site logistics. At the scale of today’s AI campuses, bringing the first block online is no longer enough, because operators also have to think about time to the last megawatt. The critical questions become how many finished modules can reach the site, how many can be unloaded and set in parallel, and how effectively limited rigging and installation crews can move from one block to the next.

### A closer look at: Transport and Logistics

In our conversations with datacenter developers, logistics appears as one of the main challenges equipment modularization presents. All these skids and modules are big and heavy, and shipping them from the factory to the site is not a minor task. That is why footprint and location matter so much, with integrators expanding their footprint to sit closer to their customer’s sites.

Federal law fixes the no-permit envelope at 102 inches wide and 80,000 pounds gross, leaving about 24 tons for the module on a standard deck. Microsoft’s Azure Modular Datacenter and Schneider’s Easy Modular ride inside a 40-foot ISO container at 96 inches wide, so they cross any state line or fly in a C-17 permit-free.

Past that threshold, you need a permit, although the truth is that permit cost has little impact and the real implication is on schedule. A standard oversize permit runs just $15-100 a state, and even the line-haul, at $12-14 a loaded mile, makes a 500 mile move only six to seven thousand dollars a trailer.

On time, loads past roughly 16 feet become superloads, triggering a bridge-engineering review that runs 7 to 21 days per state and stacks toward months across a route, and escorts force restricted travel windows. Besides, the thresholds are not even uniform, as a module engineered to clear Virginia (superload at 18 feet or 250,000 pounds) can still trip Ohio’s far lower 14-foot, 120,000-pound line.

Transport also becomes part of the reliability program. A module may experience greater mechanical stress on the road than during normal operation, particularly through vibration, braking, and loading. In one validation exercise, Aligned DC shipped a 3 MW module from Utah to Omaha and back with force loggers to measure the conditions it experienced in transit.

On top of all this, transport can also be constrained by the insurance it carries. High-value AI racks may be shipped only one or two at a time because concentrating too much equipment on a single trailer creates an unacceptable insured loss no insurance company is willing to bet on. The risk is not theoretical and we have heard cases where truck carrying large UPS module tipped over on a road in West Virginia while traveling toward Northern Virginia, leading to large reimbursement.

Considering all these implications, operators are designing around the haul, like AWS engineering Houdini’s skids onto low double-drop trailers to stay under bridges. Also Nautilus floated its datacenter 50 miles to the Port of Stockton on a barge, and Compass put a Schneider module factory next to its Red Oak campus. That said, some operators like DXN do manage to ship containers from their factories in Perth, Western Australia all the way to the US. These are, however, mostly smaller containers.

Once the module reaches the site, it must be lifted onto the prepared foundation, anchored, and connected to upstream power and downstream load. Even crane selection becomes part of the design process. A crawler crane’s lifting capacity falls sharply as the load moves farther from the boom: a Manitowoc 18000 can lift roughly 600 tons at 7.3 meters, but only about 10 tons at 104 meters, so the module’s weight, lifting points, and final landing position determine which crane is required and how much the lift will cost, typically around $5,000 to $25,000 per day. A single Schneider 500 kW power module, for example, weighs 50,000 pounds, needs six lifting points, and its load distribution is not known until it is built.

### Stage 5: Site Commissioning

With the modules in place, it’s time to commission them. Factory testing proves the individual unit, while commissioning proves the system under real conditions. Operators consistently call this the single biggest gap in the modular cycle, with a full site commissioning running 3 to 8 months end to end. While some vendors claim it can be shifted offsite, in practice the parts that matter can’t be, because the major energy sources (the utility feed, the generators, the BESS) only meet on site.

### The levels of commissioning

The industry generally runs a 6-level ladder, while some frameworks add a Level 0 design review at the front.

- L1 - Factory Witness Test (the “red tag”): each skid or module proven as a standalone unit at the manufacturer. This is the level factory testing covers, and the level modular front loads.

- L2 - Delivery & installation verification: the unit is received, set, anchored and inspected on site.

- L3 - Pre-functional / startup (the “green tag”): each system energized and started up on its own.

- L4 - Functional performance testing (the “blue tag”): each system run to the switchgear, the cooling loop.

- L5 - Integrated Systems Testing / IST (the “white tag”): every system energized and running together, on site, under simulated failure, an A-side outage, a UPS/STS transfer, a pump failover, a black-building start.

From L2 onward the work has to happen physically on site, because the sources being tested against like utility feed, generators, BESS are only present there.

To understand where time can actually be recovered, we identify two levers. First, parallelize commission modules and subsystems as they land rather than waiting for the whole site, so L2–L4 on the early modules overlap the delivery of later ones and only L5 has to wait for the full set. Second, reuse the plant as its own load bank: the power equipment and its battery storage can serve as the load bank during commissioning, so instead of trucking in rented gensets and resistive banks that leave when the test ends, the same gear that proves the plant stays on as part of it.

### Parallel Factory Commissioning

At scale the binding constraint is usually the Level 3 point-to-point work, because every PDU, control panel, and field device must be wired, addressed, named, and verified back to the BMS. Across hundreds of PDUs each exposing dozens to hundreds of points, this is the real commissioning bottleneck. To move faster, some big datacenter operators are running parallel factory commissioning tracks alongside the standard on-site process, completing equipment verification and control checks before shipment (repeating some tests post-transport) while the site team keeps delivery checks, live interconnection, and integrated-system testing.

This consideration also matters when studying aggressive project timelines claims. Some 6-9 month schedules are achieved partly by compressing or minimizing the commissioning process. That may accelerate initial turn-up, but it significantly shifts risk into operations.

# Putting the Value Proposition of Modular Solutions to Test

All modular pitches mainly rest on three claims: (1) Speed to market; (2) Quality of Build and Safety; and (3) Total Cost of Ownership. The marketed numbers are huge figures, with Vertiv claiming MegaMod at up to 50% faster on module deployment and SmartRun at up to 85%, and Schneider claiming 60% faster and 13% lower first cost on power and cooling.

Those are big (big!) numbers, so we rebuilt the case bottom-up against our baseline reference datacenter that we include in the SemiAnalysis Industrials Model, a 50 MW liquid cooled AI hall in the US. As headline, our numbers estimate a ~36% shorter construction window for modular construction when considering the full construction timeline, and a ~8% lower all-in cost. Let’s break down these figures.

## The Speed Advantage

Speed is undoubtedly the core vendor selling point. Following our previous taxonomy, the realized savings will depend a lot on which modular solutions you use in the build. To understand where the speed savings come from, we need to understand the construction timeline in commonly four blocks:

- Groundworks: 4-6 months, averaging about 5 months. Modularization changes little here beyond simplifying some pad and foundation work.

- Structure and shell: 2.5-4.5 months, with a midpoint of about 3.5 months.

- Mechanical and electrical fit-out: 7-11 months. Today’s baseline already includes some preassembled electrical equipment, such as LV switchgear and UPS lineups.

- Commissioning to IT-ready: 3-8 months, with a single-hall midpoint of about 4.5 months. Longer timelines usually reflect phased, multi-hall handovers.

Added together, a conventional 50MW building runs about 18 to 24 months from groundbreaking to IT-ready, with permitting excluded from that clock. In addition to the mentioned commissioning considerations, faster timelines claims are also sometimes related to a counting convention, often starting the clock at the electrical fit-out or the vertical works rather than at groundworks. Besides, permitting adds another 12 to 13 months that cannot overlap with construction, taking the all-in timeline to roughly ~30-35+ months for a stick build against ~24-30 for modular.

In the table below, which considers a scenario of an operator going full modular, modularization can compresses the construction window to about 12-18 months, around ~36% faster than a pure stick build and about ~30% faster than today’s baseline that considers some modularization.

The savings scale with how much scope moves to the factory. An operator taking only MEP skids, midway between today’s baseline and a full modular build, lands around 17 months. That schedule can be shortened even further when deploying all-in-one prefabricated block or containerized datacenters, which can take the building window all the way down to about 12 months. Today we can hear some claims even for under 12-month deliveries.

Digging deeper, during the MEP fit-out, an AI data hall absorbs about 12,000 field man-hours per MW, with electrical the dominant trade. A standard 50 MW hall concentrates 600,000 field hours into one building and stacks about 300 craft workers at peak. Relocating that MEP scope to the factory, on-site hours fall about ~63% to 4,500 per MW and licensed-electrician hours about 85%. The window itself compresses by less than the hours because the relocated work now runs in the factory in parallel with sitework. In addition, moving work into the factory also reduces dependence on weather and geographic constraints.

Speed equals money

Speed is compute and compute is revenue, so the true value of pulling go-live forward is the opportunity cost of the delay. In our calculations we consider as a rule of thumb that today, for CSPs, a megawatt of IT load generates on the order of $12M to 15M of revenue a year, or about $1-1.25M per IT MW per month. That said, in such a capacity constrained market, we are seeing new deals being made on much higher disclosed pays, see SpaceX and Anthropic deal, or as we recently covered in our Meta newsletter post, revenues of $50M per IT MW. Companies like Anthropic or OpenAI are making over $50M/MW on API.

On the COGS side, the relevant cost is GPU depreciation, at an average $30M/MW for an Nvidia cluster depreciated over five years, roughly $500,000/MW per month. An idle month strands at least that depreciation, on GPUs already on the clock whether or not the hall is ready, so we value an earlier month to the owner-operator at about $500k/MW, a conservative figure since the contribution margin on live compute is higher. For a wholesale colocation operator that never owns the GPUs, the value of an earlier month is just the lease it can now bill, about $190,000/MW per month, roughly $190/kW/mo.

Applying those unit economics to the roughly 8-month lead over a pure stick build, the owner-operator captures about $200M undiscounted across the 50 MW hall, or ~$4M/MW.

Of course, all of this is conditional on the building being the binding constraint. Go-live is the latest of three dates, building ready, power available, and GPUs delivered, and accelerating the building earns nothing if it was not the date that bound.

## The TCO Advantage

Compared to the realized speed benefits, Capex savings are not meaningful. We estimate that same full modular 50 MW liquid cooled hall costs about ~$1.1M/MW less all-in, ~$13.5M/MW against ~$14.6M/MW, just under an ~8% delta.

When looking at the all-in content/MW for the datacenter equipment, we can separate between hardware cost and service or installation cost. The hardware piece itself does not change much: switchgear, UPS, transformers, and other core hardware cost the same whether they are installed in a field-built room or integrated into a factory skid. The gross savings come from two places mainly, the labor portion and a shorter build time.

We estimate that moving MEP into the factory saves about $0.6M/MW on construction services and $0.5M/MW on installation. The wage gap is small, as BLS puts field construction at $34/hour against $33/hour in the factory, though overtime and site premiums lift the effective field electrician to roughly $63/hour. The real lever here is higher factory throughput, dropping a full field hour of scope.

Second is the effect from shorter build time. Locking factory cost earlier and compressing the field period trims escalation, contingency, change orders and site general conditions.

Against those savings, modular carries some penalties, with double margin being the largest. A stick build marks up installed content once, through the general contractor and its subs. A modular build adds a separate module-vendor margin on top of the site integrator’s. That layer compresses when the OEM also integrates on site, as Vertiv and Schneider do on their turnkey programs. Schneider’s WP163 shows this dynamic, putting module hardware about 40% above traditional and netting to 13% lower first cost, after design and install labor savings are counted.

Two smaller penalties follow, including the module premium (chassis, bracing, extra interconnects, transport and craning), and from the vendor perspective, the additional factory burden.

## The Quality and Predictability Advantage

Factory first-pass quality, the share of test and inspection points cleared without rework, is supposed to exceed 95% in modular solutions, against a field baseline of 60-70%, thanks to the on-factory fixed work instructions. The benefit is system predictability. Flex frames this as a design choice and engineers it through design failure-mode-and-effects analysis for productized configurations, design-for-manufacturing and design-for-assembly reviews for project-specific ones.

That said, recent conversations point to the opposite side, with operators and MEP contractors claiming that modular solutions have proven reliability issues and haven’t lived up to their claims. This eventually means not only losing all the time savings gained initially, with a field team having to go on site, but more importantly, putting the precious hardware at risk.

## Re-evaluating Vendors’ Claims

Our ~36% time savings, or around 8 months, lands just above Flex’s published 30%+ floor on whole projects. In order to do a fair comparison, we must consider that vendors’ numbers usually come from narrower scopes or composite definitions, not the end-to-end construction timings. Vertiv’s 85% SmartRun claim applies to overhead busway and containment, while MegaMod’s 50% claim measures module deployment against on-site build. Schneider’s 60% claim is for power-and-cooling modules.

# What Operators and Developers Are Modularizing Today

Across the market, operators and developers are not converging on one modular strategy.

## Hyperscalers

Hyperscalers most frequently build their own fleet, vertically integrate buildouts, and engineer the datacenter design around their actual workload. That’s why hyperscalers tend to show the innovator traits and have leading experimental footprint.

AWS

AWS shows the fastest scaling buildout currently, adding almost 3.9 GW of capacity to the end of 2025. Project Houdini is their largest internal attempt to modularization model. Rather than designing a modular building from scratch, AWS took its standard data-hall map and re-cut it into a factory-built skid roughly 45-feet in length and weighing about 2000 pounds that is transportable on double-drop trailers. This puts Houdini squarely in the “factor-built white-space” category.

The approach cuts deployment from as much as 15 weeks to roughly 2–3 weeks and can eliminate more than 50,000 on-site electrician hours per module. The skids are built in Houston, Salt Lake City, and Topeka, with early deployments in Texas and South Bend, targeting ~25 weeks from construction start to the first server room.

Houdini is also notable for its approval model. Instead of relying only on site-level engineering sign-off, the factory process requires separate validation of the design and the physical build. Cupertino Electric serves as the main partner, responsible for the latter.

Meta

Meta has recently focused on how to get the building enclosed. Its “tents” datacenters, or rapid-deployment structures, are the clearest example of shell-level modularization in the taxonomy above. A lightweight structural frame supports a tensioned fabric membrane, creating a weather-protected enclosure much faster than a conventional steel-and-concrete building.

At Prometheus in New Albany, Meta is using this strategy to pull shell construction forward

Meta has built six rapid deployment structure at this campus, with each roughly 125,000 in square feet dimension. To put speed savings into the picture, it’s worth noting that the site’s first five permanent buildings took Meta two to three years to complete, while the tents took a fraction of that, with eight standing by April 2026 from our satellite tracking since their announcement of the tent buildout in July of 2025.

This does not mean Meta built the complete datacenters in nine months, because the tent accelerate the shell but not the full facility. Also, the trade off on the other hand, is resilience. A fabric structure does not provide the same long-term durability or weather protection as a permeant steel or concrete shell as we had described above, it is also not built with intent to provide decade-long protection service.

## GPU Clouds and Neoclouds

Crusoe

Crusoe participates in both the shell modularization and whole facility modularization taxonomy. At the Abilene Stargate campus, Crusoe accelerated the shell using structural steel and factory-made insulated metal panels. Working with Digital Building Components, each building used roughly 672 prefabricated panels. The panels were manufactured in under 40 days and installed at a rate of roughly 15 to 20 per day, allowing the building to reach a dried-in state in under eight weeks.

In addition, Crusoe’s decided to vertically integrate the manufacturing process. Its 2022 acquisition of Easter-Owens brought modular datacenter and electrical-system manufacturing in-house, giving Crusoe greater control over design, supply chain, and production. The company is now expanding that capability through a dedicated Spark factory in Brighton, Colorado.

Each Spark unit are roughly one megawatt in scale and arrive substantially complete, placing Spark in the whole-facility modularization category.

The Redwood Materials deployment in Nevada shows how this model can scale. Crusoe initially installed four Spark units alongside a 12 MW microgrid and later announced an expansion to 24 units.

Hut 8

Hut 8 is buying the entire infrastructure stack. A former bitcoin miner with power and land positions, it is racing to convert those positions into leasable AI capacity, and the fastest way to do that is to buy a finished modular stack.

At its Beacon Point campus in Corpus Christi it runs Vertiv’s OneCore to commercialize a 704MW IT lease.

The project is being designed around Nvidia’s DSX reference architecture and delivered through a group of established counterparties. American Electric Power provides the utility relationship, Jacobs Solutions owns the EPCM scope, and Vertiv supplies the critical power and cooling infrastructure.

Nebius

Nebius takes a lighter approach to modularization by defining the facility around its own compute architecture and modularizing selected parts of the infrastructure such as power and cooling.

At the New Jersey campus, the facility is being built to Nebius’s own design through its partnership with DataOne and is planned as a phased development expandable to 300 MW. The company used precast structural components to accelerate the shell, while pairing the site with Bloom Energy behind the meter fuel cells as the power solution.

At Béthune, France, the company follows the same operating logic through a different construction method. The project reuses the former Bridgestone tire plant, avoiding part of the greenfield shell and permitting process. Azur Datacenter is responsible for the land, utility intake, construction, and physical plant, while Nebius focuses on the GPUs, racks, networking, and software.

## Colocation Providers

Compass

Compass is the colo that has run the modular playbook longest. They industrialize the whole facility into a repeatable kit of parts, not just one subsystem. We estimate roughly 70 - 85% of each building is manufactured off-site and bolted together on site, standing up a building’s framework and roof in 18 to 21 days. The kit spans the full stack:

- Shell: a rebar-free, fiber-reinforced precast shell, Compass casts itself from on-site batch plants

- White space: Standardized prefabricated rack and containment systems such as using Schneider’s EcoStruxure Pod

- Power block: a repeatable ~1.25 MW Schneider power center (Galaxy VX UPS, lithium-ion batteries, QED-2 switchgear)

- MV switchgear: modular medium-voltage switchgear skids under a Siemens deal for up to 1,500 units over five years

It runs this same kit across campuses, up to 360 MW at Red Oak, Texas and eight buildings across 1.8 million square feet at Goodyear, Arizona.

QTS

QTS’s modular strategy is built around locking the design early, standardizing the interfaces between vendors, and purchasing critical equipment before a specific building needs it. The company maintains roughly 7 million square feet of warehouse capacity in Kansas for long-lead equipment, allowing UPS systems, switchgear, cooling equipment, and other owner-furnished components to be held in inventory rather than ordered after each customer signs.

The approach began with the Freedom Design, which keeps the building shell flexible but repeats the power architecture. Each factory-built pod combines a 1.5 MW UPS and switchgear package with a 2.25 MW generator, and the system scales in 1.5 MW increments. Freedom LC+ expands the same concept into cooling, with an architecture that can support either fully air-cooled or fully liquid-cooled deployments. QTS’s newer rapid-deployment design pushes modularization further into the building itself, organizing capacity around repeatable 60 MW data-hall blocks.

QTS has therefore continued to move more scope off-site: first the power train, then parts of the cooling system, and now portions of the shell and data hall. For the shell, some QTS facilities use tilt-up concrete, including Manassas, while larger campuses such as Cedar Rapids use structural steel.

The value is labor, safety, and schedule certainty. QTS estimates that labor pressure has increased datacenter construction costs by roughly 20–30% per MW. Moving to modular is the company is trend, and they begin by stocking long-lead equipment in advance removes another source of delay, giving QTS greater control over when the final megawatts can be commissioned.

QTS developed subsequently the “Rapids” design, which materially accelerates construction timelines. Two major AI companies have adopted this design at scale.

Aligned Data Centers

Aligned’s modular strategy is centered on adaptability, keeping the core power and cooling architecture standardized while allowing the hall configuration to change as customer requirements and rack densities evolve. The approach began with core MEP infrastructure, including a 2 MW UPS container with integrated distribution switchgear and power. This approach is now extending into site conveyance through examples like prefabricated chilled-water assemblies. For customers able to coordinate early, the scope can extend even further into the white space through things like secondary fluid piping.

The other core element is Aligned’s Adaptive Modular Infrastructure platform, which keeps the underlying power and cooling systems consistent while allowing the hall to shift between air, hybrid, and liquid cooling as rack densities evolve. The platform combines

- Delta³, Aligned’s air-cooling system, supporting densities of up to roughly 50 kW per rack.

- DeltaFlow, its liquid-cooling platform, supporting densities above 350 kW per rack

Because the underlying chilled-water loop and facility interfaces remain consistent, the cooling mix can change without redesigning the entire hall. The components inside the modules remain standardized and do not change. An example is found in Project Caprock in Texas, 540 MW across six buildings and 1.65 million square feet.

# Winners and Losers: Supplier Implications

## Integrated Equipment Platforms

Vertiv (VRT US)

Vertiv has the strongest modular position among all the public equipment suppliers. Its portfolio spans from individual sub-system modularization platforms like the SmartMod product, all the way to the entire datacenter in a box stack design known as the OneCore platform. OneCore became the building block of Nvidia’s Vera Rubin DSX reference design as of March 2026.

We estimate Vertiv’s content can increase from roughly $3.5 million per MW for discrete power and cooling equipment toward approximately $7 million per MW under a full OneCore deployment. As noted before, we have seen already demand running ahead of supply, with some modular units sold out for over 12 months. Vertiv ended 2025 with $15.0 billion of backlog and a 2.9x fourth-quarter book-to-bill ratio. Its April 2026 acquisition of BMarko is expected to increase regional modular manufacturing capacity by roughly seven times.

The Hut 8 relationship provides an early example of this model in the field. Vertiv is using its digital-twin platform and factory-integrated OneCore infrastructure to support repeatable AI-campus deployments, and positioning itself to carry the infrastructure from digital design through factory assembly, site deployment, and lifecycle support.

Schneider Electric (SU FP)

Schneider has the second-broadest modular portfolio after Vertiv, spanning nearly the full modular taxonomy. Secure Power Systems, which includes three-phase UPS and prefabricated datacenter products, represents almost 32% of Schneider’s Data Center & Networks portfolio. EcoStruxure adds the common controls and management architecture across those systems, while AVEVA extends Schneider’s role into design, simulation, and lifecycle operation.

Schneider’s full-stack approach is a little different from a single turnkey module that Vertiv provide with OneCore. EcoStruxure is a family of configurable building blocks, customers can deploy the pieces independently or combine them around their own building and redundancy design. OneCore, by comparison, is sold as a coordinated above-foundation delivery system.

The Compass partnership shows how Schneider’s model works in practice. Schneider and Compass have a $3 billion multi-year agreement covering prefabricated infrastructure, supported by a 105,000-square-foot integration facility beside Compass’s Red Oak campus. Schneider manufactures and tests the power and white-space systems while Compass constructs the shell, allowing both workstreams to proceed in parallel. Schneider may not own the finished building, but it can capture several equipment inside it. The Nvidia relationship pushes Schneider further upstream with validated Vera Rubin facility designs.

Management estimates Schneider’s addressable datacenter content at approximately $1.2 million to $3.3 million per MW. Demand visibility has also expanded materially with group backlog now exceeding €25 billion. Management noted 18 to 24 months of visibility across datacenter projects. The limitation for Schneider lies in its dependence for partnerships with operators and integrators to assemble the full facility, but it is none-the-less a credible player in the industry.

## Systems Integrators and Modular Contractors

Comfort Systems (FIX US)

Comfort Systems has built one of the largest modular platforms among the specialty contractors. Through TAS in Houston and Environmental Air Systems in Greensboro, it manufactures modular cooling plants, MEP skids, white-space assemblies, and larger volumetric infrastructure units. Management draws a clear line between ordinary prefabrication and modular: every Comfort subsidiary performs some off-site fabrication, but only the volumetric work at TAS and EAS is classified as modular.

In a note published to subscribers to our Industrials Model subscribers this week, we showed Comfort Systems investing heavily behind its modular platform to serve demand from its key hyperscale customers Google and Meta, which we view as a clear positive for its prospects in modular. We estimate that their modular capex in CY26 alone will be greater than the cumulative modular capex in the preceding 12 years, which will bring modular production space to 5 million square feet by late summer 2027. Read the full Comfort Systems outlook here.

On its Q2 2026 earnings call last week, Comfort Systems also disclosed pilot modular contracts with frontier AI labs and colocation providers, which extends its customer base beyond its core hyperscaler focus. If the pilots convert into volume orders with  advance-purchase commitments, we expect Comfort Systems to add incremental modular capacity to serve the buildout.Modular work represented 17% of revenue in the first half of 2026, roughly a $2B annualized run-rate. Backlog reached a record $14.1 billion, up 73% year over year, with modular bookings accounting for roughly a third of the sequential increase.

Importantly, operating cash flow is taking a step up from increased advance billings. Comfort generated $1.14 billion of operating cash flow in the quarter, supported by advance billings which increased by $1.11 billion over the last six months to $3.23 billion as of the latest quarter. In other words, customers are paying well upfront, and these advances will help support Comfort Systems’ capital investments in modular.

One advantage Comfort possesses is it does not ask the customer to adopt a fixed TAS or EAS datacenter design. The hyperscaler keeps its own equipment choices, while Comfort takes the repeatable cooling and MEP scope and builds it in a factory instead of building it in-situ. As customers repeat the same campus design, TAS and EAS can manufacture the modules while Comfort’s field businesses prepare the site and complete installation, allowing the company to capture both the factory work and the final integration, thereby increasing their total addressable value per MW.

Quanta Services (PWR US)

Quanta’s modular position is built around Cupertino Electric, which allows the company to retain both the factory work and the onsite electrical scope as more of the datacenter moves offsite. CEI is the electrical integrator for AWS’s Project Houdini, with the first designs targeting completion in May 2026, and the first skid scheduled for delivery in September. Quanta does not break out modular share of revenue, but disclosed that the technology end-market, which encompasses datacenters and other advanced manufacturing work, has gone from less 5% of the backlog a year ago to roughly 10% as of March this year, and is growing north of 100%.

By participating in Houdini’s design, offsite fabrication, delivery, onsite connection, and commissioning, Quanta will capture the benefits of modularization by moving labor into the factory without surrendering the field handoff to another company.

The company is investing heavily behind that position. Quanta has approximately 7 million square feet under roof, including transformer manufacturing, and has committed around $700 million to factory expansion and MEP fabrication. Cupertino carries roughly $1.5 billion of datacenter-related backlog and has grown more than 50% since Quanta acquired it. Management frames the broader datacenter construction opportunity at approximately $13 million per MW.

Sterling Infrastructure (STRL)

Sterling’s modular positioning is different from Comfort and Quanta. It does not own a broad equipment platform, but it controls a huge portion of the physical campus buildout than most specialty contractors, being a site-development incumbent and buying its way into mission-critical via CEC acquisition.

Most of Sterling’s current efforts on prefabrication are for internal efficiency use rather than a standalone module business. Sterling market its modular strategy as Integrated Modular Solutions, or IMS. A distinctive part of the model is bringing the outside electrical duct-bank scope into the site package. Instead of completing the civil work and later working around the finished site to install electrical infrastructure, Sterling can sequence the duct banks alongside excavation, grading, and concrete work.

They do all this in their facilities dedicated for prefabrication, which they are quickly growing. A Texas lease roughly triples modular capacity, and management says throughput has about doubled.

On the broader Sterling outlook, as we covered recently, we remain bullish on the company’s content uplift opportunity by increasing the penetration of their integrated offering with CEC, as they have proven at Meta’s Cheyenne and El Paso campuses. The company is also being pulled into Texas, the Pacific Northwest, and the Midwest, expanding its addressable datacenter capacity from roughly 3.8GW to 14GW. Read the full Sterling outlook here.

IES Holdings (IESC US)

IES is not a pure modular contractor. Its Communications segment designs and installs the network infrastructure inside the data hall. Their Commercial & Industrial unit handles electrical and mechanical construction, and Infrastructure Solutions manufactures custom equipment such as generator enclosures.

IES already provides materials warehousing and prefabrication for datacenter projects, and it has been adding capacity within Infrastructure Solutions while integrating more services across its segments. Rather than only installing the electrical or communications package after the module arrives, the company can potentially fabricate supporting infrastructure, complete portions of the electrical and network fit-out, and then install and maintain those systems onsite.

IES may be a narrower winner from the modularization story as its modular exposure is still primarily an extension of its contracting and fabrication businesses rather than a separate product line. It has the labor base, customer relationships, and cross-segment capabilities to retain more work as scope shifts into controlled facilities, especially across electrical, communications, and custom infrastructure products.

## Modular Power and Electrical Systems

Flex (FLEX US)

Flex is using its contract-manufacturing base to absorb work that historically sat across several different suppliers and contractors. The strategic value of Flex’s subdivision, Anord Mardix, is intent to deliver a substantially complete power system. That shifts Flex from earning manufacturing margin on individual components to earning the integration margin on the electrical package itself. Anord Mardix claims this can reduce onsite testing by as much as 70%.

The broader M&A strategy shows that Flex is trying to repeat that model across the rest of the AI-infrastructure stack. Crown adds utility-grade power distribution, JetCool adds liquid cooling, and EP² adds modular control buildings and protection systems. The result is a company that can increasingly connect end to end buildout under one manufacturing platform. This is particularly valuable as 800 VDC and liquid-cooled rack designs force power, thermal, and compute infrastructure to be engineered together rather than procured as separate systems.

The company’s Cloud and Power Infrastructure segment reached $6.6 billion of fiscal 2026 revenue, with Power growing 61%, and the planned separation should make that economics more visible. The key question is whether Flex can integrate Anord Mardix, Crown, JetCool, and EP² into one repeatable platform.

nVent (NVT US)

nVent is one of the more unique modular players because its strategy focuses on using acquisitions to move from selling enclosures around electrical equipment to owning a much larger share of the engineered building itself. It paid roughly $688 million for Trachte and another $980 million for Avail EPG, acquiring customer relationships, backlog, and engineering capabilities rather than just physical plants.

Trachte gives it the factory-built structure, while Avail’s Electrical Products Group adds switchgear, bus systems, and internal electrical integration. The strategic shift is to increases nVent’s content per project and moves it closer to the customer’s critical power architecture rather than leaving it as a component vendor. The numbers suggest that the strategy is already scaling with nVent estimating an opportunity of around $1 million per MW across its data-center portfolio.

We view nVent as a net beneficiary because it can capture more value around the equipment it historically enclosed. The company can increasingly provide the building, internal electrical integration, testing, and delivery as one package. The open question is whether nVent can combine Trachte and Avail into a standardized modular platform rather than continuing to operate them as adjacent businesses.

Eaton (ETN US)

Eaton has one of the broadest portfolios within modular power. Management estimates its addressable datacenter content at approximately $2.9 million per MW, increasing to $3.4 million per MW with the addition of liquid cooling. The opportunity is supported by a growing set of modular platforms that allow Eaton to participate at the modular scale.

NordicEPOD is the most standardized part of the portfolio. The platform packages medium-voltage switchgear, transformers, UPS systems, batteries, low-voltage distribution, and cooling into transportable power modules of roughly 1.7 MW to 2.0 MW, with configurations reaching as high as 3.1 MW. Fibrebond expands that model into larger pre-integrated electrical buildings in North America, while Flexnode extends Eaton into turnkey modular data halls ranging from approximately 3.5 MW to 35 MW. Eaton supplies critical-power backup, racks, cable management, and 800 VDC-ready infrastructure into the Flexnode design, which the companies say can reduce deployment schedules by roughly 35%. Together, these offerings give Eaton coverage from the power enclosure through the data hall, with the ability to carry more of the electrical package inside a common modular design.

Eaton Beam Rubin DSX is the company’s attempt to bring those modular assets together. The platform combines Fibrebond enclosures, NordicEPOD power skids, Flexnode modular halls, 800 VDC distribution, and Boyd liquid cooling around Nvidia’s Vera Rubin reference architecture.

Siemens (SIE GR)

Siemens’ modular exposure centered around the MV switchgear section and is among the first suppliers with both IEC and UL variant for Nvidia’s Rubin DSX architecture. It has also secured a program for as many as 1,500 modular switchgear skids over five years for a colocation developer which we believe is Compass, giving the company a repeat-production role across multiple datacenter buildings rather than a series of one-off switchgear orders. Siemens extends that position through partners such as Delta, combining its medium- and low-voltage equipment with third-party UPS, batteries, cooling, and module assembly.

The scale is already visible in Smart Infrastructure: datacenter revenue reached roughly €2.9 billion in fiscal 2025, up 40%, while datacenter orders were €1.8 billion in Q1 FY2026 and €1.9 billion in Q2. Siemens should therefore benefit from repeat volume and factory integration, but it does not capture the full scale of modularization cycle as much of the enclosure, cooling, and final integration margin remains with its partners.

ABB (ABB SS)

ABB’s modular strategy is similar to Siemens and Flex where its intention is to own the electrical block around it. The company’s strongest position is in medium-voltage power, where HiPerGuard allows the UPS, switchgear, controls, and protection equipment to be packaged into repeatable power blocks before they reach the site.

Each HiPerGuard unit is rated at 2.5 MVA and can be combined into 25 MW blocks, while the newer 34.5 kV version connects directly at campus distribution voltage, reducing conversion stages and shrinking the electrical footprint by an estimated 20–25%. ABB is already applying this architecture at Applied Digital’s 400 MW North Dakota campus.

The company is also broadening what sits inside that electrical block. Its parternship with VoltaGrid  combines prefabricated eHouses with medium- and low-voltage distribution, automation, and synchronous condensers that stabilize behind-the-meter generation for high-density AI loads. The first two phases cover 62 synchronous condensers and associated eHouse infrastructure, showing how ABB can extend beyond conventional switchgear into the power-quality and grid-support systems required by large AI campuses.

That positioning should allow ABB to benefit from the modular cycle even as the company claim electrification orders increased 60% in Q2 2026 to $7.2 billion, while backlog reached $13.7 billion. ABB is adding roughly $200 million of medium-voltage manufacturing capacity across Europe to signaling its strategy remains deliberately focused on the factory-built electrical package.

## Other Specialized Modular and Construction Players

Modine (MOD US)

Modine’s modular exposure is concentrated in liquid cooling through Airedale, where its skid-mounted CDUs range from roughly 400 kW to more than 2 MW. Management estimates that a fully captured cooling package represents roughly $0.6M/MW, potentially increasing toward $0.7M/MW as liquid cooling, controls, service, and more integrated modular systems are added.

Modine’s more tangible demand signal remains its agreement to reserve more than $4 billion of cooling capacity for a hyperscale customer from 2027 through 2029, supported by a $165 million upfront payment, which we suspect to be Google.

We believe Modine’s upside from modularization lies in becoming embedded in the thermal architecture before the module is finalized. As cooling moves closer to the rack and becomes more integrated with the building design, the line between equipment supplier and cooling-system integrator begins to blur. The key question is whether these customer-specific designs can be repeated across multiple programs or remain bespoke engagements that are difficult to replicate.

Foxconn (2317 TT)

Foxconn’s modular strategy is an extension of its existing position as one of the largest AI server ODMs. The company already controls rack design, key components, liquid-cooling systems and final assembly, and is now trying to move further downstream into the infrastructure surrounding the rack. Its 2025 share swap with TECO was explicitly framed around combining Foxconn’s compute and manufacturing capabilities with TECO’s electromechanical engineering to offer more standardized datacenter modules and a broader construction package.

Foxconn unveiled its Modular Data Center concept at GTC 2026 and is working with Schneider Electric where Foxconn brings the compute platform, rack integration and manufacturing scale, and Schneider contributes the power, energy-management and cooling infrastructure. Its manufacturing footprint and output of roughly 1,000 AI racks per week give it a scale advantage and serve as its fundamental backbone to capture the growing market.

The company claims more than 1 GW of deployed modular datacenter infrastructure, supported by a 242,000-square-foot Houston facility that is scaling toward roughly 2,000 racks per week and a further $569 million expansion in Wisconsin. Together, those investments give Foxconn the foundation to move into larger portions of the white-space and datacenter assembly process the company intends to play in.

Jacobs (J US)

Jacobs does not manufacture the module, but it sits at the point where standardized designs have to be translated into a real-world functioning campus. The company is one of the few engineering firms working with Nvidia’s DSX reference architecture (The other been Bechtel) and serves as EPCM on Hut 8’s River Bend and Beacon Point campuses.

Its role becomes more important as modular programs scale to production. In a common modular build out, the module itself may be standardized, but the exact level of site commissioning and connection still need to be adopted and change by campus. This is where Jacob comes in, and they can easily reuse existing design to solve the problem.

Although Jacobs does not capture the equipment or manufacturing content inside the modules, it is materially expanding its addressable content per project. Its traditional design scope was worth approximately $2–5 million for a 50 MW-class facility, while management says some current full-program engagements are two orders of magnitude larger as they move towards broader EPCM role. Its opportunity is to expand from traditional design work into digital coordination, site adaptation, program management, and commissioning.

EMCOR (EME US)

EMCOR fields one of the largest specialty mechanical and electrical labor pools in the country with roughly 35,000 tradespeople. Their modular story primarily around expansion of factory-like fabrication capacity for internal use, which means it is not selling to third parties or buying from the market, it is using its own shop to pre-build portion on already contracted sites to install. Management says roughly 95% of this fabrication supports EMCOR’s own projects.

The company is investing meaningfully behind this model. EMCOR is adding roughly 400,000 - 450,000 square feet of fabrication space over an 18-month period. Management is optimistic on the expansion project and applies a three-year payback threshold based on visible demand. It’s worth noting that four large hyperscalers had shared construction plans extending through 2031 with EMCOR with its performance obligation reaching $4.5B (Comparing to 4.1Bof revenue in 2025)

The upside from the modular cycle is therefore operational rather than product-driven for EMCOR. AI datacenters carry more scope, with management estimating roughly 1.2 times the electrical content and 1.4 - 1.8 times the mechanical content of traditional cloud facilities. Prefabrication allows EMCOR to absorb that higher workload by becoming a more productive installer.

MYR Group

MYR Group is primarily an electrical contractor, with datacenter exposure across both on-site electrical construction and the grid infrastructure. MYR modular strategy involves prefabrication, but mainly as an internal construction tool similar to EMCOR. Subsidiaries such as Sturgeon Electric and Huen Electric pre-build items including junction boxes, control panels, and in some cases complete electrical rooms for internal uses only.

The company’s Commercial & Industrial margins improved to 8.1% from 4.7% a year ago, with management specifically linking that increase to prefab buildout. MYR is continuing to invest in those capabilities, including through the acquisition of Valley Electric and Comet, which add BIM, prefabrication, design-assist, and mission-critical electrical experience.

What MYR lacks compare to EMCOR is the scale and multi-trade breadth of a larger prefabrication platform. Its activity remains concentrated primarily in electrical assemblies. The approximately $328 million acquisition of Valley Electric and Comet adds more mission-critical electrical capability and expands MYR’s design, BIM, prefabrication, and installation capacity, but it still reinforces the company’s position as an electrical contractor rather than moving it into full modular-system integration.

## Private Companies: Infra Partners, Bladeroom, FTI and Other

One final mention is for private players. Construction is a segment where privately held firms command a massive share of the market, and modular follows the same trend. Across our conversations with hyperscalers and top datacenter developers, the names that come up most often aren’t just the publicly traded ones like Comfort Systems or Sterling, but private integrators like InfraPartners, BladeRoom, Faith Technologies (FTI), Cadolto, and Flexnode. Besides, as introduced before, as big OEMs are sold out and top EPC/integrator capacity is locked up by hyperscalers, new players are entering the market.

InfraPartners is the name we hear more often. The British integrator delivered Nscale’s Glomfjord facility in Norway, billed as the first fully modular datacenter purpose-built for AI workloads, and has disclosed a nameplate of roughly 1.2GW of annual deployment capacity. They ship out of a 150,000 sq ft Houston plant and their Romania factory it is doubling footprint. They are following a comprehensive portfolio strategy similar to Vertiv’s. In March 2026 it launched a productized suite (RapidNode, RapidHub, RapidFrame) built on its Standard Reference Design, and it is stacking itself into the power chain via partnerships with DG Matrix, Nvidia, EPRI, and Prologis.

BladeRoom is part of UK-based BRG Technologies, with decades of factory-built mission-critical facilities behind it, it has delivered 30+ datacenters across Europe, Asia, and Africa in as little as 20 weeks and now offers hyperscale designs in 30MW-plus blocks, having entered the US through a JV with Rosendin’s Modular Power Solutions, manufacturing out of Michigan.

Faith Technologies is a pure play on the electrical labor bottleneck. Through its Excellerate brand they ship complete modular electrical buildings, fully assembled and tested, to hyperscale datacenters nationwide. Beyond Appleton and its 438,000 sq ft Olathe flagship, it is adding a $79M Alabama plant, a 500,000 sq ft facility in Indiana and further capacity in El Paso, roughly tripling its footprint.
