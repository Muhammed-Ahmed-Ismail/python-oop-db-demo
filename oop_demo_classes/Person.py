class Person:
    def __init__(self, name, age, money=1000, sleepmood='happy', heathRate=100):

        self.name = name
        self.money = money
        self.sleep_mood = sleepmood
        self.heathRate = heathRate
        self.age = age

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        if money < 0:
            print(f'money for {self.name} cannot be less than 0 so 0 was set as a property. ')
            self.__money = 0
        else:
            self.__money = money

    @property
    def sleep_mood(self):
        return self.__sleep_mood

    @sleep_mood.setter
    def sleep_mood(self, sleepmode):
        if sleepmode not in ['happy', 'lazy', 'tired']:
            print('this sleepMode is not valid happy was set')
            self.__sleep_mood = 'happy'
            return
        self.__sleep_mood = sleepmode

    @property
    def health_rate(self):
        return self.__heathRate

    @health_rate.setter
    def health_rate(self, heathRate):
        if heathRate not in range(0, 100):
            print(f'health rate cannot be out of 0 to 100  so 100 was set for {self.name}')
            self.__heathRate = 100
            return
        self.__heathRate = heathRate

    def sleep(self, hours):
        if hours > 7:
            self.__sleep_mood = 'lazy'
        elif hours == 7:
            self.__sleep_mood = 'happy'
        else:
            self.__sleep_mood = 'tired'

    def buy(self, items):
        if self.__money - items * 10 > 0:
            self.__money -= items * 10
            print(f'you {self.name} bought items by {items * 10} $ and he has now {self.__money}')
        else:
            print(f'{self.name} do not have enough money')

    def eat(self, meals):
        if meals == 3:
            self.__heathRate = 100
        elif meals == 2:
            self.__heathRate = 75
        else:
            self.__heathRate = 50

    def __str__(self):
        return f'''
         name:{self.name}
         money:{self.__money}
         healthRate:{self.__heathRate} 
         sleeping_mood:{self.__sleep_mood}'''
