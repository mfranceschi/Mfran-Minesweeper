from game_engine.fill_grid import RandomGridFiller
from gui.gui import GUI
from controller.controller import Controller
from enum import Enum
from typing import Union
from game_engine.gridmanager import GridManager


class DifficultyLevel:
    def __init__(self, nbr_mines: int, grid_x: int, grid_y: int) -> None:
        self.nbr_mines = nbr_mines
        self.grid_x = grid_x
        self.grid_y = grid_y


class DifficultyLevels(Enum):
    EASY = DifficultyLevel(nbr_mines=10, grid_x=10, grid_y=15)


class ControllerImpl(Controller):
    INITIAL_DIFFICULTY = DifficultyLevels.EASY

    def __init__(self) -> None:
        self.main_window: GUI = None
        self.difficulty: DifficultyLevel
        self.game_over: bool = False
        self.set_difficulty(self.INITIAL_DIFFICULTY.value)

    def set_difficulty(self, level: Union[DifficultyLevel, None] = None):
        self.difficulty = level or self.difficulty

    def init_gui(self, gui: GUI) -> None:
        self.main_window = gui
        self.main_window.set_on_new_game(self.on_new_game)
        self.on_new_game()

    def on_left_click(self, x: int, y: int) -> None:
        self.grid_manager.reveal_cell(x, y)
        if self.grid_manager.get_cell_has_mine(x, y):
            self.game_over = True
            self.main_window.set_grid(self.grid_manager.reveal_all())
        else:
            self.main_window.set_grid(self.grid_manager.get_grid_for_display())

    def on_right_click(self, x: int, y: int) -> None:
        self.grid_manager.toggle_flag_cell(x, y)
        self.main_window.set_grid(self.grid_manager.get_grid_for_display())

    def on_new_game(self) -> None:
        self.grid_manager = GridManager(
            self.difficulty.grid_x, self.difficulty.grid_y)
        self.grid_manager.fill_with_mines(
            nbr_mines=self.difficulty.nbr_mines, procedure=RandomGridFiller(self.difficulty.grid_x, self.difficulty.grid_y))
        self.main_window.set_grid(self.grid_manager.get_grid_for_display())
