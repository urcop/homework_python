class Phone:
    @staticmethod
    def country_code(num):  # +21-999-999-99-99
        if num[0] == '+':
            return f'код страны - {num.split("-")[0][1:]}'

    @staticmethod
    def check_phone(num):
        result = ''.join(num.split("-")[1:])
        check_digits = result.isdigit()
        check_plus = num[0] == '+'
        check = (num[-3] + num[-6] + num[-10] + num[-14]) == ('-' * 4)
        return check and check_plus and check_digits


print(Phone.country_code('+79-999-999-99-99'))
print(Phone.check_phone('+79-999-999-99-99'))

from typing import List


class Engine:
    def __init__(self, power, volume, weight, q):
        self.power = power
        self.volume = volume
        self.weight = weight
        self.quality = q


class Wheel:
    def __init__(self, weight, mfr, radius, q):
        self.weight = weight
        self.manufacture = mfr
        self.radius = radius
        self.quality = q


class Steering:
    def __init__(self, shape, mfr, weight, q):
        self.mrf = mfr
        self.shape = shape
        self.weight = weight
        self.quality = q
        self.place = 'right' if mfr in ['eng', 'jpn'] else 'left'


class Car:
    def __init__(self, eng: Engine, whs: List[Wheel], st: Steering):
        w_all = sum([item.weight for item in [eng, st].extend(whs)])
        self.hp = eng.power / w_all
        self.engine = eng
        self.wheels = whs
        self.steering = st
        q_whs = sum([w.quality for w in whs]) / len(whs)
        q = (eng.quality + q_whs + st.quality) / 3
