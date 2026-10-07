from abc import ABC, abstractmethod


class Shape(ABC):
    """Абстрактный класс геометрической фигуры."""

    @abstractmethod
    def area(self):
        """Вычислить площадь фигуры."""
        pass
