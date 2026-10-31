---
type: concept
title: Planning hierarchy and S&OP
description: Functions, decision horizons, and the monthly S&OP/IBP cycle
---
Decisions get finer in granularity and shorter in horizon as you go down.

| Function | What it decides | Typical analytics |
|---|---|---|
| Planning | How much to make/buy, when, where | Demand forecasting, S&OP, supply planning |
| Procurement | Which supplier, how much, at what terms | Spend analytics, supplier segmentation (Kraljic matrix), supplier risk scoring |
| Manufacturing | What to run on which line, in what sequence | Production planning, lot sizing, scheduling, OEE |
| Inventory | How much stock, where, which policy | Safety stock, reorder policies, multi-echelon optimization |
| Logistics | How goods move | Network design, facility location, VRP, load planning, mode selection |

Planning levels (horizons are typical ranges, not fixed rules):
- Network design (strategic): 2-10 years, sites and lanes; decides which plants/DCs and capacities.
- S&OP / IBP (tactical): 12-24 months, monthly, product families and regions; one agreed volume plan.
- Master production schedule (MPS): weeks to a few months, SKU, weekly; what finished goods to make when.
- MRP: same horizon as MPS, components (BOM explosion); planned orders for parts and materials.
- Scheduling / execution: days and shifts, machine and order; sequence on each line.

S&OP monthly cycle: data gathering, demand review (consensus forecast), supply review (capacity check), pre-S&OP (reconcile gaps, build scenarios), executive S&OP (decide). IBP = S&OP extended to tie volumes to financial plans.

Forecast grain should match the decision, see [hierarchical forecasting](hierarchical-forecasting.md).
