from controller.controller import Controller, DifficultyLevel, DifficultyLevels
import tkinter as tk
from typing import Callable


class NewGameButton(tk.Button):
    def __init__(self, master, command, *args, **kwargs):
        super().__init__(master=master, command=command,
                         background="yellow", *args, **kwargs)
        self.grid(row=0, column=0, columnspan=2)


class NbrMinesLabel(tk.Label):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.grid(row=0, column=2, padx=20)
        pass

    def _make_string_for_nbr_mines(self, nbr: int) -> str:
        return f"There are {nbr} mines!"

    def set_nbr_mines(self, nbr: int) -> None:
        self.configure(text=self._make_string_for_nbr_mines(nbr))


class DifficultyChoice(tk.Frame):
    def __init__(self, master, on_new_difficulty: Callable[[DifficultyLevel], None], *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.on_new_difficulty = on_new_difficulty
        self.grid(row=0, column=3, padx=20)

        self.listbox = tk.Listbox(
            master=self, selectmode=tk.SINGLE, width=0, height=0)
        choices = [x.name.title() for x in DifficultyLevels]
        self.listbox.insert(tk.END, *choices)
        self.listbox.selection_anchor(0)
        self.listbox.pack()

        self.ok_button = tk.Button(
            master=self, text="OK (new game)", command=self._handle_ok)
        self.ok_button.pack()

    def _handle_ok(self):
        choice: str = str(self.listbox.get(tk.ANCHOR)).upper()
        assert choice in DifficultyLevels.__dict__.keys()
        self.on_new_difficulty(getattr(DifficultyLevels, choice).value)


class ControlsWidget(tk.Frame):
    def __init__(self, controller: Controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(padx=15, pady=15, background="white")

        self.new_game_button = NewGameButton(
            master=self, command=controller.on_new_game, text="New game")

        self.nbr_mines_label = NbrMinesLabel(master=self)
        self.nbr_mines_label.set_nbr_mines(controller.get_nbr_mines())

        self.difficulty_choice = DifficultyChoice(
            master=self, on_new_difficulty=controller.on_new_game)

    def set_nbr_mines(self, nbr: int) -> None:
        self.nbr_mines_label.configure(
            text=self._make_string_for_nbr_mines(nbr))
