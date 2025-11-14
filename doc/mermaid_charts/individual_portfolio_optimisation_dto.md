```mermaid
classDiagram

    class Prices {
        prices: list[TimeValue]
    }

    class OptimizationInstance {
        instance_id: str
    }

    class ExternalInteractions {
        grid_offtake_volume: Schedule
        grid_injection_volume: Schedule
        community_offtake_volume: Schedule
        community_injection_volume: Schedule
    }

    class DecisionIndividualOptimisationOutput {
        dispatches: list[AssetSchedule]
        external_interactions: ExternalInteractions
    }

    class CommunityContract {
        supply_prices: Prices
        resale_prices: Prices
        max_supply_community: Schedule
        max_offtake_community: Schedule
    }

    class AssetSchedule {
        asset_id: str
        direction: Direction
    }

    class Objective {
        name: ObjectiveName
        weight: float | None = 1
    }

    class Household {
        community_members: list[CommunityMember]
        assets: list[Asset]
    }

    class DecisionIndividualOptimisationInput {
        household: Household
        community_contract: CommunityContract | None = None
        objectives: list[Objective] | None = None
        start_datetime: datetime | None = None
        end_datetime: datetime | None = None
    }

    class Schedule {
        schedule: list[TimeValue]
    }


    OptimizationInstance <|-- DecisionIndividualOptimisationInput
    OptimizationInstance <|-- DecisionIndividualOptimisationOutput

```