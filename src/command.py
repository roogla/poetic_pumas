from typing import Callable

from elements import ElementData

Command = Callable[[ElementData], None]


def do_nothing(data: ElementData) -> None:
    """Does nothing."""


def move_left(data: ElementData) -> None:
    """Attempt to move the level element leftward."""
    data.level_element.move_left(data)


def move_right(data: ElementData) -> None:
    """Attempt to move the level element leftward."""
    data.level_element.move_right(data)


def interact(data: ElementData) -> None:
    """Interact using the specific level element."""


def exit_terminal(data: ElementData) -> None:
    """Completely exit the script."""
    quit()
