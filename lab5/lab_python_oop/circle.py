import math
from .figure import Figure
from .color import FigureColor

class Circle(Figure):
    """Класс Круг"""

    figure_type = "Круг"

    def __init__(self, radius, color):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")

        self.radius = radius
        self.color = FigureColor()
        self.color.color = color

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"{self.figure_type} {self.color.color} цвета радиусом {self.radius}. Площадь: {self.area():.2f}"
