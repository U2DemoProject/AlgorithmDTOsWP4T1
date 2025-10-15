from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class OptimizationInstance(BaseModel):
    instance_id: str


class TimeParameters(BaseModel):
    timestep_minutes: int
    horizon_hours: int
    scheduling_time: datetime


class TimeValue(BaseModel):
    time: datetime
    value: float


class ForecastType(StrEnum):
    DETERMINISTIC = "deterministic"
    STOCHASTIC = "stochastic"


class Forecast(BaseModel):
    forecast_type: ForecastType
    forecast_date: datetime
    forecast_values: list[list[TimeValue]]


class Schedule(BaseModel):
    schedule: list[TimeValue]


class Prices(BaseModel):
    prices: list[TimeValue]


class ContractCategory(StrEnum):
    FIXED = "fixed"
    PEAK_OFF_PEAK = "peak_off_peak"


class Supplier(BaseModel):
    category: ContractCategory
    supply_prices: Prices
    resale_prices: Prices
    capacity_tariffs: Prices
    max_power_consumed_kw: float | None = None  # These set the grid connection capacity limit
    max_power_injected_kw: float | None = None  # These set the grid connection capacity limit


class Contract(BaseModel):
    id: str
    supplier: Supplier
    linked_distribution_point: str | None = None


class Meter(BaseModel):
    id: str
    contract_id: str
    power_kw: list[TimeValue]
    contract: Contract


class CommunityMember(BaseModel):
    id: str
    meters: list[Meter]


class ObjectiveName(StrEnum):
    SOCIAL_WELFARE = "social_welfare_maximisation"
    CLEARED_VOLUME = "cleared_volume_maximisation"
    COST_MINIMISATION = "cost_minimisation"
    GRID_SUPPLY = "grid_supply_minimisation"
    RENEWABLE_SUPPLY = "renewable_supply_maximisation"


class Objective(BaseModel):
    name: ObjectiveName = Field(..., description="Objective name.")
    weight: float | None = Field(
        default=1,
        ge=0,
        le=1,
        description="Preservation factor of the objective in next optimization phase. If 1 the objective will be fully preserved.",
    )
