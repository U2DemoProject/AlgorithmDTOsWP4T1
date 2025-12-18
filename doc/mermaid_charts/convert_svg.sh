
# npm install -g @mermaid-js/mermaid-cli


#!/bin/bash

# Define your list of base names
names=('commons_energy_management_system_dto' 'commons_dto' 'energy_management_system_community_dto' 'energy_management_system_p2p_dto' 'energy_management_system_collective_benefit_allocation_dto' 'energy_management_system_individual_portfolio_dto' 'market_clearing_dto' 'pricing_mechanism_dto' 'heuristic_benefit_allocation_dto')


# Loop through each name and generate the SVG
for n in "${names[@]}"; do
    mmdc -i "doc/mermaid_charts/${n}.md" -o "doc/mermaid_charts/${n}.svg"
done