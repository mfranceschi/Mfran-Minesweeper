from .gui import GUI
from .controls import ControlsWidget
from controller.controller import Controller
from typing import Callable, List
from .grid import MinesweeperGridWidget
import tkinter as tk


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
        self.root.title("Mfran Minesweeper!")

        self.top_frame = tk.Frame(master=self.root, height=50,
                                  width=WIN_WIDTH, bg="yellow")
        self.top_frame.pack(fill=tk.X)

        self.grid_frame = MinesweeperGridWidget(
            master=self.root,
            height=WIN_WIDTH,
            bg="red",

            size_x=grid_x,
            size_y=grid_y,
            on_left_click=self.on_left_click_on_cell,
            on_right_click=self.on_right_click_on_cell
        )
        self.grid_frame.pack(fill=tk.X)

        self.bottom_frame = ControlsWidget(
            master=self.root, height=30, bg="blue")
        self.bottom_frame.pack(fill=tk.X)

    def set_grid(self, grid: List[str]) -> None:
        self.grid_frame.set_grid(grid)

    def on_left_click_on_cell(self, x, y):
        self.controller.on_left_click(x, y)

    def on_right_click_on_cell(self, x, y):
        self.controller.on_right_click(x, y)

    def set_on_new_game(self, function: Callable[[], None]):
        self.bottom_frame.new_game_button.configure(command=function)
