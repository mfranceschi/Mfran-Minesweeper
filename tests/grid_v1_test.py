# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:45:05 2021

@author: Utilisateur
"""

import pytest
from game_engine.grid_v1 import Grid_V1

def test_game_is_running():
    assert Grid_V1().game_is_running == False
