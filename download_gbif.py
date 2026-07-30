import os
import time
import requests
import json

base_dir = "./datasets"
os.makedirs(f"{base_dir}/gbif/data", exist_ok=True)
output_path = f"{base_dir}/gbif/data/lion_occurrences.json"

# Using the correct API endpoint instead of the HTML homepage to get valid JSON data
gbif_url = "https://api.gbif.org/v1/occurrence/search?taxonKey=5219404&limit=10"

# Loop trying the server 3 times with a delay if it fails
for attempt in range(3):
    try:
        print(f"Connecting to GBIF (Attempt {attempt + 1}/3)...")
        # Added a 15-second timeout so the script doesn't hang forever
        response = requests.get(gbif_url, timeout=15)
        
        if response.status_code == 200:
            with open(output_path, "w", encoding="utf-8") as f:
                # Save as proper JSON
                json.dump(response.json(), f, indent=4)
            print("Success! GBIF JSON maps saved securely.")
            break
            
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print(f"Server dropped connection. Retrying in 5 seconds... Error: {e}")
        time.sleep(5)
else:
    print("Failed to reach GBIF after 3 tries. Please check your internet connection.")
