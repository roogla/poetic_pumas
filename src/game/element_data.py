from __future__ import annotations

from dataclasses import dataclass

from ..elements import LevelElement
from .level import Level
from .physics import Movements, RigidBody


@dataclass
class ElementData:
    """Object aggregation for easier movement through code.

    Packages up the data LevelElements need to know in order to move properly
    and render appropriately.
    """

    level: Level
    level_element: LevelElement

    def move_left(self) -> None:
        """Return the left-movement level element position according to its rules."""
        self.level_element.position = RigidBody.apply_movement(data=self, movement=Movements.LEFT)

    def move_right(self) -> None:
        """Return the left-movement level element position according to its rules."""
        self.level_element.position = RigidBody.apply_movement(data=self, movement=Movements.RIGHT)

    def move_up(self) -> None:
        """Return the left-movement level element position according to its rules."""
        self.level_element.position = RigidBody.apply_movement(data=self, movement=Movements.UP)

    def move_down(self) -> None:
        """Return the left-movement level element position according to its rules."""
        self.level_element.position = RigidBody.apply_movement(data=self, movement=Movements.DOWN)
