from time import time
from typing import Optional

from overrides import overrides

from ..model.fill_grid import RandomGridFiller
from ..model.utils import Point2D
from ..utils.action_on_close import do_after
from ..view.gui import GUI

from .controller import Controller, DifficultyLevel, DifficultyLevels
from .game import Game


class ControllerImpl(Controller):
    """
    Actual implementation of a controller.
    Initial difficulty is easy.
    """

    INITIAL_DIFFICULTY = DifficultyLevels.EASY

    def __init__(self) -> None:
        self.gui: GUI
        self.game = Game(difficulty=self.INITIAL_DIFFICULTY.value)

        self.game.start_game()

    def set_difficulty(self, level: DifficultyLevel):
        self.game.difficulty = level

    @overrides
    def init_gui(self, gui: GUI) -> None:
        self.gui = gui
        self.on_new_game()

    @overrides
    def on_left_click(self, cell_coord: Point2D) -> None:
        with do_after(self._update_gui):
            if self.game.reveal_cell_if_possible(cell_coord):
                self._check_victory_or_defeat(cell_coord)

    def _check_victory_or_defeat(self, clicked_cell: Point2D):
        if self.game.check_cell_has_mine(clicked_cell):
            self.game.stop_game()
            self.gui.game_over()
        elif self.game.is_won():
            self.game.stop_game()
            self.gui.victory()

    @overrides
    def on_right_click(self, cell_coord: Point2D) -> None:
        with do_after(self._update_gui):
            self.game.toggle_flag_if_possible(cell_coord)

    @overrides
    def on_new_game(self, difficulty: Optional[DifficultyLevel] = None) -> None:
        if not difficulty:
            difficulty = self.game.difficulty

        self.game = Game(difficulty=difficulty)
        self.game.reset_grid(
            fill_grid_procedure=RandomGridFiller(
                grid_dim=difficulty.grid_dim,
                nbr_mines=difficulty.nbr_mines))
        grid_dim = self.game.difficulty.grid_dim
        nbr_mines = self.game.difficulty.nbr_mines

        self.gui.reset_grid_size(grid_dim)
        self.gui.set_nbr_mines(nbr_mines)
        self._update_gui()
        self.game.start_game()
        self.gui.game_starts()

    @ overrides
    def get_nbr_mines(self) -> int:
        return self.game.nbr_mines

    @ overrides
    def get_current_game_time(self) -> float:
        if self.game is not None:
            if self.game.game_is_running:
                return time() - self.game.game_starting_time
            else:
                return self.game.game_ending_time - self.game.game_starting_time
        else:
            return 0.

    def _update_gui(self) -> None:
        self.gui.set_grid(self.game.grid_for_display)
