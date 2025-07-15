from functools import cached_property
from typing import Literal
from pathlib import Path


from infrasys import Component, BaseQuantity
from scipy.stats import _continuous_distns
from pydantic import field_validator
import numpy as np

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
        if not any(isinstance(v, BaseQuantity) for v in value):
            raise ValueError("There should be atleast one BaseQuantity in the parameters")
        
        units = set([v.units for v in value if isinstance(v, BaseQuantity)])
        if not len(units) == 1:
            raise ValueError("All BaseQuantities should have the same units")
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
    
    def plot(self, file_path: Path, x_min: float = 0, x_max: float = None, number_of_points: int = 100):
        """Plot the fragility curves."""
        try:
            import matplotlib.pyplot as plt
        except:
            raise ImportError("matplotlib is required for plotting. Please install it using 'pip install matplotlib'")
        
        if not self.curves:
            raise ValueError("No curves to plot")
        
        quantities = [p for p in self.curves[0].prob_function.parameters if isinstance(p, BaseQuantity)]

        x_label = self.asset_state_param.replace("_", " ").title()
        x = np.linspace(x_min, x_max, number_of_points)
        
        fig, ax = plt.subplots()
        fig.set_size_inches(12, 8, forward=True)
        for curve in self.curves:
            model_class = quantities[0].__class__
            units = quantities[0].units
            prob_model = curve.prob_function.prob_model
            y = prob_model.probability(model_class(x, units))
            label =curve.asset_type.name.replace("_", " ").title()
            ax.plot(x, y, label=label)
        ax.set_xlabel(f'{x_label} [{units}]')
        ax.set_ylabel('Probability of Faliure')
        ax.set_title(f'Fragility Curves for {x_label}')
        ax.legend()
        fig.tight_layout()
        fig.savefig(file_path, dpi=300)
        plt.show()