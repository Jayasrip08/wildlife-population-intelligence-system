from typing import Dict, Any

class ConservationEngine:
    """
    Conservation Recommendation & Wildlife Health Scoring Engine
    Implements the PDF Specification Weighted Ecosystem Health Scoring Model:
    Ecosystem Health Score = (30% * Species Diversity) 
                           + (25% * Population Stability) 
                           + (20% * Habitat Quality) 
                           + (15% * Endangered Species Status) 
                           + (10% * Environmental Conditions)
    """

    def calculate_health_and_recommendations(
        self,
        region: str,
        species_diversity: float,
        population_stability: float,
        habitat_quality: float,
        endangered_species_status: float,
        environmental_conditions: float
    ) -> Dict[str, Any]:
        
        # Clamp scores between 0 and 100
        sd = max(0.0, min(100.0, species_diversity))
        ps = max(0.0, min(100.0, population_stability))
        hq = max(0.0, min(100.0, habitat_quality))
        es = max(0.0, min(100.0, endangered_species_status))
        ec = max(0.0, min(100.0, environmental_conditions))

        # PDF Formula calculation
        overall_health = round((0.30 * sd) + (0.25 * ps) + (0.20 * hq) + (0.15 * es) + (0.10 * ec), 1)

        # Tiered Status Classification according to PDF specifications
        if overall_health >= 85.0:
            health_status = "Excellent"
            priority_action = "Maintain continuous anti-poaching surveillance and monitor seasonal breeding zones."
            patrol_units = 3
            corridor = "Standard Reserve Buffer Zone"
        elif overall_health >= 70.0:
            health_status = "Healthy"
            priority_action = "Deploy targeted water point sensors and expand buffer boundary monitoring."
            patrol_units = 5
            corridor = "Eastern Migratory Buffer Corridor"
        elif overall_health >= 55.0:
            health_status = "Moderate Concern"
            priority_action = "Establish anti-poaching patrols along agricultural boundaries and restrict cattle grazing access."
            patrol_units = 8
            corridor = "Sector B-4 Restoration Corridor"
        elif overall_health >= 40.0:
            health_status = "Vulnerable"
            priority_action = "URGENT: Deploy rapid response anti-poaching forces and initiate immediate artificial water supplementation."
            patrol_units = 12
            corridor = "Critical Northern Wildlife Passage"
        else:
            health_status = "Critical"
            priority_action = "EMERGENCY: Immediate multi-agency intervention required. Lock down boundary access, deploy drone aerial patrols, and implement habitat rescue protocols."
            patrol_units = 20
            corridor = "High-Risk Sanctuary Emergency Corridor"

        return {
            "region": region,
            "species_diversity_score": sd,
            "population_stability_score": ps,
            "habitat_quality_score": hq,
            "endangered_species_score": es,
            "environmental_conditions_score": ec,
            "overall_ecosystem_health": overall_health,
            "health_status": health_status,
            "priority_action": priority_action,
            "patrol_unit_allocation": patrol_units,
            "restoration_corridor_needed": corridor
        }

conservation_engine = ConservationEngine()
