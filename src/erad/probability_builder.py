from infrasys import BaseQuantity
import scipy.stats as stats
import numpy as np
from typing import Callable, Union

class ProbabilityFunctionBuilder:
    """Class containing utility fuctions for scenario definations."""
    
    def __init__(self, dist: Union[str, Callable], params: list[float | BaseQuantity]):
        """Constructor for ProbabilityFunctionBuilder.

        Args:
            dist (str or Callable): Name of the distribution (for scipy.stats) or a custom CDF function.
            params (list): Parameters for the distribution or custom CDF.
        """
        self.is_custom = callable(dist)
        self.dist = dist
        self.params = params

        if not self.is_custom:
            # Scipy-style distribution: expect first param as BaseQuantity
            self.quantity = params[0].__class__
            self.units = params[0].units
            self.dist = getattr(stats, dist)
            self.params = [params[0].magnitude] + params[1:]
        else:
            # Custom function
            pass
    
    def sample(self):
        """Sample the distribution (only supported for Scipy distributions)."""
        if self.is_custom:
            raise NotImplementedError("Sampling is not supported for custom CDF functions.")
        return self.quantity(self.dist.rvs(*self.params, size=1)[0], self.units)

    def probability(self, value: BaseQuantity) -> float:
        """Calculate survival probability of a given asset.

        Args:
            value (BaseQuantity): The variable of interest (e.g., wind speed).
        """
        assert isinstance(value, BaseQuantity), "Value must be a BaseQuantity"

        if self.is_custom:
            # Unpack parameters and pass to custom CDF
            return self.dist(*self.params)
        else:
            cdf = self.dist.cdf
            return cdf(value.to(self.units).magnitude, *self.params)