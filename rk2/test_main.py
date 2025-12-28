import unittest
from main import Table, Database, TableDatabase, task_b1, task_b2, task_b3

class TestDatabaseLogic(unittest.TestCase):

    def setUp(self):
        """Подготовка тестовых данных"""
        self.dbs = [
            Database(1, 'DB1'),
            Database(2, 'DB2')
        ]
        self.tables = [
            Table(1, 'А_Таблица', 100, 1),
            Table(2, 'Б_Таблица', 200, 1),
            Table(3, 'А_Логи', 50, 2)
        ]
        self.links = [
            TableDatabase(1, 1),
            TableDatabase(2, 3)
        ]

    def test_task_b1(self):
        """Тест фильтрации таблиц на букву 'А'"""
        result = task_b1(self.tables, self.dbs)
        expected = [('А_Логи', 'DB2'), ('А_Таблица', 'DB1')]
        # Сортировка в b1 идет по имени таблицы
        self.assertEqual(result, expected)

    def test_task_b2(self):
        """Тест поиска минимального количества строк"""
        result = task_b2(self.tables, self.dbs)
        # DB1: min(100, 200) = 100
        # DB2: min(50) = 50
        # Сортировка по значению: (DB2, 50), (DB1, 100)
        expected = [('DB2', 50), ('DB1', 100)]
        self.assertEqual(result, expected)

    def test_task_b3(self):
        """Тест связи многие-ко-многим"""
        result = task_b3(self.tables, self.dbs, self.links)
        expected = [('А_Логи', 'DB2'), ('А_Таблица', 'DB1')]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
