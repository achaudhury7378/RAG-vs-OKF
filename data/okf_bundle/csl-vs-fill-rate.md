---
type: concept
title: Cycle service level vs fill rate
description: Two service targets that are not the same and how they relate
---
CSL = probability of no stockout in a replenishment cycle. Fill rate = fraction of demand met from stock.

They differ: a stockout late in a cycle may miss only a few units, so fill rate is usually higher than CSL for the same policy, especially when order quantities are large. Always ask the client which one their target means.

The [safety stock formula](safety-stock-and-rop.md) targets CSL; for a fill rate target use the expected shortage per cycle (see that page). Order-level service is measured by OTIF in [supply chain metrics](supply-chain-metrics.md).
