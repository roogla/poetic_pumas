import os
import sys
from typing import Callable

from .element_data import ElementData

# TODO REMOVE FOR PRODUCTION
import sys, traceback, threading

Command = Callable[[ElementData], None]


def do_nothing(data: ElementData) -> None:
    """Does nothing."""


def move_left(data: ElementData) -> None:
    """Attempt to move the level element leftward."""
    data.active_element.move_left(data)


def move_right(data: ElementData) -> None:
    """Attempt to move the level element leftward."""
    data.active_element.move_right(data)


def move_down(data: ElementData) -> None:
    """Attempt to move the level element downward."""
    data.active_element.move_down(data)


def move_up(data: ElementData) -> None:
    """Attempt to move the level element upward."""
    data.active_element.move_up(data)


def interact(data: ElementData) -> None:
    """Interact using the specific level element."""


def box_action(data: ElementData) -> None:
    """Box action placeholder."""
    # TODO: Remove type ignore comment; move to controller class
    data.level_element.box_action(data)  # type: ignore


def level_reset(data: ElementData) -> None:
    pass


def exit_terminal(data: ElementData) -> None:
    """Completely exit the script."""
    while 1:
        interpreter = sys.executable
        os.system(f'{interpreter} blockdude.py')
        print("restarting")
        exit()
