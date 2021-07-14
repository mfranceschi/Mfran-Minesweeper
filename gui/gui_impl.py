from .gui import GUI
from .controls import ControlsWidget
from controller.controller import Controller
from typing import Callable, List
from .grid import MinesweeperGridWidget
import tkinter as tk
from overrides import overrides

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

        self.bottom_frame = ControlsWidget(
            master=self.root,
            controller=self.controller,
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

    @overrides
    def reset_grid_size(self, grid_x: int, grid_y: int) -> None:
        self.grid_frame = self._make_grid_widget(grid_x, grid_y)
