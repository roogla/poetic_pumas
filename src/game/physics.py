from __future__ import annotations

from ..elements.space import is_space_element
from . import element_data
from .vector2D import Vector2D


class Movements:
    """Movements class to hold all the basic movements"""

    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    UP = Vector2D(0, -1)
    DOWN = Vector2D(0, 1)


class RigidBody:
    """Imitates rigitbody movements on elements using statis methods. Utilizes Vector2D class"""

    @staticmethod
    def drop(data: element_data.ElementData, position: Vector2D) -> tuple[bool, Vector2D]:
        """Applies drop

        :param data: The element data
        :param position: Position of the element
        :return tuple of boolean successful drop and new position
        """
        one_below = position + Movements.DOWN
        while is_space_element(data.level.get_element_at_position(one_below)):
            one_below.add(Movements.DOWN)

        new_position = one_below + Movements.UP

        if new_position == position:
            return False, position

        return True, new_position

    @staticmethod
    def apply_movement(data: element_data.ElementData, movement: Vector2D) -> Vector2D:
        """
        Apply movement

        Applies the given movement to the body
        :param data: the element data
        :param movement: The movement vector
        """
        """Moves this level element laterally by some number of spaces given.

        The number of spaces can be positive or negative.
        """
        curr_position = data.level_element.position
        destination = curr_position + movement
        lateral_element = data.level.get_element_at_position(destination)

        if is_space_element(lateral_element):
            status, new_destination = RigidBody.drop(data, destination)
            if status:
                destination = new_destination
            data.level.move_element(curr_position, destination)
            return destination

        return curr_position
