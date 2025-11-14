
import pydantic_mermaid.pydantic_parser as pp
from pydantic_mermaid import MermaidGenerator, Relations

from u2demo_clearing_engine.dto import (
    a_1_1_centralized_dispatch_cems_dto,
    a_1_2_centralized_dispatch_peer_to_peer_dto,
    a_1_3_centralized_dispatch_collective_benefit_allocation_dto,
    a_1_4_decision_individual_portfolio_optimization_dto,
    a_2_centralized_market_clearing_dto,
    a_3_pricing_model_dto,
    a_4_heuristic_settlement_dto,
)
from u2demo_clearing_engine.dto.algorithm_libraries import commons_dispatch_optimization_dto, commons_dto

if __name__ == "__main__":
    ignored_types = {"datetime", "dict"}

    old_call = pp.PydanticParser.__call__

    def safe_call(self, module):
        graph = old_call(self, module)

        # Different versions of pydantic-mermaid store data differently
        # We check dynamically and adapt.
        if hasattr(graph, "relations") and hasattr(graph, "models"):
            # Legacy version (0.5.x – 0.6.x)
            graph.relations = [rel for rel in graph.relations if getattr(rel, "target", None) not in ignored_types]
            graph.models = [m for m in graph.models if getattr(m, "name", None) not in ignored_types]
        elif hasattr(graph, "elements"):
            # Newer version (0.7.x and above)
            filtered_elements = []
            for el in graph.elements:
                # Skip standalone boxes for ignored types
                if getattr(el, "name", None) in ignored_types:
                    continue
                # Skip arrows pointing to ignored types
                if hasattr(el, "target") and el.target in ignored_types:
                    continue
                filtered_elements.append(el)
            graph.elements = filtered_elements

        return graph

    pp.PydanticParser.__call__ = safe_call

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

    generator = MermaidGenerator(a_1_4_decision_individual_portfolio_optimization_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/individual_portfolio_optimisation_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_2_centralized_market_clearing_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/market_clearing_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_3_pricing_model_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/pricing_model_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_4_heuristic_settlement_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/heuristic_settlement_dto.md", "w") as f:
        f.write(chart)
