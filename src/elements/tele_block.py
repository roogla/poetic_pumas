from __future__ import annotations

import src.game.element_data as element_data
from src.elements.controller import TelekinesisController
from src.game.movement import Movement

from .levelelement import ControllableLevelElement

class TelekinesisBlock(ControllableLevelElement):
    level_symbol = "C"
    string_symbol = "🔮"
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.controller = TelekinesisController()
