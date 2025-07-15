from collections import defaultdict, Counter

from gdm.distribution import DistributionSystem
import gdm.distribution.components as gdc
from gdm.quantities import Distance
from infrasys import System
import geopandas as gpd
import networkx as nx
import pandas as pd

from erad.gdm_mapping import asset_to_gdm_mapping
from erad.constants import ASSET_TYPES
from erad.models.asset import Asset
from erad.enums import AssetTypes, NodeTypes


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

    def get_undirected_graph(self):
        """Get the undirected graph of the AssetSystem."""
        g = nx.Graph()
        
        for asset in self.get_components(Asset):
            if not asset.connections and asset.asset_type not in NodeTypes:
                asset.devices.append(str(asset.distribution_asset))
        
        for asset in self.get_components(Asset):
            if asset.connections:
                u, v = asset.connections
                g.add_edge(str(u), str(v), **asset.model_dump())
            else:
                if asset.asset_type in NodeTypes:
                    asset.pprint()
                    g.add_node(str(asset.distribution_asset), **asset.model_dump())
        
        return g


    @classmethod
    def from_gdm(cls, dist_system: DistributionSystem)->'AssetSystem':
        """Create a AssetSystem from a DistributionSystem."""
        asset_map = AssetSystem.map_asets(dist_system)
        list_of_assets = AssetSystem._build_assets(asset_map)
        system = AssetSystem(auto_add_composed_components=True)
        system.add_components(*list_of_assets)
        return system

    def to_gdf(self)->gpd.GeoDataFrame:
        """Create a geodataframe from an AssetSystem."""
        node_data = defaultdict(list)
        assets : list[Asset] = self.get_components(Asset)
        for asset in assets:
            if asset.asset_state:
                for asset_state in asset.asset_state:
                    node_data["name"].append(asset.name)
                    node_data["type"].append(asset.asset_type.name)
                    node_data["height"].append(asset.height.to("meter").magnitude)
                    node_data["elevation"].append(asset.elevation.to("meter").magnitude)
                    node_data["latitude"].append(asset.latitude)
                    node_data["longitude"].append(asset.longitude)
                    node_data["timestamp"].append(asset_state.timestamp)
                    node_data["survival_prob"].append(asset_state.survival_probability)
                    node_data["wind_speed"].append(asset_state.wind_speed)
                    node_data["fire_boundary_dist"].append(asset_state.fire_boundary_dist)
                    node_data["flood_depth"].append(asset_state.flood_depth)
                    node_data["flood_velocity"].append(asset_state.flood_velocity)
                    node_data["peak_ground_acceleration"].append(asset_state.peak_ground_acceleration)
                    node_data["peak_ground_velocity"].append(asset_state.peak_ground_velocity)
            else:
                node_data["name"].append(asset.name)
                node_data["type"].append(asset.asset_type.name)
                node_data["height"].append(asset.height.to("meter").magnitude)
                node_data["elevation"].append(asset.elevation.to("meter").magnitude)
                node_data["latitude"].append(asset.latitude)
                node_data["longitude"].append(asset.longitude)
                node_data["timestamp"].append(None)
                node_data["survival_prob"].append(None)
                node_data["wind_speed"].append(None)
                node_data["fire_boundary_dist"].append(None)
                node_data["flood_depth"].append(None)
                node_data["flood_velocity"].append(None)
                node_data["peak_ground_acceleration"].append(None)
                node_data["peak_ground_velocity"].append(None)
        
        nodes_df = pd.DataFrame(node_data)
        gdf_nodes = gpd.GeoDataFrame(
            nodes_df,
            geometry=gpd.points_from_xy(nodes_df.longitude, nodes_df.latitude),
            crs="EPSG:4326",
        )
        return gdf_nodes  

    def to_geojson(self)-> str:
        """Create a GeoJSON from an AssetSystem."""
        gdf_nodes = self.to_gdf()
        return gdf_nodes.to_json()

    @staticmethod
    def _build_assets(asset_map: dict[AssetTypes: list[gdc.DistributionComponentBase]]) -> list[Asset]:
        list_of_assets = []
        for asset_type, components in asset_map.items():
            for component in components:
                lat, long = AssetSystem._get_component_coordinate(component)
                
                list_of_assets.append(Asset(
                    name=component.name,
                    connections=[c.uuid for c in component.buses] if hasattr(component, "buses") else [],
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
        AssetSystem._map_transformers(asset_dict, dist_system)
        return asset_dict

    @staticmethod
    def _maps_buses(asset_dict: dict[AssetTypes: list[gdc.DistributionComponentBase]], dist_system:DistributionSystem):
        for bus in dist_system.get_components(gdc.DistributionBus):
            asset_type =  AssetSystem._get_bus_type(bus, asset_dict, dist_system)
            if asset_type:
                asset_dict[asset_type].append(bus)

    @staticmethod
    def _map_transformers(asset_dict: dict[AssetTypes: list[gdc.DistributionComponentBase]], dist_system:DistributionSystem):
        for transformer in dist_system.get_components(gdc.DistributionTransformerBase):
            bus_types = [ 
                AssetSystem._get_bus_type(
                    b, 
                    asset_dict, 
                    dist_system
                ) for b in transformer.buses
            ]
            if AssetTypes.transmission_junction_box in bus_types or AssetTypes.transmission_tower in bus_types:
                asset_dict[AssetTypes.transformer_mad_mount].append(transformer)
            elif all(bus_type == AssetTypes.distribution_junction_box for bus_type in bus_types):
                asset_dict[AssetTypes.transformer_mad_mount].append(transformer)
            else:
                asset_dict[AssetTypes.transformer_mad_mount].append(transformer)
             

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