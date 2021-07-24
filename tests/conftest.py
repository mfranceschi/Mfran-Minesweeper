import pytest

from model.grid import Grid, GridImplWithPythonList
from model.utils import Point2D


@pytest.fixture
def grid_5_7() -> Grid:
    return GridImplWithPythonList(Point2D(5, 7))
