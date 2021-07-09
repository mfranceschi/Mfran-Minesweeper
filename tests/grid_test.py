# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:45:05 2021

@author: Utilisateur
"""

import pytest
from game_engine.grid import Grid


@pytest.fixture
def my_grid():
    return Grid(5, 7)


def test_dimensions(my_grid: Grid):
    assert my_grid.dim.x == 5
    assert my_grid.dim.y == 7


class TestGetNeighbours:
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


    def test_for_corners(self, my_grid):
        # Top left
        assert len(my_grid.get_neighbours(0, 0)) == 3

        # Bottom left
        assert len(my_grid.get_neighbours(0, 6)) == 3

        # Top right
        assert len(my_grid.get_neighbours(4, 0)) == 3

        # Bottom right
        assert len(my_grid.get_neighbours(4, 6)) == 3


    def test_for_sides(self, my_grid):
        # Top
        assert len(my_grid.get_neighbours(2, 0)) == 5

        # Left
        assert len(my_grid.get_neighbours(0, 2)) == 5

        # Bottom
        assert len(my_grid.get_neighbours(2, 6)) == 5

        # Right
        assert len(my_grid.get_neighbours(4, 2)) == 5


def test_subscript(my_grid):
    my_cell = my_grid[1, 2]
    assert my_cell.x == 1
    assert my_cell.y == 2
