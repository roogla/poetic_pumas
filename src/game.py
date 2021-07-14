from blessed.keyboard import Keystroke

from .elements.element_data import ElementData
from .input_handler import InputHandler
from .level import Level
from .renderer import Renderer


class GameState:
    """Overall game state.

    Contains all necessary information about the game information and processes
    user input actions.
    """

    def __init__(self, level: Level, renderer: Renderer):
        self.level = level
        self.renderer = renderer
        self.input_handler = InputHandler()

    def process_input(self, keystroke: Keystroke) -> None:
        """Takes the active element of the level and applies the input onto it."""
        level_element = self.level.active_element
        # Package up data into a neat object
        element_data = ElementData(
            level=self.level, renderer=self.renderer, level_element=level_element
        )
        self.input_handler.handle_input(keystroke, data=element_data)

    def update(self, keystroke: Keystroke) -> None:
        """Process the game on every looped update call.

        Args:
            keystroke (Keystroke): user input on keyboard
        """
        self.process_input(keystroke)
