TL;DR:
General intelligence ≈ universal computation.
Universality requires: reliable (1) thinking, (2) and memory of what you thought.
Your average human with a pen and paper can compute anything computable, powered only by sandwiches.
Current AI achieves this through transformer attention—at a quadratic cost thats on pace to eat the worlds venture capital and boil our oceans.
We can do better.
CRISPR shows us that, when efficient universality is needed, state appears.
The recurrent nature of natural intelligence suggests a way forward.
Be true to yourself, and remember what you've done.

----

On a morning in early December I was running by the Mississippi when I saw a large industrial plume on the horizon.

[image of plume]

The plume is water vapor and nitrous oxides from xAI's "Colossus" supercomputer.
100k H100s are boiling 5 million liters of water a day from the Memphis sands aquifer, powered by dozens of portable methane generators pumping out 100 MW—enough for 50,000 homes.
They couldn't wait for the Tennessee Valley Authority to build new capacity; that delay might mean losing the race for a quantum leap in human capability.
Soon, the plant will begin cooling with graywater from the city, but for now it boils some of the cleanest municipal water on the planet.

This plume, now dominating Memphis's skyline, is compute's heat waste made visible in our rush to train an artificial general intelligence (AGI).
xAI's stated goal is a "1% shot at a Kardashev type 1 civilization"—a society capable of harnessing all its planet's energy, presumably enabled by the AGI they aim to bring into the world.
And they're just getting started, planning a tenfold expansion of Colossus to 1M GPUs.

You may have noticed that, although ravenous and hyperactive, a learning human child doesn't generate a thousand meter plume of water vapor and reactive particulates to develop their intelligence.
Yet your average human, fueled by sandwiches, can implement any algorithm with just pen and paper.
So augmented with bronze age technology, we become "universal" computers in Turing's language—the quintessential "general" intelligence capable of solving any problem given enough time and snacks.
 For the sake of argument, let’s agree: general intelligence ≈ universal computer.

That link has been on my mind for two years, ever since I first read the magic words "Let’s think step by step" in a groundbreaking machine learning paper.
I was amused by how a simple phrase seemed to invoke a more deliberate, thoughtful mode in large language models (LLMs).
It was as if some psychological "effect" flipped them into a more rigorous and structured part of their state space, leading to dramatic improvement in performance, and encouraging the world's LLM whisperers to add this incantation to every time they saw models faltering.

But theoretical analyses of transformers revealed something deeper than just a neat psychology trick.
Transformers, in a single forward pass, are restricted to a class called TC0, basically a family of threshold circuits that can be computed in parallel with aggregation.
TC0 systems are often called "bounded parallel".
They can quickly match patterns, but can't count, do math, or follow a recipe unless the process can be encoded in a fixed set of circuits.
_However_, if you use "chain-of-thought" or a series of recursive prompts—feeding each of the model's outputs back into its input—the combined system becomes capable of simulating a universal Turing machine.
The model’s expressivity, harnessed across multiple steps, blossoms into general computation.

Out of deep love for this line of research, I spent much of December in a meditation on the link between memory and computation.
This post is a human introduction to that paper, where I provide the simplest and most intuitive explanation of universality (a.k.a. general intelligence) that I could synthesize.
Universality requires only (1) stable evolution of thought (no hallucinations), and (2) reliable access to the history of thought.
This synthesis rightly seems banal, dull, too simple to be useful, too theory of computation 101 to be interesting.
And OK, if you studied the theory of computation, yes, it is, but why did y'all forget the textbook and start imaging that threshold circuits and feedforward networks could achieve general intelligence?
If you can remember, this perspective quickly takes us to some amazing places.

The first place is an intuitive understanding of what LLMs are.
Machine learning got excited by the observation that adding more parameters and training tokens could yield "scaling laws" that took us to a place where intelligence "emerged".
Another interpretation is that LLMs are a quintessential example of transfer learning, where humans and our society is the model that's being transferred.
By trying to predict what humans might say or do next, the models effectively learned patterns embedded in our writing—including the latent computational rules that shape human reasoning.
They’re not just modeling words but the programs behind those words (which might be human minds, or other models, or entire cryptographic protocols).
Looking through the lens of Turing machines, we've transferred our state transition functions to them, which they are now they are able to generalize to new input contexts (drawing tikz unicorns and such).

Part of the magic is that LLMs, must of which are Transformers, are forging a shared computational interface with us, letting us push each other around in a collaborative workspace space that can solve new tasks.
However, they have a costly flaw that makes them otherworldly in their resource demands: attention.
In effect, attention is a learned function for memory and association across the input.
But with n tokens, each must attend to every other token—an n × n explosion in both compute and memory.
Double your context length, quadruple the cost.
Want to "think" four times longer?
That’s sixteen times more overhead.
And because memory is the key to intelligence, model context length must be increased, leading to quadratic increases in costs which I saw made visible in Memphis last month.

But the truth is, generality doesn’t require a quadratic cost.
Look at a single cell.
It has gigabases of DNA and a swarm of biomolecules, operating in a parallel soup with no centralizing control.
By some definitions, each cell’s molecular interactions also fall in that threshold-circuit-like class: essentially parallel transformations, no large sequential pipeline.
But cells offset this limitation with state—encoded in their components and their DNA, which holds a record of life’s entire lineage.
When cells need to store or recall specific bits of information, they literally write it into the genome.
CRISPR, for example, is a chronological log of viral infections, allowing bacteria to remember which infections are recent and worth the most defensive energy.

The ARC AGI Prize nicely illustrates where today’s models stand.
A single forward-pass language model—like GPT-4—gets about 0–5% accuracy on ARC tasks.
Cheaper chain-of-thought–based systems that do a bit of test-time training get close to 50%.
Meanwhile, a careful human solver can reach 100% if you just give them enough time to think.

Then along comes OpenAI's O3, which nearly solved the entire benchmark in late December.
If you let the model "think less"—what they call high-efficiency mode—it answers 400 tasks at 82.8% accuracy for about $6,600.
But if you let it think 172 times longer, exploring many more possible solution paths in parallel, it climbs to 91.5%.
That final push costs $1.15 million in total compute
O3's authors describe this not primarily as an engineering hack but as an ethical one, "deliberative alignment" wherein an overseer system that prunes and merges an entire forest of thought.
They apparently pay the monstrous quadratic cost to keep all those partial reasoning traces in memory, to preserve consistency, and let the model think longer in pursuit of another apparent scaling law.

In effect, by brute-forcing memory into reliability, they show how easily you can approach universal computation if you’re willing to burn a fortune on tokens.
Soon after, OpenAI's Board said that to achieve AGI, we'll just need "unimaginable sums of money", proposing to restructure as a public benefit corporation to attract fresh capital.
They plan to scale up, spin more GPUs, and chase universal intelligence through raw power.

As a sandwich-eating universal intelligence, I'm not convinced.
Humans got smarter not by growing our brains, but by distributing memory across society—spoken word, libraries, the internet—finding ways to preserve and share knowledge without a ruinous overhead.
I'll bet on a resurgence of recurrent approaches that drastically reduce inference costs by maintaining a rolling hidden state, incrementally processing new information (an exciting hybrid direction is "Chain of Continuous Thought").
Yes, we might need specialized modules for robust memory access—but if biology, evolution, and a good pen-and-paper can do it, so can we.
Generality doesn't require industrial-scale power plants.
It just needs a reliable way to remember and recall what you've thought.

Let's remember.
