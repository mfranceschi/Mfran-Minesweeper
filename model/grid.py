from abc import ABC, abstractmethod
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Iterable, Tuple

from overrides.enforce import EnforceOverrides

from .utils import Point2D


@dataclass(frozen=False)
class Cell:
    """
    Position and attributes of a cell in a grid.
    """

    pos: Point2D
    has_mine: bool = False
    is_flagged: bool = False
    is_revealed: bool = False

    def __repr__(self) -> str:
        return f"Cell[x={self.pos.x},y={self.pos.y}," + \
            f"has_mine={self.has_mine},is_flagged={self.is_flagged}"

    @property
    def x(self) -> int:  # pylint: disable=invalid-name
        return self.pos.x

    @property
    def y(self) -> int:  # pylint: disable=invalid-name
        return self.pos.y


class Grid(ABC, EnforceOverrides):
    """
    Container for a 2D grid of cells.
    Use __getitem__(x, y) to get a specific cell.
    """

    def __init__(self, dim: Point2D):
        assert dim.x >= 2
        assert dim.y >= 2
        self.dim = dim

    @abstractmethod
    def _get_cell_or_raise(self, coord: Point2D) -> Cell:
        raise NotImplementedError()

    def __getitem__(self, coord_xy: Tuple[int, int]) -> Cell:
        return self._get_cell_or_raise(Point2D(*coord_xy))

    @abstractmethod
    def get_neighbours(self, cell: Point2D) -> Iterable[Cell]:
        raise NotImplementedError()

    def get_nb_of_close_mines(self, cell_coord: Point2D) -> int:
        assert not self.get_cell_has_mine(cell_coord)
        return sum((cell.has_mine for cell in self.get_neighbours(cell_coord)))

    def set_cell_flagged(self, cell_coord: Point2D, flagged: bool) -> None:
        self._get_cell_or_raise(cell_coord).is_flagged = flagged

    def set_cell_revealed(self, cell_coord: Point2D, revealed: bool) -> None:
        self._get_cell_or_raise(cell_coord).is_revealed = revealed

    def get_cell_has_mine(self, cell_coord: Point2D) -> bool:
        return self._get_cell_or_raise(cell_coord).has_mine

    @abstractmethod
    def __iter__(self) -> Iterator[Cell]:
        raise NotImplementedError()
