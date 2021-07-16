from typing import Optional

from blessed.keyboard import Keystroke

from . import command as cmd
from .command import Command
from .element_data import ElementData
from .key import Key


class InputHandler:
    """Handles the input to action commands."""

    mapping: dict[Optional[str], Command] = {
        Key.UP: cmd.move_up,
        Key.DOWN: cmd.box_action,
        Key.LEFT: cmd.move_left,
        Key.A: cmd.move_left,
        Key.a: cmd.move_left,
        Key.SPACE: cmd.interact,
        Key.RIGHT: cmd.move_right,
        Key.D: cmd.move_right,
        Key.d: cmd.move_right,
        Key.UP: cmd.move_up,
        Key.W: cmd.move_up,
        Key.w: cmd.move_up,
        Key.ESCAPE: cmd.exit_terminal,
        Key.Q: cmd.exit_terminal,
        Key.q: cmd.exit_terminal,
        Key.w: cmd.move_up,
        Key.W: cmd.move_up,
        Key.a: cmd.move_left,
        Key.A: cmd.move_left,
        Key.s: cmd.box_action,
        Key.S: cmd.box_action,
        Key.d: cmd.move_right,
        Key.D: cmd.move_right,
    }

    def __init__(self) -> None:
        pass

    def handle_input(self, keystroke: Keystroke, data: ElementData) -> None:
        """Handles the player input and information regarding handling input."""
        command: Command = self.mapping.get(Key(keystroke).name, cmd.do_nothing)
        command(data)
