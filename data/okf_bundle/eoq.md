---
type: formula
title: Economic Order Quantity (EOQ)
description: EOQ formula, robustness, worked example, EPQ and quantity discounts
---
Assumes constant known demand, fixed lead time, no shortages, instant replenishment.

TC(Q) = (D/Q) S + (Q/2) h, and Q* = sqrt(2DS / h). At Q*, annual ordering cost = annual holding cost.

Robustness: TC(Q)/TC(Q*) = 1/2 (Q/Q* + Q*/Q). Ordering 20% above Q* raises cost only about 1.7%; ordering 2x Q* raises it 25%. This flatness is why EOQ works despite rough cost inputs.

Worked example: D = 12,000 units/yr, S = Rs 500/order, c = Rs 200, i = 25%, so h = Rs 50. Q* = sqrt(2 x 12,000 x 500 / 50) is about 490 units, about 24.5 orders a year, total cost about Rs 24,500.

Extensions:
- EPQ (production rate P > demand rate D): Q* = sqrt(2DS / (h(1 - D/P))).
- Quantity discounts: compute Q* at each price; if it falls below that price's break, push it up to the break; pick the lowest total cost including purchase cost.

Cost parameters are explained in [why inventory exists](inventory-types.md).
