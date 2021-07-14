from typing import Callable, Set, Tuple
import random


def fill_grid_dummy(function: Callable[[int, int], None], nbr_mines: int) -> None:
    """
    Fills the first line with mines. Fails if it results in too many mines!
    """
    x_cell = 0
    y_cell = 0
    for i_cell in range(nbr_mines):
        try:
            function(x_cell, y_cell)
            x_cell += 1
        except:
            x_cell = 0
            y_cell += 1
            function(x_cell, y_cell)
            x_cell += 1


class RandomGridFiller:
    def __init__(self, grid_x: int, grid_y: int) -> None:
        self.grid_x = grid_x
        self.grid_y = grid_y

    def make_new_position(self) -> Tuple[int, int]:
        return (random.randint(0, self.grid_x - 1),
                random.randint(0, self.grid_y - 1))

    def __call__(self, place_mine: Callable[[int, int], None], nbr_mines: int) -> None:
        placed_mines: Set[Tuple[int, int]] = set()

        for i_mine in range(nbr_mines):
            position = self.make_new_position()
            while position in placed_mines:
                position = self.make_new_position()
            place_mine(*position)
