from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from u2demo_clearing_engine.dto.algorithm_libraries.commons_dispatch_optimization_dto import (
    AssetSchedule,
    Household,
)
from u2demo_clearing_engine.dto.algorithm_libraries.commons_dto import (
    Objective,
    OptimizationInstance,
    Prices,
    Schedule,
)

# -------- INPUT STRUCTURES -------- #


class CommunityContract(BaseModel):
    supply_prices: Prices
    resale_prices: Prices
    max_supply_community: Schedule  # Maximum demand which can be satisfied by the community
    max_offtake_community: Schedule  # Maximum generation which can be offtaken by the community


class DecisionIndividualOptimisationInput(OptimizationInstance):
    household: Household
    community_contract: CommunityContract | None = None
    objectives: list[Objective] | None = None
    start_datetime: datetime | None = None
    end_datetime: datetime | None = None


# -------- OUTPUT STRUCTURES -------- #


class ExternalInteractions(
    BaseModel
):  # Amount of volumes bought and sold from external agents (within community or from the grid)
    grid_offtake_volume: Schedule
    grid_injection_volume: Schedule
    community_offtake_volume: Schedule
    community_injection_volume: Schedule


class DecisionIndividualOptimisationOutput(OptimizationInstance):
    dispatches: list[AssetSchedule]
    external_interactions: ExternalInteractions
