import json
import sys
from unique import Unique
from gen_random import gen_random
from print_result import print_result
from cm_timer import cm_timer_1

path = sys.argv[1] if len(sys.argv) > 1 else None

if not path:
    print("Укажите путь к файлу data_light.json")
    print("Пример: python process_data.py data_light.json")
    sys.exit(1)

try:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Успешно загружено {len(data)} записей из файла {path}")
except FileNotFoundError:
    print(f"Ошибка: Файл {path} не найден")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Ошибка: Файл {path} содержит некорректный JSON")
    sys.exit(1)
except Exception as e:
    print(f"Неизвестная ошибка при загрузке файла: {e}")
    sys.exit(1)

if not data or not isinstance(data, list):
    print("Ошибка: Данные должны быть непустым списком")
    sys.exit(1)

if not all(isinstance(item, dict) for item in data):
    print("Ошибка: Все элементы данных должны быть словарями")
    sys.exit(1)

missing_profession = [i for i, item in enumerate(data) if 'profession' not in item]
if missing_profession:
    print(f"Ошибка: Ключ 'profession' отсутствует в элементах: {missing_profession}")
    sys.exit(1)

@print_result
def f1(arg):
    """Отсортированный список профессий без повторений (игнорируя регистр)"""
    return sorted(Unique([item['profession'] for item in arg], ignore_case=True))

@print_result
def f2(arg):
    """Фильтрация элементов, начинающихся со слова 'программист'"""
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    """Добавление строки ' с опытом Python' к каждой профессии"""
    return list(map(lambda x: x + ' с опытом Python', arg))

@print_result
def f4(arg):
    """Генерация зарплат и объединение с профессиями"""
    salaries = list(gen_random(len(arg), 100000, 200000))
    return [f"{profession}, зарплата {salary} руб." for profession, salary in zip(arg, salaries)]


if __name__ == '__main__':
    print("\nНачало обработки данных...")
    with cm_timer_1():
        result = f4(f3(f2(f1(data))))

    print(f"\nОбработка завершена. Получено {len(result)} результатов.")
