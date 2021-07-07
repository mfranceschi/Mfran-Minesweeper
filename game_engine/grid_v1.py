# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:43:41 2021

@author: Utilisateur
"""

from typing import Callable, List

class Cell:
    def __init__(self, x, y, has_mine: bool):
        self.x = x
        self.y = y
        self.has_mine = has_mine
        self.is_flagged = False
        self.is_revealed = False

    def __repr__(self) -> str:
        return f"Cell[x={self.x},y={self.y},has_mine={self.has_mine},is_flagged={self.is_flagged}"


class Grid_V1:
    def __init__(self, grid_x: int = 10, grid_y: int = 10):
        self.grid_dimensions = {"x": grid_x, "y": grid_y}
        self.nbr_mines = 0

        self.game_is_running = False

        # TODO using a list might not be ideal for perfs. To be profiled?
        self.grid = [ [ Cell(x, y, False) for x in range(grid_x)] for y in range(grid_y)]
    
    def _get_cell(self, x: int, y: int) -> Cell:
        return self.grid[x][y]

    def fill_with_mines(self, nbr_mines: int = 3, procedure: Callable[[], None] = None):
        for i_cell in range(nbr_mines):
            self._get_cell(0, i_cell).has_mine = True

    def _assert_coordinates_in_bounds(self, x: int, y: int):
        assert (0 <= x < self.grid_dimensions["x"]) and (0 <= y < self.grid_dimensions["y"])

    def _get_neighbours(self, x: int, y: int) -> List[int]:
        neighbours = []
        max_x = self.grid_dimensions["x"] - 1
        max_y = self.grid_dimensions["y"] - 1

        if x != 0:
            # Top left
            if y != 0:
                neighbours.append(self.grid[x-1][y-1])

            # Left
            neighbours.append(self.grid[x-1][y])

            # Bottom left
            if y != max_y:
                neighbours.append(self.grid[x-1][y+1])
        
        # Top
        if y != 0:
            neighbours.append(self.grid[x][y-1])

        # Bottom
        if y != max_y:
            neighbours.append(self.grid[x][y+1])

        if x != max_x:
            # Top right
            if y != 0:
                neighbours.append(self.grid[x+1][y-1])

            # Right
            neighbours.append(self.grid[x+1][y])

            # Bottom right
            if y != max_y:
                neighbours.append(self.grid[x+1][y+1])
        
        return neighbours

    def get_nb_of_close_mines(self, x: int, y: int) -> int:
        self._assert_coordinates_in_bounds(x, y)
        assert not self._get_cell(x, y).has_mine
        return sum((cell.has_mine for cell in self._get_neighbours(x, y)))

    def flag_unflag_cell(self, x: int, y: int, value: bool) -> None:
        self._assert_coordinates_in_bounds(x, y)
        self._get_cell(x, y).is_flagged = value

    def reveal_cell(self, x: int, y: int):
        self._assert_coordinates_in_bounds(x, y)
        self._get_cell(x, y).is_revealed = True


if __name__ == "__main__":
    grid = Grid_V1(5, 5)
    grid.fill_with_mines(1)

    print(grid.grid)
    print(grid.get_nb_of_close_mines(1, 0))
    print(grid.get_nb_of_close_mines(1, 1))
    print(grid.get_nb_of_close_mines(0, 1))
    print(grid.get_nb_of_close_mines(0, 2))
