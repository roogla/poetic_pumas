from __future__ import annotations

from blessed import Terminal

# named lvl to avoid namespace conflict with var names
import src.level as lvl
from src.Vector2D import Vector2D


class Renderer:
    """Renders the Level and Level changes using blessed functionality."""

    def __init__(self, terminal: Terminal, level: lvl.Level):
        self.terminal = terminal
        # The history of level states.
        self.level_states: list[lvl.Level] = [level.shallow_copy]
        self.level_origin: Vector2D = Vector2D(0, 0)

    @property
    def previous_level_state(self) -> lvl.Level:
        """The most recent level state stored in memory."""
        return self.level_states[-1]

    def get_top_padding(self, level: lvl.Level) -> int:
        """Get the top padding for centering the terminal."""
        return (self.terminal.height - level.height) // 2

    def get_left_padding(self, level: lvl.Level) -> int:
        """Get the left padding for centering the terminal."""
        return (self.terminal.width - level.width) // 2

    def render_level(self, level: lvl.Level) -> None:
        """Re-renders the level completely based on the `Level` state.

        Completely wipes the terminal and refreshes with the current level state.

        Args:
            level (lvl.Level): the level state
        """
        terminal = self.terminal
        print(terminal.home + terminal.clear)

        # Center the level in the terminal
        top_padding = self.get_top_padding(level)
        left_padding = self.get_left_padding(level)

        # Print the level into the terminal
        for row in level.level_elements:
            cursor = terminal.move_xy(x=left_padding, y=top_padding)
            stringified_elements = [str(element) for element in row]
            stringified_row = "".join(stringified_elements)
            print(cursor + stringified_row)
            top_padding += 1

        self.add_level_state_to_history(level)

    def add_level_state_to_history(self, level: lvl.Level) -> None:
        """Sets the previous level state by deep copying the given level."""
        self.level_states.append(level.shallow_copy)
