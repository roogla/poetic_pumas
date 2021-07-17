import os
import sys
from pathlib import Path

from blessed import Terminal

from .game import GameState
from .level import create_level_from_file
from .renderer import Renderer

# Timeout speed for inputs
TIMEOUT = 0.1

levels_folder = os.listdir(path="src/resources/levels/")


def starting_level_from_script_args() -> str:
    """Takes the Python script input to jump to a particular level.

    e.g. `python ./blockdude.py level-5`
    """
    starting_level = "level-1"
    if len(sys.argv) >= 2:
        if f"{sys.argv[1]}.txt" in levels_folder:
            starting_level = str(sys.argv[1])
    return starting_level


def main(terminal: Terminal) -> None:
    """Main entry point and loop for the game."""
    # Necessary when running with Docker; Docker's terminal defaults to 8 colors
    terminal.number_of_colors = 1 << 24

    starting_level = starting_level_from_script_args()

    # initalize game vars
    level = create_level_from_file(
        level_file_name=f"{starting_level}.txt",
        levels_directory=Path(__file__).parent.parent / Path("resources/levels"),
    )
    renderer = Renderer(terminal=terminal, level=level)
    gamestate = GameState(level=level, renderer=renderer)

    with terminal.cbreak(), terminal.hidden_cursor(), terminal.fullscreen():
        renderer.render_level()

        while True:
            keystroke = terminal.inkey(timeout=TIMEOUT)

            if keystroke:
                gamestate.update(keystroke)


if __name__ == "__main__":
    main(Terminal())
