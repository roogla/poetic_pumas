from typing import Optional

from blessed.keyboard import Keystroke

from . import command as cmd
from .command import Command
from .element_data import ElementData
from .key import Key


class InputHandler:
    """Handles the input to action commands."""

    mapping: dict[Optional[str], Command] = {
        Key.W: cmd.move_up,
        Key.w: cmd.move_up,
        Key.UP: cmd.move_up,
        Key.A: cmd.move_left,
        Key.a: cmd.move_left,
        Key.LEFT: cmd.move_left,
        Key.D: cmd.move_right,
        Key.d: cmd.move_right,
        Key.RIGHT: cmd.move_right,
        Key.S: cmd.move_down,
        Key.s: cmd.move_down,
        Key.DOWN: cmd.move_down,
        Key.SPACE: cmd.interact,
        Key.Q: cmd.exit_terminal,
        Key.q: cmd.exit_terminal,
        Key.ESCAPE: cmd.exit_terminal,
    }

    def __init__(self) -> None:
        pass

    def handle_input(self, keystroke: Keystroke, data: ElementData) -> None:
        """Handles the player input and information regarding handling input."""
        command: Command = self.mapping.get(Key(keystroke).name, cmd.do_nothing)
        command(data)
