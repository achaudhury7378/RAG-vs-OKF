---
type: concept
title: Bullwhip effect
description: Order variability amplifying upstream, its four causes and remedies
---
Order variability amplifies as you move upstream from retailer to supplier. Measured as Var(orders) / Var(demand) > 1 at each stage.

Four causes (Lee, Padmanabhan and Whang, 1997):
1. Demand signal processing: each stage forecasts from the orders it receives, not true demand.
2. Order batching: periodic or full-truckload ordering creates lumpy orders.
3. Price fluctuations: promotions and forward buying.
4. Rationing and shortage gaming: customers inflate orders when supply is short.

Remedies: share POS data, VMI, CPFR, smaller and more frequent orders, everyday low pricing, allocate shortages on past sales rather than current orders.

Cost to a client and how to show it: plot order variance vs POS demand variance by tier; the excess drives capacity, overtime and safety stock upstream (see [safety stock](safety-stock-and-rop.md)).
