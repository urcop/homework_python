from random import choice

big_letters = [i for i in range(65, 91)]
little_letters = [i for i in range(97, 123)]


def gen_name(big_letters, little_letters, num):
    i = 1
    while i < num:
        s = ''
        for x in range(0, 5):
            s += chr(choice(big_letters))
            for y in range(0, 9):
                s += chr(choice(little_letters))

            if x < 4:
                s += ' '
        yield s
        i += 1


ranger = gen_name(big_letters, little_letters, 5)
result = [x for x in ranger]
print(result)
