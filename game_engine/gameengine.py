# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:43:41 2021

@author: Utilisateur
"""

from .grid import Grid
from typing import Callable, List


class GameEngine:
    def __init__(self, grid_x: int = 10, grid_y: int = 10):
        self._grid = Grid(grid_x, grid_y)
        self.nbr_mines = 0
        self.game_is_running = False

    def fill_with_mines(self, nbr_mines: int = 3, procedure: Callable[[], None] = None):
        # TODO better abstraction system
        for i_cell in range(nbr_mines):
            self._grid._get_cell(0, i_cell).has_mine = True

    def get_nb_of_close_mines(self, x: int, y: int) -> int:
        assert not self._grid.get_cell_has_mine(x, y)
        return sum((cell.has_mine for cell in self._grid.get_neighbours(x, y)))

    def flag_cell(self, cell_x: int, cell_y: int) -> None:
        self._grid.set_cell_flagged(cell_x, cell_y, True)

    def unflag_cell(self, cell_x: int, cell_y: int) -> None:
        self._grid.set_cell_flagged(cell_x, cell_y, False)

    def reveal_cell(self, cell_x: int, cell_y: int):
        self._grid.set_cell_revealed(cell_x, cell_y, True)

    def get_grid_for_display(self) -> List[str]:
        cells = []
        for cell in self._grid:
            if cell.is_revealed:
                if cell.has_mine:
                    cells.append("M")
                else:
                    neighbours = self.get_nb_of_close_mines(cell.x, cell.y)
                    cells.append(str(neighbours))
            elif cell.is_flagged:
                cells.append("F")
            else:
                cells.append(".")
        return cells
