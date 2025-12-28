import unittest
import math
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.color import FigureColor

class TestFiguresTDD(unittest.TestCase):
    """TDD тесты для геометрических фигур"""

    def test_rectangle_area_calculation(self):
        """Тест вычисления площади прямоугольника"""
        # Arrange
        rect = Rectangle(5, 3, "синий")

        # Act
        area = rect.area()

        # Assert
        self.assertEqual(area, 15)

    def test_circle_area_calculation(self):
        """Тест вычисления площади круга"""
        # Arrange
        circle = Circle(5, "красный")

        # Act
        area = circle.area()

        # Assert
        expected_area = math.pi * 25
        self.assertAlmostEqual(area, expected_area, places=2)

    def test_square_inheritance(self):
        """Тест наследования квадрата от прямоугольника"""
        # Arrange & Act
        square = Square(4, "зеленый")

        # Assert
        self.assertIsInstance(square, Rectangle)
        self.assertEqual(square.figure_type, "Квадрат")

    def test_invalid_rectangle_dimensions(self):
        """Тест валидации некорректных размеров прямоугольника"""
        # Arrange & Act & Assert
        with self.assertRaises(ValueError):
            Rectangle(-5, 3, "синий")

    def test_color_validation(self):
        """Тест валидации цвета"""
        # Arrange
        color = FigureColor()

        # Act & Assert
        with self.assertRaises(ValueError):
            color.color = 123  # Не строка

    def test_figure_representation(self):
        """Тест строкового представления фигур"""
        # Arrange
        rect = Rectangle(5, 3, "синий")

        # Act
        representation = str(rect)

        # Assert
        self.assertIn("Прямоугольник", representation)
        self.assertIn("синий", representation)
        self.assertIn("15.00", representation)

if __name__ == '__main__':
    # Запуск тестов с детализированным выводом
    unittest.main(verbosity=2)
