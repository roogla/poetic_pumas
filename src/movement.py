from dataclasses import dataclass

from src.vector2D import Vector2D


@dataclass(init=False)
class Movement:
    """Helper basic movement `Vector2D` instances."""

    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    UP = Vector2D(0, -1)
    DOWN = Vector2D(0, 1)
    UP_LEFT = Vector2D(-1, -1)
    UP_RIGHT = Vector2D(1, 1)
