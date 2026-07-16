<!-- AUTHORED: expanded 2026-07-11 -->
# Chapter 3: The Map of Mathematical Fields
## Phase I: What Mathematics Is
### Slides

---

## What This Map Is For

- Not to file ideas into boxes.
- To locate yourself when your own work stalls.
- Name the field you are standing in, find the tool you need.
> A good map says what each region is *for* and how to cross between them.

## Each Field, One Central Question

| Field | It asks |
|---|---|
| Algebra | what are the symmetries of this structure? |
| Analysis | what happens in the limit? |
| Geometry | what survives rigid motion? |
| Topology | what survives continuous deformation? |
| Number theory | how are the primes distributed? |
| Logic | what can (and cannot) be proved? |
| Probability | what can be inferred under uncertainty? |

## Orientations, Not Definitions

- The question is a *compass bearing*, telling you which way a field faces.
- One object can be interrogated by several fields at once.
- Each field's question extracts something different from it.
- That overlap is the map's most useful feature, not a defect.

## The Borders Hold the Power

> When two fields ask the same question about different objects, a bridge forms.

- A bridge beats either field alone: carry a hard question across, answer, carry back.
- Inside one field you are stuck with one toolkit; a bridge frees you.
- The border is not a boundary. It is a translation.

## Four Load-Bearing Bridges

- **Algebraic geometry**: polynomial equations = geometric shapes.
- **Analytic number theory**: continuous functions govern the discrete primes.
- **Differential geometry**: calculus on curved surfaces (and curved data).
- **Algebraic topology**: attach algebra to shapes to tell them apart.
- Each lets one field's tools answer another field's question.

## Bridges Already in Your Work

- Persistent homology (TDA) = algebraic topology on point clouds.
- The manifold hypothesis = differential geometry on high-dimensional data.
- Steady states of a reaction network = algebraic geometry (polynomial solution sets).
- Robust features survive noise because they are *topological*, not metric.

## One Object, Three Fields: The Eigenvalue

- Algebraic: a root of the characteristic polynomial.
- Analytic: sets the rates and long-term behavior of a system.
- Geometric: a stretch factor along a principal axis.
- Biologist, physicist, geometer are not disagreeing; each names one facet.
- Which field you adopt decides which powers you may use.

## Same Decomposition, Two Readings

- PCA: eigenvalues *geometrically* = variance along principal axes.
- Markov chain: eigenvalues *analytically* = stationary state and mixing rate.
- The math object is identical; the question you bring changes the meaning.
- Eigendecomposition is powerful because it works *along the grain* (Ch 5, Ch 8).

## "Are These Two Clusters Different?"

- Probability: unlikely to share one underlying distribution (a test).
- Geometry: centers far apart relative to spread (metric distance).
- Topology: two disconnected pieces, not one blob (connectivity).
- Same question, three fields, three non-interchangeable meanings.
- Knowing which you want is half of asking well.

## Hierarchy: How Much Structure Is Kept

- Geometry (distance, angle) → forget distance →
- Topology (only continuity) → forget continuity →
- Set theory (only membership).
- Each step forgets something; what remains is more general, less powerful.
- More structure = fewer situations, stronger results; less = more situations, weaker.

## The Algebraic Ladder

- Fields (+, ×, both invertible: ℝ, ℂ) → forget × inverses →
- Rings (two operations, × not invertible: ℤ) → drop an operation →
- Groups (one operation, with inverses) → forget inverses →
- Monoids (one associative operation: ℕ under +).
- A theorem proved low on the ladder holds everywhere above it (Ch 7).

## Cube = Sphere, Donut Different

- Topology already forgot distance, angle, curvature.
- What it keeps is connectivity and holes.
- Euler characteristic: cube 2, sphere 2, donut 0.
- "Topologically protected" = survives all continuous deformation.
- Only a tear or glue (a discontinuous event) can destroy it, never mere noise.

## The Many Meanings of Distance

- Euclidean distance: geometry, most specific, richest (trigonometry).
- Metric (three axioms): analysis, holds for any sensible space.
- Neighborhoods: topology, only "near," no "how near."
- KL divergence: information theory, not even a metric (asymmetric).
> Most structure and least general, down to least structure and most general.

## Choosing the Right Generality

- Too specific: your result is a one-off, true of your data and nothing else.
- Too general: nothing strong is left to say.
- The skill: use the *least* structure the problem actually needs.
- Then your conclusion is as portable as the problem allows.
- You feel this every time you weigh a bespoke model against a general method.

## Where You Now Stand

- Fields are oriented by a question, joined by bridges, ranked by structure kept.
- One object can live at several fields at once; pick the field, unlock its powers.
- Choosing generality is now a navigable axis, not a matter of taste.
> One cell waited: Logic, "what can be proved?" Chapter 4 opens Phase II, formal systems, proof as mechanism, and Gödel's limit where Chapter 2's diagonal returns.
