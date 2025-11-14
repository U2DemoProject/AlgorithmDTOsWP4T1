```mermaid
classDiagram

    class DispatchableProductionAsset {
        production_cost: float
    }

    class VariableAsset {
        forecasted_profile: Forecast | None = None
    }

    class StorageDevice {
        max_cycles: int
        charge_efficiency: float | None = 1.0
        self_discharge_rate: float | None = 0.0
        storage_capacity: float
        soc_min: float = 0.0
        soc_max: float = 1.0
        soc_init: float = 0.0
    }

    class SocValue {
        time: datetime
        value: float
        asset_id: str
    }

    class Meter {
        id: str
        linked_distribution_point: str | None = None
        contracts: list[Contract]
        contract_shares: list[ContractShare] | None = None
        power_kw: list[TimeValue] | None = None
    }

    class StrEnum {
        <<Enumeration>>
    }

    class CommunityMember {
        id: str
        meters: list[Meter]
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
    }

    class BatteryStorage {
        weight_cycling: float
        t_target: datetime
        soc_target: float
    }

    class Asset {
        id: str
        meter: Meter | None = None
        p_min_kw: float | None = None
        p_max_kw: float | None = None
        context: dict = dict
    }

    class FlexAvailability {
        time: datetime
        availability: bool
    }

    class Household {
        community_members: list[CommunityMember]
        assets: list[Asset]
    }

    class HouseEnergyManagementSystem {
        house: Household
        meters: list[Meter]
    }

    class FlexibleLoadAsset {
        total_expected_energy_consumption: float | None = None
        baseline_forecast: Forecast | None = None
        weight_flexible: float | None = None
    }

    class NonFlexibleLoadAsset {
        load: list[TimeValue]
    }

    class VariableProductionAsset {
        max_acceptable_curtailment_rate: int | None = None
    }

    class ElectricVehicleCharger {
        c_max: float
    }

    class TimeValue {
        time: datetime
        value: float
    }

    class EnergyCommunityManager {
        id: str
        contract: Contract
    }

    class AssetSchedule {
        asset_id: str
        direction: Direction
    }

    class PV {
        rated_capacity: float
        weight_curtailment: float
    }

    class ElectricVehicle {
        charger: ElectricVehicleCharger
        weight_comfort: float
    }

    class Contract {
        category: ContractCategory
        id: str
        supplier: Supplier
        max_power_consumed_kw: float | None = None
        max_power_injected_kw: float | None = None
    }

    class DispatchAsset {
        auto_control: bool | None = None
        ramp_rate_kw_per_step: float | None = None
        min_on_duration: float | None = None
        min_off_duration: float | None = None
        availability_flex: list[FlexAvailability] | None = None
    }

    class Direction {
        <<Enumeration>>
        PRODUCTION: str = 'production'
        CONSUMPTION: str = 'consumption'
    }

    class Schedule {
        schedule: list[TimeValue]
    }

    class Forecast {
        forecast_type: ForecastType
        forecast_date: datetime
        forecast_values: list[list[TimeValue]]
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
    FlexibleLoadAsset <|-- HVAC
    FlexibleLoadAsset <|-- ElectricVehicleCharger
    BatteryStorage <|-- ElectricVehicle
    VariableProductionAsset <|-- PV

```