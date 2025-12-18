```mermaid
classDiagram

    class OptimizationInstance {
        instance_id: str
    }

    class ContractShare {
        contract_id: str
        share: float
    }

    class Meter {
        id: str
        linked_distribution_point: str | None = None
        contracts: list[Contract]
        contract_shares: list[ContractShare] | None = None
        power_kw: list[TimeValue] | None = None
    }

    class ContractCategory {
        <<Enumeration>>
        FIXED: str = 'fixed'
        PEAK_OFF_PEAK: str = 'peak_off_peak'
        ENERGY_MARKET: str = 'energy_market'
    }

    class Supplier {
        supply_prices: Prices
        resale_prices: Prices
        capacity_tariffs: Prices | None = None
    }

    class ForecastType {
        <<Enumeration>>
        DETERMINISTIC: str = 'deterministic'
        STOCHASTIC: str = 'stochastic'
    }

    class StrEnum {
        <<Enumeration>>
    }

    class Prices {
        prices: list[TimeValue]
    }

    class CommunityMember {
        id: str
        meters: list[Meter]
    }

    class Schedule {
        schedule: list[TimeValue]
    }

    class ObjectiveName {
        <<Enumeration>>
        SOCIAL_WELFARE: str = 'social_welfare_maximisation'
        CLEARED_VOLUME: str = 'cleared_volume_maximisation'
        COST_MINIMISATION: str = 'cost_minimisation'
        MAX_VOLUME_SQUARED_DEVIATION: str = 'max_volume_squared_deviation'
        GRID_SUPPLY: str = 'grid_supply_minimisation'
        RENEWABLE_SUPPLY: str = 'renewable_supply_maximisation'
    }

    class Forecast {
        forecast_type: ForecastType
        forecast_date: datetime
        forecast_values: list[list[TimeValue]]
    }

    class TimeParameters {
        timestep_minutes: int
        horizon_hours: int
        scheduling_time: datetime
    }

    class Contract {
        category: ContractCategory
        id: str
        supplier: Supplier
        max_power_consumed_kw: float | None = None
        max_power_injected_kw: float | None = None
    }

    class TimeValue {
        time: datetime
        value: float
    }

    class Objective {
        name: ObjectiveName
        weight: float | None = 1
    }


    StrEnum <|-- ContractCategory
    StrEnum <|-- ObjectiveName
    StrEnum <|-- ForecastType

```