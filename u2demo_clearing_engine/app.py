import uvicorn
from fastapi import FastAPI

from u2demo_clearing_engine.dto.a_1_1_energy_management_system_community_dto import (
    EnergyManagementSystemCommunityInput,
    EnergyManagementSystemCommunityOutput,
)
from u2demo_clearing_engine.dto.a_1_2_energy_management_system_peer_to_peer_dto import (
    EnergyManagementSystemP2PInput,
    EnergyManagementSystemP2POutput,
)
from u2demo_clearing_engine.dto.a_1_3_energy_management_system_collective_benefit_allocation_dto import (
    EnergyManagementSystemCollectiveBenefitAllocationInput,
    EnergyManagementSystemCollectiveBenefitAllocationOutput,
)
from u2demo_clearing_engine.dto.a_1_4_energy_management_system_individual_portfolio_dto import (
    EnergyManagementSystemIndividualPortfolioInput,
    EnergyManagementSystemIndividualPortfolioOutput,
)
from u2demo_clearing_engine.dto.a_2_centralized_market_clearing_dto import MarketClearingInput, MarketClearingOutput
from u2demo_clearing_engine.dto.a_3_pricing_mechanism_dto import PricingMechanismInput, PricingMechanismOutput
from u2demo_clearing_engine.dto.a_4_heuristic_benefit_allocation_dto import (
    HeuristicBenefitAllocationInput,
    HeuristicBenefitAllocationOutput,
)

app = FastAPI(title="U2Demo Optimization Engine API")


@app.post("/energy_management_system_community")
def run_dispatch_cems(input_data: EnergyManagementSystemCommunityInput) -> EnergyManagementSystemCommunityOutput:  # noqa: ARG001
    pass


@app.post("/energy_management_system_peer_to_peer")
def run_dispatch_p2p(input_data: EnergyManagementSystemP2PInput) -> EnergyManagementSystemP2POutput:  # noqa: ARG001
    pass


@app.post("/centralized_dispatch_benefit_allocation")
def run_dispatch_benefit_allocation(
    input_data: EnergyManagementSystemCollectiveBenefitAllocationInput,
) -> EnergyManagementSystemCollectiveBenefitAllocationOutput:  # noqa: ARG001
    pass


@app.post("/individual_portfolio_optimisation")
def run_individual_portfolio_optimisation(
    input_data: EnergyManagementSystemIndividualPortfolioInput,
) -> EnergyManagementSystemIndividualPortfolioOutput:  # noqa: ARG001
    pass


@app.post("/market_clearing")
def run_market_clearing(input_data: MarketClearingInput) -> MarketClearingOutput:  # noqa: ARG001
    pass


@app.post("/pricing_mechanism")
def run_pricing_mechanism(input_data: PricingMechanismInput) -> PricingMechanismOutput:  # noqa: ARG001
    pass


@app.post("/heuristic_benefit_allocation")
def run_heuristic_benefit_allocation(input_data: HeuristicBenefitAllocationInput) -> HeuristicBenefitAllocationOutput:  # noqa: ARG001
    pass


if __name__ == "__main__":
    # uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False, workers=1)  # noqa: S104
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False, workers=1)  # noqa: S104
