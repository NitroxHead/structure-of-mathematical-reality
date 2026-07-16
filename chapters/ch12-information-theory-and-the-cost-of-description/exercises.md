# Chapter 12: Information Theory and the Cost of Description
## Phase IV: Information, Compression, and Models
### Exercises

---

1. You have a dataset of 1 million values, each either 0 or 1, with 90% zeros. What is the entropy? What is the minimum number of bits needed to store the dataset? Compare this to the naive storage of 1 million bits. What is the compression ratio?

2. You fit two models to the same data: a linear model and a neural network. The neural network has lower cross-entropy loss. In information-theoretic terms, what does this mean? Does it necessarily mean the neural network is a better model? What additional information would you need to decide?

3. In your data science work, you have almost certainly used regularization (L1, L2, dropout). Regularization penalizes model complexity. Restate this in information-theoretic terms: what is regularization doing to the *description length* of the model? Why does this help generalization?

4. You have two variables, X and Y. Their correlation is 0 but their mutual information is high. Draw or describe a situation where this is possible. What does this tell you about the limitations of correlation as a measure of dependence?
