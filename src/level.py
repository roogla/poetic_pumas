from __future__ import annotations

import itertools as it
from pathlib import Path
from typing import Generator, Union

from .elements import BlockDude, NullElement
from .level_parser import LevelElement, LevelElements, parse_text_level
from .vector2D import Vector2D


class Level:
    """The level class containing the various level elements and related information."""

    def __init__(self, level_elements: LevelElements):

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

    def iterate_positions(self) -> Generator[Vector2D, None, None]:
        """Iterate through the positions in the level from left to right, top to bottom."""
        yield from iter(self._positions)

    def _generate_positions_on_elements(
        self, level_elements: LevelElements
    ) -> tuple[Vector2D, ...]:
        """Helper method called upon initialization to generate iterable of positions.

        The positions of the elements go from top-left to bottom-right.
        """
        positions = []
        for row_index, row in enumerate(level_elements):
            positions_row = [
                Vector2D(x=column_index, y=row_index) for column_index in range(len(row))
            ]
            positions.extend(positions_row)
        return tuple(positions)

    def iterate_elements(self) -> Generator[LevelElement, None, None]:
        """Iterate through the elements of the level.

        This iteration is performed horizontally, then vertically, from the top left
        to the bottom right.
        """
        yield from it.chain.from_iterable(self.level_elements)

    def difference(self, other: Level) -> set[Vector2D]:
        """Gives a set of positions between this level and another based on their differences."""
        self_elements = it.chain.from_iterable(self.level_elements)
        other_elements = it.chain.from_iterable(other.level_elements)

        iter_positions = iter(self.iterate_positions())
        positions: set[Vector2D] = set()
        for self_element, other_element in zip(self_elements, other_elements):
            position = next(iter_positions)
            if self_element is other_element:
                continue
            positions.add(position)
        return positions

    def get_element_at_position(self, position: Vector2D) -> LevelElement:
        """Determines which element is lcoated at a particular position."""
        try:
            y, x = int(position.y), int(position.x)
            return self.level_elements[y][x]
        except IndexError:
            return NullElement()

    def set_element_at_position(
        self, level_element: LevelElement, position: Vector2D
    ) -> None:
        """Sets an element at a given position to another element."""
        y, x = int(position.y), int(position.x)
        self.level_elements[y][x] = level_element

    def move_element(self, from_position: Vector2D, to_position: Vector2D) -> None:
        """Moves an element from a particular coordinate position to another."""
        from_element = self.get_element_at_position(from_position)
        to_element = self.get_element_at_position(to_position)

        self.set_element_at_position(from_element, to_position)
        self.set_element_at_position(to_element, from_position)

    def get_main_character(self) -> LevelElement:
        """Gets the main character in the level."""
        MAIN_CHARACTER = BlockDude
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
    level_elements = parse_text_level(path)
    return Level(level_elements)


# TODO: Testing purposes, remove in prod
def test() -> None:
    """Remove in Prod."""
    level = create_level_from_file("resources/levels/level-99.txt")
    print(str(level))


if __name__ == "__main__":
    test()
