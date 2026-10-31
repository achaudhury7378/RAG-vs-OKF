---
type: method
title: Classify the demand pattern (Syntetos-Boylan)
description: ADI and CV2 cut-offs and which forecasting methods fit each quadrant
---
The consulting answer is never "I'd use LightGBM". It is: classify the demand, set a naive baseline, pick methods per segment, validate with rolling backtests, and measure in the metric the decision uses.

Syntetos-Boylan classification uses ADI (average interval between non-zero demands) and CV2 (squared coefficient of variation of non-zero demand sizes). The usual cut-offs are ADI = 1.32 and CV2 = 0.49.

| | CV2 < 0.49 | CV2 >= 0.49 |
|---|---|---|
| ADI < 1.32 | Smooth: ETS, ARIMA, ML | Erratic: ML with features, wider safety stock |
| ADI >= 1.32 | Intermittent: Croston, SBA, TSB | Lumpy: Croston-type or aggregate up, consider MTO |

Methods: [baselines, ETS and ARIMA](forecasting-methods.md), [intermittent demand](intermittent-demand.md), [ML global models](ml-forecasting.md).
