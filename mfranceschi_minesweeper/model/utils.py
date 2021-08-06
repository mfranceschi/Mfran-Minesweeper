from dataclasses import dataclass
import functools
import sys


@dataclass(frozen=True)
class Point2D:
    """
    2D coordinates in a grid.
    """

    x: int  # pylint: disable=invalid-name
    y: int  # pylint: disable=invalid-name


def mfranceschi_get_cache_decorator():
    """
    Helper: returns a cache decorator, optimised if Python >= 3.9.
    """
    use_lru_cache = sys.version_info.minor < 9
    return functools.lru_cache(maxsize=None) if use_lru_cache else functools.cache
