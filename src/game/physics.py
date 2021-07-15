from __future__ import annotations

from ..elements.space import is_space_element
from .element_data import ElementData
from .vector2D import Vector2D


class Movements:
    """Movements class to hold all the basic movements"""

    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    UP = Vector2D(0, 1)
    DOWN = Vector2D(0, -1)


class RigidBody:
    """Creates a RigitBody object. Utilizes Vector2D class"""

    def __init__(self, x: int, y: int):
        self.position = Vector2D(x, y)
        self.facing: Vector2D = Movements.LEFT

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position})"

    def drop(self, data: ElementData, position: Vector2D) -> tuple[bool, Vector2D]:
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

    def apply_movement(self, data: ElementData, movement: Vector2D) -> None:
        """
        Apply movement

        Applies the given movement to the body
        :param data: the element data
        :param movement: The movement vector
        """
        """Moves this level element laterally by some number of spaces given.

        The number of spaces can be positive or negative.
        """
        destination = self.position + movement
        lateral_element = data.level.get_element_at_position(destination)

        if is_space_element(lateral_element):

            status, new_destination = self.drop(data, destination)

            if status:
                destination = new_destination

            data.level.move_element(self.position, destination)
            self.position = destination

            data.renderer.render_level(data.level)