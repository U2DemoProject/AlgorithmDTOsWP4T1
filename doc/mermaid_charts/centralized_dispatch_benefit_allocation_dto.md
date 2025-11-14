```mermaid
classDiagram

    class OptimizationInstance {
        instance_id: str
    }

    class CentralizedDispatchCollectiveBenefitAllocationInput {
        asset: list[Asset]
        asset_dispatches: list[AssetSchedule]
        grid_offtake: list[Schedule]
        grid_injection: list[Schedule]
        members: list[CommunityMember]
        member_preferences: list[BehaviouralWeight]
        behavioural_constraint: BehaviouralConstraint
    }

    class AssetSchedule {
        asset_id: str
        direction: Direction
    }

    class StrEnum {
        <<Enumeration>>
    }

    class TimeValue {
        time: datetime
        value: float
    }

    class CommunityMember {
        id: str
        meters: list[Meter]
    }

    class CentralizedDispatchCollectiveBenefitAllocationOutput {
        community_total_benefit: float
        benefit_allocations: list[BenefitAllocation]
    }

    class Asset {
        id: str
        meter: Meter | None = None
        p_min_kw: float | None = None
        p_max_kw: float | None = None
        context: dict = dict
    }

    class BehaviouralConstraint {
        <<Enumeration>>
        HARD_CONSTRAINT: str = 'hard constraint'
        SOFT_CONSTRAINT: str = 'soft constraint'
        NO_CONSTRAINT: str = 'no constraint'
    }

    class BenefitAllocation {
        id: CommunityMember
        sharing_coefficient_result: list[TimeValue]
    }

    class Schedule {
        schedule: list[TimeValue]
    }

    class BehaviouralWeight {
        id: CommunityMember
        sharing_coefficient: float
    }


    StrEnum <|-- BehaviouralConstraint
    OptimizationInstance <|-- CentralizedDispatchCollectiveBenefitAllocationOutput
    OptimizationInstance <|-- CentralizedDispatchCollectiveBenefitAllocationInput

```