
from blessed import Terminal

from .game import GameState
from .level import create_level_from_file
from .renderer import Renderer
from .title import Title


import os
import sys

# Timeout speed for inputs
TIMEOUT = 0.06

levels_folder = os.listdir(path='src/resources/levels/')

def main(terminal: Terminal, level_num: str) -> None:
    """Main entry point and loop for the game."""
    # Necessary when running with Docker
    # Docker's terminal defaults to 8 colors
    terminal.number_of_colors = 1 << 24
    if level_num is None:
        level_num = "level-1"
    starting_level = f"{level_num}"
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
            if gamestate.game_state():
                gamestate = None
                renderer = None
                break
            elif keystroke:
                gamestate.update(keystroke)

    if gamestate.current_level == 10:
        end_game = create_level_from_file("./resources/levels/level-99.txt")
        print(renderer.render_level(end_game))
        end_game = Title()
        end_game.display_logo()
        print(f"{renderer.terminal.move_xy(8, 8)} YOU'VE WON THE GAME, ENJOY A DELICIOUS COOKIE!")

