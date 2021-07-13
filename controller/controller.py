from controller.abstract_controller import AbstractController
from enum import Enum
from typing import List
from game_engine.gridmanager import GridManager


class DifficultyLevel:
    def __init__(self, nbr_mines: int, grid_x: int, grid_y: int) -> None:
        self.nbr_mines = nbr_mines
        self.grid_x = grid_x
        self.grid_y = grid_y


class DifficultyLevels(Enum):
    EASY = DifficultyLevel(nbr_mines=10, grid_x=10, grid_y=15)


class Controller(AbstractController):
    INITIAL_DIFFICULTY = DifficultyLevels.EASY

    def __init__(self) -> None:
        self.main_window = None
        self.set_difficulty(self.INITIAL_DIFFICULTY.value)
        self.game_over = False

    def set_difficulty(self, level: DifficultyLevel):
        self.difficulty = level
        print(level)
        self.grid_manager = GridManager(level.grid_x, level.grid_y)

    def init_gui(self, gui) -> None:
        self.main_window = gui
        self.grid_manager

    def on_left_click(self, x: int, y: int) -> List[str]:
        self.grid_manager.reveal_cell(x, y)
        if self.grid_manager.get_cell_has_mine(x, y):
            self.game_over = True
            return self.grid_manager.reveal_all()
        else:
            return self.grid_manager.get_grid_for_display()

    def on_right_click(self, x: int, y: int) -> List[str]:
        self.grid_manager.toggle_flag_cell(x, y)
        return self.grid_manager.get_grid_for_display()

    def on_new_game(self) -> List[str]:
        self.grid_manager = GridManager(
            self.difficulty.grid_x, self.difficulty.grid_y)
        return self.grid_manager.get_grid_for_display()
