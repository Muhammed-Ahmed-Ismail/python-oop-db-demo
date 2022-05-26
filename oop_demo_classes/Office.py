from oop_demo_classes.Employee import Employee


class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        employee = list(filter(lambda emp: emp.id == emp_id, self.employees))
        if len(employee) == 0:
            return None
        return employee[0]

    def hire(self, employee: Employee):
        self.employees.append(employee)

    def fire(self, emp_id):
        self.employees.remove(self.get_employee(emp_id))
