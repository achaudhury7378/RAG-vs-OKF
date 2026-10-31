---
type: method
title: Inventory review policies
description: Periodic vs continuous review safety stock and the (s,Q), (s,S), (R,S), (R,s,S), base stock policies
---
Periodic review must cover R + L, not just L: SS = z x sigma_d x sqrt(R + L) and S = d-bar (R + L) + SS.

Same numbers as the [safety stock example](safety-stock-and-rop.md) with R = 7: SS = 1.645 x 20 x 4 = about 132, S = about 1,732. Periodic review always needs more safety stock than continuous review.

| Policy | Rule | Fits |
|---|---|---|
| (s, Q) continuous review | When inventory position <= s, order fixed Q | A items, systems with real-time stock visibility |
| (s, S) continuous review | When <= s, order up to S | Lumpy demand, variable order sizes acceptable |
| (R, S) periodic review | Every R periods, order up to S | Coordinated ordering from one supplier, simpler ops |
| (R, s, S) | Every R, if <= s, order up to S | Fewer small orders; harder to optimize |
| Base stock (S-1, S) | Replace each unit as sold | Expensive, slow-moving parts |

The order-up-to level is a newsvendor fractile over R + L, see [newsvendor](newsvendor.md).
