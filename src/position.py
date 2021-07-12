from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """Coordinate system has origin at the top-left, (0, 0)."""

    x: int
    y: int

    def __add__(self, other: Position):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Position):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int):
        return Position(other * self.x, other * self.y)
