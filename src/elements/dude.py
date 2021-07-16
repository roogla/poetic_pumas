from __future__ import annotations

import src.game.element_data as element_data
from src.elements.controller import DudeController
from src.game.movement import Movement

from .levelelement import ControllableLevelElement


class Dude(ControllableLevelElement):
    """Block Dude himself. The main character."""

    level_symbol = "D"
    face = {
        Movement.LEFT: "👈",
        Movement.RIGHT: "👉",
    }
    string_symbol = "👉"

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.controller = DudeController()

        self.string_symbol = self.face[self.facing]

        # Which block this element is carrying
        self.carrying = False

    @property
    def is_facing_left(self) -> bool:
        """Whether the level element is facing left."""
        return self.string_symbol == self.face[Movement.LEFT]

    @property
    def is_facing_right(self) -> bool:
        """Whether the level element is facing right."""
        return self.string_symbol == self.face[Movement.RIGHT]

    def set_facing_left(self) -> None:
        """Changes the direction of the level element to face leftward symbolically."""
        self.string_symbol = self.face[Movement.LEFT]

    def set_facing_right(self) -> None:
        """Changes the direction of the level element to face rightward symbolically."""
        self.string_symbol = self.face[Movement.RIGHT]

    def move_left(self, data: element_data.ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.set_facing_left()
        super().move_left(data)

    def move_right(self, data: element_data.ElementData) -> None:
        """Move this level element rightward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.set_facing_right()
        super().move_right(data)
