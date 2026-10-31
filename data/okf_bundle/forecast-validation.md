---
type: method
title: Validating a forecasting model
description: Rolling-origin backtests, error by horizon, baselines, leakage
---
Rolling-origin backtest (time-series cross-validation): train up to t, forecast t+1...t+h, roll t forward, average errors. Never a random train/test split.

Report error by horizon (lag), since planners act on a specific lag (for example, the 4-week-ahead forecast that drives a purchase order). Compare against seasonal naive ([baselines](forecasting-methods.md)). Avoid leakage from future-known features ([ML forecasting](ml-forecasting.md)).

Forecast value add (FVA): compare each step (statistical model, planner override, consensus) against naive. If planner overrides make accuracy worse, show it; it is a strong consulting insight. Metrics are in [forecast accuracy metrics](forecast-accuracy-metrics.md).
