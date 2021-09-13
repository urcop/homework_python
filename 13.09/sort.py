def sorted(array):
    for j in range(0, len(array) - 1):
        for i in range(0, len(array) - 1 - j):
            tmp = 0
            if array[i] > array[i + 1]:
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp
    return array


print(sorted([1, 16, 200, 13, 2, 5]))
