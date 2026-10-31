---
type: method
title: Handling constraints in a GA
description: Feasible by construction, repair, penalty, Deb's rules, death penalty
---
GA has no native way to handle constraints. Options, in rough order of preference:
1. Feasible by construction: an encoding or decoder that can only produce feasible solutions (e.g., a greedy decoder that assigns customers to the cheapest DC with remaining capacity). Best when possible.
2. Repair: fix infeasible children with a heuristic. Risk: biases the search toward the repair's habits.
3. Penalty: fitness = cost + lambda x violation. Static lambda is hard to tune; too small and the GA converges to infeasible solutions, too large and it can't cross infeasible regions to reach better feasible ones. Dynamic or adaptive lambda (raise it over generations, or when the population is mostly infeasible) helps.
4. Feasibility rules in selection (Deb's rules): feasible beats infeasible; between feasibles, lower cost wins; between infeasibles, lower violation wins. No lambda to tune.
5. Death penalty (discard infeasibles): only when feasible solutions are easy to find.

See [encoding](ga-loop-and-encoding.md) and the [p-median example](p-median-ga-example.md).
