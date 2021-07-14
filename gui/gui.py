from typing import Any, Callable, List


class GUI:
    def reset_grid_size(self, grid_x: int, grid_y: int) -> None:
        raise NotImplementedError()

    def set_grid(self, grid: List[str]) -> None:
        raise NotImplementedError()

    def victory(self) -> None:
        raise NotImplementedError()

    def game_over(self) -> None:
        raise NotImplementedError()
