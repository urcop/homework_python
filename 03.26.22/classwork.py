import itertools as iter
from pprint import pprint

closer_nums = {
    '1': '142',
    '2': '1235',
    '3': '236',
    '4': '1457',
    '5': '45268',
    '6': '3569',
    '7': '487',
    '8': '59782',
    '9': '689',
    '0': '08',
}


def hack(password: str):
    closer_nums_res = list()
    nums = password.split(' ')
    for num in nums:
        closer_nums_res.append(closer_nums[num])
    one, two, three, four = closer_nums_res[0], closer_nums_res[1], closer_nums_res[2], closer_nums_res[3],
    result = list(iter.product(one, two, three, four))
    return result


pprint(hack('4 0 3 7'))
