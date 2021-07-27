from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Union

from overrides import EnforceOverrides

from model.utils import Point2D


class CellValueAsString(Enum):
    REVEALED_ZERO_NEIGHBOUR = "0"
    FLAGGED = "F"
    MINE = "M"
    NOT_REVEALED = " "


CellValue = Union[int, CellValueAsString]


class GUI(ABC, EnforceOverrides):
    """
    Interface for some controller to send and display information and data.
    """

    @abstractmethod
    def reset_grid_size(self, grid_dim: Point2D) -> None:
        raise NotImplementedError()

    @abstractmethod
    def set_nbr_mines(self, nbr_mines: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def set_grid(self, grid: List[CellValue]) -> None:
        raise NotImplementedError()

    @abstractmethod
    def victory(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def game_over(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def game_starts(self) -> None:
        raise NotImplementedError()
