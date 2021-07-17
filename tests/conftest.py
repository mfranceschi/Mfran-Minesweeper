import pytest

from game_engine.grid import Grid


@pytest.fixture
def grid_5_7():
    return Grid(5, 7)
