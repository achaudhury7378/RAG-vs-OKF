---
type: method
title: Intermittent demand: Croston, SBA, TSB
description: Methods for sporadic demand and how each fixes the previous one's bias
---
Croston: separately smooths non-zero demand size and the interval between demands; forecast = size / interval.

Croston is biased upward; SBA corrects it with a factor (1 - alpha/2).

TSB smooths demand probability every period instead of interval, so it decays toward zero for obsolete items.

Used for the intermittent quadrant of the [demand classification](demand-classification.md). For lumpy demand consider aggregating up or make-to-order.
