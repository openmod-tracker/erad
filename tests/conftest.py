
from gdmloader.constants import GCS_CASE_SOURCE
from gdm.distribution import DistributionSystem
from gdmloader.source import SystemLoader 

import pytest

@pytest.fixture
def gdm_system():
    loader = SystemLoader()
    loader.add_source(GCS_CASE_SOURCE)
    return loader.load_dataset(
        system_type=DistributionSystem,
        source_name=GCS_CASE_SOURCE.name,
        dataset_name="p5r"
    )

