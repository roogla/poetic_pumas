import time

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
    level = create_level_from_file("./levels/level-99.txt")
    renderer = Renderer(terminal=terminal)
    gamestate = GameState(level=level, renderer=renderer)

    with terminal.cbreak(), terminal.hidden_cursor(), terminal.fullscreen():
        print(terminal.home + terminal.clear)
        t = time.time()
        key_input = ''

        while key_input != "q":
            key_input = terminal.inkey(timeout=TIMEOUT)
            action = key_input

            # check for keyboard input
            # how to keep track using the enum row for map
            # needed for erase function (erase function needed)
            # graphics
            # action = Action(key_input)
            # TODO: Figure out FPS and stuff here
            # gamestate.next(action)
            gamestate.next(key_input)

            print(terminal.home + str(level))


if __name__ == "__main__":
    main(Terminal())
