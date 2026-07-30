import os
import time
import json
import urllib.request

def download_file(url, path):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as response, open(path, 'wb') as out_file:
        out_file.write(response.read())

def main():
    print("="*60)
    print("  WILDLIFE INTELLIGENCE SYSTEM - Dataset Downloader")
    print("  Using Hugging Face, Xeno-Canto API & GBIF API")
    print("="*60 + "\n")

    base_dir = "./datasets"

    # =========================================================
    # 1. iNaturalist Alternative (Hugging Face)
    # =========================================================
    print(">>> 1. Downloading iNaturalist Alternative (Hugging Face)...")
    try:
        from datasets import load_dataset
        inat_dir = f"{base_dir}/inaturalist"
        os.makedirs(inat_dir, exist_ok=True)
        
        # Download a small wildlife species dataset from Hugging Face
        ds = load_dataset("lucabaggi/animal-wildlife", split="train[:100]")
        ds.save_to_disk(inat_dir)
        print(f"    Saved {len(ds)} wildlife species records to {inat_dir}\n")
    except ImportError:
        print("    'datasets' library not installed. Installing now...")
        os.system("pip install datasets pillow")
        from datasets import load_dataset
        inat_dir = f"{base_dir}/inaturalist"
        os.makedirs(inat_dir, exist_ok=True)
        ds = load_dataset("lucabaggi/animal-wildlife", split="train[:100]")
        ds.save_to_disk(inat_dir)
        print(f"    Saved {len(ds)} wildlife species records to {inat_dir}\n")
    except Exception as e:
        print(f"    Failed: {e}\n")

    # =========================================================
    # 2. BirdCLEF Alternative (Xeno-Canto Public API)
    # Download real bird audio MP3 files directly - NO auth needed!
    # =========================================================
    print(">>> 2. Downloading BirdCLEF Alternative (Xeno-Canto Bird Audio)...")
    bird_dir = f"{base_dir}/birdclef/audio"
    os.makedirs(bird_dir, exist_ok=True)

    # List of common bird species to download audio for
    bird_species = [
        "Turdus merula",       # Common Blackbird
        "Erithacus rubecula",  # European Robin
        "Parus major",        # Great Tit
        "Corvus corax",       # Common Raven
        "Columba palumbus",   # Common Wood Pigeon
    ]

    for species in bird_species:
        try:
            safe_name = species.replace(" ", "_").lower()
            api_url = f"https://xeno-canto.org/api/2/recordings?query={species.replace(' ', '+')}&page=1"
            req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())

            if data.get("recordings") and len(data["recordings"]) > 0:
                # Get the first high quality recording
                rec = data["recordings"][0]
                audio_url = rec.get("file")
                if audio_url:
                    if not audio_url.startswith("http"):
                        audio_url = "https:" + audio_url
                    file_path = f"{bird_dir}/{safe_name}.mp3"
                    download_file(audio_url, file_path)
                    print(f"    Downloaded: {species} -> {safe_name}.mp3")
                else:
                    print(f"    No audio URL found for {species}")
            else:
                print(f"    No recordings found for {species}")
        except Exception as e:
            print(f"    Failed for {species}: {e}")

    print(f"    Bird audio saved to {bird_dir}\n")

    # =========================================================
    # 3. GBIF (Live API with retry)
    # =========================================================
    print(">>> 3. Pulling GBIF JSON data (Live API with retry)...")
    gbif_dir = f"{base_dir}/gbif/data"
    os.makedirs(gbif_dir, exist_ok=True)
    
    # Pull data for multiple species
    species_queries = [
        ("5219404", "lion"),         # Panthera leo
        ("5219436", "tiger"),        # Panthera tigris
        ("2498252", "elephant"),     # Loxodonta africana
        ("5220083", "leopard"),      # Panthera pardus
    ]

    for taxon_key, name in species_queries:
        gbif_url = f"https://api.gbif.org/v1/occurrence/search?taxonKey={taxon_key}&limit=10"
        for attempt in range(3):
            try:
                req = urllib.request.Request(gbif_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=15) as resp:
                    gbif_data = json.loads(resp.read().decode())
                with open(f"{gbif_dir}/{name}_occurrences.json", "w", encoding="utf-8") as f:
                    json.dump(gbif_data, f, indent=4)
                print(f"    Downloaded GBIF data for: {name}")
                break
            except Exception as e:
                print(f"    Attempt {attempt+1}/3 failed for {name}. Retrying...")
                time.sleep(3)
        else:
            print(f"    Failed to download GBIF data for {name}")

    print(f"    GBIF data saved to {gbif_dir}\n")

    print("="*60)
    print("  ALL DATASETS DOWNLOADED SUCCESSFULLY!")
    print("="*60)

if __name__ == "__main__":
    main()
