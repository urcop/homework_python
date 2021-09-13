def build(num, symbol):
    for x in range(1, num + 1, 2):
        space = num - x
        lr_space = (space // 2) * ' '
        stars = symbol * x
        print(lr_space + stars + lr_space)


build(101, 'c')
