```mermaid
classDiagram

    class Objective {
        name: ObjectiveName
        weight: float | None = 1
    }

    class EnergyManagementSystemCommunityInput {
        time_units: TimeParameters
        households: list[Household]
        members: list[CommunityMember]
        objective: list[Objective]
        community_manager: EnergyCommunityManager
        schedules: list[AssetSchedule]
    }

    class Household {
        community_members: list[CommunityMember]
        assets: list[PV | BatteryStorage | ElectricVehicle | HVAC | NonFlexibleLoadAsset | FlexibleLoadAsset]
        risk_aggressiveness: RiskAggressiveness = 50
    }

    class Schedule {
        schedule: list[TimeValue]
    }

    class EnergyManagementSystemCommunityOutput {
        asset_dispatches: list[AssetSchedule]
        grid_offtake: list[Schedule]
        grid_injection: list[Schedule]
    }

    class TimeParameters {
        timestep_minutes: int
        horizon_hours: int
        scheduling_time: datetime
    }

    class OptimizationInstance {
        instance_id: str
    }

    class EnergyCommunityManager {
        id: str
        contract: Contract
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
    OptimizationInstance <|-- EnergyManagementSystemCommunityOutput
    OptimizationInstance <|-- EnergyManagementSystemCommunityInput

```