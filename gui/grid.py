import tkinter as tk
from functools import partial
from typing import List, Tuple, Union


class MinesweeperGridWidget(tk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.grid_to_display: List[List[Union[int, str]]] = [
            [0, 0, 0, ],
            [1, 2, 1, ],
            ["BOMB", 2, "BOMB"],
        ]
        self.buttons: List[List[tk.Button]] = []

        for y, line in enumerate(self.grid_to_display):
            self.buttons.append([])
            for x, cell in enumerate(line):
                button = tk.Button(master=self, text=str(
                    cell), bg="purple", command=partial(handle_button_click, self, x, y))
                button.grid(row=y, column=x)
                self.buttons[y].append(button)


def handle_button_click(frame: MinesweeperGridWidget, x, y):
    print(f"CLICK {x=} {y=}")
    button = frame.buttons[y][x]
    button.configure(
        bg="purple" if button["background"] == "yellow" else "yellow")
