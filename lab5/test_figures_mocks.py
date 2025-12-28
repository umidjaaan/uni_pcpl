import unittest
from unittest.mock import Mock, patch, MagicMock
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle

class TestFiguresWithMocks(unittest.TestCase):
    """Тесты с использованием Mock-объектов"""

    def test_rectangle_with_mock_color(self):
        """Тест прямоугольника с mock-объектом цвета"""
        # Arrange - создаем mock для цвета
        mock_color = Mock()
        mock_color.color = "синий"

        # Создаем прямоугольник и подменяем его цвет
        rect = Rectangle(5, 3, "синий")
        rect.color = mock_color

        # Act
        representation = str(rect)

        # Assert - проверяем, что цвет использовался в представлении
        mock_color.__str__.assert_not_called()  # Проверяем, что не вызывался как строка
        self.assertIn("синий", representation)

    def test_circle_area_with_mocked_pi(self):
        """Тест площади круга с mock-значением pi"""
        # Arrange
        circle = Circle(5, "красный")

        # Act & Assert - подменяем math.pi
        with patch('math.pi', 3.14):
            area = circle.area()
            expected_area = 3.14 * 25
            self.assertEqual(area, expected_area)

    def test_figure_representation_with_mock(self):
        """Тест строкового представления с mock-объектом"""
        # Arrange - создаем mock-фигуру
        mock_figure = MagicMock()
        mock_figure.figure_type = "ТестоваяФигура"
        mock_figure.color.color = "золотой"
        mock_figure.area.return_value = 42.0

        # Act
        representation = f"{mock_figure.figure_type} {mock_figure.color.color} цвета площадью {mock_figure.area():.2f}"

        # Assert
        self.assertEqual(representation, "ТестоваяФигура золотой цвета площадью 42.00")
        mock_figure.area.assert_called_once()

if __name__ == '__main__':
    unittest.main(verbosity=2)
