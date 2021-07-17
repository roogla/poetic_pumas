from src.elements import LevelElement

from .level import Level
from .vector2D import Vector2D


class Camera(Level):
    """The camera app"""

    def __init__(self, level_elements: list[list[LevelElement]]):
        super().__init__(level_elements)

    @property
    def dimensions(self) -> Vector2D:
        """Property that stores the camera's max dimensions"""
        return Vector2D(18, 12)

    def get_renderable_elements(self) -> list[list[LevelElement]]:
        """
        Get renderable elements

        :return: 2D list containing the renderable elements
        """
        a_pos: LevelElement = self.active_element.position
        cam_top_left: Vector2D = a_pos - self.dimensions // 2
        cam_bottom_right: Vector2D = a_pos + self.dimensions // 2

        top_left: Vector2D = Vector2D(
            x=max(0, min(cam_top_left.x, self.width - self.dimensions.x)),
            y=max(0, min(cam_top_left.y, self.height - self.dimensions.y)),
        )

        bottom_right: Vector2D = Vector2D(
            x=max(min(self.width, cam_bottom_right.x), self.dimensions.x),
            y=max(min(self.height, cam_bottom_right.y), self.dimensions.y),
        )

        return self.get_elements_in_range(top_left, bottom_right)

    def get_elements_in_range(
        self, lower: Vector2D, upper: Vector2D
    ) -> list[list[LevelElement]]:
        """
        Gets elements in the provided range

        :param lower: the lower limit to start at
        :param upper: the upper limit to stop at
        :return: list of elements in range
        """

        def is_valid_position(position: Vector2D) -> bool:
            return lower.x <= position.x <= upper.x and lower.y <= position.y <= upper.y

        in_range: list[list[LevelElement]] = [
            [element for element in row if is_valid_position(element.position)]
            for row in self.level_elements
        ]

        # to filter empty lists created by the list comprehension above
        in_range = list(filter(lambda lst: lst, in_range))

        return in_range
