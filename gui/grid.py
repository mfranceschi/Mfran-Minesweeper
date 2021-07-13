import tkinter as tk
from functools import partial
from tkinter.constants import E
from typing import Callable, List


class MinesweeperGridWidget(tk.Frame):
    def __init__(
            self,
            size_x=5, size_y=5,
            on_left_click: Callable[[int, int], None] = None,
            on_right_click: Callable[[int, int], None] = None,
            *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.size_x = size_x
        self.size_y = size_y
        self.on_left_click = on_left_click
        self.on_right_click = on_right_click

        for y in range(self.size_y):
            self.rowconfigure(y, minsize=25, weight=1)
        for x in range(self.size_x):
            self.columnconfigure(x, minsize=25, weight=1)

        self.grid_to_display: List[str] = ["0"] * (size_x * size_y)
        self.buttons: List[tk.Button] = [None] * len(self.grid_to_display)

        for y in range(self.size_y):
            for x in range(self.size_x):
                button = tk.Button(
                    master=self,
                    text=self._get_at_index(x, y, self.grid_to_display),
                    bg="purple",
                    # command=partial(self.on_left_click, x, y)
                )
                button.bind("<ButtonRelease>", partial(
                    self.handle_button_event, x, y))
                button.grid(row=y, column=x, sticky="nsew")
                self._set_at_index(x, y, self.buttons, button)

    def _get_at_index(self, x: int, y: int, array: list):
        return array[y * self.size_x + x]

    def _set_at_index(self, x: int, y: int, array: list, value):
        array[y * self.size_x + x] = value

    def handle_button_event(self, x: int, y: int, event: tk.Event):
        if event.num == 1:
            # Left click
            self.on_left_click(x, y)
        elif event.num == 2 or event.num == 3:
            # Middle or right click
            self.on_right_click(x, y)
        print(f"CLICK {event=} {x=} {y=}")

    def set_grid(self, grid: List[str]) -> None:
        for i, value in enumerate(grid):
            b = self.buttons[i]
            if value == "0":
                b.configure(bg="grey", text=" ", state="disabled")
            elif value == "F":
                b.configure(bg="yellow", text=" ")
            elif value == "M":
                b.configure(bg="red", text=" ")
            else:
                b.configure(bg='purple', text=value, state="normal")
