import tkinter as tk
from typing import Any, Callable, Dict

from model.utils import Point2D
from view.gui import CellValue, CellValueAsString


class MyDefaultDict(dict):
    """
    Helper class: like defaultdict but the factory takes the key as argument.
    """

    def __init__(self, factory: Callable[[Any], Any], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.missing_factory = factory

    def __missing__(self, key):
        return self.missing_factory(key)


def get_configure_contents_for_revealed_with_neighbours(cell_value):
    return {"state": "disabled", "text": str(cell_value), "bg": "white"}


WIDGET_CONFIGURE_CONTENTS: Dict[CellValue, dict] = MyDefaultDict(
    get_configure_contents_for_revealed_with_neighbours,
    {
        CellValueAsString.FLAGGED.value: {"state": "disabled", "text": " ", "bg": "yellow"},
        CellValueAsString.MINE.value: {"state": "normal", "text": " ", "bg": "red"},
        CellValueAsString.REVEALED_ZERO_NEIGHBOUR.value: {
            "state": "normal", "text": " ", "bg": "grey"},
        CellValueAsString.NOT_REVEALED.value: {"state": "disabled", "text": " ", "bg": "blue"},
    }
)


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
        data = WIDGET_CONFIGURE_CONTENTS[cell_value]
        self.widget.configure(**data)
