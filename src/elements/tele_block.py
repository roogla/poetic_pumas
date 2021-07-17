from __future__ import annotations

from src.elements.controller import TelekinesisController

from .levelelement import ControllableLevelElement


class TelekinesisBlock(ControllableLevelElement):
    level_symbol = "C"
    string_symbol = "🔮"

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.controller = TelekinesisController()
