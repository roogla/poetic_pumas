from blessed import Terminal

from .game import GameState
from .level import create_level_from_file
from .renderer import Renderer

import os
import sys

# Timeout speed for inputs
TIMEOUT = 0.06

levels_folder = os.listdir(path='src/resources/levels/')

def main(terminal: Terminal) -> None:
    """Main entry point and loop for the game."""
    # Necessary when running with Docker
    # Docker's terminal defaults to 8 colors
    terminal.number_of_colors = 1 << 24

    starting_level = "level-1"
    if len(sys.argv) >= 2:
        if f'{sys.argv[1]}.txt' in levels_folder:
            starting_level = str(sys.argv[1])
    # initalize game vars
    level = create_level_from_file(f"./resources/levels/{starting_level}.txt")
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
