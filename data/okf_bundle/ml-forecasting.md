---
type: method
title: ML global models and probabilistic forecasts
description: One LightGBM/XGBoost across all SKUs, features, lag leakage, deep learning, quantile forecasts
---
One gradient-boosted model (LightGBM/XGBoost) trained across all SKU-store series shares patterns across series and handles thousands of SKUs.

Features: lags (t-1, t-7, t-52), rolling means and std, calendar (week, month, holidays, paydays), price and discount depth, promo flags, display/feature, stockout flags, SKU and store attributes, weather where relevant.

Lags must respect the horizon: to forecast 4 weeks out, the shortest usable lag is 4 weeks. Using lag-1 for a 4-week horizon is leakage. Freeze features as known at forecast time; promo plans that change later are a common hidden leak. See [forecast validation](forecast-validation.md).

Deep learning options you can name: DeepAR, N-BEATS, Temporal Fusion Transformer. Usually only worth it at large scale.

Probabilistic forecasts: inventory needs a distribution, not a point. Use quantile regression (pinball loss) in LightGBM, or residual-based intervals. The 95th percentile forecast feeds [safety stock](safety-stock-and-rop.md) directly.
