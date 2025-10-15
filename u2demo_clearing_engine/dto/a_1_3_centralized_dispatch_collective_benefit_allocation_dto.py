from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel

from u2demo_clearing_engine.dto.algorithm_libraries.commons_dispatch_optimization_dto import (
    Asset,
    AssetSchedule,
)
from u2demo_clearing_engine.dto.algorithm_libraries.commons_dto import (
    CommunityMember,
    OptimizationInstance,
    Schedule,
    TimeValue,
)

# -------- INPUT STRUCTURES -------- #


# The community should be able to add its own benefit allocation preferences, which should be integrated into the algorithmic result.
class BehaviouralWeight(BaseModel):
    id: CommunityMember
    sharing_coefficient: float


# The BehaviouralConstraint object specifies to which extent the sharing coefficients specified by the community should be followed by the algorithm, even if it yields suboptimal results.
class BehaviouralConstraint(StrEnum):
    HARD_CONSTRAINT = "hard constraint"  # SHaring coefficient must be respected.
    SOFT_CONSTRAINT = "soft constraint"  # Deviation from preference expressed as a cost in the objective function
    NO_CONSTRAINT = "no constraint"  # Sharing coefficients ignored


class CentralizedDispatchCollectiveBenefitAllocationInput(OptimizationInstance):
    asset: list[Asset]
    asset_dispatches: list[AssetSchedule]
    grid_offtake: list[Schedule]
    grid_injection: list[Schedule]
    members: list[CommunityMember]  # Members store the list of meters and contracts connected to this member.
    member_preferences: list[BehaviouralWeight]
    behavioural_constraint: BehaviouralConstraint


# -------- OUTPUT STRUCTURES -------- #


class BenefitAllocation(BaseModel):
    id: CommunityMember
    sharing_coefficient_result: list[
        TimeValue
    ]  # Could also be a Schedule, if talk about redistribution in volumes, rather than % of total benefit. This value could be negative.


class CentralizedDispatchCollectiveBenefitAllocationOutput(OptimizationInstance):
    community_total_benefit: float
    benefit_allocations: list[
        BenefitAllocation
    ]  # The BenefitAllocation result does not necessarily correspond to the member_preferences used in input, if the algorithm finds a more suitable redistribution.
