import time
from contextlib import contextmanager

class cm_timer_1:
    """
    Контекстный менеджер на основе класса для измерения времени выполнения
    """

    def __enter__(self):
        """Вызывается при входе в контекст"""
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Вызывается при выходе из контекста"""
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"time: {elapsed_time:.1f}")


@contextmanager
def cm_timer_2():
    """
    Контекстный менеджер на основе contextlib для измерения времени выполнения
    """
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"time: {elapsed_time:.1f}")


if __name__ == '__main__':
    print("Тест контекстного менеджера на основе класса (cm_timer_1):")
    with cm_timer_1():
        time.sleep(1.5)

    print("\nТест контекстного менеджера на основе contextlib (cm_timer_2):")
    with cm_timer_2():
        time.sleep(2.3)

    print("\nТест с разным временем выполнения:")

    print("Короткое время (0.7 сек):")
    with cm_timer_1():
        time.sleep(0.7)

    print("Длинное время (3.1 сек):")
    with cm_timer_2():
        time.sleep(3.1)

    print("\nСравнение двух реализаций на одинаковом времени:")

    sleep_time = 1.2
    print(f"Время сна: {sleep_time} сек")

    print("cm_timer_1:")
    with cm_timer_1():
        time.sleep(sleep_time)

    print("cm_timer_2:")
    with cm_timer_2():
        time.sleep(sleep_time)
