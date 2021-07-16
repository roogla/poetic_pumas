from blessed.keyboard import Keystroke

from .element_data import ElementData
from .input_handler import InputHandler
from .level import Level
from .renderer import Renderer
from .soundboard import Soundboard


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

    def process_input(self, keystroke: Keystroke) -> None:
        """Takes the active element of the level and applies the input onto it."""
        # Package up data into a neat object
        element_data = ElementData(
            level=self.level,
            soundboard=self.soundboard,
            renderer=self.renderer,
        )
        self.input_handler.handle_input(keystroke, data=element_data)

    def update(self, keystroke: Keystroke) -> None:
        """Process the game on every looped update call.

        Args:
            keystroke (Keystroke): user input on keyboard
        """
        self.process_input(keystroke)
        self.renderer.render_level(self.level)
