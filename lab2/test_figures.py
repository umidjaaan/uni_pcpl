#!/usr/bin/env python3
"""
Модульные тесты для геометрических фигур
"""
import unittest
import math
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

class TestFigures(unittest.TestCase):
    """
    Тестовый класс для геометрических фигур
    """

    def test_rectangle(self):
        """Тест для прямоугольника"""
        rect = Rectangle(5, 3, "синий")

        self.assertEqual(rect.area(), 15)
        self.assertEqual(rect.figure_type, "Прямоугольник")
        self.assertEqual(rect.color.color, "синий")
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)

    def test_circle(self):
        """Тест для круга"""
        circle = Circle(5, "зеленый")

        expected_area = math.pi * 25
        self.assertAlmostEqual(circle.area(), expected_area)
        self.assertEqual(circle.figure_type, "Круг")
        self.assertEqual(circle.color.color, "зеленый")
        self.assertEqual(circle.radius, 5)

    def test_square(self):
        """Тест для квадрата"""
        square = Square(4, "красный")

        self.assertEqual(square.area(), 16)
        self.assertEqual(square.figure_type, "Квадрат")
        self.assertEqual(square.color.color, "красный")
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)

    def test_square_inheritance(self):
        """Тест наследования квадрата от прямоугольника"""
        square = Square(4, "красный")

        self.assertIsInstance(square, Rectangle)

    def test_repr_methods(self):
        """Тест строкового представления объектов"""
        rect = Rectangle(5, 3, "синий")
        circle = Circle(5, "зеленый")
        square = Square(4, "красный")

        self.assertIsInstance(str(rect), str)
        self.assertIsInstance(str(circle), str)
        self.assertIsInstance(str(square), str)

        self.assertIn("Прямоугольник", str(rect))
        self.assertIn("Круг", str(circle))
        self.assertIn("Квадрат", str(square))
        self.assertIn("синий", str(rect))
        self.assertIn("зеленый", str(circle))
        self.assertIn("красный", str(square))

if __name__ == "__main__":
    unittest.main(verbosity=2)
