from typing import List


class GUI:
    """
    Interface for some controller to send and display information and data.
    """

    def reset_grid_size(self, grid_x: int, grid_y: int) -> None:
        raise NotImplementedError()

    def set_nbr_mines(self, nbr_mines: int) -> None:
        raise NotImplementedError()

    def set_grid(self, grid: List[str]) -> None:
        raise NotImplementedError()

    def victory(self) -> None:
        raise NotImplementedError()

    def game_over(self) -> None:
        raise NotImplementedError()

    def game_starts(self) -> None:
        raise NotImplementedError()
