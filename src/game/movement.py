from dataclasses import dataclass

from .vector2D import Vector2D


@dataclass(frozen=True)
class Movement:
    """Helper basic movement `Vector2D` instances."""

    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    UP = Vector2D(0, -1)
    DOWN = Vector2D(0, 1)
    NONE = Vector2D(0, 0)
