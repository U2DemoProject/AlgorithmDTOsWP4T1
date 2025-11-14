```mermaid
classDiagram

    class OptimizationInstance {
        instance_id: str
    }

    class TimeParameters {
        timestep_minutes: int
        horizon_hours: int
        scheduling_time: datetime
    }

    class AssetSchedule {
        asset_id: str
        direction: Direction
    }

    class EnergyCommunityManager {
        id: str
        contract: Contract
    }

    class DispatchOutput {
        asset_dispatches: list[AssetSchedule]
        grid_offtake: list[Schedule]
        grid_injection: list[Schedule]
    }

    class CommunityMember {
        id: str
        meters: list[Meter]
    }

    class Objective {
        name: ObjectiveName
        weight: float | None = 1
    }

    class Household {
        community_members: list[CommunityMember]
        assets: list[Asset]
    }

    class DispatchInput {
        time_units: TimeParameters
        households: list[Household]
        members: list[CommunityMember]
        objective: list[Objective]
        community_manager: EnergyCommunityManager
        schedules: list[AssetSchedule]
    }

    class Schedule {
        schedule: list[TimeValue]
    }


    OptimizationInstance <|-- DispatchInput
    OptimizationInstance <|-- DispatchOutput

```