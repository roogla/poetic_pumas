from .elements import LevelElement
from .level import Level
from .vector2D import Vector2D


class Camera(Level):
    """The camera app"""

    _RADII: Vector2D = Vector2D(6, 9)

    def get_renderable_elements(self) -> list[list[LevelElement]]:
        """
        Get renderable elements

        :return: 2D list containing the renderable elements
        """
        active_elem = self.active_element
        top_left = active_elem.position - self._RADII
        top_left.clamp(0, 0, self.width, self.height)
        bot_right = active_elem.position + self._RADII
        bot_right.clamp(0, 0, self.width, self.height)
        return self.get_elements_in_range(top_left, bot_right)

    def get_elements_in_range(
        self, lower: Vector2D, upper: Vector2D
    ) -> list[list[LevelElement]]:
        """
        Gets elements in the provided range

        :param lower: the lower limit to start at
        :param upper: the upper limit to stop at
        :return: list of elements in range
        """
        in_range: list[list[LevelElement]] = [
            [element for element in row if lower <= element.position <= upper]
            for row in self.level_elements
        ]

        return in_range
