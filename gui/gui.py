from typing import Callable


class GUI:
    def set_grid(self, *args, **kwargs):
        raise NotImplementedError()

    def set_on_new_game(self, function: Callable[[], None]):
        raise NotImplementedError()
