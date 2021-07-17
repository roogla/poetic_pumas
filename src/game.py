from blessed.keyboard import Keystroke

from .element_data import ElementData
from .input_handler import InputHandler
from .level import Level
from .level import create_level_from_file
from .renderer import Renderer
from .soundboard import Soundboard
from src.vector2D import Vector2D
from .elements.exitdoor import ExitDoor


class GameState:
    """Overall game state.

    Contains all necessary information about the game information and processes
    user input actions.
    """

    def __init__(self, level: Level, renderer: Renderer):
        self.level = level
        self.renderer = renderer
        self.input_handler = InputHandler()
        self.soundboard = Soundboard()
        self.current_level = 10
        self.level_dict = {
            0: "./resources/levels/level-0.txt",
            1: "./resources/levels/level-1.txt",
            2: "./resources/levels/level-2.txt",
            3: "./resources/levels/level-3.txt",
            4: "./resources/levels/level-4.txt",
            5: "./resources/levels/level-5.txt",
            6: "./resources/levels/level-6.txt",
            7: "./resources/levels/level-7.txt",
            8: "./resources/levels/level-8.txt",
            9: "./resources/levels/level-9.txt",
            10: "./resources/levels/level-10.txt",
        }

    def game_state(self) -> None:
        """Checks near MAIN_CHARACTER position for exit door element"""
        exit_checks = [
            self.level.active_element.position + Vector2D(-1, 0),
            self.level.active_element.position + Vector2D(-1, -1),
            self.level.active_element.position + Vector2D(1, -1),
            self.level.active_element.position + Vector2D(1, 0),
            self.level.active_element.position + Vector2D(-1, 1),
            self.level.active_element.position + Vector2D(1, 1),
            ]

        if self.current_level == 0:
            pass
        else:
            for check in exit_checks:
                if isinstance(self.level.get_element_at_position(check), ExitDoor):
                    if self.current_level == 10:
                        return True
                    else:
                        self.current_level += 1
                        self.level = create_level_from_file(self.level_dict[self.current_level])

    def check_state(self):
        """Checks for telekinesis block activation between MAIN_CHARACTER and TELE_BLOCK"""
        pass

    def load_game_file(self, level: int) -> str:
        """Checks game state for Splash/Menu or In-game"""
        return self.level_dict[level]

    def process_input(self, keystroke: Keystroke) -> None:
        """Takes the active element of the level and applies the input onto it."""
        # Package up data into a neat object
        element_data = ElementData(level=self.level, soundboard=self.soundboard)
        self.input_handler.handle_input(keystroke, data=element_data)

    def update(self, keystroke: Keystroke) -> None:
        """Process the game on every looped update call.

        Args:
            keystroke (Keystroke): user input on keyboard
        """
        self.process_input(keystroke)
        self.renderer.render_level(self.level)
