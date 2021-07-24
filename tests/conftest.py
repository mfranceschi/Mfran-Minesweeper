import pytest

from model.grid import Grid
from model.utils import Point2D


@pytest.fixture
def grid_5_7():
    return Grid(Point2D(5, 7))
