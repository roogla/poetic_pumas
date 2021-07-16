from __future__ import annotations

from abc import ABC, abstractmethod

from ..vector2D import Vector2D


class LevelElement(ABC):
    """An abstract base class for all level elements.

    Args:
        ABC (): abstract base class helper class
    """

    def __init__(self, x: int, y: int):
        self.position = Vector2D(x=x, y=y)

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
