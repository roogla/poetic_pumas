from __future__ import annotations

import itertools as it
from pathlib import Path
from typing import Union

from .elements import BlockDude, LevelElement, NullElement, Space
from .level_parser import LevelElements, parse_text_level
from .position import Position


class Level:
    """The level class containing the various level elements and related information."""

    def __init__(self, elements: LevelElements):
        self.elements = elements
        self.active_element = self.get_main_character()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.size}"

    def __str__(self) -> str:
        level = ""
        for row in self.elements:
            stringified_elements = [str(element) for element in row]
            stringified_row = "".join(stringified_elements)
            level += stringified_row + "\n"
        return level

    @property
    def size(self) -> tuple[int, int]:
        """Dimensions of the Level in blocks."""
        return self.width, self.height

    @property
    def height(self) -> int:
        """Height of the level map in blocks."""
        return len(self.elements)

    @property
    def width(self) -> int:
        """Width of the level map in blocks."""
        return len(self.elements[0])

    def get_element_at_position(self, position: Position) -> LevelElement:
        """Determines which element is lcoated at a particular position."""
        try:
            return self.elements[position.y][position.x]
        except IndexError:
            return NullElement()

    def get_element_position(self, level_element: LevelElement) -> Position:
        """Determines the location of the level element."""
        # TODO: If this process is inefficient, try caching elements to positions in a
        # dictionary
        for row_index, row in enumerate(self.elements):
            for column_index, column in enumerate(row):
                if column is level_element:
                    return Position(x=column_index, y=row_index)
        raise RuntimeError(f"Element `{level_element}` was not found.")

    def set_element_at_position(
        self, level_element: LevelElement, position: Position
    ) -> None:
        self.elements[position.y][position.x] = level_element

    def move_element(self, from_position: Position, to_position: Position) -> None:
        element = self.get_element_at_position(from_position)
        self.elements[from_position.y][from_position.x] = Space()
        self.elements[to_position.y][to_position.x] = element

    def get_main_character(self) -> LevelElement:
        """Gets the main character in the level."""
        MAIN_CHARACTER = BlockDude

        for element in it.chain.from_iterable(self.elements):
            # TODO: Probably bad design. Too lazy to think right now. Strongly coupled.
            if isinstance(element, MAIN_CHARACTER):
                return element
        raise LookupError(f"No such element {MAIN_CHARACTER} in the level.")


def create_level_from_file(file_path: Union[str, Path]) -> Level:
    """Returns a `Level` object from the level layout filepath.

    Args:
        file_path (Path): the path is in the shape of "./levels/*.txt"
    """
    path = Path(__file__).parent / Path(file_path)
    level_elements = parse_text_level(path)
    return Level(level_elements)


# TODO: Testing purposes, remove in prod
def test() -> None:
    """Remove in Prod."""
    level = create_level_from_file("./levels/level-99.txt")
    print(str(level))


if __name__ == "__main__":
    test()
