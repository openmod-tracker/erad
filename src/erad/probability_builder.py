from infrasys import BaseQuantity  
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np



class ProbabilityFunctionBuilder:
    """Class containing utility fuctions for sceario definations."""
    
    
    def __init__(self, dist, params:list[float | BaseQuantity]):
        """Constructor for BaseScenario class.

        Args:
            dist (str): Name of teh distribution. Should follow Scipy naming convention
            params (list): A list of parameters for the chosen distribution function. See Scipy.stats documentation
        """
        self.quantity =  params[0].__class__
        self.units = params[0].units
        self.dist = getattr(stats, dist)
        self.params = [params[0].magnitude] + params[1:]
        return 

    def sample(self):
        """Sample the distribution """
        return self.quantity(self.dist.rvs(*self.params, size=1)[0], self.units)

    def plot_cdf(self, x:np.linspace, ax =None, label="") -> None:
        """Plot the cumalative distribution fuction"""
        cdf = self.dist.cdf
        if ax is None:
            plt.plot(x,cdf(x, *self.params), label=label)
        else:
            ax.plot(x,cdf(x, *self.params), label=label)
    

    def probability(self, value: BaseQuantity) -> float:
        """Calculates survival probability of a given asset.

        Args:
            value (float): value for vetor of interest. Will change with scenarions
        """
        assert isinstance(value, BaseQuantity), "Value must be a BaseQuantity"
        
        
        cdf = self.dist.cdf
        return cdf(value.to(self.units).magnitude, *self.params)