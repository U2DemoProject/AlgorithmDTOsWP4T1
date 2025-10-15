from u2demo_clearing_engine.dto.algorithm_libraries.commons_dispatch_optimization_dto import (
    AssetSchedule,
    EnergyCommunityManager,
    Household,
)
from u2demo_clearing_engine.dto.algorithm_libraries.commons_dto import (
    CommunityMember,
    Objective,
    OptimizationInstance,
    Schedule,
    TimeParameters,
)

# -------- INPUT STRUCTURES -------- #


class DispatchInput(OptimizationInstance):
    time_units: TimeParameters
    households: list[Household]  # Households store the list of physical assets connected to this household
    members: list[CommunityMember]  # Members store the list of meters and contracts connected to this member
    objective: list[Objective]
    community_manager: EnergyCommunityManager
    schedules: list[
        AssetSchedule
    ]  # List of scheduled profiles for assets which ran an individual optimisation beforehand at household level.


# -------- OUTPUT STRUCTURES -------- #

# In the central energy management system, there is no community price being set, it is already provided as an input variable.
# Outputs therefore only focus on volumes.


class DispatchOutput(OptimizationInstance):
    asset_dispatches: list[AssetSchedule]
    grid_offtake: list[Schedule]
    grid_injection: list[Schedule]
