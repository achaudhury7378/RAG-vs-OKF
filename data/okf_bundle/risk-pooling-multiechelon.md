---
type: concept
title: Risk pooling and multi-echelon inventory
description: Square-root law, when pooling benefit disappears, stochastic vs guaranteed service models
---
Risk pooling (square-root law): with n identical locations and independent demand, centralizing stock cuts total safety stock by a factor of sqrt(n). Four DCs merged into one need half the safety stock. The benefit shrinks as demand correlation rises and is zero at perfect positive correlation.

Multi-echelon optimization decides where in the network to hold safety stock (plant, central DC, regional DC). Two model families:
- Stochastic service model (from Clark and Scarf's work): lead times vary when upstream stocks out.
- Guaranteed service model (Graves and Willems): each stage promises a service time to the next; optimize where to buffer. Common in commercial tools.

You are unlikely to be asked the math; explain echelon stock (stock at a node plus everything downstream) and the trade-off between pooling upstream and responsiveness downstream. Base formula: [safety stock](safety-stock-and-rop.md).
