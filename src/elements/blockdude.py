# from ..level import Level
from ..position import Position
from .element_data import ElementData
from .levelelement import LevelElement
from .space import is_space_element


class BlockDude(LevelElement):
    """Block Dude himself. The main character."""

    level_symbol = "D"
    string_symbol = "Á"

    def move_left(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        position = data.level.get_element_position(self)
        one_unit_leftward = position + Position(-1, 0)
        left_element = data.level.get_element_at_position(one_unit_leftward)

        if not is_space_element(left_element):
            return

        data.level.move_element(position, one_unit_leftward)
        data.renderer.update_level_render(data.level)

    def move_right(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        position = data.level.get_element_position(self)
        one_unit_rightward = position + Position(1, 0)
        left_element = data.level.get_element_at_position(one_unit_rightward)

        if not is_space_element(left_element):
            return

        data.level.move_element(position, one_unit_rightward)
        data.renderer.update_level_render(data.level)
