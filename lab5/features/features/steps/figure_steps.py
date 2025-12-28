from behave import given, when, then
import math
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

@given('прямоугольник с шириной {width}, высотой {height} и цветом "{color}"')
def step_create_rectangle(context, width, height, color):
    context.rectangle = Rectangle(float(width), float(height), color)

@given('круг с радиусом {radius} и цветом "{color}"')
def step_create_circle(context, radius, color):
    context.circle = Circle(float(radius), color)

@given('квадрат со стороной {side} и цветом "{color}"')
def step_create_square(context, side, color):
    context.square = Square(float(side), color)

@when('я вычисляю площадь прямоугольника')
def step_calculate_rectangle_area(context):
    context.calculated_area = context.rectangle.area()

@when('я вычисляю площадь круга')
def step_calculate_circle_area(context):
    context.calculated_area = context.circle.area()

@when('я вычисляю площадь квадрата')
def step_calculate_square_area(context):
    context.calculated_area = context.square.area()

@then('площадь должна быть {expected_area}')
def step_verify_area(context, expected_area):
    assert abs(context.calculated_area - float(expected_area)) < 0.01

@then('тип фигуры должен быть "{expected_type}"')
def step_verify_figure_type(context, expected_type):
    if hasattr(context, 'rectangle'):
        assert context.rectangle.figure_type == expected_type
    elif hasattr(context, 'circle'):
        assert context.circle.figure_type == expected_type
    elif hasattr(context, 'square'):
        assert context.square.figure_type == expected_type

@then('цвет фигуры должен быть "{expected_color}"')
def step_verify_figure_color(context, expected_color):
    if hasattr(context, 'rectangle'):
        assert context.rectangle.color.color == expected_color
    elif hasattr(context, 'circle'):
        assert context.circle.color.color == expected_color
    elif hasattr(context, 'square'):
        assert context.square.color.color == expected_color
