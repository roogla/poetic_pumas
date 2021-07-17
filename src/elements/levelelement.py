from __future__ import annotations

from abc import ABC, abstractmethod

import src.game.element_data as element_data
from src.elements.controller import Controller
from src.game.movement import Movement
from src.game.vector2D import Vector2D


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
        return self._string_symbol

    @string_symbol.setter
    def string_symbol(self, symbol: str) -> None:
        """Setter function for the string symbol."""
        self._string_symbol = symbol


class ControllableLevelElement(LevelElement):
    """Only the controllable elements."""

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.controller = Controller()
        self.facing = Movement.LEFT

    def move_up(self, data: element_data.ElementData) -> None:
        """Move this level element upward according to the rules."""
        self.controller.move_up(data)

    def move_left(self, data: element_data.ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.facing = Movement.LEFT
        self.controller.move_left(data)

    def move_right(self, data: element_data.ElementData) -> None:
        """Move this level element rightward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.facing = Movement.RIGHT
        self.controller.move_right(data)

    def move_down(self, data: element_data.ElementData) -> None:
        """Move this level element rightward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.controller.move_down(data)

    def interact(self, data: element_data.ElementData) -> None:
        """Enable the interact function of the controller
        """
        self.controller.interact(data)