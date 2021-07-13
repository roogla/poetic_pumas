from __future__ import annotations
from typing import Union
from typing import Optional
from math import acos
from math import sqrt


class Vector2D:
    """
    2 Dimensional vector math class. Implements vector operations.
    """

    def __init__(self, x: Union[float, int], y: Union[float, int]):
        self._x = x
        self._y = y
        self._limit: Optional[float, int] = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._x},{self._y})"

    def add(self, other: Vector2D) -> None:
        """
        adds the other vector to instance vector
        in vector form A + B
        :param other: other 2D vector
        """
        self._x += other._x
        self._y += other._y

    def sub(self, other: Vector2D) -> None:
        """
        subtracts the other vector from instance vector
        in vector form A - B
        :param other: other 2D vector
        """
        self._x -= other._x
        self._y -= other._y

    def mult(self, scaler: Union[float, int]) -> None:
        """
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
        :return: Magnitude of the instance vector
        """
        return sqrt(self._x ** 2 + self._y ** 2)

    def normalize(self) -> None:
        """
        Normalizes the vecter
        """
        mag = self.magnitude()
        self.div(mag)

    def set_mag(self, mag: Union[float, int]) -> None:
        """
        Sets the magnitude of the vector
        :param mag: the new magnitude of the vector
        """
        self.normalize()
        self.mult(mag)

    def limit(self, limit: Union[float, int]):
        self._limit = limit
        self.set_mag(self._limit)

    def dot(self, other: Vector2D) -> Union[float, int]:
        """
        dot product of two vectors
        in vector form A • B
        :param other: other 2D vector
        :return: the value of A • B
        """
        return self._x * other._x + self._y * other._y

    def cross(self, other: Vector2D) -> Union[float, int]:
        """
        cross product of two vectors
        in vector form of A × B
        :param other: other 2D vector
        :return: value of A × B
        """
        return self._x * other._y - other._x * self._y

    def angle_between(self, other: Vector2D) -> float:
        """
        calculates the angle between two 2 Dimensional vectors
        :param other: the other vector
        :return: the angle between the A and B
        """
        dot = self.dot(other)
        mag = self.magnitude() + other.magnitude()
        return acos(dot / mag)
