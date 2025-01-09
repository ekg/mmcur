Here's a comprehensive checklist from our entire conversation:

ESSENTIAL FIXES:
- [x] Fix typo: "must of which" → "most of which" in LLMs/Transformers section
- [x] Add "2024" to December morning run
- [x] Remove duplicate (last) reference to how this is an introduction to the arxiv preprint
- [x] Break up long CRISPR sentence about chronological logs
- [x] Change "The Attention Tax" to "The Bitter Pill" (section title + TOC + anchor)

KEY CITATIONS TO ADD:
- [x] https://arxiv.org/abs/2205.11916 for first "Let's think step by step" mention
- [x] https://arxiv.org/abs/2310.07923 "The Expressive Power of Transformers with Chain of Thought" Merrill & Sabharwal for TC0 limitations / chain of thought capabilities (also https://openreview.net/forum?id=NjNGlPh8Wh for reviews and discussion... add inline somehow with a light touch)
- [x] https://arxiv.org/abs/2410.01201 "Were RNNs All We Needed?" if not already cited in closing
- [x] http://www.incompleteideas.net/IncIdeas/BitterLesson.html Sutton's bitter lesson essay
- [ ] https://doi.org/10.1112/plms/s2-42.1.230 Turing 1936 for computation foundations
- [ ] https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo for "MCMC"
- [ ] Sadremomtaz for CRISPR memory
- [ ] https://arxiv.org/abs/2203.15556 "Training Compute-Optimal Large Language Models" by Hoffmann et. al for scaling laws ("Chinchilla optimal")
- [ ] https://doi.org/10.1007/BF02459572 Turing's reaction-diffusion theory
- [ ] https://arxiv.org/abs/2410.21333 "Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse" Liu et al. for chain-of-thought limitations
- [ ] https://arxiv.org/abs/2407.21783 add this Meta Llama 3 technical paper link in addition to the blog post one we have now

FIGURE IMPROVEMENTS:
- [ ] Add axes description to quadratic scaling figure caption
- [ ] Check all image attributions/copyrights

LINK VERIFICATION:
- [ ] Verify all URLs resolve correctly
- [ ] Check xAI/Colossus news links are stable
- [ ] Ensure paper links use consistent format

OPTIONAL REFINEMENTS:
- [ ] Add transition before Herculaneum image
- [ ] Consider italicizing key terms on first use (e.g., _TC0_)
- [ ] Review section transitions for flow
- [ ] Check anchor tag consistency throughout

MINOR TWEAKS:

- [ ] For universal computation/AGI equivalence, you could add a brief clarification when you first connect them:
```markdown
So augmented with bronze age technology, we become "universal" computers in Turing's language—the quintessential "general" intelligence capable of solving any problem given enough time and snacks. For the sake of argument, let's agree: general intelligence ≈ universal computer. (After all, if you can simulate any computation, you can solve any well-defined problem.)
```

- [ ] For the CRISPR transition, perhaps:
```markdown
But the truth is, generality doesn't require a quadratic cost. Nature shows us why. Look at a single cell.
```

- [ ] For MCMC, you could add a brief parenthetical:
```markdown
"forest of thought", MCMC sampled chains-of-thought (exploring multiple possible reasoning paths like a chess computer) which are kept in check.
```
