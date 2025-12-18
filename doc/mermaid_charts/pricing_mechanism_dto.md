```mermaid
classDiagram

    class TimeValue {
        time: datetime
        value: float
    }

    class RetailPrices {
        injection_price: list[TimeValue]
        offtake_price: list[TimeValue]
    }

    class PricingMechanismOutput {
        internal_prices: list[TimeValue]
        billing: list[BillingReprocessing]
    }

    class StrEnum {
        <<Enumeration>>
    }

    class TimeParameters {
        timestep_minutes: int
        horizon_hours: int
        scheduling_time: datetime
    }

    class PricingMechanismInput {
        time: TimeParameters
        pricing_rule: PricingRule
        loads: list[TimeValue]
        productions: list[TimeValue]
        prices: RetailPrices
    }

    class OptimizationInstance {
        instance_id: str
    }

    class PricingRule {
        <<Enumeration>>
        MID_MARKET: str = 'Mid-market rate'
        SUPPLY_DEMAND: str = 'Supply-demand ratio'
    }

    class BillingReprocessing {
        contract_id: str
        payback_amount: float
        supplier_id: str | None
        notes: str | None
    }


    StrEnum <|-- PricingRule
    OptimizationInstance <|-- PricingMechanismOutput
    OptimizationInstance <|-- PricingMechanismInput

```