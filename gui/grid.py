import tkinter as tk
from functools import partial
from typing import Callable, List


class MinesweeperGridWidget(tk.Frame):
    def __init__(
            self,
            size_x=5, size_y=5,
            on_click: Callable[[int, int], None] = None,
            *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.size_x = size_x
        self.size_y = size_y
        self.on_click = on_click

        self.grid_to_display: List[str] = ["0"] * (size_x * size_y)
        self.buttons: List[tk.Button] = [None] * len(self.grid_to_display)

        for y in range(self.size_y):
            for x in range(self.size_x):
                button = tk.Button(
                    master=self,
                    text=self._get_at_index(x, y, self.grid_to_display),
                    bg="purple",
                    command=partial(self.on_click, x, y)
                )
                button.grid(row=y, column=x)
                self._set_at_index(x, y, self.buttons, button)

    def _get_at_index(self, x: int, y: int, array: list):
        return array[y * self.size_x + x]

    def _set_at_index(self, x: int, y: int, array: list, value):
        array[y * self.size_x + x] = value

    def handle_button_click(self, x, y):
        print(f"CLICK {x=} {y=}")
        button = self._get_at_index(x, y, self.buttons)
        button.configure(
            bg="purple" if button["background"] == "yellow" else "yellow")

    def set_grid(self, grid: List[str]) -> None:
        for i, value in enumerate(grid):
            self.buttons[i].configure(text=value)
