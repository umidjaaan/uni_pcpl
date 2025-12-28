class Unique(object):
    """
    Итератор для удаления дубликатов
    """

    def __init__(self, items, **kwargs):
        """
        Конструктор итератора

        Args:
            items: массив или генератор данных
            **kwargs: именованные параметры, включая ignore_case
        """
        self.ignore_case = kwargs.get('ignore_case', False)

        self.items = iter(items)

        self.seen = set()

        self.next_item = None

    def __iter__(self):
        """Возвращает сам объект как итератор"""
        return self

    def __next__(self):
        """Возвращает следующий уникальный элемент"""
        while True:
            try:
                item = next(self.items)
            except StopIteration:
                raise StopIteration

            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item

            if key not in self.seen:
                self.seen.add(key)
                return item


if __name__ == "__main__":
    print("Тест 1: числа с дубликатами")
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 1, 2, 3]
    print(f"Исходные данные: {data}")
    print("Ожидается: 1, 2, 3")
    print("Результат:", end=" ")
    for item in Unique(data):
        print(item, end=", ")
    print("\n")

    print("Тест 2: строки без ignore_case")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(f"Исходные данные: {data}")
    print("Ожидается: a, A, b, B")
    print("Результат:", end=" ")
    for item in Unique(data):
        print(item, end=", ")
    print("\n")

    print("Тест 3: строки с ignore_case=True")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(f"Исходные данные: {data}")
    print("Ожидается: a, b")
    print("Результат:", end=" ")
    for item in Unique(data, ignore_case=True):
        print(item, end=", ")
    print("\n")

    print("Тест 4: работа с генератором")
    from gen_random import gen_random
    data = gen_random(10, 1, 3)
    print("Генератор: 10 случайных чисел от 1 до 3")
    print("Ожидается: только уникальные числа 1, 2, 3 (в случайном порядке)")
    print("Результат:", end=" ")
    result = list(Unique(data))
    result.sort()
    print(result)
    print()

    print("Тест 5: смешанные данные с ignore_case")
    data = ['Hello', 'hello', 'WORLD', 'world', 'Hello', 'TEST']
    print(f"Исходные данные: {data}")
    print("Ожидается с ignore_case=False: Hello, hello, WORLD, world, TEST")
    print("Результат:", end=" ")
    for item in Unique(data):
        print(item, end=", ")
    print()

    print("Ожидается с ignore_case=True: Hello, WORLD, TEST")
    print("Результат:", end=" ")
    for item in Unique(data, ignore_case=True):
        print(item, end=", ")
    print("\n")

    print("Тест 6: пустые данные")
    data = []
    print(f"Исходные данные: {data}")
    print("Ожидается: ничего не выведется")
    print("Результат:", end=" ")
    for item in Unique(data):
        print(item, end=", ")
    print("(ничего не выведено)")
