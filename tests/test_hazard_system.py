from infrasys import Component

import pytest

from erad.systems.hazard_system import HazardSystem
from erad.constants import HAZARD_MODELS

def test_component_addition():
    h = HazardSystem(auto_add_composed_components=True)
    for m in HAZARD_MODELS:
        h.add_component(m.example())

def test_component_failure():

    class Testing(Component):
        ...

    test = Testing(
        name = "asdf"
    )

    h = HazardSystem(auto_add_composed_components=True)
    with pytest.raises(AssertionError):
        h.add_component(test)

def test_system_serialization_deserialization(tmp_path):
    h = HazardSystem(auto_add_composed_components=True)
    for m in HAZARD_MODELS:
        h.add_component(m.example())
    h.to_json(tmp_path / "test_system.json")

    HazardSystem.from_json(tmp_path / "test_system.json")

def test_earthquake_example():
    HazardSystem.earthquake_example()

def test_fire_example():
    HazardSystem.fire_example()

def test_wind_example():
    HazardSystem.wind_example()

def test_flood_example():
    HazardSystem.flood_example()