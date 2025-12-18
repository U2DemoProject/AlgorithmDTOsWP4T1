import pydantic_mermaid.pydantic_parser as pp
from pydantic_mermaid import MermaidGenerator, Relations

from u2demo_clearing_engine.dto import (
    a_1_1_energy_management_system_community_dto,
    a_1_2_energy_management_system_peer_to_peer_dto,
    a_1_3_energy_management_system_collective_benefit_allocation_dto,
    a_1_4_energy_management_system_individual_portfolio_dto,
    a_2_centralized_market_clearing_dto,
    a_3_pricing_mechanism_dto,
    a_4_heuristic_benefit_allocation_dto,
)
from u2demo_clearing_engine.dto.algorithm_libraries import commons_dto, commons_energy_management_system_dto

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

    generator = MermaidGenerator(commons_energy_management_system_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)

    with open("doc/mermaid_charts/commons_energy_management_system_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(commons_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/commons_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_1_1_energy_management_system_community_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/energy_management_system_community_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_1_2_energy_management_system_peer_to_peer_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/energy_management_system_p2p_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_1_3_energy_management_system_collective_benefit_allocation_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/energy_management_system_collective_benefit_allocation_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_1_4_energy_management_system_individual_portfolio_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/energy_management_system_individual_portfolio_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_2_centralized_market_clearing_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/market_clearing_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_3_pricing_mechanism_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/pricing_mechanism_dto.md", "w") as f:
        f.write(chart)

    generator = MermaidGenerator(a_4_heuristic_benefit_allocation_dto)
    chart = generator.generate_chart(relations=Relations.Inheritance)
    with open("doc/mermaid_charts/heuristic_benefit_allocation_dto.md", "w") as f:
        f.write(chart)
