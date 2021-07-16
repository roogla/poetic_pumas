from __future__ import annotations

from .elements import LevelElement, Space
from .level import Level
from .movement import Movement
from .physics import RigidBody
from .soundboard import Soundboard


class ElementData:
    """Object aggregation for easier movement through code.

    Packages up the data LevelElements need to know in order to move properly
    and render appropriately.
    """

    def __init__(self, level: Level, soundboard: Soundboard):
        self.level: Level = level
        self.level_element: LevelElement = level.active_element
        self.soundboard: Soundboard = soundboard

    def move_left(self) -> None:
        """Return the left-movement level element position according to its rules."""
        self.level_element.position = RigidBody.apply_movement(
            data=self, movement=Movement.LEFT
        )

    def move_right(self) -> None:
        """Return the left-movement level element position according to its rules."""
        self.level_element.position = RigidBody.apply_movement(
            data=self, movement=Movement.RIGHT
        )

    def move_up(self) -> None:
        """Return the left-movement level element position according to its rules."""
        self.level_element.position = RigidBody.apply_movement(
            data=self, movement=Movement.UP
        )

    def move_down(self) -> None:
        """Return the left-movement level element position according to its rules."""
        self.level_element.position = RigidBody.apply_movement(
            data=self, movement=Movement.DOWN
        )

    def jump(self) -> None:
        """Implements player jump movement"""
        facing = self.level_element.facing
        position = self.level_element.position
        if not isinstance(self.level.get_element_at_position(position + facing), Space):
            lateral_position = facing + Movement.UP
            self.level_element.position = RigidBody.apply_movement(
                data=self, movement=lateral_position
            )
