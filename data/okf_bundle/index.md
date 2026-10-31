---
type: index
title: EY Supply Chain Interview Notes
---

Knowledge bundle for supply chain interview prep. One concept per file.

- [ABC / XYZ segmentation](abc-xyz-segmentation.md) (method): Applying different inventory policies to different SKUs by value and variability
- [Bullwhip effect](bullwhip-effect.md) (concept): Order variability amplifying upstream, its four causes and remedies
- [Cycle service level vs fill rate](csl-vs-fill-rate.md) (concept): Two service targets that are not the same and how they relate
- [Classify the demand pattern (Syntetos-Boylan)](demand-classification.md) (method): ADI and CV2 cut-offs and which forecasting methods fit each quadrant
- [Economic Order Quantity (EOQ)](eoq.md) (formula): EOQ formula, robustness, worked example, EPQ and quantity discounts
- [Forecast accuracy metrics](forecast-accuracy-metrics.md) (metric): MAE, RMSE, MAPE, WMAPE, MASE, bias, tracking signal, pinball loss and when to use MAPE vs WMAPE
- [Validating a forecasting model](forecast-validation.md) (method): Rolling-origin backtests, error by horizon, baselines, leakage
- [Baselines, exponential smoothing and ARIMA](forecasting-methods.md) (method): Naive baselines, SES/Holt/Holt-Winters, damped trend, ARIMA/SARIMA
- [Practical forecasting issues in cases](forecasting-practical-issues.md) (concept): Censored demand, promotions, new products, outliers
- [Handling constraints in a GA](ga-constraints.md) (method): Feasible by construction, repair, penalty, Deb's rules, death penalty
- [GA crossover and mutation operators](ga-crossover-mutation.md) (method): Operators per encoding, OX/PMX/CX for permutations, mutation rates
- [Replacement, elitism and premature convergence](ga-elitism-diversity.md) (concept): Generational vs steady-state, elitism size, diversity fixes and monitoring
- [Genetic algorithm loop and encoding](ga-loop-and-encoding.md) (concept): The GA loop steps and encodings (binary, integer, real, permutation, random keys)
- [GA selection methods](ga-selection.md) (method): Roulette, rank, tournament, stochastic universal sampling and why tournament is the default
- [GA theory: schema theorem and memetic algorithms](ga-theory.md) (concept): What the schema theorem does and does not say, no optimality bound, memetic GA
- [GA vs MILP](ga-vs-milp.md) (concept): Optimality, objective type, scale, tuning, best use, hybrid and the honest positioning line
- [Hierarchical forecasting](hierarchical-forecasting.md) (method): Bottom-up, top-down, middle-out, MinT reconciliation and choosing the grain
- [Intermittent demand: Croston, SBA, TSB](intermittent-demand.md) (method): Methods for sporadic demand and how each fixes the previous one's bias
- [Rapid self-test Q&A](interview-self-test.md) (faq): Crisp one-minute answers to common interview questions across inventory, forecasting and GA
- [Why inventory exists and the cost trade-off](inventory-types.md) (concept): Ordering, holding and shortage costs and the five types of stock
- [ML global models and probabilistic forecasts](ml-forecasting.md) (method): One LightGBM/XGBoost across all SKUs, features, lag leakage, deep learning, quantile forecasts
- [Newsvendor model (single period)](newsvendor.md) (formula): Critical ratio, underage and overage cost, worked example with two salvage values
- [Worked example: p-median facility location with a GA](p-median-ga-example.md) (example): Encoding, fitness, crossover, mutation, selection and validation for p-median
- [Planning hierarchy and S&OP](planning-hierarchy.md) (concept): Functions, decision horizons, and the monthly S&OP/IBP cycle
- [Inventory review policies](review-policies.md) (method): Periodic vs continuous review safety stock and the (s,Q), (s,S), (R,S), (R,s,S), base stock policies
- [Risk pooling and multi-echelon inventory](risk-pooling-multiechelon.md) (concept): Square-root law, when pooling benefit disappears, stochastic vs guaranteed service models
- [Safety stock and reorder point](safety-stock-and-rop.md) (formula): SS formulas with demand and lead-time variability, z-values, worked example and refinements
- [SCOR model and core supply chain terms](scor-and-terms.md) (concept): Plan-Source-Make-Deliver-Return framing and the vocabulary interviewers expect
- [Key supply chain metrics](supply-chain-metrics.md) (metric): Fill rate, OTIF, perfect order, inventory turns, days of supply, cash-to-cash, forecast accuracy, OEE, cost to serve
