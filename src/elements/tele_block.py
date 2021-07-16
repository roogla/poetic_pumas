from src import elements
from src.movement import Movement
from src.vector2D import Vector2D

from .element_data import ElementData
from .levelelement import LevelElement
from .space import is_space_element

class TelekinesisBlock(LevelElement):
    """The block that gets moved by Telekinesis"""

    level_symbol = "C"
    string_symbol = "🔮"

    def move(self, data: ElementData, direction: Vector2D) -> None:
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
        data.renderer.render_level(data.level)
    
    def drop(self, data: ElementData) -> None:
        """Drop this level element down if hanging over space.
        
        This function is a copy from dude.py so it could be usefull to have
        drop in levelelement.py for every item
        """
        position = data.level.get_element_position(self)
        below = position + Movement.DOWN
        while is_space_element(data.level.get_element_at_position(below)):
            below.add(Movement.DOWN)

        destination = below + Movement.UP

        data.level.move_element(position, destination)

    def move_up(self, data: ElementData) -> None:
        """Move this level element upward according to the rules.

        If there are any objects on top of the block, it cannot move upward.
        """
        self.move(data, Movement.UP)
    
    def move_down(self, data: ElementData) -> None:
        """Move this level element downward according to the rules.

        If there are any objects below the block, it cannot move downward.
        """
        self.move(data, Movement.DOWN)
    
    def move_left(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of the block, he cannot move left.
        """
        self.move(data, Movement.LEFT)

    def move_right(self, data: ElementData) -> None:
        """Move this level element rightward according to the rules.

        If there are any objects to the right of the block, he cannot move right.
        """
        self.move(data, Movement.RIGHT)
    
    def interact(self, data: ElementData) -> None:
        """Gives the controls back to blockdude
        
        Also drops the block before so that it doesn't float
        """
        self.drop(data)
        data.level.change_main_character(elements.Dude)
        
