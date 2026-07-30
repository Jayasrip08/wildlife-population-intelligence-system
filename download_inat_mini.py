import os
import requests
import urllib.request
import time

def download_inaturalist_mini():
    print("="*60)
    print("  Downloading Custom iNaturalist Mini Dataset (via Open API)")
    print("="*60 + "\n")

    base_dir = "./datasets/inaturalist"
    
    # Taxon IDs for 5 distinct wildlife species
    species_list = {
        "47347": "Red_Fox",
        "47761": "American_Black_Bear",
        "48662": "Monarch_Butterfly",
        "1856": "Bald_Eagle",
        "47398": "Raccoon"
    }

    # iNaturalist Open API URL (No Authentication Required!)
    api_url = "https://api.inaturalist.org/v1/observations"

    for taxon_id, name in species_list.items():
        species_dir = os.path.join(base_dir, name)
        os.makedirs(species_dir, exist_ok=True)
        print(f">>> Fetching data for {name.replace('_', ' ')}...")

        # Request 10 observations with photos for this species
        params = {
            "taxon_id": taxon_id,
            "has[]": "photos",
            "quality_grade": "research", # Research grade only
            "per_page": 10
        }

        try:
            # Add headers to act as a normal web client
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(api_url, params=params, headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                
                downloaded_count = 0
                for obs in results:
                    photos = obs.get("photos", [])
                    if photos:
                        # Get the medium-sized image URL
                        img_url = photos[0].get("url").replace("square", "medium")
                        
                        img_path = os.path.join(species_dir, f"{name}_{downloaded_count+1}.jpg")
                        
                        # Download the image
                        req = urllib.request.Request(img_url, headers=headers)
                        with urllib.request.urlopen(req, timeout=15) as img_resp, open(img_path, 'wb') as f:
                            f.write(img_resp.read())
                            
                        downloaded_count += 1
                        print(f"    Downloaded image {downloaded_count}/10")
                        
                print(f"Successfully created mini-dataset for {name}!\n")
            else:
                print(f"API Error for {name}: Status {response.status_code}\n")
                
        except Exception as e:
            print(f"Connection error for {name}: {e}\n")
            
        # Sleep briefly to respect the API rate limits
        time.sleep(2)

    print("="*60)
    print(f"  Mini iNaturalist Dataset successfully created at: {base_dir}")
    print("="*60)

if __name__ == "__main__":
    download_inaturalist_mini()
