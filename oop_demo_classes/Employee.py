from .Person import Person
from .util import *


class Employee(Person):
    def __init__(self, name, age, is_manager, emp_id, money=1000, sleep_mood='happy', health_rate=100, email='example@gmail.com', work_mood='happy', salary=10000):
        super().__init__(name, age, money, sleep_mood, health_rate)
        self.id = emp_id
        self.email = email
        self.work_mood = work_mood
        self.salary = salary
        self.is_manager = is_manager

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        print('checker')
        if email_checker(email):

            self.__email = email
        else:
            print('invalid email it is set to null ')
            self.__email = None

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            print(f'salary for {self.name} cannot be less than 1000 so 1000 was set as a property. ')
            self.__salary = 0
        else:
            self.__salary = salary

    def work(self, hours):
        if hours > 8:
            self.work_mood = 'tires'
        elif hours == 8:
            self.work_mood = 'happy'
        else:
            self.work_mood = 'lazy'

    def send_email(self, to, sub, body, receiver_name):
        if self.__email is not None:
            email = formate_email(self.__email, to, sub, receiver_name, body)
            write_email(email)
        else:
            print(f"cannot send email as the email for {self.name} is not valid ")
