# from ..level import Level
from ..position import Position
from .element_data import ElementData
from .levelelement import LevelElement
from .space import Space


class BlockDude(LevelElement):
    """Block Dude himself. The main character."""

    level_symbol = "D"
    string_symbol = "Á"

    def move_left(self, data: ElementData) -> None:
        """Give the new position for the block dude when moving left.

        If there are any objects to the left of block dude, he cannot move left.
        """

        position = data.level.get_element_position(self)
        one_unit_leftward = position + Position(-1, 0)
        left_element = data.level.get_element_at_position(one_unit_leftward)
        data.level.move_element(position, one_unit_leftward)
        # TODO: Something with renderer
        # print(data.level

        if isinstance(left_element, Space):
            return one_unit_leftward
        return position
