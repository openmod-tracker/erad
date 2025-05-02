
from gdm.distribution.components import DistributionBus
from shapely.geometry import MultiPolygon, Polygon
from gdm.distribution import DistributionSystem
from scipy.spatial import ConvexHull
import numpy as np

def _build_convex_hull(lat_lon_points):
    if len(lat_lon_points) < 3:
        raise ValueError("Need at least 3 points to compute a convex hull.")

    points = np.array([(lon, lat) for lat, lon in lat_lon_points])  # Note: x=lon, y=lat
    hull = ConvexHull(points)
    hull_points = points[hull.vertices]

    return [(lat, lon) for lon, lat in hull_points]


def get_multipolygon_from_system(system: DistributionSystem):
    coords = []
    for bus in system.get_components(DistributionBus):
        coords.append((bus.coordinate.x, bus.coordinate.y))
    
    hull = _build_convex_hull(coords)
    polygon = Polygon([(lon, lat) for lat, lon in hull])
    multi_poly = MultiPolygon([polygon])
    return multi_poly, coords
