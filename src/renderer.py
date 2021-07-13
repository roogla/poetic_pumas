from __future__ import annotations

from blessed import Terminal

# named lvl to avoid namespace conflict with var names
import src.level as lvl
from src.position import Position


class Renderer:
    """Renders the Level and Level changes using blessed functionality."""

    def __init__(self, terminal: Terminal, level: lvl.Level):
        self.terminal = terminal
        # The level state before a render change is made.
        self.previous_level_state: lvl.Level = level
        self.level_origin: Position = Position(0, 0)

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
        # terminal.move_xy(x=left_padding, y=top_padding)

        # Print the level into the terminal
        for row in level.level_elements:
            cursor = terminal.move_xy(x=left_padding, y=top_padding)
            stringified_elements = [str(element) for element in row]
            stringified_row = "".join(stringified_elements)
            print(cursor + stringified_row)
            top_padding += 1

        # TODO: Planning on performing the printing inside this renderer rather than using
        # the level class functionality. Or add functionality to the level class
        # to make this easier. It's better to do it with a one-sided approach though
        # (reduced coupling)

        self.set_previous_level_state(level)

    def update_level_render(self, level: lvl.Level) -> None:
        """Renders any updates to the level based on the previous level state.

        Given the difference between the previous level state and the current level
        state, update the individual differences in the renderer accordingly.
        """
        if level is None:
            raise ValueError(
                "There is no previous level to update from. Use `render_level` instead?"
            )

        # type ignore because linter is not catching the exception above
        positions = level.difference(self.previous_level_state)
        # TODO: Render updates to the positions. Scaling and coordinate frames need to be sorted out.
        # TODO: e.g. block-space (number of blocks) vs. pixel or terminal space
        terminal = self.terminal

        # The origin with respect to the terminal origin
        top_padding = self.get_top_padding(level)
        left_padding = self.get_left_padding(level)
        level_origin = Position(x=left_padding, y=top_padding)

        for position in positions:
            # from the terminal's frame of reference
            changed_position_terminal_frame = level_origin + position
            with terminal.location(
                changed_position_terminal_frame.x, changed_position_terminal_frame.y
            ):
                element = level.get_element_at_position(position)
                print(str(element))

        self.set_previous_level_state(level)

    def set_previous_level_state(self, level: lvl.Level) -> None:
        """Sets the previous level state by deep copying the given level."""
        self.previous_level_state = level.shallow_copy
