from datetime import datetime

from gdm.distribution.components import DistributionBus
from gdm.distribution import DistributionSystem
from gdm.quantities import Distance
from shapely.geometry import Point

from erad.systems.hazard_system import HazardSystem
from erad.models.hazard import EarthQuakeModel
from erad.runner import HarzardSimulator

def test_gdm_model_earthquake(gdm_system: DistributionSystem):
    hazard_scenario = HarzardSimulator.from_gdm(gdm_system)
    buses: list[DistributionBus] = list(gdm_system.get_components(DistributionBus))
    buses = sorted(buses, key=lambda b: b.name)
    earthquake = EarthQuakeModel(
        name = "earthquake_1", 
        timestamp = datetime.now(),
        origin = Point(buses[0].coordinate.y, buses[0].coordinate.x),
        depth = Distance(100, "kilometer"),
        magnitude = 5.8

    )
    hazard_system = HazardSystem(auto_add_composed_components=True)
    hazard_system.add_component(earthquake)
    hazard_scenario.run(hazard_system)

    