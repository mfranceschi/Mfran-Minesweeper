# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:45:05 2021

@author: Utilisateur
"""

import pytest
import grid_v1

def test_magic_number():
    assert grid_v1.Grid_V1().magic_number == 42
