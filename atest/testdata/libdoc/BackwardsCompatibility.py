"""Library for testing backwards compatibility.

Especially testing argument type information that has been changing after RF 4.
Examples are only using features compatible with all tested versions.
"""

import enum
import typing


ROBOT_LIBRARY_VERSION = '1.0'


class Color(enum.Enum):
    """RGB colors."""
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'


class Size(typing.TypedDict):
    """Some size."""
    width: int
    height: int


def simple():
    """Some doc.

    Tags: example
    """
    pass


def arguments(a, b=2, *c, d=4, e, **f):
    pass


def types(a: int, b: bool = True):
    pass


def special_types(a: Color, b: Size):
    pass


def union(a: typing.Union[int, bool]):
    pass
