def build(num):
    for x in range(1, num + 1, 2):
        space = num - x
        lr_space = (space // 2) * ' '
        stars = '*' * x
        print(lr_space + stars + lr_space)


build(7)
