# from ..level import Level
from src import elements
from src.vector2D import Vector2D

from .element_data import ElementData
from .levelelement import LevelElement
from .space import is_space_element


class Movements:
    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    UP = Vector2D(0, -1)
    DOWN = Vector2D(0, 1)
    UP_LEFT = Vector2D(-1, -1)
    UP_RIGHT = Vector2D(1, 1)

class Dude(LevelElement):
    """Block Dude himself. The main character."""

    level_symbol = "D"
    face = { 'LEFT': '👈', 'RIGHT': '👉'}
    string_symbol = face['LEFT']
    carrying = False

    def move(self, data: ElementData, direction: Movements) -> None:
        """Moves this level element laterally by some number of spaces given.

        The number of spaces can be positive or negative.
        """
        position = data.level.get_element_position(self)
        lateral_position = position + direction
        lateral_element = data.level.get_element_at_position(lateral_position)
        destination = lateral_position

        if is_space_element(lateral_element):
            destination = lateral_position
        else:
            destination = position

        data.level.move_element(position, destination)
        self.drop(data)
        data.renderer.render_level(data.level)

    def drop(self, data: ElementData) -> None:
        position = data.level.get_element_position(self)
        below = position + Movements.DOWN
        while is_space_element(data.level.get_element_at_position(below)):
            below.add(Movements.DOWN)

        destination = below + Movements.UP

        data.level.move_element(position, destination)

    def move_up(self, data: ElementData) -> None:
        if self.string_symbol == self.face['LEFT']:
            self.move(data, Movements.UP + Movements.LEFT)
        if self.string_symbol == self.face['RIGHT']:
            self.move(data, Movements.UP + Movements.RIGHT)

    def move_left(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.string_symbol = self.face['LEFT']
        self.move(data, Movements.LEFT)

    def move_right(self, data: ElementData) -> None:
        """Move this level element rightward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.string_symbol = self.face['RIGHT']
        self.move(data, Movements.RIGHT)

    def interact(self, data: ElementData) -> None:
        pass

    def box_action(self, data: ElementData) -> None:
    
        position = data.level.get_element_position(self)
        if self.string_symbol == self.face['LEFT']:
            lateral_position = position + Movements.LEFT
        if self.string_symbol == self.face['RIGHT']:
            lateral_position = position + Movements.RIGHT

        lateral_element = data.level.get_element_at_position(lateral_position)
        if self.carrying is False:
            if isinstance(lateral_element, elements.Block):
                data.level.move_element(lateral_position, position + Movements.UP)
                self.carrying = True
        if self.carrying is True:
            if isinstance(lateral_element, elements.Space):
                data.level.move_element(position + Movements.UP, lateral_position)
                self.carrying = False

        data.renderer.render_level(data.level)


