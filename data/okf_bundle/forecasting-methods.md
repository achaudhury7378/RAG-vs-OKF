---
type: method
title: Baselines, exponential smoothing and ARIMA
description: Naive baselines, SES/Holt/Holt-Winters, damped trend, ARIMA/SARIMA
---
Baselines (always report these): naive (last value), seasonal naive (same period last year/week), moving average. A model that can't beat seasonal naive is not worth deploying.

Exponential smoothing (ETS): simple exponential smoothing is level only, l_t = alpha y_t + (1 - alpha) l_(t-1). Holt adds trend. Holt-Winters adds seasonality; additive when seasonal swings are constant in size, multiplicative when they scale with level. Damped trend is often the safer default for longer horizons.

ARIMA / SARIMA: AR(p) = regression on own lags, I(d) = differencing for stationarity, MA(q) = regression on past errors. SARIMA adds seasonal terms. Identify via ACF/PACF or auto-search on AIC. ARIMAX adds regressors like price or promo. Weakness at scale: one model per series, slow across thousands of SKUs.

Choosing a method depends on the [demand pattern](demand-classification.md). Check against baselines using [forecast validation](forecast-validation.md).
