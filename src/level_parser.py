from __future__ import annotations

from typing import Type

from .elements import ACTIVE_ELEMENTS, LevelElement
import os


"""
Level parser.

Contains helper class and functions to read map layout files.
"""

from pathlib import Path

"""Reference for level elements.

W -> wall
T -> top wall
V -> bottom wall
I -> top and bottom wall
B -> block
D -> block dude start location
G -> ground
. -> space/emptiness
X -> exit/door
"""

# Custom type alias for grid of level elements.
# Wrapped in try-block because of circular references.
try:
    LevelElements = list[list[LevelElement]]
except AttributeError:
    pass


def convert_character_to_element(char: str) -> Type[LevelElement]:
    """Converts a level ASCII character into a `LevelElement` object.

    Args:
        char (str): ASCII level map character

    Raises:
        Exception: if a character in the level map does not match an active object

    Returns:
        LevelElement: the object representation of the level element
    """
    for element in ACTIVE_ELEMENTS:
        if element.level_symbol == char:
            return element
    raise Exception(f"Invalid character in the level map: `{char}`.")


def parse_text_level(file_path: Path) -> LevelElements:
    """Parses a level layout file into `LevelElements`.

    Takes a file path to the level layout and converts the ASCII characters into
    a grid of level elements (Python objects).

    Args:
        file_path (Path): the path to the level layout file

    Returns:
        LevelElements: a 2D grid of level elements
    """
    level: list[list[str]] = []
    try:
        with open(file_path) as fp:
            # remove the "\n" characters
            level = [list(line.strip()) for line in fp.readlines()]
    except OSError as e:
        os.system('py blockdude.py')


    level_elements = []

    for row_index, row in enumerate(level):
        level_elements_row = []
        for column_index, cell in enumerate(row):
            element: Type[LevelElement] = convert_character_to_element(cell)
            level_elements_row.append(element(x=column_index, y=row_index))
        level_elements.append(level_elements_row)

    return level_elements
