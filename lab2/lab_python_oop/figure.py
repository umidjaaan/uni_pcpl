from abc import ABC, abstractmethod

class Figure(ABC):
    """
    Абстрактный класс Геометрическая фигура
    """

    @property
    @abstractmethod
    def figure_type(self):
        """Возвращает название фигуры"""
        pass

    @abstractmethod
    def area(self):
        """Вычисляет площадь фигуры"""
        pass

    def __repr__(self):
        """Строковое представление фигуры"""
        return "{} {} цвета площадью {:.2f}".format(
            self.figure_type,
            self.color.color,
            self.area()
        )
