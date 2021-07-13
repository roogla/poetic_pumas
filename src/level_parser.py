from __future__ import annotations

"""
Level parser.

Contains helper class and functions to read map layout files.
"""

from pathlib import Path

import src.elements as elements

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
    LevelElements = list[list[elements.LevelElement]]
except AttributeError:
    pass


def convert_character_to_element(char: str) -> elements.LevelElement:
    """Converts a level ASCII character into a `LevelElement` object.

    Args:
        char (str): ASCII level map character
        position (Position): coordinate position with origin in the top-left

    Raises:
        Exception: if a character in the level map does not match an active object

    Returns:
        LevelElement: the object representation of the level element
    """
    for element in elements.active_elements:
        if element.level_symbol == char:
            return element()
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
    with open(file_path) as fp:
        # remove the "\n" characters
        level = [list(line.strip()) for line in fp.readlines()]

    level_elements = []
    # TODO: Refactor for readability.
    for row_index, row in enumerate(level):
        level_elements_row = [
            convert_character_to_element(element)
            for column_index, element in enumerate(row)
        ]
        level_elements.append(level_elements_row)

    return level_elements
