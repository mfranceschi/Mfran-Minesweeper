from typing import Callable, Set, Tuple
import random

from overrides.overrides import overrides


def fill_grid_dummy(function: Callable[[int, int], None], nbr_mines: int) -> None:
    """
    Fills the first line with mines. Fails if it results in too many mines!
    """
    x_cell = 0
    y_cell = 0
    for __ in range(nbr_mines):
        try:
            function(x_cell, y_cell)
            x_cell += 1
        except AssertionError:
            x_cell = 0
            y_cell += 1
            function(x_cell, y_cell)
            x_cell += 1


class RandomGridFiller:
    """
    Call my constructor with the grid size.
    My call method randomly fills the grid with no duplicates.
    """

    def __init__(self, grid_x: int, grid_y: int) -> None:
        self.grid_x = grid_x
        self.grid_y = grid_y

    def make_new_random_position(self) -> Tuple[int, int]:
        return (random.randint(0, self.grid_x - 1),
                random.randint(0, self.grid_y - 1))

    def make_position(self, known_positions: Set[Tuple[int, int]]) -> Tuple[int, int]:
        position = self.make_new_random_position()
        while position in known_positions:
            position = self.make_new_random_position()
        known_positions.add(position)
        return position

    @overrides
    def __call__(self, place_mine: Callable[[int, int], None], nbr_mines: int) -> None:
        placed_mines: Set[Tuple[int, int]] = set()

        for __ in range(nbr_mines):
            place_mine(*self.make_position(placed_mines))
