```mermaid
classDiagram

    class PricingModelOutput {
        internal_prices: list[TimeValue]
        billing: list[BillingReprocessing]
    }

    class RetailPrice {
        injection_price: TimeValue
        offtake_price: TimeValue
    }

    class OptimizationInstance {
        instance_id: str
    }

    class TimeValue {
        time: datetime
        value: float
    }

    class BillingReprocessing {
        contract_id: str
        payback_amount: float
        supplier_id: str | None
        notes: str | None
    }

    class PricingModelInput {
        time: TimeParameters
        pricing_rule: PricingRule
        loads: list[TimeValue]
        productions: list[TimeValue]
        prices: list[RetailPrice]
    }

    class TimeParameters {
        timestep_minutes: int
        horizon_hours: int
        scheduling_time: datetime
    }

    class StrEnum {
        <<Enumeration>>
    }

    class PricingRule {
        <<Enumeration>>
        MID_MARKET: str = 'Mid-market rate'
        SUPPLY_DEMAND: str = 'Supply-demand ratio'
    }


    StrEnum <|-- PricingRule
    OptimizationInstance <|-- PricingModelInput
    OptimizationInstance <|-- PricingModelOutput

```