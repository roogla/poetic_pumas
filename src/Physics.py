from __future__ import annotations

from typing import Union

from src.vector2D import Vector2D


class RigidBody:
    """Creates a RigitBody object. Utilizes Vector2D class"""

    def __init__(self, x: Union[float, int], y: Union[float, int]):
        self.pos = Vector2D(x, y)
        self.velocity: Vector2D = Vector2D(0, 0)
        self.accel: Vector2D = Vector2D(0, 0)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.pos})"

    def apply_movement(self, movement: Vector2D) -> None:
        """
        Apply movement

        Applies the given movement to the body
        :param movement: The movement vector
        """
        self.pos.add(movement)

    def apply_force(self, force: Vector2D) -> None:
        """
        Apply Force

        Applies the given force to the body
        :param force: the force to be applied
        """
        self.accel.add(force)

    def update(self) -> None:
        """
        Update body

        Updates the body's position based on acceleration and velocity
        """
        self.velocity.add(self.accel)
        self.pos.add(self.velocity)
