f_n = 'Zagrebin Kirill Maksimovich'
names = ['Zagrebin Kirill Maksimovich', 'Volkov Alexander Dmitrievich', 'Pogrebnoy Vyacheslav Petrovich']


def initials(full_name):
    name = full_name.split(' ')
    return name[0] + ' ' + name[1][0] + '. ' + name[2][0] + '.'


def initials_(full_name):
    length = len(full_name)
    name = []
    start = 0
    for i in range(length):
        if full_name[i] == ' ':
            name.append(full_name[start:i])
            start = i + 1
        if i == length - 1:
            name.append(full_name[start:i])

    return name[0] + ' ' + name[1][0] + '. ' + name[2][0] + '.'


def more_initials(names):
    return [initials(i) for i in names]


print(more_initials(names))
