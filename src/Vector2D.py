from __future__ import annotations

from math import acos, sqrt
from typing import Union


class Vector2D:
    """2 Dimensional vector math class. Implements vector operations."""

    def __init__(self, x: int = 0, y: int = 0):
        self._x = x
        self._y = y
        self._limit: Union[float, int, None] = None

    @property
    def x(self) -> int:
        """Get x"""
        return self._x

    @property
    def y(self) -> int:
        """Get y"""
        return self._y

    @x.setter
    def x(self, value: int) -> None:
        """Set x"""
        self._x = value

    @y.setter
    def y(self, value: int) -> None:
        """Set y"""
        self._y = value

    def __repr__(self) -> str:
        """repr method for class"""
        return f"{self.__class__.__name__}({self.x},{self.y})"

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
        Vector subtraction

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

    def mul(self, scalar: int) -> None:
        """
        Vector multiplication

        scales the vector by given scalar or to the max limit defined by
        Vector2D.limit() function
        in vector form A * n
        :param scalar: the scale multiplier
        """
        if self._limit is not None:
            scalar = max(self._limit, scalar)

        self.x *= scalar
        self.y *= scalar

    def __mul__(self, scalar: int) -> Vector2D:
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

    def div(self, scalar: Union[int, float]) -> None:
        """
        Vector division

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
        Limit vector

        limits the vector to an upperbound
        :param limit: the limit to be set on vector
        """
        self._limit = limit
        self.set_mag(self._limit)

    def dot(self, other: Vector2D) -> int:
        """
        Dot product

        dot product of two vectors
        in vector form A • B
        :param other: other 2D vector
        :return: the value of A • B
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other: Vector2D) -> int:
        """
        Cross product

        cross product of two vectors
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
