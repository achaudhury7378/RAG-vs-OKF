---
type: formula
title: Safety stock and reorder point
description: SS formulas with demand and lead-time variability, z-values, worked example and refinements
---
SS = z x sigma_d x sqrt(L) (demand variability only).
SS = z x sqrt(L x sigma_d^2 + d-bar^2 x sigma_L^2) (demand and lead-time variability).
ROP = d-bar x L + SS.

z from target cycle service level: 90% -> 1.28, 95% -> 1.645, 98% -> 2.05, 99% -> 2.33.

Worked example: d-bar = 100/day, sigma_d = 20, L = 9 days, 95% CSL.
- Demand variability only: SS = 1.645 x 20 x 3 = about 99, ROP = 900 + 99 = 999.
- Add lead-time sigma_L = 2 days: SS = 1.645 x sqrt(9 x 400 + 10,000 x 4) = 1.645 x sqrt(43,600) = about 344.

Insight to say out loud: lead-time variability more than tripled safety stock. Fixing supplier reliability can free more cash than better forecasting. Lead-time variance enters multiplied by d-bar^2, so it often dominates.

Two refinements interviewers like:
1. sigma_d should be the forecast error standard deviation, not raw demand sigma. Seasonal demand has high sigma but may be well forecast. Safety stock covers what you can't predict. Better forecasts translate directly into lower stock (see [forecast accuracy metrics](forecast-accuracy-metrics.md)); quantify that for the client in rupees, not WMAPE points.
2. The formula targets CSL. For a fill rate target beta, use the expected shortage per cycle: beta = 1 - sigma_LT x G(z) / Q, where G(z) = phi(z) - z(1 - Phi(z)) is the standard normal loss function. Solve for z. See [CSL vs fill rate](csl-vs-fill-rate.md).

Periodic review needs more: see [review policies](review-policies.md). Pooling reduces it: see [risk pooling](risk-pooling-multiechelon.md).
