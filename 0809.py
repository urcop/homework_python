def even(n):  # n - это число до которого будет идти счет
    i = 2
    array = list()
    while i <= n:
        array.append(i)
        i += 2
    return array


def odd(n):
    i = 1
    array = list()
    while i <= n:
        array.append(i)
        i += 1
    return array


print(even(50))
print(odd(50))
