from typing import Callable

from .elements.element_data import ElementData

Command = Callable[[ElementData], None]

def do_nothing(data: ElementData) -> None:
    """Does nothing."""

def move_left(data: ElementData) -> None:
    """Attempt to move the level element leftward."""
    data.level_element.move_left(data)

def move_right(data: ElementData) -> None:
    """Attempt to move the level element rightward."""
    data.level_element.move_right(data)

def move_up(data:  ElementData) -> None:
    """Attempt to move the level element upward."""
    data.level_element.move_up(data)

def interact(data: ElementData) -> None:
    """Interact using the specific level element."""

def exit_terminal(data: ElementData) -> None:
    """Completely exit the script."""
    quit()
