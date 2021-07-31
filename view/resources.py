
from functools import cache
import pathlib
from tkinter import PhotoImage
from typing import Union


@cache
def get_flag_icon() -> Union[PhotoImage, str]:
    return PhotoImage(
        file=(pathlib.Path(".").parent / "resources" / "flag.png").resolve(),
        width=22, height=22
    )


@cache
def get_mine_icon() -> Union[PhotoImage, str]:
    return PhotoImage(
        file=(pathlib.Path(".").parent / "resources" / "mine.png").resolve(),
        width=22, height=22
    )


@cache
def get_no_icon() -> Union[PhotoImage, str]:
    return ""
