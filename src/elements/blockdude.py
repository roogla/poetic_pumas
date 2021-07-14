# from ..level import Level
from ..Vector2D import Vector2D
from .element_data import ElementData
from .levelelement import LevelElement
from .space import is_space_element


class BlockDude(LevelElement):
    """Block Dude himself. The main character."""

    level_symbol = "D"
    string_symbol = "🤷"

    def move_laterally(self, data: ElementData, spaces: int = 1) -> None:
        """Moves this level element laterally by some number of spaces given.

        The number of spaces can be positive or negative.
        """
        position = data.level.get_element_position(self)
        lateral_position = position + Vector2D(spaces, 0)
        lateral_element = data.level.get_element_at_position(lateral_position)
        destination = lateral_position

        if not is_space_element(lateral_element):
            # the element directly up and laterally
            one_up_and_lateral_position = position + Vector2D(spaces, -1)
            one_up_lateral_element = data.level.get_element_at_position(
                one_up_and_lateral_position
            )

            # if there's a block above the one in the way
            if not is_space_element(one_up_lateral_element):
                return
            destination = one_up_and_lateral_position

        data.level.move_element(position, destination)
        data.renderer.render_level(data.level)

    def move_left(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.move_laterally(data, spaces=-1)

    def move_right(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.move_laterally(data, spaces=1)
