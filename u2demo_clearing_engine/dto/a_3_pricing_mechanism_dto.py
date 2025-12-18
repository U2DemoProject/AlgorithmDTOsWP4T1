from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel

from u2demo_clearing_engine.dto.algorithm_libraries.commons_dto import (
    OptimizationInstance,
    TimeParameters,
    TimeValue,
)

# Classes specific to model 3


class RetailPrices(BaseModel):
    injection_price: list[TimeValue]
    offtake_price: list[TimeValue]


class PricingRule(StrEnum):
    MID_MARKET = "Mid-market rate"
    SUPPLY_DEMAND = "Supply-demand ratio"


class PricingMechanismInput(OptimizationInstance):
    time: TimeParameters
    pricing_rule: PricingRule
    loads: list[TimeValue]
    productions: list[TimeValue]
    prices: RetailPrices


# Output of algorithm
class BillingReprocessing(BaseModel):
    contract_id: str
    payback_amount: float
    supplier_id: str | None
    notes: str | None


#  The same algo is ran twice (with forecast and realized values)
class PricingMechanismOutput(OptimizationInstance):
    internal_prices: list[TimeValue]
    billing: list[BillingReprocessing]
