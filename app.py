#! /usr/bin/env python3

from oop_demo_classes.util import get_db_curser, prepare_data_base
from models.Employee import Employee


def add_employee(name, age, is_manager):
    Employee.add(name, age, is_manager)


cur = get_db_curser()

print("Employees App")
clear_data_choice = input("do you want to clear the previous data? (y,any button for no ) :  ").lower()
if clear_data_choice == 'y':
    prepare_data_base()

choice = ''
while choice is not 'q':
    choice = input("type add if you want to add a new employee: ")
    if choice == 'add':
        name = input("Enter the name: ")
        age = input("Enter the age: ")
        level = input("enter whether the employee is a normal or manager for normal enter nrml and mngr for manager ")
        if level == 'nrml':
            add_employee(name, age, False)
        else:
            add_employee(name, age, True)
