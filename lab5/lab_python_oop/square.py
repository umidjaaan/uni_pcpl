from .rectangle import Rectangle

class Square(Rectangle):
    """Класс Квадрат"""

    figure_type = "Квадрат"

    def __init__(self, side, color):
        if side <= 0:
            raise ValueError("Сторона должна быть положительным числом")

        super().__init__(side, side, color)

    def __repr__(self):
        return f"{self.figure_type} {self.color.color} цвета со стороной {self.width}. Площадь: {self.area():.2f}"
