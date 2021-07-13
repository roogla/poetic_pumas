from blessed.keyboard import Keystroke

from . import command as cmd
from .command import Command
from .elements.element_data import ElementData
from .key import Key


class InputHandler:
    """Handles the input to action commands."""

    mapping: dict[str, Command] = {
        Key.LEFT: cmd.move_left,
        Key.SPACE: cmd.interact,
    }

    def __init__(self) -> None:
        pass

    def handle_input(self, key_input: Keystroke, data: ElementData) -> None:
        """Handles the player input and information regarding handling input."""
        command: Command = self.mapping.get(key_input, cmd.do_nothing)
        command(data)
