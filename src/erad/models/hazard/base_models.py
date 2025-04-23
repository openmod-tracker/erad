from pydantic import ConfigDict
from infrasys import Component

class BaseDisasterModel(Component):

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra='forbid'
    )
