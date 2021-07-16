from ..movement import Movement
from .levelelement import LevelElement


class BlockDude(LevelElement):
    """Block Dude himself. The main character."""

    level_symbol = "D"
    string_symbol = "🤷"

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.facing = Movement.LEFT
