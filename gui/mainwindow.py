from game_engine.gameengine import GameEngine
from typing import List
from .grid import MinesweeperGridWidget
import tkinter as tk


WIN_WIDTH = 500


class MainWindow():
    def __init__(self, grid_x: int, grid_y: int,
                 game_engine: GameEngine = None,) -> None:
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.game_engine = game_engine

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
            on_click=self.on_click_on_cell
        )
        self.grid_frame.pack(fill=tk.X)

        self.bottom_frame = tk.Frame(master=self.root, height=30, bg="blue")
        self.bottom_frame.pack(fill=tk.X)

    def set_grid(self, grid: List[str]) -> None:
        self.grid_frame.set_grid(grid)

    def on_click_on_cell(self, x, y):
        self.game_engine.reveal_cell(x, y)
        self.set_grid(self.game_engine.get_grid_for_display())


if __name__ == "__main__":
    MainWindow().root.mainloop()
