from oop_demo_classes.util import get_db_curser, prepare_data_base


class Employee:
    query = ''
    where = False
    db,db_cursor = get_db_curser()

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

        if cls.where:
            cls.query += f'&{colm} {cond} {value}'
        else:
            cls.query += f'where {colm} {cond} {value}'
            cls.where = True
        return cls

    @classmethod
    def get(cls):
        cls.excecute()
        return cls.db_cursor.fetchall()

    @classmethod
    def excecute(cls):
        cls.db_cursor.execute(cls.query)
        cls.db.commit()
        cls.query = ''

    @classmethod
    def add(cls, emp_name, age, is_manager):
        cls.query = f'insert into employees(name,age,is_manager) values("{emp_name}",{age},{is_manager}); '
        cls.excecute()

