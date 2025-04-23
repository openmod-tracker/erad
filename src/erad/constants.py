""" Module for managing constants in ERAD package.

_Do not change this constants in your code._
"""
from pathlib import Path

import erad.models.fragility_curve as frag
import erad.models.probability as prob
import erad.models.hazard as hazard
import erad.models.asset as asset

# Get list of continuous distributions


ROOT_PATH = Path(__file__).parent.parent.parent
TEST_PATH = Path(__file__).parent.parent.parent / "tests"
DATA_FOLDER_NAME = "data"
DATA_FOLDER = TEST_PATH / DATA_FOLDER_NAME


ASSET_TYPES = (
    asset.AssetState,
    asset.Asset,
    prob.AccelerationProbability,
    prob.TemperatureProbability,
    prob.DistanceProbability,
    prob.SpeedProbability,
)

HAZARD_TYPES = (
    hazard.EarthQuakeModel,
    hazard.FloodModel,
    hazard.FireModel,
    hazard.WindModel,
)

HAZARD_MODELS = (
    hazard.EarthQuakeModel,
    hazard.FloodModelArea,
    hazard.FireModelArea,
    hazard.FloodModel,
    hazard.FireModel,
    hazard.WindModel,
    frag.ProbabilityFunction,
    frag.FragilityCurve,
    frag.HazardFragilityCurves,
)

SUPPORTED_MODELS = [
    hazard.EarthQuakeModel,
    hazard.FloodModelArea,
    hazard.FireModelArea,
    hazard.FloodModel,
    hazard.FireModel,
    hazard.WindModel,
    prob.AccelerationProbability,
    prob.TemperatureProbability,
    prob.DistanceProbability,
    prob.SpeedProbability,
    frag.ProbabilityFunction,
    frag.FragilityCurve,
    frag.HazardFragilityCurves,
    asset.AssetState,
    asset.Asset,
]