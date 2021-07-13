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

    def next(self, key_input: Keystroke) -> None:
        level_element = self.level.active_element
        element_data = ElementData(
            level=self.level, renderer=self.renderer, level_element=level_element
        )
        self.input_handler.handle_input(key_input, data=element_data)


