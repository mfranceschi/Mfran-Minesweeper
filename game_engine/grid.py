# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:43:41 2021

@author: Utilisateur
"""

from collections.abc import Iterator
from typing import List


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_mine = False
        self.is_flagged = False
        self.is_revealed = False

    def __repr__(self) -> str:
        return f"Cell[x={self.x},y={self.y}," + \
            f"has_mine={self.has_mine},is_flagged={self.is_flagged}"


class Dimension2D:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Grid:
    def __init__(self, grid_x: int = 10, grid_y: int = 10):
        assert grid_x >= 2
        assert grid_y >= 2

        self.dim = Dimension2D(grid_x, grid_y)

        # TODO using a list might not be ideal for perfs. To be profiled?
        self.grid = [[Cell(x, y) for x in range(grid_x)]
                     for y in range(grid_y)]

    def _get_cell_or_raise(self, x: int, y: int) -> Cell:
        assert 0 <= x < self.dim.x
        assert 0 <= y < self.dim.y
        return self.grid[y][x]

    def __getitem__(self, coord_xy):
        x, y = coord_xy
        return self._get_cell_or_raise(x, y)

    def get_neighbours(self, x: int, y: int) -> List[int]:
        neighbours = []
        max_x = self.dim.x - 1
        max_y = self.dim.y - 1

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

    def set_cell_flagged(self, cell_x: int, cell_y: int, flagged: bool) -> None:
        self._get_cell_or_raise(cell_x, cell_y).is_flagged = flagged

    def set_cell_revealed(self, cell_x: int, cell_y: int, revealed: bool) -> None:
        self._get_cell_or_raise(cell_x, cell_y).is_revealed = revealed

    def get_cell_has_mine(self, cell_x: int, cell_y: int) -> bool:
        return self._get_cell_or_raise(cell_x, cell_y).has_mine

    def __iter__(self) -> Iterator[Cell]:
        return (cell for line in self.grid for cell in line)
