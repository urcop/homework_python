def unique(list):
    set_list = set(list)
    return [i for i in set_list if list.count(i) == 1]


def intersection(list_1, list_2):
    return [i for i in set.intersection(set(list_1), set(list_2))]


print(unique([1, 2, 2, 2, 4, 5, 1, 4, 10, 100, 11, 11]))
print(intersection([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 6, 7, 8]))
