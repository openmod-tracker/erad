from collections import defaultdict, Counter
from datetime import datetime

from gdm.distribution import DistributionSystem
import gdm.distribution.components as gdc
from gdm.quantities import Distance
from infrasys import System
from rich import print

from erad.gdm_mapping import asset_to_gdm_mapping
from erad.constants import ASSET_TYPES
from erad.models.asset import Asset
from erad.enums import AssetTypes


class AssetSystem(System):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_component(self, component, **kwargs):
        assert isinstance(component, ASSET_TYPES), f"Unsupported model type {component.__class__.__name__}"
        return super().add_component(component, **kwargs)

    def add_components(self, *components, **kwargs):
        assert all(isinstance(component, ASSET_TYPES) for component in components), \
        f"Unsupported model types in passed component. Valid types are: \n" + "\n".join([s.__name__ for s in ASSET_TYPES])
        return super().add_components(*components, **kwargs)

    @classmethod
    def from_gdm(cls, dist_system: DistributionSystem)->'AssetSystem':
        """Create a AssetSystem from a DistributionSystem."""
        asset_map = AssetSystem.map_asets(dist_system)
        list_of_assets = AssetSystem._build_assets(asset_map)
        system = AssetSystem(auto_add_composed_components=True)
        system.add_components(*list_of_assets)
        return system


    @staticmethod
    def _build_assets(asset_map: dict[AssetTypes: list[gdc.DistributionComponentBase]]) -> list[Asset]:
        list_of_assets = []
        for asset_type, components in asset_map.items():
            for component in components:
                lat, long = AssetSystem._get_component_coordinate(component)
                
                list_of_assets.append(Asset(
                    name=component.name,
                    asset_type=asset_type,
                    distribution_asset=component.uuid,
                    height=Distance(3, "meter"),
                    latitude=lat,
                    longitude=long,
                    asset_state=[],
                ))
        return list_of_assets

    @staticmethod
    def _get_component_coordinate(component:gdc.DistributionComponentBase):
        if hasattr(component, "buses"):
            xs = [bus.coordinate.x for bus in component.buses]
            ys = [bus.coordinate.y for bus in component.buses]
            return (sum(xs) / len(xs), sum(ys) / len(ys))
        elif hasattr(component, "bus"):
            return (component.bus.coordinate.x, component.bus.coordinate.y)
        elif isinstance(component, gdc.DistributionBus):
            return (component.coordinate.x, component.coordinate.y)
    
    @staticmethod
    def map_asets(dist_system:DistributionSystem)-> dict[AssetTypes: list[gdc.DistributionComponentBase]]:
        asset_dict = defaultdict(list)
        for asset, filters in asset_to_gdm_mapping.items():
            for filter_info in filters:
                models = dist_system.get_components(filter_info.component_type, filter_func=filter_info.component_filter)
                asset_dict[asset].extend(list(models))
                
        AssetSystem._maps_buses(asset_dict, dist_system)
        return asset_dict

    @staticmethod
    def _maps_buses(asset_dict: dict[AssetTypes: list[gdc.DistributionComponentBase]], dist_system:DistributionSystem):
        for bus in dist_system.get_components(gdc.DistributionBus):
            asset_type =  AssetSystem._get_bus_type(bus, asset_dict, dist_system)
            if asset_type:
                asset_dict[asset_type].append(bus)

    @staticmethod
    def _map_transsformers(asset_dict: dict[AssetTypes: list[gdc.DistributionComponentBase]], dist_system:DistributionSystem):
        for transformer in dist_system.get_components(gdc.DistributionTransformer):
            asset_type =  AssetSystem._get_bus_type(transformer.bus1, asset_dict, dist_system)
            if asset_type in [AssetTypes.distribution_poles]:
                asset_dict[AssetTypes.transformers_overhead].append(transformer)
            else:
                asset_dict[AssetTypes.transformers_mad_mount].append(transformer)

    @staticmethod
    def _get_bus_type(bus:gdc.DistributionBus, asset_dict: dict[AssetTypes: list[gdc.DistributionComponentBase]], dist_system:DistributionSystem):
        components = dist_system.get_bus_connected_components(bus.name, gdc.DistributionBranchBase)
        connected_types = []
        for component in components:
            if component in asset_dict[AssetTypes.distribution_overhead_lines]:
                connected_types.append(AssetTypes.distribution_poles)
            elif component in asset_dict[AssetTypes.transmission_overhead_lines]:
                connected_types.append(AssetTypes.transmission_tower)
            elif component in asset_dict[AssetTypes.transmission_underground_cables]:
                connected_types.append(AssetTypes.transmission_junction_box) 
            elif component in asset_dict[AssetTypes.distribution_underground_cables]:
                connected_types.append(AssetTypes.distribution_junction_box) 
            else:
                ...
        if connected_types:
            counter = Counter(connected_types)
            return counter.most_common(1)[0][0]