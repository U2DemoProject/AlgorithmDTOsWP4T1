```mermaid
classDiagram

    class BehaviouralConstraint {
        <<Enumeration>>
        HARD_CONSTRAINT: str = 'hard constraint'
        SOFT_CONSTRAINT: str = 'soft constraint'
        NO_CONSTRAINT: str = 'no constraint'
    }

    class BehaviouralWeight {
        id: CommunityMember
        sharing_coefficient: float
    }

    class TimeValue {
        time: datetime
        value: float
    }

    class EnergyManagementSystemCollectiveBenefitAllocationInput {
        asset: list[Asset]
        asset_dispatches: list[AssetSchedule]
        grid_offtake: list[Schedule]
        grid_injection: list[Schedule]
        members: list[CommunityMember]
        member_preferences: list[BehaviouralWeight]
        behavioural_constraint: BehaviouralConstraint
    }

    class Schedule {
        schedule: list[TimeValue]
    }

    class BenefitAllocation {
        id: CommunityMember
        sharing_coefficient_result: list[TimeValue]
    }

    class StrEnum {
        <<Enumeration>>
    }

    class Asset {
        id: str
        meter: Meter | None = None
        p_min_kw: float | None = None
        p_max_kw: float | None = None
        context: dict = dict
    }

    class OptimizationInstance {
        instance_id: str
    }

    class EnergyManagementSystemCollectiveBenefitAllocationOutput {
        community_total_benefit: float
        benefit_allocations: list[BenefitAllocation]
    }

    class CommunityMember {
        id: str
        meters: list[Meter]
    }

    class AssetSchedule {
        asset_id: str
        direction: Direction
    }


    Schedule <|-- AssetSchedule
    StrEnum <|-- BehaviouralConstraint
    OptimizationInstance <|-- EnergyManagementSystemCollectiveBenefitAllocationInput
    OptimizationInstance <|-- EnergyManagementSystemCollectiveBenefitAllocationOutput

```