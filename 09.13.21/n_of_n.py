def n_of_n(num):
    num2 = str(num) * 2
    num3 = str(num) * 3
    return num + int(num2) + int(num3)


print(n_of_n(10))


def n_of_n2(num, count):
    result = num
    for i in range(2, count + 1):
        result += int(str(num) * i)
    return result


print(n_of_n2(1, 3))
