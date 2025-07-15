from datetime import datetime

from pydantic import field_serializer, field_validator
from shapely.geometry import Polygon, Point
from gdm.quantities import Distance

from erad.models.hazard.base_models import BaseDisasterModel
from erad.quantities import Speed


class FloodModelArea(BaseDisasterModel):
    name: str = ""
    affected_area: Polygon
    water_velocity: Speed
    water_elevation: Distance

    @field_validator("affected_area", mode="before")
    def deserialize_polygon(cls, value):
        if isinstance(value, dict) and value.get("type") == "Polygon":
            points = [Point(c) for c in value["coordinates"]]
            return Polygon(points)
        return value

    @field_serializer("affected_area")
    def serialize_polygon(self, poly: Polygon, _info):
        return {"type": "Polygon", "coordinates": list(poly.exterior.coords)}

    @classmethod
    def example(cls) -> "FloodModelArea":
        return FloodModelArea(
            affected_area=Polygon(
                [
                    (-120.93036, 36.60144),
                    (-120.91072, 36.60206),
                    (-120.91127, 36.5712),
                    (-120.93405, 36.58100),
                ]
            ),
            water_velocity=Speed(50, "meter/second"),
            water_elevation=Distance(10, "feet"),
        )


class FloodModel(BaseDisasterModel):
    timestamp: datetime
    affected_areas: list[FloodModelArea]

    @classmethod
    def example(cls) -> "FloodModel":
        return FloodModel(
            name="flood 1",
            timestamp=datetime.now(),
            affected_areas=[FloodModelArea.example()],
        )
