# Chapter 15: Algorithmic Complexity and the Search for Generative Equations
## Phase IV: Information, Compression, and Models
### Exercises

---

1. Consider the string: 0101010101010101 (length 16). What is its Kolmogorov complexity (approximately, not exactly)? What short program generates it? Now consider a random 16-bit string. What is its Kolmogorov complexity? Why?

2. You have a dataset and you find that a 3-parameter equation fits it with R² = 0.97. Your colleague fits a neural network with 10,000 parameters and gets R² = 0.99. In terms of Kolmogorov complexity: which model provides a better "compression" of the data? What additional information would you need to decide? Is R² the right metric for this question?

3. Design a simple grammar for symbolic regression over one variable: specify the set of operations and the rules for combining them. How many distinct equations of depth 3 (three levels of nesting) does your grammar produce? How would you prune this search space using structural knowledge about the system?

4. Solomonoff induction is uncomputable. List three approximations used in practice (you may look these up). For each, what does it sacrifice relative to the theoretical ideal?

5. The diagonal argument has now appeared four times in this curriculum: Cantor (Chapter 2), Gödel (Chapter 4, via Nagel & Newman), the halting problem, and the uncomputability of K. Write the shared skeleton as a three-step recipe, (a) assume a complete list or decider, (b) construct a defeating object by systematic disagreement, (c) locate the contradiction, then instantiate the recipe explicitly for two of the four cases. Where does the self-reference enter in each?
