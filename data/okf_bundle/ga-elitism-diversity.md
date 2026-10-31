---
type: concept
title: Replacement, elitism and premature convergence
description: Generational vs steady-state, elitism size, diversity fixes and monitoring
---
Replacement: generational means children replace the whole population; steady-state replaces a few worst each step.

Elitism: carry the top e individuals unchanged, so the best-so-far is never lost. Small e (1-5% of N) is typical; large e reduces diversity.

Premature convergence: the population becomes near-identical early and best fitness plateaus. Fixes: lower selection pressure (smaller tournament, see [selection](ga-selection.md)), raise mutation (or adapt it when diversity drops), fitness sharing or crowding (penalize individuals in crowded regions), island models (sub-populations with occasional migration), restarts that keep the elite.

Monitor diversity explicitly: average pairwise Hamming distance, or fitness standard deviation in the population.
