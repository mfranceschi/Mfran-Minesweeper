from collections.abc import Iterator
from dataclasses import dataclass
from typing import List, Tuple

from game_engine.utils import Point2D


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


class Grid:
    """
    Container for a 2D grid of cells.
    Use __getitem__(x, y) to get a specific cell.
    """

    def __init__(self, grid_dim: Point2D = Point2D(x=10, y=10)):
        assert grid_dim.x >= 2
        assert grid_dim.y >= 2

        self.dim = grid_dim

        # TODO using a list might not be ideal for perfs. To be profiled?
        self.grid = [[Cell(Point2D(x, y)) for x in range(grid_dim.x)]
                     for y in range(grid_dim.y)]

    def _get_cell_or_raise(self, coord: Point2D) -> Cell:
        assert 0 <= coord.x < self.dim.x
        assert 0 <= coord.y < self.dim.y
        return self.grid[coord.y][coord.x]

    def __getitem__(self, coord_xy: Tuple[int, int]) -> Cell:
        return self._get_cell_or_raise(Point2D(*coord_xy))

    def get_neighbours(self, cell: Point2D) -> List[Cell]:
        neighbours = []
        max_x = self.dim.x - 1
        max_y = self.dim.y - 1

        x, y = cell.x, cell.y

        if x != 0:
            # Top left
            if y != 0:
                neighbours.append(self[x-1, y-1])

            # Left
            neighbours.append(self[x-1, y])

            # Bottom left
            if y != max_y:
                neighbours.append(self[x-1, y+1])

        # Top
        if y != 0:
            neighbours.append(self[x, y-1])

        # Bottom
        if y != max_y:
            neighbours.append(self[x, y+1])

        if x != max_x:
            # Top right
            if y != 0:
                neighbours.append(self[x+1, y-1])

            # Right
            neighbours.append(self[x+1, y])

            # Bottom right
            if y != max_y:
                neighbours.append(self[x+1, y+1])

        return neighbours

    def set_cell_flagged(self, cell_coord: Point2D, flagged: bool) -> None:
        self._get_cell_or_raise(cell_coord).is_flagged = flagged

    def set_cell_revealed(self, cell_coord: Point2D, revealed: bool) -> None:
        self._get_cell_or_raise(cell_coord).is_revealed = revealed

    def get_cell_has_mine(self, cell_coord: Point2D) -> bool:
        return self._get_cell_or_raise(cell_coord).has_mine

    def __iter__(self) -> Iterator[Cell]:
        return (cell for line in self.grid for cell in line)
