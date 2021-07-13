import tkinter as tk
from typing import Callable


class ControlsWidget(tk.Frame):
    def __init__(self, on_new_game: Callable[[], None] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_new_game = on_new_game or (lambda: print("new game"))
        self.configure(padx=15, pady=15, background="white")

        self.new_game_button = tk.Button(
            master=self, background="yellow", text="New game", command=self.on_new_game)
        self.new_game_button.grid(row=0, column=0)
