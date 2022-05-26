from oop_demo_classes.util import get_db_curser, prepare_data_base


class Employee:
    query = ''
    db, db_cursor = get_db_curser()

    def __init__(self, emp_id, name, age, is_manager):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.is_manager = is_manager

    @classmethod
    def select(cls):
        cls.query += 'select * from employees'
        return cls

    @classmethod
    def where(cls, colm, cond, value):
        value = value if isinstance(value, int) else f'"{value}"'
        cls.query += f' where {colm} {cond} {value}'
        return cls

    @classmethod
    def get(cls):
        cls.excecute()
        return cls.db_cursor.fetchall()

    @classmethod
    def excecute(cls):
        cls.db_cursor.execute(cls.query)
        print(cls.query)
        cls.query = ''
        cls.where = False

    @classmethod
    def add(cls, emp_name, age, is_manager):
        cls.query = f'insert into employees(name,age,is_manager) values("{emp_name}",{age},{is_manager}) '
        cls.excecute()
        cls.db.commit()

    @classmethod
    def _and(cls, col, cond, value):
        value = value if isinstance(value, int) else f'"{value}"'
        cls.query += f' and {col} {cond} {value}'
        return cls
