from typing import List


class AbstractController:
    def init_gui(self, gui) -> None:
        raise NotImplementedError()

    def on_left_click(self, x: int, y: int) -> List[str]:
        raise NotImplementedError()

    def on_right_click(self, x: int, y: int) -> List[str]:
        raise NotImplementedError()
