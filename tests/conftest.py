import pytest

from game_engine.grid import Grid
from game_engine.utils import Point2D


@pytest.fixture
def grid_5_7():
    return Grid(Point2D(5, 7))
