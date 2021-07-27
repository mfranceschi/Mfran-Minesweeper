from dataclasses import dataclass

from model.utils import Point2D


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
