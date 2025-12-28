class FigureColor:
    """Класс Цвет фигуры"""

    def __init__(self):
        self._color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            raise ValueError("Цвет должен быть строкой")
        self._color = value
