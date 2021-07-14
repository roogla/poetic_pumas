from __future__ import annotations

from abc import ABC, abstractmethod

import src.elements.element_data as element_data
from src.vector2D import Vector2D


class LevelElement(ABC):
    """An abstract base class for all level elements.

    Args:
        ABC (): abstract base class helper class
    """

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
        return "?"

    def move_left(self, data: element_data.ElementData) -> None:
        """Return the left-movement level element position according to its rules."""
        position = data.level.get_element_position(self)
        one_unit_leftward = position + Vector2D(-1, 0)
        data.level.move_element(position, one_unit_leftward)
        data.renderer.render_level(data.level)

    def move_right(self, data: element_data.ElementData) -> None:
        """Return the left-movement level element position according to its rules."""
        position = data.level.get_element_position(self)
        one_unit_leftward = position + Vector2D(1, 0)
        data.level.move_element(position, one_unit_leftward)
        data.renderer.render_level(data.level)
