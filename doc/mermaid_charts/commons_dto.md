```mermaid
classDiagram

    class Forecast {
        forecast_type: ForecastType
        forecast_date: datetime
        forecast_values: list[list[TimeValue]]
    }

    class Prices {
        prices: list[TimeValue]
    }

    class ForecastType {
        <<Enumeration>>
        DETERMINISTIC: str = 'deterministic'
        STOCHASTIC: str = 'stochastic'
    }

    class Contract {
        id: str
        supplier: Supplier
        linked_distribution_point: str | None = None
    }

    class Objective {
        name: ObjectiveName
        weight: float | None = 1
    }

    class Supplier {
        category: ContractCategory
        supply_prices: Prices
        resale_prices: Prices
        capacity_tariffs: Prices
        max_power_consumed_kw: float | None = None
        max_power_injected_kw: float | None = None
    }

    class OptimizationInstance {
        instance_id: str
    }

    class Schedule {
        schedule: list[TimeValue]
    }

    class TimeValue {
        time: datetime
        value: float
    }

    class CommunityMember {
        id: str
        meters: list[Meter]
    }

    class ObjectiveName {
        <<Enumeration>>
        SOCIAL_WELFARE: str = 'social_welfare_maximisation'
        CLEARED_VOLUME: str = 'cleared_volume_maximisation'
        COST_MINIMISATION: str = 'cost_minimisation'
        GRID_SUPPLY: str = 'grid_supply_minimisation'
        RENEWABLE_SUPPLY: str = 'renewable_supply_maximisation'
    }

    class TimeParameters {
        timestep_minutes: int
        horizon_hours: int
        scheduling_time: datetime
    }

    class StrEnum {
        <<Enumeration>>
    }

    class ContractCategory {
        <<Enumeration>>
        FIXED: str = 'fixed'
        PEAK_OFF_PEAK: str = 'peak_off_peak'
    }

    class Meter {
        id: str
        contract_id: str
        power_kw: list[TimeValue]
        contract: Contract
    }


    StrEnum <|-- ObjectiveName
    StrEnum <|-- ForecastType
    StrEnum <|-- ContractCategory

```