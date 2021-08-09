import pytest

from mfranceschi_minesweeper.model.grid import Grid
from mfranceschi_minesweeper.model.grid_impl_with_python_list import GridImplWithPythonList
from mfranceschi_minesweeper.utils import Point2D


@pytest.fixture
def grid_5_7() -> Grid:
    return GridImplWithPythonList(Point2D(5, 7))
