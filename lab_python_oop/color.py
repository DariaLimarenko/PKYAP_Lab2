class Color:
    """Цвет геометрической фигуры."""

    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        """Получить цвет."""
        return self._color

    @color.setter
    def color(self, value):
        """Изменить цвет."""
        self._color = value
