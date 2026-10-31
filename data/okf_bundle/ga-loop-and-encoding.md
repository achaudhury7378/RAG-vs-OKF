---
type: concept
title: Genetic algorithm loop and encoding
description: The GA loop steps and encodings (binary, integer, real, permutation, random keys)
---
Every GA design choice controls one trade-off: selection pressure (exploit) versus diversity (explore). The probe is usually "why did you choose that operator?"

The loop:
1. Initialize a population of N candidate solutions (random, or seeded with heuristic solutions).
2. Evaluate fitness of each.
3. Select parents (biased toward fitter ones), see [selection](ga-selection.md).
4. Crossover parents to produce children (with probability pc), see [crossover and mutation](ga-crossover-mutation.md).
5. Mutate children (with small probability pm per gene).
6. Replace: form the next generation, usually keeping the best few (elitism), see [elitism and diversity](ga-elitism-diversity.md).
7. Repeat from step 2 until a stopping rule: max generations, time limit, or no improvement for k generations.

Encoding is the most important choice; it decides which operators make sense and whether children stay feasible.

| Encoding | Example problem | Notes |
|---|---|---|
| Binary string | Facility open/close, knapsack | Simple; bit-flip mutation |
| Integer vector | Assign each customer to a DC | Operators must keep values in range |
| Real-valued vector | Continuous parameters, prices | Use blend or SBX crossover, Gaussian mutation |
| Permutation | TSP, job sequencing, VRP routes | Needs special crossover (OX, PMX); one-point crossover creates duplicates |
| Random keys | Any permutation problem | Real vector decoded by sorting into a permutation; any crossover stays valid |

Constraints: [GA constraint handling](ga-constraints.md).
