from __future__ import annotations
from typing import Union
from typing import Optional
from math import acos
from math import sqrt


class Vector2D:
    """2 Dimensional vector math class. Implements vector operations."""

    def __init__(self, x: Union[float, int], y: Union[float, int]):
        self._x = x
        self._y = y
        self._limit: Optional[float, int] = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._x},{self._y})"

    def add(self, other: Vector2D) -> None:
        """
        Vector addition

        Adds the other vector to instance vector
        in vector form A + B
        :param other: other 2D vector
        """
        self._x += other._x
        self._y += other._y

    def sub(self, other: Vector2D) -> None:
        """
        Vector subtraction

        Subtracts the other vector from instance vector
        in vector form A - B
        :param other: other 2D vector
        """
        self._x -= other._x
        self._y -= other._y

    def mult(self, scaler: Union[float, int]) -> None:
        """
        Vector multiplication

        scales the vector by given scaler or to the max limit defined by
        Vector2D.limit() function
        in vector form A * n
        :param scaler: the scale multiplier
        """
        if self._limit is not None:
            scaler = max(self._limit, scaler)

        self._x *= scaler
        self._y *= scaler

    def div(self, scaler: Union[float, int]) -> None:
        """
        Vector division

        scales the vector by given scaler
        in vector form A / n
        :param scaler: the scale multiplier
        """
        if scaler == 0:
            raise ZeroDivisionError("Scaler cannot be zero")

        self._x /= scaler
        self._y /= scaler

    def magnitude(self) -> Union[float, int]:
        """
        Vector magnitude

        Calculates the magnitude of the vector
        in vector form |A|
        :return: Magnitude of the instance vector
        """
        return sqrt(self._x ** 2 + self._y ** 2)

    def normalize(self) -> None:
        """
        Vector normalization

        Normalizes the instance vecter
        if magnitude is 0, exits safely
        """
        mag = self.magnitude()
        try:
            self.div(mag)
        except ZeroDivisionError:
            pass

    def set_mag(self, mag: Union[float, int]) -> None:
        """
        Set vector magnitude

        Sets the magnitude of the vector
        :param mag: the new magnitude of the vector
        """
        self.normalize()
        self.mult(mag)

    def limit(self, limit: Union[float, int]) -> None:
        """
        Limit vector

        limits the vector to an upperbound
        :param limit: the limit to be set on vector
        """
        self._limit = limit
        self.set_mag(self._limit)

    def dot(self, other: Vector2D) -> Union[float, int]:
        """
        Dot product

        dot product of two vectors
        in vector form A • B
        :param other: other 2D vector
        :return: the value of A • B
        """
        return self._x * other._x + self._y * other._y

    def cross(self, other: Vector2D) -> Union[float, int]:
        """
        Cross product

        cross product of two vectors
        in vector form of A × B
        :param other: other 2D vector
        :return: value of A × B
        """
        return self._x * other._y - other._x * self._y

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
