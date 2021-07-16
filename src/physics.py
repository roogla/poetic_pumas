from __future__ import annotations

from . import element_data
from .elements.space import is_space_element
from .movement import Movement
from .vector2D import Vector2D


class RigidBody:
    """Imitates rigitbody movements on elements using statis methods. Utilizes Vector2D class"""

    @staticmethod
    def drop(data: element_data.ElementData, position: Vector2D) -> Vector2D:
        """Applies drop

        :param data: The element data
        :param position: Position of the element
        :return tuple of boolean successful drop and new position
        """
        one_below = position + Movement.DOWN
        while is_space_element(data.level.get_element_at_position(one_below)):
            one_below.add(Movement.DOWN)

        new_position = one_below + Movement.UP

        return new_position

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
            data.soundboard.play_sfx("step")
        else:
            destination = curr_position
            data.soundboard.play_sfx("bump")

        destination = RigidBody.drop(data, destination)
        data.level.move_element(curr_position, destination)

        return destination
