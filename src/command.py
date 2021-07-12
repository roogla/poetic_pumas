from typing import Callable

from .elements.element_data import ElementData

Command = Callable[[ElementData], None]


def do_nothing(data: ElementData) -> None:
    """Does nothing."""


def move_left(data: ElementData) -> None:
    """Attempt to move the level element leftward."""
    data.level_element.move_left(data.level)


def interact(data: ElementData) -> None:
    """Interact using the specific level element."""
