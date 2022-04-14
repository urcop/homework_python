import random


def create_city(population, size):
    return {'Население': population, 'Размер города': size}


def create_region(names, cities):
    d = dict()
    for names, cities in zip(names, cities):
        d[names] = cities
    return d


cities = [create_city(random.randint(30000, 100000), random.randint(135000, 140000)) for _ in range(1, 10)]
names = ['Angarsk', 'Irkutsk', 'Rostov', 'Sochi', 'Moscow', 'Ajsnfk', 'JNSKVH', 'wjhdbj', 'sfnkhb', 'vhndfnsh']

print(create_region(names, cities))
