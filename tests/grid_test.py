# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:45:05 2021

@author: Utilisateur
"""

from typing import List, Tuple
import pytest
from game_engine.grid import Cell, Grid


@pytest.fixture
def my_grid():
    return Grid(5, 7)


def test_dimensions(my_grid: Grid):
    assert my_grid.dim.x == 5
    assert my_grid.dim.y == 7


class TestGetNeighbours:
    @classmethod
    def check_list_of_cells(cls, list_to_review: List[Cell], cells_to_look_for: List[Tuple[int, int]], check_len: bool = True):
        if check_len:
            assert len(list_to_review) == len(cells_to_look_for), "Invalid amount of neighbours"
        
        for cell in cells_to_look_for:
            x, y = cell[0], cell[1]
            assert any(cell_from_list for cell_from_list in list_to_review if cell_from_list.x == x and cell_from_list.y == y), f"Unable to find cell of coordinates (x={x}, y={y}) within the list of neighbours"

    def test_raises_error_if_out_of_range(self, my_grid: Grid):
        # Negative values
        with pytest.raises(AssertionError):
            my_grid.get_neighbours(-1, 0)
        with pytest.raises(AssertionError):
            my_grid.get_neighbours(0, -1)
        with pytest.raises(AssertionError):
            my_grid.get_neighbours(-4, -4)
        
        # Equal to grid size
        with pytest.raises(AssertionError):
            my_grid.get_neighbours(my_grid.dim.x, 0)
        with pytest.raises(AssertionError):
            my_grid.get_neighbours(0, my_grid.dim.y)
        with pytest.raises(AssertionError):
            my_grid.get_neighbours(my_grid.dim.x, my_grid.dim.y)

        # More than grid size
        with pytest.raises(AssertionError):
            my_grid.get_neighbours(my_grid.dim.x + 1, 0)
        with pytest.raises(AssertionError):
            my_grid.get_neighbours(0, my_grid.dim.y + 1)
        with pytest.raises(AssertionError):
            my_grid.get_neighbours(my_grid.dim.x + 4, my_grid.dim.y + 4)

    def test_for_corners(self, my_grid: Grid):
        # Top left
        self.check_list_of_cells(my_grid.get_neighbours(0, 0), [(0, 1), (1, 0), (1, 1)])

        # Bottom left
        self.check_list_of_cells(my_grid.get_neighbours(0, 6), [(0, 5), (1, 6), (1, 5)])

        # Top right
        self.check_list_of_cells(my_grid.get_neighbours(4, 0), [(3, 0), (4, 1), (3, 1)])

        # Bottom right
        self.check_list_of_cells(my_grid.get_neighbours(4, 6), [(3, 6), (4, 5), (3, 6)])

    def test_for_sides(self, my_grid: Grid):
        # Top
        assert len(my_grid.get_neighbours(2, 0)) == 5

        # Left
        assert len(my_grid.get_neighbours(0, 2)) == 5

        # Bottom
        assert len(my_grid.get_neighbours(2, 6)) == 5

        # Right
        assert len(my_grid.get_neighbours(4, 2)) == 5

    def test_all_other_cells(self, my_grid: Grid):
        for x in range(1, my_grid.dim.x - 1):
            for y in range(1, my_grid.dim.y - 1):
                assert len(my_grid.get_neighbours(x,y)) == 8


def test_subscript(my_grid):
    my_cell = my_grid[1, 2]
    assert my_cell.x == 1
    assert my_cell.y == 2
