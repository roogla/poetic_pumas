from typing import Callable

from .element_data import ElementData

Command = Callable[[ElementData], None]


def do_nothing(data: ElementData) -> None:
    """Does nothing."""


def move_left(data: ElementData) -> None:
    """Attempt to move the level element leftward."""
    data.move_left()


def move_right(data: ElementData) -> None:
    """Attempt to move the level element leftward."""
    data.move_right()


def move_up(data: ElementData) -> None:
    """Attempt to move the level element upward."""
    data.move_up()


def interact(data: ElementData) -> None:
    """Interact using the specific level element."""


def exit_terminal(data: ElementData) -> None:
    """Completely exit the script."""
    quit()
