<!-- AUTHORED: expanded 2026-07-11 -->
# Chapter 10: Dynamics and Approximation: The Structure of Change
## Phase III: The Grammar of Structure
### Slides

---

## What a Dynamical System Is

- Anything that runs forward in time by a rule: a population, a drug clearing, a gene switching on.
- The field your mechanistic instinct already lived in, unnamed.
- The flagship example (decay = populations = capacitors) is a fact about *change*, not algebra.
> Topology gave a static stage. Dynamics puts a flow on it.

## State and State Space

- **State**: the minimal numbers that fix the entire future from *now*.
- Isotope: one number (amount). Pendulum: two (angle *and* angular velocity).
- Minimal = the present is a sufficient summary of the past (Markov property).
- The set of all states is the **state space** (phase space).

## The Flow

- The rule dx/dt = f(x) is a *vector field*: an arrow at every point.
- A trajectory = drop a marble, follow the arrows.
- Stop studying one history; study the whole field of all histories at once.
> State space = the canvas of Chapter 8, now set in motion.

## Fixed Points: The Skeleton

- A **fixed point** is where f(x) = 0: velocity vanishes, the system stays.
- Equilibria are the skeleton of the flow; find them first.
- Stability is NOT read off the equilibrium *value*.
- It is a property of the flow *around* the point: do neighboring arrows converge or flee?

## Three Kinds of Equilibrium

- **Stable**: pulls nearby states in. Marble in a bowl.
- **Unstable**: pushes nearby states away. Marble on a dome.
- **Saddle**: stable some directions, unstable others. Marble on a mountain pass.
- Same location can be stable or unstable; the flow around it decides.

## Logistic Worked Example

- dN/dt = rN(1 - N/K). Fixed points: N = 0 and N = K.
- Small N: arrows point right (grow). Above K: arrows point left (fall back).
- Extinction (0) is unstable; carrying capacity (K) is stable.
- Read straight off the arrows, without solving the equation.

## Linearization

- Near x*, write state as x* + δ, with δ small.
- Taylor: f(x* + δ) = f(x*) + f'(x*)·δ + (order δ² and smaller).
- At a fixed point f(x*) = 0, so dδ/dt ≈ f'(x*)·δ.
- Local evolution is *linear*; the coefficient is the **Jacobian** matrix.

## Eigenvalues Are Rate Constants

| Jacobian eigenvalue | What the flow does |
|---|---|
| negative real part | decays, stable |
| positive real part | grows, unstable |
| nonzero imaginary part | rotates, oscillation |

- The eigenvalue is the *rate constant* of the flow (its analytic role, Chapter 3).

## Why Linear Methods Work

- Not because the world is linear. Because the world is *smooth*.
- Taylor: a smooth system, viewed closely near equilibrium, *is* linear.
- That is the deepest reason linear algebra is disproportionately powerful.
> Linearity is the first-order shadow every smooth system casts near a fixed point.

## Linearity Lives in the Canvas

- Exponential growth: nonlinear in N, perfectly linear in log N. Same system, different canvas.
- Your own intuition, made exact: linearity is system-plus-canvas, not the system alone.
- The displacement δ *is* the right canvas, handed to you for free near equilibrium.
- Error, stability margin, and perturbation size are one quantity: the size of δ.

## Multistability

- Two or more stable fixed points; outcome depends on where you start.
- State space splits into **basins of attraction** separated by ridges.
- Cell-fate decisions, genetic toggle switches, hysteresis: memory in the landscape.
- A linear system has one equilibrium, so it can offer only one destiny.

## Oscillation

- A **limit cycle**: a closed loop trajectories spiral onto. A stable *rhythm*.
- Circadian clocks, heartbeats, predator-prey, gene oscillators.
- Linear systems oscillate only at a knife's edge, amplitude set by the kick.
- Born in a **Hopf bifurcation**: a complex eigenvalue pair crosses into positive real part.

## Bifurcation: The Meaning of Threshold

- A *qualitative* reorganization of the flow as a parameter crosses a critical value.
- A fixed point appears, vanishes, or swaps stability; behavior changes all at once.
- This is the "threshold" a linear (proportional-everywhere) model structurally cannot carry.
- It is Chapter 14's "structural misspecification" seen from the inside.

## Chaos

- Deterministic yet unpredictable: an exact rule, no randomness.
- Nearby trajectories separate exponentially (sensitive dependence).
- Short rule, incompressible long-range behavior.
> "We know the equations" and "we can predict the future" are different claims (Chapter 15).

## Feedback = Sign of the Jacobian

- A term in f(x) that depends on x is a feedback loop.
- Negative feedback builds stable points: homeostasis.
- Positive feedback builds switches and multistability.
- Fast negative + slow positive builds oscillation. Same fact as the Jacobian's sign.

## Where You Now Stand

- Change has structure: fixed points, stability, bifurcations; and multistability, oscillation, chaos.
- Approximation is Taylor's theorem: smoothness makes the world locally linear.
- Your next real wall will usually be a nonlinear-dynamics wall; now you have its name.
> Next: Chapter 11. A system can be determined yet unpredictable, and one fixed point can govern many mechanisms. Probability and universality take that step.
