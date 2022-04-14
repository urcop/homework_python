import string
from random import choice


def rand_str(length):
    letters = list(string.ascii_letters)
    s = ''
    for _ in range(length):
        s += choice(letters)
    return s


def score_letters(str):
    upper_count = 0
    lower_count = 0
    for i in str:
        if i.isupper():
            upper_count += 1
        else:
            lower_count += 1
    if upper_count > lower_count:
        return 1
    elif upper_count == lower_count:
        return 2
    else:
        return 0


def array_of_strings(length, count_strings):
    return [rand_str(length) for _ in range(count_strings)]


def ratio(array):
    big_letters = 0
    small_letters = 0
    equal = 0
    for x in array:
        if score_letters(x) == 1:
            big_letters += 1
        elif score_letters(x) == 0:
            small_letters += 1
        else:
            equal += 1
    ratio_big = (big_letters / len(array)) * 100
    ratio_small = (small_letters / len(array)) * 100
    ratio_equal = (equal / len(array)) * 100
    s = f'В этой строке {round(ratio_big)}% строк где заглавных букв больше {round(ratio_small)}% \
строк где маленьких букв больше {round(ratio_equal)}% строк где и маленьких и больших букв поровну'
    return s


print(ratio(array_of_strings(5, 9)))
