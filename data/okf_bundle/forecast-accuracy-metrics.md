---
type: metric
title: Forecast accuracy metrics
description: MAE, RMSE, MAPE, WMAPE, MASE, bias, tracking signal, pinball loss and when to use MAPE vs WMAPE
---
| Metric | Formula | Notes |
|---|---|---|
| MAE | mean abs(A - F) | Scale-dependent |
| RMSE | sqrt(mean (A - F)^2) | Penalizes big misses |
| MAPE | mean abs(A - F) / A | Undefined at A = 0, explodes on low volume, penalizes over-forecasts more |
| WMAPE | Sum abs(A - F) / Sum A | Industry default; volume-weighted, robust to zeros |
| MASE | MAE / in-sample naive MAE | Scale-free; < 1 means better than naive |
| Bias | Sum(F - A) / Sum(A) | Sign shows over/under-forecasting |
| Tracking signal | Cumulative error / MAD | Beyond about +-4 flags persistent bias (rule of thumb) |
| Pinball loss | Quantile loss | For probabilistic forecasts |

When MAPE vs WMAPE? WMAPE for SKU portfolios: volume-weighted, handles zeros. MAPE breaks on low-volume and zero-demand items.

Consensus process: statistical forecast + market intelligence overrides; track bias by who overrides. Safety stock uses the standard deviation of forecast error at the replenishment lead time, so better forecasts translate directly into lower stock ([safety stock](safety-stock-and-rop.md)). Quantify that for the client in rupees, not WMAPE points.
