from abc import ABC, abstractmethod

class Figure(ABC):
    """Абстрактный класс Геометрическая фигура"""

    @property
    @abstractmethod
    def figure_type(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def __repr__(self):
        return f"{self.figure_type} {self.color.color} цвета площадью {self.area():.2f}"
