# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:43:41 2021

@author: Utilisateur
"""

from .grid import Grid
from typing import Callable


class GameEngine:
    def __init__(self, grid_x: int = 10, grid_y: int = 10):
        self.grid = Grid(grid_x, grid_y)
        self.nbr_mines = 0
        self.game_is_running = False

    def fill_with_mines(self, nbr_mines: int = 3, procedure: Callable[[], None] = None):
        for i_cell in range(nbr_mines):
            self.grid.get_cell(0, i_cell).has_mine = True

    def _assert_coordinates_in_bounds(self, x: int, y: int):
        assert (0 <= x < self.grid.dim.x) and (0 <= y < self.grid.dim.y)

    def get_nb_of_close_mines(self, x: int, y: int) -> int:
        self._assert_coordinates_in_bounds(x, y)
        assert not self.grid.get_cell_has_mine(x, y)
        return sum((cell.has_mine for cell in self.grid.get_neighbours(x, y)))

    def flag_cell(self, cell_x: int, cell_y: int) -> None:
        self.grid.set_cell_flagged(cell_x, cell_y, True)

    def unflag_cell(self, cell_x: int, cell_y: int) -> None:
        self.grid.set_cell_flagged(cell_x, cell_y, False)

    def reveal_cell(self, cell_x: int, cell_y: int):
        self.grid.set_cell_revealed(cell_x, cell_y, True)


if __name__ == "__main__":
    grid = GameEngine(5, 5)
    grid.fill_with_mines(1)

    print(grid.grid)
    print(grid.get_nb_of_close_mines(1, 0))
    print(grid.get_nb_of_close_mines(1, 1))
    print(grid.get_nb_of_close_mines(0, 1))
    print(grid.get_nb_of_close_mines(0, 2))
