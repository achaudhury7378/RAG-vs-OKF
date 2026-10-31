---
type: method
title: GA crossover and mutation operators
description: Operators per encoding, OX/PMX/CX for permutations, mutation rates
---
Crossover combines good partial solutions (building blocks) from two parents.
- Binary or integer: one-point, two-point, uniform (each gene from either parent with probability 0.5). Uniform mixes more but breaks up adjacent good genes.
- Real-valued: arithmetic (child = lambda p1 + (1 - lambda) p2), BLX-alpha (sample from an interval extended around the parents), SBX (simulated binary crossover).
- Permutation: OX (order crossover) copies a slice from parent 1 and fills the rest in the order they appear in parent 2, preserving relative order. PMX (partially mapped) copies a slice and resolves conflicts through the mapping, preserving absolute positions. CX (cycle crossover) takes each position from one parent, following cycles.
Typical pc is 0.6-0.9 in textbooks; treat it as a tuning parameter, not a rule.

Mutation keeps diversity and makes every solution reachable, so the search can escape local optima.
- Binary: flip each bit with probability about 1/L (L = string length).
- Real: add Gaussian noise; the step size can shrink over generations.
- Permutation: swap two positions, insert one element elsewhere, or invert a segment (inversion is the 2-opt move for TSP).
Too low means premature convergence; too high means random search ([diversity](ga-elitism-diversity.md)).

Operators must match the [encoding](ga-loop-and-encoding.md).
