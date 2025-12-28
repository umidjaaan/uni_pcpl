import random

def gen_random(num_count, begin, end):
    """
    Генератор случайных чисел в заданном диапазоне

    Args:
        num_count: количество случайных чисел
        begin: начало диапазона (включительно)
        end: конец диапазона (включительно)

    Yields:
        Случайные целые числа в диапазоне [begin, end]
    """
    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == "__main__":
    print("Тест 1: 5 чисел в диапазоне от 1 до 3")
    print("Ожидается: 5 случайных чисел от 1 до 3 включительно")
    print("Результат:", end=" ")
    for num in gen_random(5, 1, 3):
        print(num, end=", ")
    print("\n")

    print("Тест 2: 3 числа в диапазоне от 10 до 10 (постоянное значение)")
    print("Ожидается: 10, 10, 10")
    print("Результат:", end=" ")
    for num in gen_random(3, 10, 10):
        print(num, end=", ")
    print("\n")

    print("Тест 3: 8 чисел в диапазоне от -5 до 5")
    print("Ожидается: 8 случайных чисел от -5 до 5 включительно")
    print("Результат:", end=" ")
    for num in gen_random(8, -5, 5):
        print(num, end=", ")
    print("\n")

    print("Тест 4: 0 чисел (пустой результат)")
    print("Ожидается: ничего не выведется")
    print("Результат:", end=" ")
    for num in gen_random(0, 1, 100):
        print(num, end=", ")
    print("(ничего не выведено)")
    print()

    print("Тест 5: 7 чисел в диапазоне от 100 до 200")
    print("Ожидается: 7 случайных чисел от 100 до 200 включительно")
    result = list(gen_random(7, 100, 200))
    print(f"Результат: {result}")
    print(f"Количество чисел: {len(result)}")
    print(f"Все числа в диапазоне: {all(100 <= x <= 200 for x in result)}")
