from show_func import show

import string

# print(list(string.ascii_lowercase))  # решение через модуль стринг

array = [chr(x) for x in range(97, 123)]  # list comprehension решение
# print(array)

array2 = list()  # while решение
i = 97
while i < 123:
    array2.append(chr(i))
    i += 1


# print(array)

@show
def get_elements_for(list_):  # функция вывода элементов массива с буквами через for
    for k in list_:
        print(k)


print(get_elements_for(array))


@show
def get_elements_while(list_):  # фунция вывода элементов массива с буквами через while
    k = 0
    while k < len(list_):
        print(list_[k])
        k += 1


print(get_elements_while(array))


#
# [
#  '  *  ',
#  ' *** ',
#  '*****',
#  ]


