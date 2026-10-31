---
type: method
title: GA selection methods
description: Roulette, rank, tournament, stochastic universal sampling and why tournament is the default
---
| Method | How | Trade-off |
|---|---|---|
| Roulette (fitness-proportional) | P(select) proportional to fitness | Needs positive fitness; one super-fit individual takes over early; pressure vanishes when fitnesses are similar |
| Rank-based | P proportional to rank, not raw fitness | Scale-invariant; steady pressure |
| Tournament (size k) | Pick k at random, best wins | Default choice: no scaling needed, works for minimization, k tunes pressure (k = 2 mild, larger k stronger) |
| Stochastic universal sampling | Roulette with evenly spaced pointers | Lower variance than roulette |

Defensible answer: "Tournament, because it's invariant to fitness scaling, works directly on cost for minimization, and k gives me one knob for selection pressure."

Part of the [GA loop](ga-loop-and-encoding.md).
