from __future__ import annotations
from typing import Union
from Vector2D import Vector2D


class RigitBody:
    def __init__(self, x: Union[float, int], y: Union[float, int]):
        self._pos = Vector2D(x, y)
        self._pos.limit(0)
        self.velocity: Vector2D = Vector2D(0, 0)
        self.accel: Vector2D = Vector2D(0, 0)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._pos})"

    def apply_force(self, force: Vector2D) -> None:
        """
        Applies the given force to the body
        :param force: the force to be applied
        """
        self.accel.add(force)

    def update(self):
        """
        Updates the body's position based on acceleration and velocity
        :return:
        """
        self.velocity.add(self.accel)
        self._pos.add(self.velocity)
