from functools import cached_property
from typing import Literal


from infrasys import Component, BaseQuantity
from scipy.stats import _continuous_distns
from pydantic import field_validator

from erad.probability_builder import ProbabilityFunctionBuilder
from erad.models.asset import AssetState
from erad.enums import AssetTypes
from erad.quantities import Speed

FRAGILITY_CURVE_TYPES = [fc for fc in AssetState.model_fields if fc not in ["name", "uuid", "timestamp"]]
SUPPORTED_CONT_DIST = [name for name in dir(_continuous_distns) if not name.startswith('_')]


class ProbabilityFunction(Component):
    name : str = ''
    distribution : Literal[*SUPPORTED_CONT_DIST]
    parameters : list[float | BaseQuantity]

    @field_validator('parameters')
    def validate_parameters(cls, value):
        if not isinstance(value[0], BaseQuantity):
            raise ValueError("First parameters must be BaseQuantity")
        for param in value[1:]:
            if not isinstance(param, float):
                raise ValueError("All values after the first parameter must be float")
        return value

    @cached_property
    def prob_model(self) -> ProbabilityFunctionBuilder:
        return ProbabilityFunctionBuilder(self.distribution, self.parameters)

    @classmethod
    def example(cls) -> "ProbabilityFunction":
        return ProbabilityFunction(
            distribution="norm",  
            parameters=[Speed(1.5, 'm/s'), 2],
        )


class FragilityCurve(Component):
    name : str = ''
    asset_type : AssetTypes
    prob_function : ProbabilityFunction

    @classmethod
    def example(cls) -> "FragilityCurve":
        return FragilityCurve(
            asset_type=AssetTypes.substation,
            prob_function=ProbabilityFunction.example(),
        )


class HazardFragilityCurves(Component):
    name : str = 'DEFAULT_CURVES'
    asset_state_param : Literal[*FRAGILITY_CURVE_TYPES]
    curves : list[FragilityCurve]

    @classmethod
    def example(cls) -> "HazardFragilityCurves":
        return HazardFragilityCurves(
            asset_state_param='peak_ground_acceleration',
            curves=[FragilityCurve.example()],
        )