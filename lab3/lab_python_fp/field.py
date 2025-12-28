def field(items, *args):
    """
    Генератор для выборки значений из словарей

    Args:
        items: список словарей
        *args: названия ключей для выборки

    Yields:
        Если передан один аргумент - значения полей
        Если несколько аргументов - словари с выбранными полями
    """
    assert len(args) > 0, "Должен быть передан хотя бы один аргумент"

    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]
    else:
        for item in items:
            result = {}
            has_valid_fields = False

            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
                    has_valid_fields = True

            if has_valid_fields:
                yield result


if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': 3000, 'color': 'white'},
        {'price': 4000},
        {'title': 'Стул', 'price': None, 'color': 'brown'},
        {'description': 'Новый товар'}
    ]

    print("Тест 1: один аргумент 'title'")
    print("Ожидается: 'Ковер', 'Диван для отдыха', 'Стул'")
    print("Результат:", end=" ")
    for title in field(goods, 'title'):
        print(f"'{title}'", end=", ")
    print("\n")

    print("Тест 2: несколько аргументов 'title', 'price'")
    print("Ожидается: {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха'}, {'price': 4000}, {'title': 'Стул'}")
    print("Результат:")
    for item in field(goods, 'title', 'price'):
        print(f"  {item}")
    print()

    print("Тест 3: несколько аргументов 'title', 'color'")
    print("Ожидается: {'title': 'Ковер', 'color': 'green'}, {'title': 'Диван для отдыха', 'color': 'black'}, {'color': 'white'}, {'title': 'Стул', 'color': 'brown'}")
    print("Результат:")
    for item in field(goods, 'title', 'color'):
        print(f"  {item}")
    print()

    print("Тест 4: аргумент с None значениями 'price'")
    print("Ожидается: 2000, 3000, 4000")
    print("Результат:", end=" ")
    for price in field(goods, 'price'):
        print(price, end=", ")
    print("\n")

    print("Тест 5: несуществующий ключ 'description'")
    print("Ожидается: 'Новый товар'")
    print("Результат:", end=" ")
    for desc in field(goods, 'description'):
        print(f"'{desc}'", end=", ")
    print("\n")

    print("Тест 6: несколько аргументов с несуществующими ключами")
    print("Ожидается: пустой вывод")
    print("Результат:", end=" ")
    for item in field(goods, 'weight', 'size'):
        print(item, end=", ")
    print("(ничего не выведено)")
