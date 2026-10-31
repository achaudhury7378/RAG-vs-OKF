---
type: formula
title: Newsvendor model (single period)
description: Critical ratio, underage and overage cost, worked example with two salvage values
---
For perishable or seasonal items: order once, leftover is salvaged, shortage is lost.

Underage cost Cu = price - cost (margin lost per unit short). Overage cost Co = cost - salvage (loss per unit left over). F(Q*) = Cu / (Cu + Co).

Marginal argument: increase Q while the expected gain of one more unit, Cu x P(D > Q), exceeds the expected loss, Co x P(D <= Q).

Worked example: price 100, cost 60, demand ~ Normal(500, 100).
- Salvage 20: Cu = 40, Co = 40, critical ratio 0.5, so Q* = 500.
- Salvage 40: Co = 20, ratio 0.667, z about 0.43, so Q* about 543. Cheaper leftovers justify ordering more.

The critical ratio is also the bridge to (R, S) policies, see [review policies](review-policies.md).
