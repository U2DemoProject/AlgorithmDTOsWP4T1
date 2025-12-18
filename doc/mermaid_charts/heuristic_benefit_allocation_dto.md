```mermaid
classDiagram

    class HeuristicBenefitAllocationInput {
        sharing_keys: list[ContractShare]
        community_member_schedules: list[CommunityMemberGridSchedule]
        total_benefit: float
    }

    class CommunityMemberBenefit {
        community_member: CommunityMember
        interval_start: datetime
        interval_end: datetime
        benefits_redistribution: float
    }

    class Schedule {
        schedule: list[TimeValue]
    }

    class OptimizationInstance {
        instance_id: str
    }

    class CommunityMember {
        id: str
        meters: list[Meter]
    }

    class ContractShare {
        contract_id: str
        share: float
    }

    class HeuristicBenefitAllocationOutput {
        member_benefits: list[CommunityMemberBenefit]
    }

    class CommunityMemberGridSchedule {
        community_member: CommunityMember
        grid_offtake: list[Schedule]
        grid_injection: list[Schedule]
    }


    OptimizationInstance <|-- HeuristicBenefitAllocationInput
    OptimizationInstance <|-- HeuristicBenefitAllocationOutput

```