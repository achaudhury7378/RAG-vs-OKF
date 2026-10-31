---
type: faq
title: Rapid self-test Q&A
description: Crisp one-minute answers to common interview questions across inventory, forecasting and GA
---
- Fill rate is 92% but OTIF is 70%. How? See [supply chain metrics](supply-chain-metrics.md): fill rate counts units; OTIF fails the whole order if any line is short or late.
- Inventory is high and service is poor at the same time. Why? Wrong stock in the wrong place: excess on slow C items, shortages on A items; one policy for all SKUs; biased forecasts per SKU; long or variable lead times. Fix with ABC/XYZ-based policies ([segmentation](abc-xyz-segmentation.md)) and re-allocation.
- Why use forecast error sigma, not demand sigma, in safety stock? Safety stock covers what you can't predict. Seasonal demand has high sigma but may be forecast well ([safety stock](safety-stock-and-rop.md)).
- How does lead-time variability affect safety stock? It enters multiplied by d-bar^2, so it often dominates; reducing supplier variability can cut SS more than better forecasting.
- When MAPE vs WMAPE? WMAPE for SKU portfolios ([metrics](forecast-accuracy-metrics.md)).
- How do you forecast a new product? Analog SKUs by attributes or clusters, scale by early sales, widen safety stock until history builds ([practical issues](forecasting-practical-issues.md)).
- How do you validate a forecasting model? Rolling-origin backtest, error by horizon, compare against seasonal naive, no leakage ([validation](forecast-validation.md)).
- Why tournament selection? Scale-invariant, works on cost directly, one parameter for pressure ([selection](ga-selection.md)).
- How do you handle constraints in a GA? Prefer feasible-by-construction decoders, then repair or adaptive penalties, or Deb's feasibility rules ([constraints](ga-constraints.md)).
- How do you know your GA is good? Benchmark against MILP optimum on small instances and the LP bound on large ones; check run-to-run variance across seeds.
- GA or MILP for facility location? See [GA vs MILP](ga-vs-milp.md).
- What does a bullwhip effect cost a client, and how do you show it? See [bullwhip effect](bullwhip-effect.md).
