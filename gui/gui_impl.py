from .gui import GUI
from .controls import ControlsWidget
from controller.controller import Controller
from typing import Callable, List
from .grid import MinesweeperGridWidget
import tkinter as tk
from overrides import overrides
import time

WIN_WIDTH = 500


class GUIImpl(GUI):
    def __init__(
            self,
            grid_x: int, grid_y: int,
            controller: Controller = None,) -> None:
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Mfranceschi Minesweeper!")

        self.grid_frame = self._make_grid_widget(grid_x, grid_y)

        self.elapsed_time_text = tk.StringVar(
            master=self.root, value="")
        self._update_elapsed_time_text()
        self.bottom_frame = ControlsWidget(
            master=self.root,
            controller=self.controller,
            elapsed_time_text=self.elapsed_time_text,
            height=30,
            bg="blue"
        )
        self.bottom_frame.grid(column=0, row=1)

    @overrides
    def set_grid(self, grid: List[str]) -> None:
        self.grid_frame.set_grid(grid)

    def on_left_click_on_cell(self, x, y):
        self.controller.on_left_click(x, y)

    def on_right_click_on_cell(self, x, y):
        self.controller.on_right_click(x, y)

    def _make_grid_widget(self, grid_x: int, grid_y: int) -> MinesweeperGridWidget:
        widget = MinesweeperGridWidget(
            master=self.root,
            height=WIN_WIDTH,
            bg="red",

            size_x=grid_x,
            size_y=grid_y,
            on_left_click=self.on_left_click_on_cell,
            on_right_click=self.on_right_click_on_cell
        )
        widget.grid(column=0, row=0)
        return widget

    def _update_elapsed_time_text(self):
        elapsed_seconds = time.time() - self.controller.get_game_starting_time()
        minutes, seconds = divmod(int(elapsed_seconds), 60)
        self.elapsed_time_text.set(
            f"Elapsed time: {f'{minutes}min ' if minutes else ''}{seconds}s")
        self.root.after(800, self._update_elapsed_time_text)

    @overrides
    def reset_grid_size(self, grid_x: int, grid_y: int) -> None:
        old_grid = self.grid_frame
        self.grid_frame = self._make_grid_widget(grid_x, grid_y)
        old_grid.grid_forget()

    @overrides
    def set_nbr_mines(self, nbr_mines: int) -> None:
        self.bottom_frame.set_nbr_mines(nbr_mines)

    @overrides
    def victory(self) -> None:
        self.root.configure(bg="green")

    @overrides
    def game_over(self) -> None:
        self.root.configure(bg="brown")

    @overrides
    def game_starts(self) -> None:
        self.root.configure(bg="sky blue")
