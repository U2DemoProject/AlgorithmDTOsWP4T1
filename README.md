# u2demo-clearing-engine

## Generating docs

Steps to follow:
1. Run python -m u2demo_clearing_engine.app. This launches the local server. The API description is found on http://localhost:8000/docs
2. Run the shell commands below (install @redocly/cli if necessary, as commented below). This generates the json and corresponding html files.

```shell commands (run in Git bash terminal)

# npm install -g @redocly/cli
curl http://localhost:8000/openapi.json > doc/openapi/u2demo_optimization_api.json
redocly build-docs doc/openapi/u2demo_optimization_api.json -o doc/openapi/u2demo-optimization-doc.html


```

3. Run python -m doc.mermaid_charts.create_mmd to create the mermaid files

4. Run the shell command below to convert the mermaid file into svgs (install mermaid-cli if necessary).

```shell commands (run in Git bash terminal)
# npm install -g @mermaid-js/mermaid-cli


#!/bin/bash

# Define your list of base names
names=('centralized_dispatch_cems_dto' 'centralized_dispatch_p2p_dto' 'centralized_dispatch_benefit_allocation_dto' 'market_clearing_dto' 'pricing_model_dto' 'individual_portfolio_optimisation_dto')

# Loop through each name and generate the SVG
for n in "${names[@]}"; do
    mmdc -i "doc/mermaid_charts/${n}.md" -o "doc/mermaid_charts/${n}.svg"
done

```
