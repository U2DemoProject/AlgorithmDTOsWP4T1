import uvicorn
from fastapi import FastAPI

from u2demo_clearing_engine.dto.a_1_1_centralized_dispatch_cems_dto import DispatchInput, DispatchOutput
from u2demo_clearing_engine.dto.a_1_2_centralized_dispatch_peer_to_peer_dto import (
    CentralizedDispatchWithP2PModelInput,
    CentralizedDispatchWithP2PModelOutput,
)
from u2demo_clearing_engine.dto.a_1_3_centralized_dispatch_collective_benefit_allocation_dto import (
    CentralizedDispatchCollectiveBenefitAllocationInput,
    CentralizedDispatchCollectiveBenefitAllocationOutput,
)
from u2demo_clearing_engine.dto.a_1_4_decision_individual_portfolio_optimization_dto import (
    DecisionIndividualOptimisationInput,
    DecisionIndividualOptimisationOutput,
)
from u2demo_clearing_engine.dto.a_2_centralized_market_clearing_dto import MarketClearingInput, MarketClearingOutput
from u2demo_clearing_engine.dto.a_3_pricing_model_dto import PricingModelInput, PricingModelOutput
from u2demo_clearing_engine.dto.a_4_heuristic_settlement_dto import HeuristicSettlementInput, HeuristicSettlementOutput

app = FastAPI(title="U2Demo Optimization Engine API")


@app.post("/centralized_dispatch_cems")
def run_dispatch_cems(input_data: DispatchInput) -> DispatchOutput:  # noqa: ARG001
    pass


@app.post("/centralized_dispatch_peer_to_peer")
def run_dispatch_p2p(input_data: CentralizedDispatchWithP2PModelInput) -> CentralizedDispatchWithP2PModelOutput:  # noqa: ARG001
    pass


@app.post("/centralized_dispatch_benefit_allocation")
def run_dispatch_benefit_allocation(
    input_data: CentralizedDispatchCollectiveBenefitAllocationInput,
) -> CentralizedDispatchCollectiveBenefitAllocationOutput:  # noqa: ARG001
    pass


@app.post("/individual_portfolio_optimisation")
def run_individual_portfolio_optimisation(
    input_data: DecisionIndividualOptimisationInput,
) -> DecisionIndividualOptimisationOutput:  # noqa: ARG001
    pass


@app.post("/market_clearing")
def run_market_clearing(input_data: MarketClearingInput) -> MarketClearingOutput:  # noqa: ARG001
    pass


@app.post("/pricing_model")
def run_pricing_model(input_data: PricingModelInput) -> PricingModelOutput:  # noqa: ARG001
    pass


@app.post("/heuristic_settlement_model")
def run_heuristic_settlement_model(input_data: HeuristicSettlementInput) -> HeuristicSettlementOutput:  # noqa: ARG001
    pass


if __name__ == "__main__":
    # uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False, workers=1)  # noqa: S104
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False, workers=1)  # noqa: S104
