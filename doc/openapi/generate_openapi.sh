

#You need to run the u2demo server on localhost:8000

#Then run bash path_to_file/generate_openapi.sh in Git bash

# npm install -g @redocly/cli
curl http://localhost:8000/openapi.json > doc/openapi/u2demo_optimization_api.json
redocly build-docs doc/openapi/u2demo_optimization_api.json -o doc/openapi/u2demo-optimization-doc.html