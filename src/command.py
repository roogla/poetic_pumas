from typing import Callable

from .element_data import ElementData
from .elements import BlockDude
from .movement import Movement

Command = Callable[[ElementData], None]


def do_nothing(data: ElementData) -> None:
    """Does nothing."""


def move_left(data: ElementData) -> None:
    """Attempt to move the level element leftward."""
    if isinstance(data.level.active_element, BlockDude):
        data.level.active_element.facing = Movement.LEFT
    data.move_left()


def move_right(data: ElementData) -> None:
    """Attempt to move the level element leftward."""
    if isinstance(data.level.active_element, BlockDude):
        data.level.active_element.facing = Movement.RIGHT
    data.move_right()


def move_up(data: ElementData) -> None:
    """Attempt to move the level element upward."""
    # TODO check if element is player or block
    # IF player
    data.jump()
    # else if block
    # data.move_up()


def interact(data: ElementData) -> None:
    """Interact using the specific level element."""


def exit_terminal(data: ElementData) -> None:
    """Completely exit the script."""
    quit()
