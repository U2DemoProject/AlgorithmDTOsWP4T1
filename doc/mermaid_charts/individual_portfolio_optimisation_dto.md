```mermaid
classDiagram

    class Prices {
        prices: list[TimeValue]
    }

    class Objective {
        name: ObjectiveName
        weight: float | None = 1
    }

    class DecisionIndividualOptimisationInput {
        household: Household
        community_contract: CommunityContract
        objectives: list[Objective]
    }

    class OptimizationInstance {
        instance_id: str
    }

    class Schedule {
        schedule: list[TimeValue]
    }

    class AssetSchedule {
        asset_id: str
        direction: Direction
    }

    class Household {
        community_members: list[CommunityMember]
        assets: list[Asset]
    }

    class CommunityContract {
        supply_prices: Prices
        resale_prices: Prices
        max_supply_community: Schedule
        max_offtake_community: Schedule
    }

    class DecisionIndividualOptimisationOutput {
        dispatches: list[AssetSchedule]
        external_interactions: ExternalInteractions
    }

    class ExternalInteractions {
        grid_offtake_volume: Schedule
        grid_injection_volume: Schedule
        community_offtake_volume: Schedule
        community_injection_volume: Schedule
    }


    OptimizationInstance <|-- DecisionIndividualOptimisationInput
    OptimizationInstance <|-- DecisionIndividualOptimisationOutput

```