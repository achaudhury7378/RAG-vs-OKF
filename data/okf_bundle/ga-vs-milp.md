---
type: concept
title: GA vs MILP
description: Optimality, objective type, scale, tuning, best use, hybrid and the honest positioning line
---
| | GA | MILP (branch and bound) |
|---|---|---|
| Optimality proof | None | Yes, with a gap |
| Objective | Any: non-linear, black-box, simulation-based | Linear (or convex with extensions) |
| Scale | Handles huge instances heuristically | May stall on large or weak formulations |
| Tuning | Many parameters | Mostly formulation quality |
| Best use | Non-linear or black-box objectives, simulation-based evaluation, very large combinatorial problems, quick good-enough answers | When a tight formulation solves in time; when you need to prove quality |

Hybrid worth mentioning: GA searches the hard discrete decisions (which facilities open), and an LP solves the continuous part (flows) inside the fitness function. You get exact sub-solutions and heuristic search only where needed.

Honest positioning line: "I'd default to MILP and reach for GA only when the objective isn't linear-izable or the instance is too large; even then, I'd benchmark it against the MILP on small instances."

GA or MILP for facility location? MILP first: linear, well-studied, gives a gap. GA only if costs are non-linear or the instance is too large. See [GA theory](ga-theory.md) and [p-median example](p-median-ga-example.md).
