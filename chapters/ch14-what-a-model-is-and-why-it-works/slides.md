<!-- AUTHORED: expanded 2026-07-11 -->
# Chapter 14: What a Model Is and Why It Works
## Phase IV: Information, Compression, and Models
### Slides

---

## The Question This Chapter Closes

- The world is not made of numbers, yet operations on numbers predict it.
- Chapter 6 gave a first answer; Chapter 12 made it about compression.
- Now: one structural definition that every modeling decision is a case of.
- Prediction is a round trip: measure in, compute, read out, check the world.

## What A Model Is

- A **system** in the world (states, behaviors, regularities).
- A **mathematical structure** (equations, distribution, graph, space).
- The **model** = a map claiming their features and operations correspond.

> A model works when the correspondence is *structure-preserving*: a homomorphism (Ch 7, Ch 16) with one foot in the world.

## Worked: Michaelis-Menten As A Map

- System: enzyme turning substrate to product.
- Structure: `v = Vmax*[S]/(Km+[S])`, one saturating function.
- Correspondence: [S] to input, v to output, Vmax to ceiling, Km to half-max.
- Preserved: rate-vs-substrate shape. Discarded: every molecular collision.
- It predicts because the relationship, not the material, is mirrored.

## Map Is Not The Territory

- The slogan is used to dismiss models; it misses the point.
- A map works *because* its structure corresponds to the territory's.
- Subway map preserves connectivity, destroys distance (a topology question).
- Road atlas preserves distance (a geometry question). Same city, two maps.
- Wrong map = preserving the wrong structure, not being inaccurate.

## "Wrong But Useful," Structurally (Box)

- **Wrong** = the structure the model discards.
- **Useful** = the structure the model preserves and predicts with.
- Every good model is both, with no tension between them.
- Failure = a correspondence you were relying on breaks.

## Failure 1: Structural Misspecification

- The model assumes a structure the system does not have.
- Linear fit to a threshold or switch (Hill-shaped dose-response).
- No amount of data fixes it: it is the wrong *type* of object.
- This is Chapter 10's bifurcation, seen from the inside.

## Failure 2: Resolution

- Right type of structure, wrong *level*.
- Too fine: every molecule when thermodynamics is the answer.
- Too coarse: bulk RNA-seq on two cell states gives a phantom average cell.
- Chapter 11's universality is why a right level exists to be found.

## Failure 3: Boundary

- Right structure, right level, wrong *domain*.
- The correspondence held locally; you extrapolated past the edge.
- qPCR standard curve outside its range; polynomial just past the data.
- The structure was never wrong; its domain was smaller than you acted.

## The Diagnostic Table

| Failure | What is wrong | Named by |
|---|---|---|
| Misspecification | wrong *type* | wrong field (Ch 3) |
| Resolution | wrong *level* | wrong rung (Ch 11) |
| Boundary | wrong *domain* | map's validity range |

- Three different sentences, three different repairs. Do not confuse them.

## Occam's Razor Is Not Taste

- "Prefer the simpler model" has an information-theoretic justification.
- A flexible model could fit many datasets, so it barely predicted yours.
- A tight model that fits made a risky prediction and was right.
- Being right where you could easily be wrong is what evidence *is*.

## The Occam Factor

- Evidence = probability a model assigns to the data, averaged over parameters.
- Each model spreads one unit of probability over the data it could produce.
- Many parameters smear it thin; few parameters concentrate it.
- Logistic (3 params) vs degree-20 polynomial: both fit, logistic wins on evidence.
- Buy a parameter only when the data force it (the bias-variance trade).

## Simplicity = Predictive Strength

- Overfitting = a long description (Ch 12): the noise is in the parameters.
- Train-good / test-bad is boundary failure and long description at once.
- A generative equation has few parameters and concentrates its probability.
- Capturing the mechanism beats capturing the pattern. (Ch 15 takes this to its limit.)

## Two Directions Of "Model"

- Scientist's model: world to mathematics (a structure mirrors a system).
- Logician's model (model theory): axioms to structure (ℤ is a model of the group axioms).
- One bridge: axioms specify a type (Ch 4), structures are models of them, a scientific model claims one mirrors the world.
- Ask which arrow someone means. Model theory: settled discipline, revisited in Ch 17.

## Where You Now Stand

- A model is a structure-preserving map: wrong in what it drops, useful in what it keeps.
- Three diagnosable failures; simplicity is evidential strength, not taste.
> Next: if evidence rises as description shortens, the strongest model is the shortest program that outputs the data. Chapter 15 names that limit, ties it to your compression intuition, and shows you the wall.
