import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from ml_population import population_engine

print("Testing Live GBIF REST API Integration...")
result = population_engine.get_gbif_species_distribution("Panthera leo")
import json
print(json.dumps(result, indent=2))
