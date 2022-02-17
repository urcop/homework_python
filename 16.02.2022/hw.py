from random import randint


def view_result(race, count_laps):
    i = 1
    for el in race.play(array_of_car, count_laps):
        print(i, el.name)
        i += 1


class Car:

    def __init__(self, speed, name):
        self.speed = speed
        self.name = name

    def __lt__(self, other):
        return self.speed < other.speed


class Race:

    @staticmethod
    def play(array_of_cars, laps):
        result = []
        for _ in range(laps):
            random_car = randint(0, len(array_of_cars) - 1)
            result.append(array_of_cars.pop(random_car))
        result += sorted(array_of_cars, reverse=True)
        return result


c1 = Car(70, 'Ferrari')
c2 = Car(300, 'Tesla')
c3 = Car(90, 'Bentley')
c4 = Car(23, 'Lada')
c5 = Car(74, 'Kirill')
c6 = Car(84, 'bymve')

array_of_car = [c1, c2, c3, c4, c5, c6]

if __name__ == "__main__":
    race1 = Race()
    view_result(race1, 3)
