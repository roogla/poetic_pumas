from .element_data import ElementData
from .physics import Movements, RigidBody


class BlockDudeController(RigidBody):
    """Controller for Blockdude."""

    def __init__(self, x: int, y: int):
        RigidBody.__init__(self, x, y)
        self.block = None

    def move_left(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.facing = Movements.LEFT
        self.apply_movement(data, Movements.LEFT)

    def move_right(self, data: ElementData) -> None:
        """Move this level element rightward according to the rules.

        If there are any objects to the right of block dude, he cannot move right.
        """
        self.facing = Movements.RIGHT
        self.apply_movement(data, Movements.RIGHT)

    def move_up(self, data: ElementData) -> None:
        """Applies diagonally upward motion to blockdude element.

        If there are any objects blocking diagonal, he cannot move
        """
        self.apply_movement(data, Movements.UP + self.facing)
