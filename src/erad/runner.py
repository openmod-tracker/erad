from datetime import datetime

from gdm.distribution import DistributionSystem
from loguru import logger

from erad.models.fragility_curve import HazardFragilityCurves
from erad.fragility_curves import DEFAULT_FRAGILTY_CURVES
from erad.systems.hazard_system import HazardSystem
from erad.systems.asset_system import AssetSystem
from erad.constants import HAZARD_TYPES
from erad.models.asset import Asset

class HarzardSimulator:

    def __init__(self, asset_system: AssetSystem):
        self.assets = list(asset_system.get_components(Asset))
    
    @classmethod
    def from_gdm(cls, dist_system: DistributionSystem)->'HarzardSimulator':
        """Create a HarzardSimulator from a DistributionSystem."""
        asset_system = AssetSystem.from_gdm(dist_system)
        return cls(asset_system)

    def _get_time_stamps(self)-> list[datetime]:
        timestamps = []
        for model_type in HAZARD_TYPES:
            for model in self.hazard_system.get_components(model_type):
                timestamps.append(model.timestamp)
        return sorted(timestamps)
    
    def run(self, hazard_system: HazardSystem, curve_set:str='DEFAULT_CURVES'):
        
        probability_models = list(hazard_system.get_components(HazardFragilityCurves, filter_func=lambda x: x.name == curve_set))

        if not probability_models:
            logger.warning("No HazardFragilityCurves definations found in the passed HazardSystem using default curve definations")
            probability_models = DEFAULT_FRAGILTY_CURVES

        self.hazard_system = hazard_system
        self.timestamps = self._get_time_stamps()
        for timestamp in self.timestamps:
            for hazard_type in HAZARD_TYPES:
                for hazard_model in self.hazard_system.get_components(hazard_type, filter_func=lambda x: x.timestamp == timestamp):
                    for asset in self.assets:
                        asset.update_survival_probability(timestamp, hazard_model, probability_models)

 