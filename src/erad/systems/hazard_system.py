from infrasys import System

from erad.constants import HAZARD_MODELS
import erad.models.fragility_curve as fc
import erad.models.hazard as hz
from erad.fragility_curves import DEFAULT_FRAGILTY_CURVES

class HazardSystem(System):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_component(self, component, **kwargs):
        assert isinstance(component, HAZARD_MODELS), f"Unsupported model type {component.__class__.__name__}"
        return super().add_component(component, **kwargs)

    def add_components(self, *components, **kwargs):
        assert all(isinstance(component, HAZARD_MODELS) for component in components), \
        f"Unsupported model types in passed component. Valid types are: \n" + "\n".join([s.__name__ for s in HAZARD_MODELS])
        return super().add_components(*components, **kwargs)

    def to_json(self, filename, overwrite=False, indent=None, data=None):
        if not list(self.get_components(fc.HazardFragilityCurves)):
            self.add_components(DEFAULT_FRAGILTY_CURVES)
        return super().to_json(filename, overwrite, indent, data)

    @classmethod
    def fire_example(cls)->'HazardSystem':
        hazard = hz.FireModel.example()
        system = HazardSystem(auto_add_composed_components=True)
        system.add_component(hazard)
        return system

    @classmethod
    def wind_example(cls)->'HazardSystem':
        hazard = hz.WindModel.example()
        system = HazardSystem(auto_add_composed_components=True)
        system.add_component(hazard)
        return system

    @classmethod
    def earthquake_example(cls)->'HazardSystem':
        hazard = hz.EarthQuakeModel.example()
        system = HazardSystem(auto_add_composed_components=True)
        system.add_component(hazard)
        return system

    @classmethod
    def flood_example(cls)->'HazardSystem':
        hazard = hz.FloodModel.example()
        system = HazardSystem(auto_add_composed_components=True)
        system.add_component(hazard)
        return system
    
    @classmethod
    def multihazard_example(cls)->'HazardSystem':
        wind_hazard = hz.WindModel.example()
        flood_hazard = hz.FloodModel.example()
        system = HazardSystem(auto_add_composed_components=True)
        system.add_component(wind_hazard)
        system.add_component(flood_hazard)
        return system