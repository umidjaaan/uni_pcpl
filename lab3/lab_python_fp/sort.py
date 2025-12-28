data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data, key=abs, reverse=True)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)

    print("Исходный массив:")
    print(data)
    print("\nСортировка по убыванию модуля (без lambda):")
    print(result)
    print("\nСортировка по убыванию модуля (с lambda):")
    print(result_with_lambda)

    print(f"\nРезультаты одинаковы: {result == result_with_lambda}")
