from __future__ import annotations

from math import acos, inf, sqrt
from typing import Union, Optional

Numerics = Union[float, int]


class Vector2D:
    """2 Dimensional vector math class. Implements vector operations."""

    def __init__(
        self, x: Numerics = 0, y: Numerics = 0, scalar_limit: Optional[Numerics] = None
    ):
        self._x = x
        self._y = y
        # The magnitude of the scalar limit
        if scalar_limit is None:
            self.scalar_limit: Numerics = inf
        else:
            self.scalar_limit: Numerics = scalar_limit

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x},{self.y})"

    @property
    def x(self) -> Numerics:
        """Get x"""
        return self._x

    @property
    def y(self) -> Numerics:
        """Get y"""
        return self._y

    @x.setter
    def x(self, value: Numerics) -> None:
        """Set x"""
        self._x = value

    @y.setter
    def y(self, value: Numerics) -> None:
        """Set y"""
        self._y = value

    def __eq__(self, other: Vector2D) -> bool:
        return self.x == other.x and self.y == other.y

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
        if abs(scalar) > self.scalar_limit:
            # the sign for the scalar (+1 or -1)
            sign = abs(scalar) // scalar
            scalar = sign * self.scalar_limit

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

    def limit(self, limit: int) -> None:
        """
        Limit vector magnitude

        limits the vector to an upperbound
        :param limit: the limit to be set on vector
        """
        self.scalar_limit = limit
        self.set_mag(self.scalar_limit)

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
