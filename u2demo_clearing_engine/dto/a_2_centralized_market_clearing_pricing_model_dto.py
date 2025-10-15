from __future__ import annotations

from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from u2demo_clearing_engine.dto.algorithm_libraries.commons_dto import OptimizationInstance


class PricingModelInput(OptimizationInstance):
    pass


class PricingModelOutput(OptimizationInstance):
    pass


class ClearingPriceModel(BaseModel, ABC):
    @abstractmethod
    def __call__(self) -> list[float]:
        pass


class PayAsBidPriceModel(ClearingPriceModel):
    def __call__(self):
        pass


class AverageMarginalPriceModel(ClearingPriceModel):
    offer_weight: float = Field(
        default=0.5,
        ge=0,
        le=1,
        description="Offer weighting factor. If equals to 1, clearing price is the marginal offer price. If equals to 0, clearing price is the marginal demand price.",
    )

    def _check_marginal_price_length(
        self, marginal_offer_price: list[float], marginal_demand_price: list[float]
    ) -> None:
        if len(marginal_offer_price) != len(marginal_demand_price):
            raise ValueError(
                f"Marginal offer price and marginal demand price arrays should have same length {len(marginal_offer_price)} vs {len(marginal_demand_price)}"
            )

    def __call__(self, marginal_offer_price: list[float], marginal_demand_price: list[float]) -> list[float]:
        """Compute average weighted clearing price for marginal offer and marginal demand price."""
        self._check_marginal_price_length(marginal_offer_price, marginal_demand_price)
        clearing_price: list[float] = [None] * len(marginal_offer_price)
        for t in range(len(clearing_price)):
            if marginal_offer_price[t] is not None and marginal_demand_price[t] is not None:
                clearing_price[t] = (
                    self.offer_weight * marginal_offer_price[t] + (1 - self.offer_weight) * marginal_demand_price[t]
                )
            else:
                clearing_price[t] = marginal_offer_price[t] or marginal_demand_price[t]
        return clearing_price
