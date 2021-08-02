
from functools import cache
import pathlib
from tkinter import PhotoImage
from typing import Union

_flag_icon_path: str = pathlib.Path(
    (pathlib.Path(".").parent / "resources" / "flag.png").resolve())
_mine_icon_path: str = pathlib.Path(
    (pathlib.Path(".").parent / "resources" / "mine.png").resolve())


@cache
def get_flag_icon() -> Union[PhotoImage, str]:
    return PhotoImage(
        file=_flag_icon_path,
        width=22, height=22
    )


@cache
def get_mine_icon() -> Union[PhotoImage, str]:
    return PhotoImage(
        file=_mine_icon_path,
        width=22, height=22
    )


@cache
def get_no_icon() -> Union[PhotoImage, str]:
    return ""
