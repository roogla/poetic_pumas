from __future__ import annotations

from abc import ABC, abstractmethod

import src.elements.element_data as element_data
from src.movement import Movement
from src.vector2D import Vector2D


class LevelElement(ABC):
    """An abstract base class for all level elements.

    Args:
        ABC (): abstract base class helper class
    """

    _string_symbol = "?"

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __str__(self) -> str:
        return self.string_symbol

    @property
    @abstractmethod
    def level_symbol(self) -> str:
        """Use a class attribute in the child classes.

        This is used to extract the element type from the map layout file.
        """
        return "?"

    @property
    @abstractmethod
    def string_symbol(self) -> str:
        """Use a class attribute in the child classes.

        This is used to represent the element in the terminal for development
        and print purposes.
        """
        return self._string_symbol

    @string_symbol.setter
    def string_symbol(self, symbol: str) -> None:
        """Setter function for the string symbol."""
        self._string_symbol = symbol

    def _default_move_by(
        self, data: element_data.ElementData, movement: Vector2D
    ) -> None:
        """The default movement ability.

        Moves the level element by an amount specified by the vector.

        Args:
            movement (Vector2D): the vector to move the element as a shift in position
        """
        position = data.level.get_element_position(self)
        one_unit_leftward = position + movement
        data.level.move_element(position, one_unit_leftward)
        data.renderer.render_level(data.level)

    def move_left(self, data: element_data.ElementData) -> None:
        """Return the left-movement level element position according to its rules."""
        self._default_move_by(data, Movement.LEFT)

    def move_right(self, data: element_data.ElementData) -> None:
        """Return the right-movement level element position according to its rules."""
        self._default_move_by(data, Movement.RIGHT)

    def move_up(self, data: element_data.ElementData) -> None:
        """Return the up-movement level element position according to its rules."""
        self._default_move_by(data, Movement.UP)

    def move_down(self, data: element_data.ElementData) -> None:
        """Return the up-movement level element position according to its rules."""
        self._default_move_by(data, Movement.DOWN)
