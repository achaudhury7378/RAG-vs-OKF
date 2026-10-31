---
type: example
title: Worked example: p-median facility location with a GA
description: Encoding, fitness, crossover, mutation, selection and validation for p-median
---
Choose p of m candidate sites to minimize total demand-weighted distance.
- Encoding: a set of p distinct site indices.
- Fitness: assign each customer to its nearest open site, sum demand x distance. Feasible by construction ([constraints](ga-constraints.md)).
- Crossover: pool the two parents' sites, keep common sites, fill to p from the rest (randomly or greedily by cost).
- Mutation: swap one open site for a closed one.
- Selection: tournament, k = 2-3, elitism of 1-2 ([selection](ga-selection.md)).
- Validation: on small instances, compare against the MILP optimum; on large ones, against the LP relaxation bound to estimate the gap ([GA vs MILP](ga-vs-milp.md)).
