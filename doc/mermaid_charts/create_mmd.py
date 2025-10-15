from pydantic_mermaid import MermaidGenerator, Relations

from u2demo_clearing_engine.dto import (
    a_1_1_centralized_dispatch_cems_dto,
    a_1_2_centralized_dispatch_peer_to_peer_dto,
    a_1_3_centralized_dispatch_collective_benefit_allocation_dto,
    a_2_centralized_market_clearing_dto,
    a_3_pricing_model_dto,
    a_4_1_decision_individual_portfolio_optimization_dto,
)

from u2demo_clearing_engine.dto.algorithm_libraries import (
    commons_dispatch_optimization_dto,
    commons_dto
)

if __name__ == "__main__":
    generator = MermaidGenerator(commons_dispatch_optimization_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/commons_dispatch_optimization_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(commons_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/commons_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_1_1_centralized_dispatch_cems_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/centralized_dispatch_cems_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_1_2_centralized_dispatch_peer_to_peer_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/centralized_dispatch_p2p_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_1_3_centralized_dispatch_collective_benefit_allocation_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/centralized_dispatch_benefit_allocation_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_2_centralized_market_clearing_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/market_clearing_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_3_pricing_model_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/pricing_model_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_4_1_decision_individual_portfolio_optimization_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/individual_portfolio_optimisation_dto.md", "w") as f:
        f.write(chart)
