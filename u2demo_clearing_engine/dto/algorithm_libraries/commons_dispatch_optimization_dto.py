from datetime import datetime
from enum import StrEnum

import loguru as log
from pydantic import BaseModel, Field, model_validator

from u2demo_clearing_engine.dto.algorithm_libraries.commons_dto import (
    CommunityMember,
    Contract,
    Forecast,
    Meter,
    Schedule,
    TimeValue,
)


class Asset(BaseModel):
    id: str
    meter: Meter | None = None
    p_min_kw: float | None = None
    p_max_kw: float | None = None

    context: dict = Field(
        default_factory=dict
    )  # Defines the time-dependent variables assigned to the asset (e.g. power schedule)

    # Each asset can contribute to the objective function, but does not have to. Overwrite the objective_asset based on asset specificities.
    def objective_asset(self):
        """Default: no contribution to the objective"""
        return 0


class VariableAsset(Asset):
    forecasted_profile: Forecast | None = None


# FlexAvailability specifies whether an asset is available to provide flexibility or not at each timestep.
class FlexAvailability(BaseModel):
    time: datetime
    availability: bool


class DispatchAsset(Asset):
    auto_control: bool | None = None
    ramp_rate_kw_per_step: float | None = None
    min_on_duration: float | None = None
    min_off_duration: float | None = None
    availability_flex: list[FlexAvailability] | None = None


class FlexibleLoadAsset(DispatchAsset):
    total_expected_energy_consumption: float | None = None
    baseline_forecast: Forecast | None = (
        None  # Expected operational schedule if no community redispatch is done. For settlement algorithms,  # the forecast is deterministic and corresponds to the physically dispatched schedule.
    )
    weight_flexible: float | None = None


class NonFlexibleLoadAsset(VariableAsset):
    load: list[TimeValue]


class StorageDevice(DispatchAsset):
    max_cycles: int
    charge_efficiency: float | None = 1.0  # Same value used for discharge efficiency.
    self_discharge_rate: float | None = 0.0
    storage_capacity: float = Field(..., ge=0, description="Maximum energy storage capacity in kW")
    soc_min: float = 0.0
    soc_max: float = 1.0
    soc_init: float = (
        0.0  # Value chosen at object instantiation corresponds to initial state of charge on object creation.
    )

    # Check that soc_init is between soc_min and soc_max on model creation.
    @model_validator(mode="after")
    def check_bounds(self):
        if not (self.soc_min <= self.soc_init <= self.soc_max):
            raise ValueError(
                f" ({self.soc_init}) must be higher or equal than ({self.soc_min}) and lower or equal than ({self.soc_max})"
            )
        return self


class VariableProductionAsset(VariableAsset):
    max_acceptable_curtailment_rate: int | None = (
        None  # Maximum share of PV production which the producer is willing to curtail.
    )


class DispatchableProductionAsset(DispatchAsset):
    production_cost: float


class Household(BaseModel):
    community_members: list[CommunityMember]  # Assume that a household can be shared across multiple community members
    assets: list[Asset]


class HouseEnergyManagementSystem(BaseModel):
    house: Household
    meters: list[Meter]


class EnergyCommunityManager(BaseModel):
    id: str
    contract: Contract  # This sets the offtake and injection prices at the community level, in case of shared assets.


class Direction(StrEnum):
    PRODUCTION = "production"
    CONSUMPTION = "consumption"


class AssetSchedule(Schedule):
    asset_id: str
    direction: Direction  # An asset which can both produce and consume (e.g. battery) will have two asset schedules associated with it, one for production, one for consumption.


class SocValue(BaseModel):
    time: datetime
    value: float
    asset_id: str


class BatteryStorage(StorageDevice):
    weight_cycling: float
    t_target: datetime  # Time by which the minimum target SoC must be achieved
    soc_target: float  # Minimum target SoC

    def update_from_context(self):
        # Timestep probably can be extracted from somewhere else, doesn't have to be in asset.
        try:
            self.dt = self.context["dt"]
        except KeyError:
            log.error("Missing timestep resolution in battery storage asset.")

    # Equation expressing impact of operations on battery
    def soc_update(
        self,
        power: float,
        soc: float,
        dt: float,
    ) -> float:  # No typing set, to allow different power object types to be used with this class.
        soc = (1 - self.self_discharge_efficiency) * soc - power * dt * self.charge_efficiency / self.storage_capacity
        return soc


class ElectricVehicleCharger(FlexibleLoadAsset):
    id: str
    c_max: float  # Maximum charging capacity of the EV charger


class ElectricVehicle(BatteryStorage):
    charger: ElectricVehicleCharger
    weight_comfort: float


class HVAC(FlexibleLoadAsset):
    setpoint_temp: float
    max_temp: float
    min_temp: float
    indoor_temp: float  # Indoor temperature initialised as a float, but expressed as a function of decision variables for the next timesteps.
    thermal_inertia: float  # Thermal inertia (theta) of the building
    efficiency_factor: float  # HVAC efficiency factor
    weight_comfort: float
    outdoor_temp: list[TimeValue] = Field(default_factory=list)

    def update_from_context(self):
        """Refresh derived attributes from the current context"""
        try:
            self.outdoor_temp = self.context["outdoor_temp"]
        except KeyError:
            log.error("Missing outdoor temp for HVAC asset.")

    def power_to_temp_cooling(self, power: float, outdoor_temp: float) -> float:
        self.indoor_temp = self.thermal_inertia * self.indoor_temp + (1 - self.thermal_inertia) * (
            outdoor_temp - self.efficiency_factor * power
        )
        return self.indoor_temp

    def power_to_temp_heating(self, power: float, outdoor_temp: float) -> float:
        self.indoor_temp = self.thermal_inertia * self.indoor_temp + (1 - self.thermal_inertia) * (
            outdoor_temp + self.efficiency_factor * power
        )
        return self.indoor_temp


class PV(VariableProductionAsset):
    rated_capacity: float  # Installed PV capacity (in kW)
    weight_curtailment: float  # Cost of solar curtailment
