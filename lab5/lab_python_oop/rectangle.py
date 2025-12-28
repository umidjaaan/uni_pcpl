from .figure import Figure
from .color import FigureColor

class Rectangle(Figure):
    """Класс Прямоугольник"""

    figure_type = "Прямоугольник"

    def __init__(self, width, height, color):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами")

        self.width = width
        self.height = height
        self.color = FigureColor()
        self.color.color = color

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"{self.figure_type} {self.color.color} цвета шириной {self.width} и высотой {self.height}. Площадь: {self.area():.2f}"
