#!/usr/bin/env python3
"""
Основной файл программы для тестирования классов геометрических фигур
"""
import math
from colorama import Fore, Back, Style, init
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

init(autoreset=True)

def main():
    """
    Основная функция программы
    """
    print(Fore.CYAN + Back.WHITE + "=" * 60)
    print(Fore.CYAN + Back.WHITE + "ЛАБОРАТОРНАЯ РАБОТА №2")
    print(Fore.CYAN + Back.WHITE + "ГЕОМЕТРИЧЕСКИЕ ФИГУРЫ")
    print(Fore.CYAN + Back.WHITE + "=" * 60)

    N = 5

    print(Fore.GREEN + "\nСОЗДАНИЕ ОБЪЕКТОВ:")

    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(Fore.YELLOW + "\nИНФОРМАЦИЯ О ФИГУРАХ:")
    print(Fore.WHITE + f"1. {rectangle}")
    print(Fore.WHITE + f"2. {circle}")
    print(Fore.WHITE + f"3. {square}")

    print(Fore.MAGENTA + "\nДЕМОНСТРАЦИЯ ВНЕШНЕГО ПАКЕТА COLORAMA:")
    print(Fore.RED + "Этот текст красного цвета")
    print(Fore.GREEN + "Этот текст зеленого цвета")
    print(Fore.BLUE + "Этот текст синего цвета")
    print(Back.YELLOW + Fore.BLACK + "Этот текст на желтом фоне")
    print(Style.BRIGHT + "Этот текст жирный")

    print(Fore.CYAN + "\nДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ:")
    print(f"Использованное значение N: {N}")
    print(f"Значение π из math: {math.pi:.6f}")

    print(Fore.CYAN + "\nПРОВЕРКА ТИПОВ ФИГУР:")
    print(f"Тип rectangle: {rectangle.figure_type}")
    print(f"Тип circle: {circle.figure_type}")
    print(f"Тип square: {square.figure_type}")

    print(Fore.CYAN + "\n" + "=" * 60)
    print("ПРОГРАММА ЗАВЕРШЕНА")

if __name__ == "__main__":
    main()
