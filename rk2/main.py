from operator import itemgetter

class Table:
    def __init__(self, id, name, row_count, db_id):
        self.id = id
        self.name = name
        self.row_count = row_count
        self.db_id = db_id

class Database:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class TableDatabase:
    def __init__(self, db_id, table_id):
        self.db_id = db_id
        self.table_id = table_id

# --- Логические функции для тестирования ---

def task_b1(tables, dbs):
    """Таблицы на 'А' и их БД (1-ко-многим)"""
    one_to_many = [(t, d) for d in dbs for t in tables if t.db_id == d.id]
    res = [(t.name, d.name) for t, d in one_to_many if t.name.startswith('А')]
    return sorted(res, key=itemgetter(0))

def task_b2(tables, dbs):
    """БД и минимальное кол-во строк в их таблицах"""
    res = []
    for d in dbs:
        d_tables = [t.row_count for t in tables if t.db_id == d.id]
        if d_tables:
            res.append((d.name, min(d_tables)))
    return sorted(res, key=itemgetter(1))

def task_b3(tables, dbs, tables_dbs):
    """Связь многие-ко-многим, сортировка по таблицам"""
    many_to_many = []
    for td in tables_dbs:
        table = next((t for t in tables if t.id == td.table_id), None)
        db = next((d for d in dbs if d.id == td.db_id), None)
        if table and db:
            many_to_many.append((table.name, db.name))
    return sorted(many_to_many, key=itemgetter(0))

# --- Данные и запуск ---

dbs = [
    Database(1, 'AnalyticsDB'),
    Database(2, 'ArchiveDB'),
    Database(3, 'AccountingDB'),
]

tables = [
    Table(1, 'Анализ_продаж', 15000, 1),
    Table(2, 'Архив_данных', 8000, 2),
    Table(3, 'Активы', 12000, 3),
    Table(4, 'Расходы', 9500, 3),
    Table(5, 'Отчеты', 7000, 2),
]

tables_dbs = [
    TableDatabase(1, 1),
    TableDatabase(2, 2),
    TableDatabase(3, 3),
    TableDatabase(3, 4),
    TableDatabase(2, 5),
]

if __name__ == '__main__':
    print('ЗАДАНИЕ В1:', task_b1(tables, dbs))
    print('ЗАДАНИЕ В2:', task_b2(tables, dbs))
    print('ЗАДАНИЕ В3:', task_b3(tables, dbs, tables_dbs))
