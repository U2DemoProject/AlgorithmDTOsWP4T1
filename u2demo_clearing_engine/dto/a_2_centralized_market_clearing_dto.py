from __future__ import annotations

from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self

from u2demo_clearing_engine.dto.algorithm_libraries.commons_dto import ObjectiveName, OptimizationInstance

# Classes specific to model 4


class OrderStep(BaseModel):  # Simple single-step bid structure
    volume_min: float = Field(..., ge=0, description="Minimum volume in MWh.")
    volume_max: float = Field(..., ge=0, description="Maximum volume in MWh.")
    price: float = Field(..., ge=0, description="Price in €/MWh.")

    @model_validator(mode="after")
    def check_order_step(self) -> Self:
        if self.volume_min >= self.volume_max:
            raise ValueError(
                f"Minimum volume of order step {self.volume_min} should be strictly lower than maximum volume {self.volume_max}"
            )
        return self


class TimeStepOrder(BaseModel):
    order_id: str = Field(..., description="Order identifier")
    linked_order_id: str | None = Field(default=None, description="Linked order identifier")
    timestep: int = Field(..., ge=0, description="Timestep index of the order submission")
    price_volume_curve: list[OrderStep]

    def check_price_volume_curve(self, is_offer: bool):
        for i in range(len(self.price_volume_curve) - 1):
            prev_price = self.price_volume_curve[i].price
            next_price = self.price_volume_curve[i + 1].price
            if is_offer and prev_price >= next_price:
                raise ValueError(
                    f"Volume curve prices of timestep offer order {self.order_id} are not strictly increasing."
                )
            if not is_offer and prev_price <= next_price:
                raise ValueError(
                    f"Volume curve prices of timestep demand order {self.order_id} are not strictly decreasing."
                )

    @model_validator(mode="after")
    def check_step_orders(self) -> Self:
        if len(self.price_volume_curve) == 0:
            raise ValueError(f"Timestep order {self.order_id} has no step order.")
        if self.price_volume_curve[0].volume_min == 0:
            raise ValueError(f"Minimum volume of first price volume curve of timestep order {self.order_id} is null.")
        return self


class Order(BaseModel):
    member_id: str  # Would generalise this statement to "MarketParticipant"
    is_offer: bool
    timestep_orders: list[TimeStepOrder]

    @model_validator(mode="after")
    def check_timestep_orders(self) -> Self:
        for timestep_order in self.timestep_orders:
            timestep_order.check_price_volume_curve(self.is_offer)
        return self

    @property
    def is_demand(self):
        return not self.is_offer

    @property
    def demand_sign(self) -> int:
        """Return 1 if is_demand is True else return -1."""
        return 2 * (self.is_demand - 0.5)


class MarketClearingInput(OptimizationInstance):
    orders: list[Order]


# Outputs of class
class TimeStepClearedOrder(TimeStepOrder):
    cleared_volume: float = Field(..., ge=0, description="Cleared volume in MWh.")
    cleared_price: float = Field(..., ge=0, description="Cleared price in €/MWh.")


class ClearedOrder(BaseModel):
    member_id: str  # Would generalise this statement to "MarketParticipant"
    is_offer: bool
    cleared_timestep_orders: list[TimeStepClearedOrder]


class MarketClearingOutput(OptimizationInstance):
    cleared_orders: list[ClearedOrder]
    clearing_price: list[float | None]
    objective_values: dict[ObjectiveName, float]
