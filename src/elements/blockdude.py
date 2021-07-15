# from ..level import Level
from ..physics import RigidBody
from .element_data import ElementData
from .levelelement import LevelElement


class BlockDude(LevelElement, RigidBody):
    """Block Dude himself. The main character."""

    level_symbol = "D"
    string_symbol = "🤷"

    def __init__(self, x: int, y: int):
        RigidBody.__init__(self, x, y)
        LevelElement.__init__(self)
        self.block = None

    def move_left(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.facing = self.LEFT
        self.apply_movement(data, self.LEFT)

    def move_right(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.facing = self.RIGHT
        self.apply_movement(data, self.RIGHT)

    def move_up(self, data: ElementData) -> None:
        self.apply_movement(data, self.UP + self.facing)
