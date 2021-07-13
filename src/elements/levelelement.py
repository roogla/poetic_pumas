from __future__ import annotations

from abc import ABC, abstractmethod

# from ..level import Level
from ..position import Position
from .element_data import ElementData


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

    def move_left(self, data: ElementData) -> Position:
        """Return the left-movement level element position according to its rules."""
        position = data.level.get_element_position(self)
        return position - Position(-1, 0)
