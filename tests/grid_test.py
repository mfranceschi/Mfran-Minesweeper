# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:45:05 2021

@author: Utilisateur
"""

import pytest
from game_engine.grid import Grid

def test_dimensions():
    my_grid = Grid(5, 7)
    assert my_grid.dim.x == 5
    assert my_grid.dim.y == 7

def test_get_neighbours_corners():
    my_grid = Grid(5, 7)
    assert len(my_grid.get_neighbours(0, 0)) == 3
    assert len(my_grid.get_neighbours(0, 6)) == 3
    assert len(my_grid.get_neighbours(4, 0)) == 3
    assert len(my_grid.get_neighbours(4, 6)) == 3

def test_subscript():
    my_grid = Grid(3, 6)
    my_cell = my_grid[1, 2]
    assert my_cell.x == 1
    assert my_cell.y == 2
