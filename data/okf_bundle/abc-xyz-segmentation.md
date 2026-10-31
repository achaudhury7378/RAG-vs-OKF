---
type: method
title: ABC / XYZ segmentation
description: Applying different inventory policies to different SKUs by value and variability
---
The point is to apply different policies to different SKUs instead of one rule for all.

ABC ranks SKUs by annual consumption value (volume x unit cost). Common cut-offs: A = top 70-80% of value, B = next 15-20%, C = the rest. These are conventions, not rules.

XYZ ranks by demand variability, using coefficient of variation CoV = sigma / mu of period demand. Thresholds such as X < 0.5, Y 0.5-1, Z > 1 are common but arbitrary; justify yours from the data.

| | X (stable) | Y (variable) | Z (erratic) |
|---|---|---|---|
| A | Tight control, low SS, automated replenishment | Statistical SS, frequent review | Planner attention, consider MTO or postponement |
| B | Automated, standard policy | Standard statistical policy | Review policy fit |
| C | Automate fully, larger lots | Simple rules | Consider delisting or MTO |

Other schemes: FSN (fast / slow / non-moving), VED (vital / essential / desirable) for spares.

If inventory is high and service poor at the same time, one cause is a single policy for all SKUs; fix with ABC/XYZ-based policies. See [interview self-test](interview-self-test.md) and [review policies](review-policies.md).
