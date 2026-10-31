---
type: concept
title: GA theory: schema theorem and memetic algorithms
description: What the schema theorem does and does not say, no optimality bound, memetic GA
---
Schema theorem (Holland): short, low-order, above-average schemata grow exponentially across generations. It motivates the building-block idea but is not a convergence guarantee.

No optimality guarantee and no bound: a GA cannot tell you how far you are from the optimum. That is the main argument against it when an exact method is feasible ([GA vs MILP](ga-vs-milp.md)).

Memetic algorithms: GA plus local search on each child (e.g., 2-opt). Usually much stronger than plain GA on combinatorial problems.
