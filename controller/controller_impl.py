from game_engine.fill_grid import RandomGridFiller
from gui.gui import GUI
from controller.controller import Controller, DifficultyLevel, DifficultyLevels
from enum import Enum
from typing import Optional, Union
from game_engine.gridmanager import GridManager
from overrides import overrides


class ControllerImpl(Controller):
    INITIAL_DIFFICULTY = DifficultyLevels.EASY

    def __init__(self) -> None:
        self.gui: GUI = None
        self.difficulty: DifficultyLevel
        self.game_over: bool = False
        self.set_difficulty(self.INITIAL_DIFFICULTY.value)

    def set_difficulty(self, level: DifficultyLevel):
        self.difficulty = level

    @overrides
    def init_gui(self, gui: GUI) -> None:
        self.gui = gui
        self.on_new_game()

    @overrides
    def on_left_click(self, x: int, y: int) -> None:
        self.grid_manager.reveal_cell(x, y)
        if self.grid_manager.get_cell_has_mine(x, y):
            self.game_over = True
            self.gui.set_grid(self.grid_manager.reveal_all())
            self.gui.game_over()
        else:
            self.gui.set_grid(self.grid_manager.get_grid_for_display())
            if self.has_won():
                self.gui.set_grid(self.grid_manager.reveal_all())
                self.gui.victory()

    @overrides
    def on_right_click(self, x: int, y: int) -> None:
        self.grid_manager.toggle_flag_cell(x, y)
        self.gui.set_grid(self.grid_manager.get_grid_for_display())

    @overrides
    def on_new_game(self, difficulty_level: Optional[DifficultyLevel] = None) -> None:
        if difficulty_level:
            self.set_difficulty(difficulty_level)

        grid_x = self.difficulty.grid_x
        grid_y = self.difficulty.grid_y
        nbr_mines = self.difficulty.nbr_mines

        self.grid_manager = GridManager(grid_x, grid_y)
        self.grid_manager.fill_with_mines(
            nbr_mines=nbr_mines,
            procedure=RandomGridFiller(grid_x, grid_y)
        )
        self.gui.reset_grid_size(grid_x, grid_y)
        self.gui.set_grid(self.grid_manager.get_grid_for_display())

    def has_won(self) -> bool:
        has_won = self.difficulty.nbr_mines == self.grid_manager.get_count_of_not_revealed_cells()
        return has_won

    @overrides
    def get_nbr_mines(self) -> int:
        return self.difficulty.nbr_mines
