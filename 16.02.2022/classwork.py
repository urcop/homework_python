class ExQuote:
    def __init__(self, quote: str):
        self.quote = quote

    def say(self):
        return self.quote + '!'


class QQuote:
    def __init__(self, quote: str):
        self.quote = quote

    def say(self):
        return self.quote + '?'


eq = ExQuote('чето')
qq = QQuote('чето')

print(eq.say())
print(qq.say())


class Counter:
    __current = 0

    def add(self):
        self.__current += 1

    def to_zero(self):
        self.__current = 0

    def get_current(self):
        return self.__current

    def set_current(self, value):
        self.__current = value

    def __str__(self):
        return 'Счетчик'


c = Counter()


class Human:
    def __init__(self, age, name, country):
        self.age = age
        self.name = name
        self.country = country

    def say(self):
        print(f'{self.age}  {self.name} {self.country}')


class Student(Human):
    def __init__(self, age, name, country, study, parent_number):
        super().__init__(age, name, country)
        self.study = study
        self.__parent_numbers = parent_number

    def say(self):
        super().say()
        print(f'{self.study}')

    @property
    def get_number(self):
        return self.__parent_numbers

    def set_number(self, value):
        self.__parent_numbers = value


stud1 = Student(15, 'oleg', 'sochi', 'sirius', '8888888888')


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


std1 = Student('oleg', 13)
std2 = Student('oleg', 13)
print(std1 == std2)


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        if self.x == other.x:
            return self.y > other.y
        elif self.y == other.y:
            return self.x > other.x
        else:
            return

    def __ge__(self, other):
        if self.x == other.x:
            return self.y < other.y
        elif self.y == other.y:
            return self.x < other.x
        else:
            return

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Dot(x, y)

    def __sub__(self, other):
        y = self.y - other.y
        x = self.x - other.x
        return Dot(x, y)
