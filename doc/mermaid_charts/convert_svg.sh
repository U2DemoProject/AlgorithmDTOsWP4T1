
# npm install -g @mermaid-js/mermaid-cli


#!/bin/bash

# Define your list of base names
names=('commons_dispatch_optimization_dto' 'commons_dto' 'centralized_dispatch_cems_dto' 'centralized_dispatch_p2p_dto' 'centralized_dispatch_benefit_allocation_dto' 'market_clearing_dto' 'pricing_model_dto' 'individual_portfolio_optimisation_dto')


# Loop through each name and generate the SVG
for n in "${names[@]}"; do
    mmdc -i "doc/mermaid_charts/${n}.md" -o "doc/mermaid_charts/${n}.svg"
done