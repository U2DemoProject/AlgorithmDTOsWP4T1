```mermaid
classDiagram

    class OptimizationInstance {
        instance_id: str
    }

    class CommunityMember {
        id: str
        meters: list[Meter]
    }

    class ProductDifferentiationParcel {
        trading_partners: set[str]
        trade_coefficient: list[float]
        trade_characteristic: list[list[float]]
    }

    class PeerSharingCoefficient {
        id: str
        sharing_coefficient: float
        sharing_price: float
    }

    class EnergyManagementSystemP2POutput {
        peer_results: list[PeerResult]
        electricity_prices: list[TimeValue]
    }

    class EnergyManagementSystemP2PInput {
        time_parameters: TimeParameters = timestep_minutes=15 horizon_hours=24 scheduling_time=datetime.datetime(2025, 12, 4, 16, 42, 46, 643878)
        peers: list[Peer]
    }

    class Peer {
        assets: list[Asset]
        cost_function: QuadraticCostFunction
        product_differentiation_parcel: ProductDifferentiationParcel
        trading_partners: set[str]
        flexibility_rate: float
        availability: SharedAvailability
    }

    class TimeParameters {
        timestep_minutes: int
        horizon_hours: int
        scheduling_time: datetime
    }

    class PeerResult {
        id: str
        load_profile: list[TimeValue]
        production_profile: list[TimeValue]
        sharing_distribution: list[PeerSharingCoefficient]
    }

    class Criterion {
        <<Enumeration>>
    }

    class SharedAvailability {
        min_availability: list[TimeValue]
        max_availability: list[TimeValue]
        direction: bool
    }

    class TimeValue {
        time: datetime
        value: float
    }

    class Asset {
        id: str
        meter: Meter | None = None
        p_min_kw: float | None = None
        p_max_kw: float | None = None
        context: dict = dict
    }

    class QuadraticCostFunction {
        a: float
        b: float
        c: float
    }


    CommunityMember <|-- Peer
    OptimizationInstance <|-- EnergyManagementSystemP2PInput
    OptimizationInstance <|-- EnergyManagementSystemP2POutput

```