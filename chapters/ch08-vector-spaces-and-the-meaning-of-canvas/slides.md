<!-- AUTHORED: expanded 2026-07-11 -->
# Chapter 8: Vector Spaces and the Meaning of "Canvas"
## Phase III: The Grammar of Structure
### Slides

---

## The Reframe

- You already run linear algebra fluently: covariance, PCA, weight matrices.
- This chapter does not teach it; it makes the choices inside it visible.
- Chapter 7 left a thread: representations act on a vector space. What is that?
- The payoff is your own intuition, made precise: linearity lives in the canvas.

## What a Vector Space Is

- A set of objects you can *add* and *scale*, obeying a short list of axioms.
- The axioms never say "arrow" or "column of numbers."
- So the only membership test is: closed under adding and scaling.
- It is a type of *structure*, not a type of object.

## Vectors That Are Not Columns

- Functions ℝ → ℝ : add their values, scale them. Zero is the zero function.
- Solutions of a linear differential equation (this is why superposition works).
- Quantum states: adding and scaling is the physics, not a metaphor.
- Polynomials of degree at most 3: a 4-dimensional space.

## Basis and Dimension

- A basis is a minimal kit of building blocks; dimension is its size.
- Same dimension for every basis: a fact about the space, not the description.
- **A choice of basis is a choice of description, not a fact about the space.**
- Coordinates change with the basis; the vector does not move.

## Worked: One Polynomial, Two Frames

- 2x³ - x + 5 in the basis {1, x, x², x³}: coordinates (5, -1, 0, 2).
- In the basis {1, (x-1), (x-1)², (x-1)³}: different coordinates (a Taylor report).
- The numbers changed completely; the polynomial is identical.
- Choosing features is choosing a basis. Re-encoding moves coordinates, not the data.

## Linear Maps

- Preserve addition and scaling: f(u+v) = f(u)+f(v), f(cv) = cf(v).
- The third instance of the Chapter 7 theme (operation, addition/scaling, nearness).
- A matrix is the *coordinate report* of a map once bases are chosen.
- Change the basis and the matrix changes; the map does not.

## Eigenvalues Are the Invariants

- The matrix is an artifact of your basis. What is real about the map?
- Eigenvalues: scaling factors along special directions, unchanged by basis.
- They belong to the map, not the coordinates (like the determinant, Chapter 5).
- Covariance eigenvalues = variance along principal directions, coordinate-free.

## Linearity Lives in the Canvas

- Choose a representation (encode the state as a vector): that is the canvas.
- On that canvas the evolution is either linear (matrix multiplication) or not.
- A different canvas can flip the same evolution linear or nonlinear.
- Linearity is a fact about system-and-canvas, not about the system alone.

## Worked: Population Growth

- Count N(t): the growth curve N(t) = N₀eʳᵗ *bends* when plotted against time.
- Log canvas: log N(t) = log N₀ + rt draws as a straight line.
- Same bacteria, same system; only the canvas changed the *shape of the plot*.
- Two senses of "linear": as a rule, dN/dt = rN already superposes on the N canvas; the log canvas straightens the *graph*, a different (everyday) sense.

## Linearization

- No exact linear canvas? Use one that is linear in a small region.
- Linearizing near equilibrium replaces the map by its best linear stand-in.
- Assumption: deviations are small enough that superposition holds well.
- A flat canvas touching a curved system at one point (doorway to Chapter 10).

## Inner Products Add Geometry

- Adding, scaling, and bases carry no length or angle.
- An inner product supplies length, angle, and orthogonality.
- Not every space has a natural one; when there is a choice, it matters.
- Different inner products make different vectors count as perpendicular.

## PCA as a Change of Canvas

- Old canvas: 100 measured features, one axis each.
- New canvas: eigenvectors of the covariance, ordered by variance.
- Keep the top 3: dimension 100 → 3.
- Lost: 5% of variance and exact invertibility. Gained: compression.

> Eigenvalues = variance per direction = the system's intrinsic dimensionality.

## Which Analyst Is Right?

- Raw features vs PCA features, same algorithm, different results: neither is simply wrong.
- They assume different bases and inner products for the phenomenon's geometry.
- Rotate before clustering and clusters move: the algorithm is not rotation-invariant.
- The "right" inner product matches the system's own notion of similarity.

## Takeaway and Bridge

- A vector space is a structure; a canvas is a basis plus an inner product.
- Linearity, coordinates, and matrices are canvas-dependent; eigenvalues are not.
- Buying geometry cost an inner product: distances and angles, and they are fragile.
- Chapter 9: throw all measurement away, keep only nearness. That is topology.
