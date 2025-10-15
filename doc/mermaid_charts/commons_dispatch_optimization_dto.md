```mermaid
classDiagram

    class Forecast {
        forecast_type: ForecastType
        forecast_date: datetime
        forecast_values: list[list[TimeValue]]
    }

    class StorageDevice {
        max_cycles: int
        charge_efficiency: float | None = 1.0
        self_discharge_rate: float | None = 0.0
        storage_capacity: float
        soc_min: float | None = 0.0
        soc_max: float | None = 1.0
        soc: float | None = 0.0
    }

    class FlexibleLoadAsset {
        total_expected_energy_consumption: float
        baseline_forecast: Forecast
    }

    class VariableAsset {
        forecasted_profile: Forecast
    }

    class EnergyCommunityManager {
        id: str
        contract: Contract
    }

    class Direction {
        <<Enumeration>>
        PRODUCTION: str = 'production'
        CONSUMPTION: str = 'consumption'
    }

    class Schedule {
        schedule: list[TimeValue]
    }

    class CommunityMember {
        id: str
        meters: list[Meter]
    }

    class TimeValue {
        time: datetime
        value: float
    }

    class Household {
        community_members: list[CommunityMember]
        assets: list[Asset]
    }

    class VariableProductionAsset {
        max_acceptable_curtailment_rate: int | None = None
    }

    class HVAC {
        setpoint_temp: float
        max_temp: float
        min_temp: float
        indoor_temp: float
        thermal_inertia: float
        efficiency_factor: float
        weight_comfort: float
        outdoor_temp: list[TimeValue] = list
        annualized_investment_cost: float
    }

    class HouseEnergyManagementSystem {
        house: Household
        meters: list[Meter]
    }

    class ElectricVehicle {
        weight_comfort: float
        target_soc: float
        time_target_soc: datetime
    }

    class Meter {
        id: str
        contract_id: str
        power_kw: list[TimeValue]
        contract: Contract
    }

    class DispatchableProductionAsset {
        production_cost: float
    }

    class NonFlexibleLoadAsset {
    }

    class Contract {
        id: str
        supplier: Supplier
        linked_distribution_point: str | None = None
    }

    class FlexAvailability {
        time: datetime
        availability: bool
    }

    class DispatchAsset {
        auto_control: bool
        ramp_rate_w_per_step: float | None = None
        min_on_duration: float | None = None
        min_off_duration: float | None = None
        availability_flex: list[FlexAvailability]
    }

    class AssetSchedule {
        asset_id: str
        direction: Direction
    }

    class Asset {
        id: str
        meter: Meter
        p_min_w: float
        p_max_w: float
        context: dict = dict
    }

    class PV {
        rated_capacity: float
        weight_curtailment: float
        irradiance: list[TimeValue] = list
        annualized_investment_cost: float
    }

    class StrEnum {
        <<Enumeration>>
    }

    class BatteryStorage {
        weight_cycling: float
        annualized_investment_cost: float
    }


    Asset <|-- VariableAsset
    Asset <|-- DispatchAsset
    DispatchAsset <|-- DispatchableProductionAsset
    DispatchAsset <|-- StorageDevice
    DispatchAsset <|-- FlexibleLoadAsset
    VariableAsset <|-- VariableProductionAsset
    VariableAsset <|-- NonFlexibleLoadAsset
    StrEnum <|-- Direction
    Schedule <|-- AssetSchedule
    StorageDevice <|-- BatteryStorage
    BatteryStorage <|-- ElectricVehicle
    FlexibleLoadAsset <|-- HVAC
    VariableProductionAsset <|-- PV

```