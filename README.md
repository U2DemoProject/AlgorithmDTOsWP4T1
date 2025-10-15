# u2demo-clearing-engine

## Purpose
This repository contains the Data Transfer Objects (DTO) used to standardise the model developments in U2Demo. These DTOs are organised by algorithm, as outlined in Deliverable D4.1, with one file per algorithm, found in u2demo_clearing_engine/dto. These algorithms also share some commonalities, which are stored in the commons files under u2demo_clearing_engine/dto/algorithm_libraries. 
In each DTO, the attributes are specified using pydantic syntax, with eventually some attribute constraints included in the attribute definition. For example, for a positive attribute, the constraint attribute >= 0 is included in the attribute definition.
Object Oriented Programming principles are followed as much as possible, with inheritence between classes whenever relevant, in order to structure the DTO definitions. 


## Structure
1. The source code containing the DTOs for each algorithm and the common algorithms is contained in u2demo_clearing_engine/dto.
2. The json files containing all class descriptions following the OpenAPI Specification are contained in u2demo_clearing_engine/openapi (see instruction in "Generating docs" to generate these documents yourself).
3. The corresponding html files are contained in the same openapi folder. 
4. The mermaid files and the corresponding svg files outline the inheritance between classes and provide a visual representation of the attributes contained in each class (see instruction in "Generating docs" to generate these documents yourself).


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
