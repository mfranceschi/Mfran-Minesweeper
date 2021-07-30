import tkinter as tk
from typing import List

from overrides import overrides

from controller.controller import Controller
from model.utils import Point2D
from .controls import ControlsWidget
from .grid_view import GridView
from .gui import CellValue, GUI

WIN_WIDTH = 500


class GUIImpl(GUI):
    """
    Actual implementation of the GUI.
    """

    def __init__(
            self,
            grid_dim: Point2D,
            controller: Controller
    ) -> None:
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Mfranceschi Minesweeper!")

        self.elapsed_time_text = tk.StringVar(master=self.root, value="")
        self._update_elapsed_time_text()

        self.make_controls_widget()

        self.make_grid_view(dim=grid_dim)

    @overrides
    def set_grid(self, grid: List[CellValue]) -> None:
        self.grid_view.set_grid(grid)

    def on_left_click_on_cell(self, cell_coord: Point2D):
        self.controller.on_left_click(cell_coord)

    def on_right_click_on_cell(self, cell_coord: Point2D):
        self.controller.on_right_click(cell_coord)

    def _update_elapsed_time_text(self):
        elapsed_seconds = self.controller.get_current_game_time()
        minutes, seconds = divmod(int(elapsed_seconds), 60)
        self.elapsed_time_text.set(
            f"Elapsed time: {f'{minutes}min ' if minutes else ''}{seconds}s")
        self.root.after(800, self._update_elapsed_time_text)

    @overrides
    def reset_grid_size(self, grid_dim: Point2D) -> None:
        self.grid_view.destroy()
        self.make_grid_view(dim=grid_dim)

    @overrides
    def set_nbr_mines(self, nbr_mines: int) -> None:
        # TODO USE TK VARIABLE
        self.controls_widget.set_nbr_mines(nbr_mines)

    @overrides
    def victory(self) -> None:
        self.root.configure(bg="green")

    @overrides
    def game_over(self) -> None:
        self.root.configure(bg="brown")

    @overrides
    def game_starts(self) -> None:
        self.root.configure(bg="sky blue")

    def make_grid_view(self, dim: Point2D) -> GridView:
        self.grid_view = GridView(
            master=self.root,
            height=WIN_WIDTH,
            bg="red",

            size_x=dim.x,
            size_y=dim.y,
            on_left_click=self.on_left_click_on_cell,
            on_right_click=self.on_right_click_on_cell,
        )
        self.grid_view.grid(column=1, row=0)

    def make_controls_widget(self) -> ControlsWidget:
        self.controls_widget = ControlsWidget(
            master=self.root,
            height=30,
            bg="blue",

            controller=self.controller,
            elapsed_time_text=self.elapsed_time_text,
        )
        self.controls_widget.grid(column=0, row=0)
