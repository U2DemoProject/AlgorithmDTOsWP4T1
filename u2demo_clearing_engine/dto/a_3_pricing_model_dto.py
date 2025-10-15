from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel

from u2demo_clearing_engine.dto.algorithm_libraries.commons_dto import (
    OptimizationInstance,
    TimeParameters,
    TimeValue,
)

# Classes specific to model 3
"""
Following classes not needed?
class OfftakeOrder(BaseModel): 
    timestep: datetime      
    offtake_volume: float 

class InjectionOrder(BaseModel): 
    timestep: datetime
    injection_volume: float  

class OfftakePrice(BaseModel): 
    timestep: datetime
    value: float

class InjectionPrice(BaseModel):
    timestep: datetime
    value: float  
"""


class RetailPrice(BaseModel):
    # timestep: datetime            #Implied in the other arguments?
    injection_price: TimeValue
    offtake_price: TimeValue


class PricingRule(StrEnum):
    MID_MARKET = "Mid-market rate"
    SUPPLY_DEMAND = "Supply-demand ratio"


class PricingModelInput(OptimizationInstance):
    time: TimeParameters
    pricing_rule: PricingRule
    loads: list[TimeValue]  # [OfftakeOrder]
    productions: list[
        TimeValue
    ]  # [InjectionOrder] #should we link to the devices? since it can be forecasted by the CM, maybe different?
    prices: list[RetailPrice]


# Output of algorithm
class BillingReprocessing(BaseModel):
    contract_id: str
    payback_amount: float
    supplier_id: str | None
    notes: str | None


#  The same algo is ran twice (with forecast and realized values)
class PricingModelOutput(OptimizationInstance):
    internal_prices: list[TimeValue]
    billing: list[BillingReprocessing]  # not sure if it should be here or as a post-process
