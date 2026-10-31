---
type: concept
title: Practical forecasting issues in cases
description: Censored demand, promotions, new products, outliers
---
- Censored demand: sales are not demand during stockouts. Flag stockout periods and impute or exclude them, or the model learns to under-forecast.
- Promotions: model uplift explicitly; also cannibalization (other SKUs drop) and halo (complements rise), plus the post-promo dip from pantry loading.
- New products (cold start): forecast from similar products (attribute-based similarity or clusters), or use a launch-curve analog scaled by early sales. Widen safety stock until history builds.
- Outliers and structural breaks: COVID-type periods; down-weight, flag, or drop them.

Related: [ML forecasting features](ml-forecasting.md).
