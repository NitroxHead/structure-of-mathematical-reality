<!-- AUTHORED: expanded 2026-07-11 -->
# Chapter 12: Information Theory and the Cost of Description
## Phase IV: Information, Compression, and Models
### Slides

---

## Understanding is compression

- Your old intuition: knowing the rule that made the data beats any statistical encoding.
- Chapter 11's debt: universality said the world is compressible but never measured it.
- This chapter measures it, in one currency: the bit.

> Information theory is where "understanding equals compression" becomes an equation you can compute.

## Information is surprise

- Certain event: no information. Unlikely event: a lot.
- Information content of an event of probability p: -log₂(p) bits.
- Coin flip: 1 bit. Fair die: log₂ 6 ≈ 2.58 bits.
- Operationally: the ideal number of yes/no questions to pin the event down.

## Why a logarithm?

- Independent events: their information should *add*.
- But their probabilities *multiply*.
- The only function turning multiplication into addition is the logarithm.
- Base 2 sets the unit; the minus sign keeps information positive.

## Entropy: expected surprise

- Entropy averages the surprise over a whole source:
- H(X) = -Σ p(x) log₂ p(x)
- One number, three questions:
- Uncertainty *before* you observe.
- Information gained *after* you observe.
- Minimum average *description length*.

## Structure is compressibility

- Entropy is largest for the *flattest* distribution.
- Skew or dependence pushes entropy below the maximum.
- That gap below the maximum is the room a compressor works in.

> High entropy is not richness; it is the absence of exploitable structure. The modelable sources are the *low*-entropy ones.

## The hard floor: source coding

- Shannon: you cannot compress below the entropy without loss, and can get arbitrarily close.
- Entropy is a law, not a rule of thumb; no future algorithm beats it.
- Shape (leaning on Chapter 11): almost all long blocks are *typical*.
- There are about 2-to-the-nH of them, each about equally likely.
- Naming one costs about nH bits: H bits per symbol.

## Worked example: a lopsided stream

- One million bits, each 0 or 1, 90% zeros.
- H = -(0.9 log₂ 0.9 + 0.1 log₂ 0.1) ≈ 0.469 bits per symbol.
- Squeezes to about 469,000 bits (≈ 59 kB), no further.
- Compression ratio ≈ 2.13.
- Compressibility is a property of the *source*, not your zip tool.

## KL divergence: the cost of being wrong

- D_KL(P || Q): extra bits per observation from coding true P with a model Q.
- Zero only when Q = P; always at least zero otherwise.
- This is model misspecification, priced in bits.
- Maximum likelihood estimation minimizes it.

## Cross-entropy, decomposed

- H(P, Q) = H(P) + D_KL(P || Q).
- H(P): the truth's entropy, a floor you cannot lower.
- D_KL: your model's penalty, which fitting *can* lower.
- A descending training-loss curve is your model shedding wasted bits.

## Overfitting and regularization

- **Overfitting**: encoding the training set's *noise* as if it were signal; the gain vanishes on new data.
- **Regularization** (L1, L2, dropout): a charge on the model's *description length*.
- Total cost = bits to write the model + bits to write the residuals.
- Spend model-bits only when they buy back more data-bits: the minimum-description-length rule.

## Mutual information

- I(X; Y) = H(X) - H(X|Y): the uncertainty about X that knowing Y removes.
- Symmetric: what X tells you about Y equals what Y tells you about X.
- Zero exactly when X and Y are independent.
- Equals H(X) when Y determines X completely.

## Mutual information beats correlation

- Correlation sees only the linear, monotone part of a relationship.
- Mutual information sees *any* constraint, linear or not.
- Example: X in {-2,-1,1,2}, Y = X². Correlation is 0; dependence is total.
- Zero correlation means "no linear dependence," not "independent."

## The chain that vindicates the intuition

1. A model is a compressed description of behavior.
2. Its quality is its KL divergence from the truth.
3. The best compression is floored by the source's entropy.
4. A short generating rule means low entropy, so tiny models.
5. The rule beats a summary because it compresses *future* data too.

## Statistical vs generative compression

- Statistical (histogram, kernel density): memorizes a *shape*; fails in a new regime.
- Generative (the rule): holds the *mechanism*; extrapolates as far as it reaches.
- A file at its entropy limit looks like random noise: all structure has been spent.

> What you understand, you can remove from the description. What remains is what you do not yet understand.

## Takeaway and the bridge ahead

> Information is surprise; entropy is the hard floor on description; KL is the bit-cost of a wrong model; mutual information is honest dependence; and the shortest faithful description wins because a rule generalizes.

- Every bit here was counted over numbers *handed to you*.
- Chapter 13 asks where the numbers came from, and which operations on them mean anything.
