import tkinter as tk
from functools import partial
from typing import Callable, List


class MinesweeperGridView(tk.Frame):
    def __init__(
            self,
            size_x=5, size_y=5,
            on_left_click: Callable[[int, int], None] = None,
            on_right_click: Callable[[int, int], None] = None,
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
        self.buttons: List[tk.Button] = [None] * len(self.grid_to_display)

        for row_index in range(self.size_y):
            for column_index in range(self.size_x):
                button = tk.Button(
                    master=self,
                    text=self._get_at_index(
                        column_index, row_index, self.grid_to_display),
                    bg="purple",
                    # command=partial(self.on_left_click, x, y)
                )
                button.bind("<ButtonRelease>", partial(
                    self.handle_button_event, column_index, row_index))
                button.grid(row=row_index, column=column_index, sticky="nsew")
                self._set_at_index(column_index, row_index,
                                   self.buttons, button)

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
            self._render_button(self.buttons[i], value)

    @staticmethod
    def _render_button(button: tk.Button, value: str):
        if value == "0":
            # Revealed, no neighbour
            button.configure(bg="grey", text=" ", state="disabled")
        elif value == "F":
            # Not revealed, flag
            button.configure(bg="yellow", text=" ", state="normal")
        elif value == "M":
            # Revealed, mine
            button.configure(bg="red", text=" ", state="disabled")
        elif value == " ":
            # Not revealed, no flag
            button.configure(bg="blue", text=" ", state="normal")
        else:
            # Revealed, has neighbours
            button.configure(bg='white', text=value, state="disabled")
