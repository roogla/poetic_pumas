from blessed import Terminal

from .game import GameState
from .level import create_level_from_file
from .renderer import Renderer

# Timeout speed for inputs
TIMEOUT = 0.1


def main(terminal: Terminal) -> None:
    """Main entry point and loop for the game."""
    # Necessary when running with Docker
    # Docker's terminal defaults to 8 colors
    terminal.number_of_colors = 1 << 24

    # initalize game vars
    level = create_level_from_file("./levels/level-1.txt")
    renderer = Renderer(terminal=terminal, level=level)
    gamestate = GameState(level=level, renderer=renderer)

    with terminal.cbreak(), terminal.hidden_cursor(), terminal.fullscreen():
        renderer.render_level(level)

        while True:
            keystroke = terminal.inkey(timeout=TIMEOUT)

            if keystroke:
                gamestate.update(keystroke)


if __name__ == "__main__":
    main(Terminal())
