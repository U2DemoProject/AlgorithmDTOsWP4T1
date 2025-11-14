from __future__ import annotations

import datetime
from enum import Enum

from pydantic import BaseModel, Field

from u2demo_clearing_engine.dto.algorithm_libraries.commons_dispatch_optimization_dto import Asset
from u2demo_clearing_engine.dto.algorithm_libraries.commons_dto import (
    CommunityMember,
    OptimizationInstance,
    TimeParameters,
    TimeValue,
)

# -------- INPUT STRUCTURES -------- #


class QuadraticCostFunction(BaseModel):
    a: float
    """Quadratic coefficient"""
    b: float
    """Linear coefficient"""
    c: float
    """Constant coefficient"""

    def __call__(self, power: float) -> float:
        """Compute quadratic cost based on power."""
        return 0.5 * self.a * power**2 + self.b * power + self.c


class Criterion(Enum):
    pass


class ProductDifferentiationParcel(BaseModel):
    trading_partners: set[str]
    trade_coefficient: list[float]
    trade_characteristic: list[list[float]]

    def __call__(self, power: list[float]) -> float:
        """Compute product differentiation parcel based on power vector."""
        return sum(
            self.trade_coefficient[g] * self.trade_characteristic[g][m] * power[m]
            for g in Criterion
            for m in self.trading_partners
        )


class SharedAvailability(
    BaseModel
):  # Availability is the aggregated value of the load_forecast or production_forecast for all loads linked to the Peer.
    min_availability: list[TimeValue]
    max_availability: list[TimeValue]
    direction: bool


class Peer(CommunityMember):
    # ID contained in CommunityMember
    # selling_price to grid contained in Contract, selling price to others contained in cost function (Quadratic cost + Product Differentiation)

    # Power lower bound is included in the contract information and the aggregated value of physical assets belonging to the peer.
    # Power upper bound is included in the contract information and the aggregated value of physical assets belonging to the peer.
    assets: list[Asset]
    cost_function: QuadraticCostFunction
    product_differentiation_parcel: ProductDifferentiationParcel
    trading_partners: set[str]
    flexibility_rate: float = Field(gt=0, lt=1)
    availability: SharedAvailability


class CentralizedDispatchWithP2PModelInput(OptimizationInstance):
    time_parameters: TimeParameters = TimeParameters(
        timestep_minutes=15, horizon_hours=24, scheduling_time=datetime.datetime.now()
    )
    """Time conditions under which the optimisation is done"""
    peers: list[Peer]
    """Peers of the market """


# -------- OUTPUT STRUCTURES -------- #


class PeerSharingCoefficient(BaseModel):
    id: str  # ID of the peer with whom energy is exchanged
    sharing_coefficient: float  # Between -1 and 1, with negative values representing consumption flow, and positive values representing production flows.
    sharing_price: float  # Price of the dual for the exchange along the considered branch.


class PeerResult(BaseModel):
    id: str
    load_profile: list[TimeValue]
    production_profile: list[TimeValue]
    sharing_distribution: list[PeerSharingCoefficient]


class CentralizedDispatchWithP2PModelOutput(OptimizationInstance):
    peer_results: list[PeerResult]
    electricity_prices: list[
        TimeValue
    ]  # Market clearing price (taken as the dual of the centralised optimisation problem)


# Comment
