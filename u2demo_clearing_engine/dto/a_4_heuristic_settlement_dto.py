from datetime import datetime

from pydantic import BaseModel

from u2demo_clearing_engine.dto.algorithm_libraries.commons_dto import (
    CommunityMember,
    ContractShare,
    OptimizationInstance,
    Schedule,
)

# Input of algorithm


class CommunityMemberGridSchedule(BaseModel):
    community_member: CommunityMember  # Each community member has a list of Meters associated to it, which can be linked back to specific contracts.
    grid_offtake: list[Schedule]  # The offtake schedule is provided for each community member
    grid_injection: list[Schedule]  # The injection schedule is provided for each community member


class HeuristicSettlementInput(OptimizationInstance):
    sharing_keys: list[ContractShare]
    community_member_schedules: list[CommunityMemberGridSchedule]
    total_benefit: float


# Output of algorithm


class CommunityMemberBenefit(BaseModel):
    community_member: CommunityMember
    interval_start: datetime  # Start time of time interval over which benefits are redistributed
    interval_end: datetime  # End time of time interval over which benefits are redistributed
    benefits_redistribution: float  # Financial value of the benefits redistributed to the community member.


#  The same algo is ran twice (with forecast and realized values)
class HeuristicSettlementOutput(OptimizationInstance):
    member_benefits: list[CommunityMemberBenefit]
