from __future__ import annotations

import itertools as it
from pathlib import Path
from typing import Generator, Union

import src.elements as elements
import src.level_parser as level_parser

from .position import Position


class Level:
    """The level class containing the various level elements and related information."""

    def __init__(self, level_elements: level_parser.LevelElements):
        self.level_elements = level_elements
        self.active_element = self.get_main_character()

        # All positions in a linear format; stretching out the level elements and assigning
        # the positions provides this.
        self._positions = self._generate_positions_on_elements(level_elements)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.size}"

    def __str__(self) -> str:
        level = ""
        for row in self.level_elements:
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
        return len(self.level_elements)

    @property
    def width(self) -> int:
        """Width of the level map in blocks."""
        return len(self.level_elements[0])

    @property
    def shallow_copy(self) -> Level:
        """Shallow copy of the level instance itself.

        The purpose of a shallow copy is to retain the instances of `LevelElements`
        contained in the level while allowing for their positions to shift.
        """
        return Level([row.copy() for row in self.level_elements])

    def iterate_positions(self) -> Generator[Position, None, None]:
        yield from iter(self._positions)

    def _generate_positions_on_elements(
        self, level_elements: level_parser.LevelElements
    ) -> tuple[Position, ...]:
        """Helper method called upon initialization to generate iterable of positions.

        The positions of the elements go from top-left to bottom-right.
        """
        positions = []
        for row_index, row in enumerate(level_elements):
            positions_row = [
                Position(x=column_index, y=row_index) for column_index in range(len(row))
            ]
            positions.extend(positions_row)
        return tuple(positions)

    def iterate_elements(self) -> Generator[elements.LevelElement, None, None]:
        """Iterate through the elements of the level.

        This iteration is performed horizontally, then vertically, from the top left
        to the bottom right.
        """
        yield from it.chain.from_iterable(self.level_elements)

    def difference(self, other: Level) -> set[Position]:
        """Gives a set of positions between this level and another based on their differences."""
        self_elements = it.chain.from_iterable(self.level_elements)
        other_elements = it.chain.from_iterable(other.level_elements)

        iter_positions = iter(self.iterate_positions())
        positions: set[Position] = set()
        for self_element, other_element in zip(self_elements, other_elements):
            position = next(iter_positions)
            if self_element is other_element:
                continue
            positions.add(position)
        return positions

    def get_element_at_position(self, position: Position) -> elements.LevelElement:
        """Determines which element is lcoated at a particular position."""
        try:
            return self.level_elements[position.y][position.x]
        except IndexError:
            return elements.NullElement()

    def get_element_position(self, level_element: elements.LevelElement) -> Position:
        """Determines the location of the level element."""
        # TODO: If this process is inefficient, try caching elements to positions in a
        # dictionary
        for row_index, row in enumerate(self.level_elements):
            for column_index, column in enumerate(row):
                if column is level_element:
                    return Position(x=column_index, y=row_index)
        raise RuntimeError(f"Element `{level_element}` was not found.")

    def set_element_at_position(
        self, level_element: elements.LevelElement, position: Position
    ) -> None:
        """Sets an element at a given position to another element."""
        self.level_elements[position.y][position.x] = level_element

    def move_element(self, from_position: Position, to_position: Position) -> None:
        """Moves an element from a particular coordinate position to another."""
        element = self.get_element_at_position(from_position)
        self.level_elements[from_position.y][from_position.x] = elements.Space()
        self.level_elements[to_position.y][to_position.x] = element

    def get_main_character(self) -> elements.LevelElement:
        """Gets the main character in the level."""
        MAIN_CHARACTER = elements.BlockDude

        for element in it.chain.from_iterable(self.level_elements):
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
    level_elements = level_parser.parse_text_level(path)
    return Level(level_elements)


# TODO: Testing purposes, remove in prod
def test() -> None:
    """Remove in Prod."""
    level = create_level_from_file("./levels/level-99.txt")
    print(str(level))


if __name__ == "__main__":
    test()
