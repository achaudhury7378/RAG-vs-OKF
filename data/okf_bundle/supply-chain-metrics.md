---
type: metric
title: Key supply chain metrics
description: Fill rate, OTIF, perfect order, inventory turns, days of supply, cash-to-cash, forecast accuracy, OEE, cost to serve
---
| Metric | Formula | Watch out for |
|---|---|---|
| Unit fill rate | Units shipped from stock on first attempt / units ordered | Line fill and order fill are stricter variants |
| OTIF | Orders delivered on time and in full / total orders | Definition of "on time" (requested vs promised date) varies by client |
| Perfect order rate | Share of orders that are OTIF, undamaged and correctly documented | Often approximated as a product of component rates (assumes independence) |
| Inventory turns | COGS / average inventory value | Higher is leaner, but too high risks stockouts |
| Days of supply (DOS / DOH) | Average inventory / average daily COGS, or 365 / turns | Forward-looking DOS uses forecast demand instead |
| Cash-to-cash cycle | DIO + DSO - DPO | Inventory (DIO) is the lever SC teams own |
| Forecast accuracy | 1 - WMAPE | Measure at the grain and lag that drives decisions; see [forecast accuracy metrics](forecast-accuracy-metrics.md) |
| Forecast bias | Sum(F - A) / Sum(A) | Persistent positive bias = excess stock |
| OEE | Availability x Performance x Quality | Manufacturing only |
| Cost to serve | Total cost (logistics, handling, service) per customer or order | Reveals unprofitable customers/channels |

Self-test: fill rate 92% but OTIF 70%? Fill rate counts units; OTIF fails the whole order if any line is short or late. Many orders are missing a few lines, or are complete but late. Check lateness separately.

Related: [cycle service level vs fill rate](csl-vs-fill-rate.md).
