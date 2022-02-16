class Washing:

    def __init__(self, water):
        self.water = water

    def wash(self, item):
        print(f"I'm washing {item} with {self.water} l of water")


class Driving:

    @staticmethod
    def drive(a, b):
        print(f"Я везу из {a} в {b}")


class Machine:

    def __init__(self, brand, price, year, color):
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color


class WashingMachine(Machine, Washing):
    def __init__(self, brand, price, year, color, water):
        Machine.__init__(self, brand, price, year, color)
        Washing.__init__(self, water)


class DrivingMachine(Machine, Driving):
    pass


dm1 = DrivingMachine('suzuki', '200$', '2005', 'yellow')
dm1.drive('a', 'b')
print(dm1.year)

wm1 = WashingMachine('bosh', '200$', '2045', 'space grey', '50')
wm1.wash('shirt')
print(wm1.price)
