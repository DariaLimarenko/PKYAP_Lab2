import math
import unittest

from lab_python_oop.shape import Shape
from lab_python_oop.color import Color
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


class TestShapes(unittest.TestCase):
    """Проверка классов геометрических фигур."""

    def test_shape_is_abstract(self):
        # Объект абстрактного класса создавать нельзя.
        with self.assertRaises(TypeError):
            Shape()

    def test_color_property(self):
        # Проверяем чтение и изменение свойства цвета.
        color = Color("синий")
        self.assertEqual(color.color, "синий")

        color.color = "красный"
        self.assertEqual(color.color, "красный")

    def test_rectangle(self):
        # Разные стороны помогают проверить формулу площади.
        rectangle = Rectangle(4, 6, "синий")

        self.assertIsInstance(rectangle, Shape)
        self.assertIsInstance(rectangle.color, Color)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.color.color, "синий")
        self.assertEqual(rectangle.area(), 24)

    def test_circle(self):
        circle = Circle(3, "зелёный")

        self.assertIsInstance(circle, Shape)
        self.assertIsInstance(circle.color, Color)
        self.assertEqual(circle.radius, 3)
        self.assertEqual(circle.color.color, "зелёный")
        self.assertAlmostEqual(circle.area(), 9 * math.pi)

    def test_square(self):
        square = Square(5, "красный")

        self.assertIsInstance(square, Rectangle)
        self.assertIsInstance(square.color, Color)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.color.color, "красный")
        self.assertEqual(square.area(), 25)

    def test_class_names(self):
        self.assertEqual(Rectangle.get_name(), "Прямоугольник")
        self.assertEqual(Circle.get_name(), "Круг")
        self.assertEqual(Square.get_name(), "Квадрат")

    def test_repr(self):
        self.assertEqual(
            repr(Rectangle(4, 6, "синий")),
            "Прямоугольник: ширина = 4, высота = 6, "
            "цвет = синий, площадь = 24.00"
        )
        self.assertEqual(
            repr(Circle(3, "зелёный")),
            "Круг: радиус = 3, цвет = зелёный, площадь = 28.27"
        )
        self.assertEqual(
            repr(Square(5, "красный")),
            "Квадрат: сторона = 5, цвет = красный, площадь = 25.00"
        )


if __name__ == "__main__":
    unittest.main()
