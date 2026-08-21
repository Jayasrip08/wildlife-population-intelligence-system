from typing import Dict, Any

class HabitatEngine:
    """
    Habitat Intelligence & Vegetation Remote Sensing Engine
    Evaluates satellite NDVI, canopy cover percentage, habitat degradation, and suitability.
    """
    
    def analyze_habitat(self, region: str, ndvi: float, canopy_cover: float, degradation: float) -> Dict[str, Any]:
        # Normalize inputs
        ndvi_clean = max(-1.0, min(1.0, ndvi))
        canopy_clean = max(0.0, min(100.0, canopy_cover))
        degrad_clean = max(0.0, min(1.0, degradation))

        # Calculate Habitat Suitability Score (0 to 100)
        # Higher NDVI & Canopy contribute positively; higher Degradation reduces suitability
        ndvi_score = max(0.0, ndvi_clean) * 40  # max 40 pts
        canopy_score = (canopy_clean / 100.0) * 35 # max 35 pts
        pristine_score = (1.0 - degrad_clean) * 25 # max 25 pts
        
        suitability_score = round(ndvi_score + canopy_score + pristine_score, 1)

        # Determine Primary Threat Driver
        if degrad_clean > 0.6:
            primary_threat = "Severe Deforestation & Agricultural Encroachment"
        elif degrad_clean > 0.3:
            primary_threat = "Habitat Fragmentation & Grazing Pressure"
        elif ndvi_clean < 0.3:
            primary_threat = "Drought Stress & Vegetation Vigor Decline"
        else:
            primary_threat = "Low Threat Level - Stable Eco-Zone"

        # Estimate Water Availability Index based on vegetation vigor
        water_availability = round(min(100.0, max(20.0, (ndvi_clean * 70.0) + 30.0)), 1)

        return {
            "region": region,
            "ndvi_index": ndvi_clean,
            "canopy_cover_pct": canopy_clean,
            "degradation_index": degrad_clean,
            "suitability_score": suitability_score,
            "primary_threat": primary_threat,
            "water_availability_score": water_availability
        }

habitat_engine = HabitatEngine()
