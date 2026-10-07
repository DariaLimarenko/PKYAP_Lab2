import math

from lab_python_oop.shape import Shape
from lab_python_oop.color import Color


class Circle(Shape):
    """Круг."""

    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def get_name(cls):
        return cls.name

    def __repr__(self):
        return (
            "{}: радиус = {}, цвет = {}, площадь = {:.2f}"
        ).format(
            self.get_name(),
            self.radius,
            self.color.color,
            self.area()
        )
