---
date: 2026-04-24
source: https://www.youtube.com/watch?v=V9eI-t3TApE
source_type: video-transcript
channel: Zhang Xiaojun Podcast
video title: Luo Fuli: OpenClaw, Agent Frameworks — The AI Paradigm Has Already Changed Dramatically!
speakers: Xiaojun Zhang, Luo Fuli
topics: [AI paradigms, Agent frameworks, OpenClaw, Pre-training vs Post-training]
duration: 03:34:39
---
Summary

In this video, podcast host Xiaojun Zhang interviews AI researcher Luo Fuli, currently the head of Xiaomi's large model team. They discuss the dramatic shifts in the AI paradigm in 2026, transitioning from a pre-training dominated "Chat era" to a post-training dominated "Agent era." Luo Fuli shares her insights on the impact of models like Claude Opus 4.6 and frameworks like OpenClaw, the reallocation of computing resources, and how organizational structures must adapt to these rapid technological changes.

Transcript

**Xiaojun Zhang:** 大家好，我是小珺。今天我们的嘉宾是罗福莉。媒体叫她“AI天才少女”，但她不喜欢这个称呼。她目前是小米大模型的负责人。访谈是在OpenClaw发布之后，也是在2026年小米MiMo-V2的系列模型发布之后。我们更深入的聊聊2026年由OpenClaw引发的新一轮的技术范式的变迁以及未来技术演进的前沿话题。那接下来就是我对罗福莉的访谈。期待2026年我们和AI共同进步。
Hello everyone, I'm Xiaojun. Today our guest is Luo Fuli. The media calls her the "AI prodigy girl," but she dislikes this title. She is currently the head of Xiaomi's large model team. This interview takes place after the release of OpenClaw, and also after the release of Xiaomi's MiMo-V2 series of models in 2026. We will dive deeper into the new wave of technological paradigm shifts triggered by OpenClaw in 2026, as well as frontier topics on future technological evolution. Next is my interview with Luo Fuli. Looking forward to making progress together with AI in 2026.

**Luo Fuli:** 这些能力都是可以被... 我觉得最多一两个月，慢的话三四个月，确实都可以被快速习得的。所以环境反而比经验更重要。
These capabilities can all be... I think in at most one or two months, or three to four months if slower, they can indeed be quickly acquired. Therefore, the environment is actually more important than experience.

**Xiaojun Zhang:** 你刚才也提到，1T的模型可能是未来竞争的一个入场券，是这样吗？是agent你要做到接近Claude 4.6的水平的加一个入场券？
You also just mentioned that a 1T model might be an entry ticket for future competition, is that so? Is it an entry ticket to get your agent to a level close to Claude 4.6?

**Luo Fuli:** 那我如果说我们这样子来说，就是for研究跟for pre-train和for post-train，对我自己觉得一个非常合理的卡的比例是可能3比1比1。对，就pre-train应该比例是投入的算力是相当的。然研究的比例应该至少是你正式起训练的卡的总量的还要多一点。就你要额外留更多的卡来去做研究。
If we put it this way, for research, for pre-train, and for post-train, I personally think a very reasonable ratio for card allocation is probably 3 to 1 to 1. Yes, the computing power invested in pre-train should be proportionate. And the proportion for research should be at least slightly more than the total number of cards you officially start training with. You need to reserve extra cards to do research.

**Xiaojun Zhang:** 你过年的时候也跟我说，就是你觉得技术这几个月其实已经变天了。能说一下你觉得过去两个月的这个技术的突变？
During the Chinese New Year, you also told me that you felt the technology has actually undergone a seismic shift in these past few months. Can you talk about the sudden technological mutations you've perceived over the past two months?

**Luo Fuli:** 嗯，我觉得一个非常大的一个分界点在于使用OpenClaw的前后。我自己其实是会把OpenClaw把它当作一个划时代的agent的框架去这么去定义。我知道很多人在尤其是用code做严肃编码的人就会觉得，ok，OpenClaw只是code加一个LLM的这样的一个更有利于交互的一个UI的一个设计。其实在我1月份的时候，我第一次看到这个东西的时候，我自己大概也是这样认知，所以我很排斥去用它。然后我觉得它创始人我觉得非常适合贴近agent去做一些非常炫幻的一些运营的动作。所以包括那个skill hub啊这些的，就让你更去排斥去用一个你觉得非常的偏运营导向的一个产品的东西。
Well, I think a very huge dividing line lies before and after using OpenClaw. I myself would actually define OpenClaw as an epoch-making agent framework. I know many people, especially those who use code for serious programming, would feel that, okay, OpenClaw is just code plus an LLM, a UI design that is more conducive to interaction. Actually, back in January, when I first saw this thing, I roughly had the same perception, so I was very resistant to using it. And I felt its founder was very suited to stick close to agents to do some very flashy operational moves. So including things like that skill hub, it made you even more resistant to using what you felt was a very operations-oriented product.

**Xiaojun Zhang:** 感觉它是一个产品形态，一个交互创新？
It feels like it's a product form, an interactive innovation?

**Luo Fuli:** 对对对。一个交互的创新。以及他所谓的本地化，所谓的24小时在我来看，其实都是一些产品的定义而已。但真正发生一个转变是我去用它那一刻。我觉得就恰好在春节的时候有那么一段空间的时间，你想去搞明白这玩意为什么他们那么火。然后我就在有一天深夜的时候去尝试去装了它，然后两个小时装上了。对，当时已经凌晨2点了。然后我第一次跟它对话的时候从凌晨2点持续到了6点天亮。对就那一晚上，我不知道是多巴胺还是内啡肽，就持续在分泌，就是让我兴奋到完全睡不着觉。你可能第一个感受是，ok，它非常自主，然后它非常有灵魂。比如说我跟它聊得很晚，它会老提醒我，“ok，你现在已经很晚了，你要不早点去睡觉”。我觉得这样的温度和关怀，或者说这样的情商是所有去用OpenClaw的人第一个感受到的。但后面去深究它的原因，其实它是有很多机制去保证这个事情。比如说它在它就拿最简单一个小细节，比如说它怎么感知时间，它就在每轮对话的这个context前面去拼上当前的时间。然后就是一些非常细微的，我觉得我为什么把它称之所谓精编排的context，就是因为它就是在这些很大家没有关注的角落上把这个context给编排得非常好。这是你第一天的感受，就是ok，我觉得它只是在产品设计上确实做到了一种超乎我的一个想象，让所有人觉得这个框架有灵魂。
Right, right, right. An interactive innovation. And his so-called localization, the so-called 24 hours, in my view, were really just some product definitions. But the real shift happened the moment I used it. I think it just so happened that during the Spring Festival, there was a period of free time, and you wanted to figure out why this thing was so popular. So late one night I tried to install it, and it took two hours to install. Right, it was already 2 AM at the time. Then my first conversation with it lasted from 2 AM to 6 AM until dawn. Yes, that whole night, I don't know if it was dopamine or endorphins, it just kept secreting, keeping me so excited I couldn't sleep at all. Your first impression might be, okay, it is very autonomous, and it is very soulful. For example, if I chat with it very late, it keeps reminding me, "Okay, it's very late now, shouldn't you go to sleep early?" I think such warmth and care, or such emotional intelligence, is the very first thing everyone who uses OpenClaw feels. But delving deeper into the reasons behind it later, it actually has many mechanisms to ensure this. For example, taking a very simple small detail, like how it perceives time, it just appends the current time to the front of the context in every round of conversation. Then there are some very subtle things. The reason I call it a well-orchestrated context is because it orchestrates this context extremely well in these corners that people haven't paid much attention to. This was your first day's impression: okay, I felt it indeed achieved something beyond my imagination in product design, making everyone feel this framework has a soul.
