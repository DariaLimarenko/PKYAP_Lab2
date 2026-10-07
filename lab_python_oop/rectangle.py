from lab_python_oop.shape import Shape
from lab_python_oop.color import Color


class Rectangle(Shape):
    """Прямоугольник."""

    name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def area(self):
        return self.width * self.height

    @classmethod
    def get_name(cls):
        return cls.name

    def __repr__(self):
        return (
            "{}: ширина = {}, высота = {}, цвет = {}, площадь = {:.2f}"
        ).format(
            self.get_name(),
            self.width,
            self.height,
            self.color.color,
            self.area()
        )
