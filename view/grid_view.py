import tkinter as tk
from typing import Callable, List
from view.gui import CellValue, CellValueAsString

from model.utils import Point2D


class GridView(tk.Frame):
    """
    Renders a grid and intercepts user clicks on cells.
    """

    def __init__(
            self,
            size_x: int = 5, size_y: int = 5,
            on_left_click: Callable[[Point2D], None] = None,
            on_right_click: Callable[[Point2D], None] = None,
            **kwargs) -> None:
        super().__init__(**kwargs)
        self.size_x = size_x
        self.size_y = size_y
        self.on_left_click = on_left_click
        self.on_right_click = on_right_click

        for row_index in range(self.size_y):
            self.rowconfigure(row_index, minsize=25, weight=1)
        for column_index in range(self.size_x):
            self.columnconfigure(column_index, minsize=25, weight=1)

        self.grid_to_display: List[str] = ["0"] * (size_x * size_y)
        self.buttons: List[CellView] = [None] * len(self.grid_to_display)

        for row_index in range(self.size_y):
            for column_index in range(self.size_x):
                coord = Point2D(x=column_index, y=row_index)

                button = CellView(
                    cell_coord=coord,
                    master=self,
                    on_left_click=self.on_left_click,
                    on_right_click=self.on_right_click)
                button.widget.grid(
                    row=row_index, column=column_index, sticky="nsew")
                self.buttons[self._index_of_point(coord)] = button

    def _index_of_point(self, point: Point2D) -> int:
        return point.y * self.size_x + point.x

    def set_grid(self, grid: List[CellValue]) -> None:
        for i, value in enumerate(grid):
            self.buttons[i].set_cell_value(value)


class CellView:
    """
    Wrapper class: configures a cell button.
    When the cell updates please set the "cell_value" string.
    """

    def __init__(
            self,
            cell_coord: Point2D,
            master: tk.Widget,
            on_left_click: Callable[[Point2D], None],
            on_right_click: Callable[[Point2D], None]
    ):
        self.widget = tk.Button(master=master)
        self.cell_coord = cell_coord
        self.on_left_click = on_left_click
        self.on_right_click = on_right_click
        self.set_cell_value(CellValueAsString.NOT_REVEALED)

        self.widget.bind("<ButtonRelease>", self.handle_button_event)

    def handle_button_event(self, event: tk.Event):
        if event.num == 1:
            # Left click
            self.on_left_click(self.cell_coord)
        elif event.num == 2 or event.num == 3:
            # Middle or right click
            self.on_right_click(self.cell_coord)

    def set_cell_value(self, cell_value: CellValue) -> None:
        state = "disabled" if cell_value == CellValueAsString.FLAGGED.value or CellValueAsString.NOT_REVEALED.value else "normal"
        text = " " if isinstance(cell_value, str) else str(cell_value)
        colour = {
            CellValueAsString.FLAGGED.value: "yellow",
            CellValueAsString.MINE.value: "red",
            CellValueAsString.REVEALED_ZERO_NEIGHBOUR.value: "grey",
            CellValueAsString.NOT_REVEALED.value: "blue",
        }.get(cell_value, "white")

        self.widget.configure(bg=colour, state=state, text=text)

        if cell_value == "0":
            # Revealed, no neighbour
            self.widget.configure(bg="grey", text=" ", state="disabled")

        elif cell_value == "F":
            # Not revealed, flag
            self.widget.configure(bg="yellow", text=" ", state="normal")

        elif cell_value == "M":
            # Revealed, mine
            self.widget.configure(bg="red", text=" ", state="disabled")

        elif cell_value == " ":
            # Not revealed, no flag
            self.widget.configure(bg="blue", text=" ", state="normal")

        else:
            # Revealed, has neighbours
            self.widget.configure(
                bg='white', text=cell_value, state="disabled")
