from __future__ import annotations

from math import acos, sqrt
from typing import Union

Numerics = Union[float, int]


class Vector2D:
    """2 Dimensional vector math class. Implements vector operations."""

    def __init__(self, x: Numerics = 0, y: Numerics = 0):
        self.x: Numerics = x
        self.y: Numerics = y

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x},{self.y})"

    def __eq__(self, other: Vector2D) -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other: Vector2D) -> bool:
        return self.x < other.x and self.y < other.y

    def __le__(self, other: Vector2D) -> bool:
        return self < other or self == other

    def __gt__(self, other: Vector2D) -> bool:
        return self.x > other.x and self.y > other.y

    def __ge__(self, other: Vector2D) -> bool:
        return self > other or self == other

    def __hash__(self):
        return hash((self.x, self.y))

    def add(self, other: Vector2D) -> None:
        """
        Vector addition

        Adds the other vector to instance vector
        in vector form A + B
        :param other: other 2D vector
        """
        self.x += other.x
        self.y += other.y

    def __add__(self, other: Vector2D) -> Vector2D:
        """
        Add operator override

        Adds the other vector to instance vector
        in vector form A + B
        :param other: other 2D vector
        :return vector equal to A + B
        """
        new_vector = self.copy()
        new_vector.add(other)
        return new_vector

    def sub(self, other: Vector2D) -> None:
        """
        Vector subtraction in place

        Subtracts the other vector from instance vector
        in vector form A - B
        :param other: other 2D vector
        """
        self.x -= other.x
        self.y -= other.y

    def __sub__(self, other: Vector2D) -> Vector2D:
        """
        Operator Vector subtraction

        Subtracts the other vector from instance vector
        in vector form A - B
        :param other: other 2D vector
        :return vector equal to A - B
        """
        new_vector = self.copy()
        new_vector.sub(other)
        return new_vector

    def mul(self, scalar: Numerics) -> None:
        """
        Vector multiplication in place

        scales the vector by given scalar or to the max limit defined by
        Vector2D.limit() function
        in vector form A * n
        :param scalar: the scale multiplier
        """
        self.x *= scalar
        self.y *= scalar

    def __mul__(self, scalar: Numerics) -> Vector2D:
        """
        Operator Vector multiplication

        scales the vector by given scalar or to the max limit defined by
        Vector2D.limit() function
        in vector form A * n
        :param scalar: the scale multiplier
        :param scalar: the scale multiplier
        :return: the scaled vector
        """
        new_vector = self.copy()
        new_vector.mul(scalar)
        return new_vector

    def div(self, scalar: Numerics) -> None:
        """
        Vector division in place

        scales the vector by given scalar
        in vector form A / n
        :param scalar: the scale multiplier
        """
        if scalar == 0:
            raise ZeroDivisionError("Scaler cannot be zero")

        self.x /= scalar
        self.y /= scalar

    def magnitude(self) -> float:
        """
        Vector magnitude

        Calculates the magnitude of the vector
        in vector form |A|
        :return: Magnitude of the instance vector
        """
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self) -> None:
        """
        Vector normalization

        Normalizes the instance vector
        if magnitude is 0, exits safely
        """
        mag = self.magnitude()
        try:
            self.div(mag)
        except ZeroDivisionError:
            pass

    def set_mag(self, mag: int) -> None:
        """
        Set vector magnitude

        Sets the magnitude of the vector
        :param mag: the new magnitude of the vector
        """
        self.normalize()
        self.mul(mag)

    def clamp(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Clamps vector magnitude

        clamps the vector within an lower and an upperbound
        :param x1: lower x value
        :param y1: lower y value
        :param x2: upper x value
        :param y2: upper y value
        """
        self.x = x1 if self.x < x1 else x2 if self.x > x2 else self.x
        self.y = y1 if self.y < y1 else y2 if self.y > y2 else self.y

    def dot(self, other: Vector2D) -> Numerics:
        """
        Dot product

        dot product of two vectors
        in vector form A • B
        :param other: other 2D vector
        :return: the value of A • B
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other: Vector2D) -> Numerics:
        """
        z-component cross product

        z-component of cross product of two vectors
        in vector form of A × B
        :param other: other 2D vector
        :return: value of A × B
        """
        return self.x * other.y - other.x * self.y

    def angle_between(self, other: Vector2D) -> float:
        """
        Angle between vectors

        calculates the angle between two 2 Dimensional vectors
        :param other: the other vector
        :return: the angle between the A and B
        """
        dot = self.dot(other)
        mag = self.magnitude() + other.magnitude()
        return acos(dot / mag)

    def copy(self) -> Vector2D:
        """
        Copy method

        :return: Deep copy of the instance vector
        """
        return Vector2D(self.x, self.y)
