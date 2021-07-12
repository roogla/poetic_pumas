from __future__ import annotations

from blessed import Terminal

# from .level import Level


class Renderer:
    """Renders the Level and Level changes using blessed functionality."""

    def __init__(self, terminal: Terminal):
        self.terminal = terminal

    def render_level(self, level) -> None:
        terminal = self.terminal
        print(terminal.home + terminal.clear)
        top_padding = (terminal.height - level.height) // 2
        terminal.move_down(top_padding)
        print(str(level))
