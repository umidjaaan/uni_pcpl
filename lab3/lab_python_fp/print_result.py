def print_result(func):
    """
    Декоратор для вывода результатов выполнения функции
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(func.__name__)

        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)

        return result

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


@print_result
def test_5():
    """Функция без возвращаемого значения"""
    print("Выполняется test_5")


@print_result
def test_6():
    """Функция с аргументами"""
    return [10, 20, 30]


@print_result
def test_7():
    """Функция, возвращающая пустые коллекции"""
    return {}


@print_result
def test_8():
    """Функция, возвращающая сложный словарь"""
    return {'name': 'John', 'age': 30, 'city': 'Moscow'}


if __name__ == '__main__':
    print('!!!!!!!!')
    print("Основные тесты из задания:")
    print("-" * 30)

    test_1()
    print()

    test_2()
    print()

    test_3()
    print()

    test_4()
    print()

    print("Дополнительные тесты:")
    print("-" * 30)

    result = test_5()
    print(f"Результат test_5: {result}")
    print()

    test_6()
    print()

    test_7()
    print()

    test_8()
    print()

    print("Проверка возвращаемых значений:")
    print(f"test_1() вернула: {test_1()}")
    print(f"test_2() вернула: {test_2()}")
    print(f"test_4() вернула: {test_4()}")
