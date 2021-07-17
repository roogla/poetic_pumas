from __future__ import annotations

import sys

from blessed import Terminal

# named lvl to avoid namespace conflict with var names
from . import level as lvl
from .camera import Camera


class Renderer:
    """Renders the Level and Level changes using blessed functionality."""

    def __init__(self, terminal: Terminal, level: lvl.Level):
        self.terminal = terminal
        self.camera = Camera(level.level_elements)

    def get_top_padding(self) -> int:
        """Get the top padding for centering the terminal."""
        return (self.terminal.height - self.camera.height) // 2

    def get_left_padding(self) -> int:
        """Get the left padding for centering the terminal."""
        return (self.terminal.width - self.camera.width) // 2

    def render_level(self) -> None:
        """Re-renders the level completely based on the `Level` state.

        Completely wipes the terminal and refreshes with the current level state.
        """
        terminal = self.terminal

        # Center the level in the terminal
        top_padding = self.get_top_padding() - 1
        left_padding = self.get_left_padding() - 1

        # list for all the print able elements, so we dont have to call print() multiple times
        printables: list[str] = []

        # go to home and clear terminal
        printables.append(terminal.home + terminal.clear)

        cursor = terminal.move_xy(x=left_padding, y=top_padding)
        # load the renderable elements
        renderable = self.camera.get_renderable_elements()
        # add border
        printables.append(cursor + f"┌{'─' * 2 * len(renderable[0])}┐")
        top_padding += 1

        # add elements
        for row in renderable:
            cursor = terminal.move_xy(x=left_padding, y=top_padding)
            stringified_elements = [str(element) for element in row]
            stringified_row = "".join(stringified_elements)
            printables.append(cursor + f"│{stringified_row}│")
            top_padding += 1

        cursor = terminal.move_xy(x=left_padding, y=top_padding - 1)
        # add closing border
        printables.append(cursor + f"└{'─' * 2 * len(renderable[0])}┘")

        # print all
        print(*printables, sep="\n")
        sys.stdout.flush()
