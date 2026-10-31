---
type: method
title: Hierarchical forecasting
description: Bottom-up, top-down, middle-out, MinT reconciliation and choosing the grain
---
Forecasts exist at many levels (SKU-store-week up to category-national-month) and must add up. Pick the forecast grain to match the decision: replenishment needs SKU-location-week, S&OP needs family-month (see [planning hierarchy](planning-hierarchy.md)).

| Approach | How | Trade-off |
|---|---|---|
| Bottom-up | Forecast lowest level, sum up | Keeps detail; noisy at the bottom |
| Top-down | Forecast top, split by historical proportions | Stable; loses local patterns |
| Middle-out | Forecast a middle level, go both ways | Compromise |
| Optimal reconciliation (MinT) | Forecast all levels, then reconcile using the error covariance | Usually most accurate; more compute |
