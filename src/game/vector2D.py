from __future__ import annotations

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

    def __floordiv__(self, scalar: Numerics) -> Vector2D:
        """
        Floor divide vector operation

        Divides the vector into floored version
        :param scalar: the scale multiplier
        :return: the scaled vector
        """
        if scalar == 0:
            raise ZeroDivisionError("Scalar cannot be zero")
        return Vector2D(self.x // scalar, self.y // scalar)

    def div(self, scalar: Numerics) -> None:
        """
        Vector division in place

        scales the vector by given scalar
        in vector form A / n
        :param scalar: the scale multiplier
        """
        if scalar == 0:
            raise ZeroDivisionError("Scalar cannot be zero")

        self.x /= scalar
        self.y /= scalar

    def __truediv__(self, scalar: Numerics) -> Vector2D:
        """
        True dividion vector operation

        Divides the vector into floored version
        :param scalar: the scale multiplier
        :return: the scaled vector
        """
        if scalar == 0:
            raise ZeroDivisionError("Scalar cannot be zero")
        new_vector = self.copy()
        new_vector.div(scalar=scalar)
        return new_vector

    def copy(self) -> Vector2D:
        """
        Copy method

        :return: Deep copy of the instance vector
        """
        return Vector2D(self.x, self.y)
