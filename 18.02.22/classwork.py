# class Library:
#     __books = []
#
#     def __init__(self, name):
#         self.name = name
#
#     def take_book(self, book):
#         if len(self.__books) < 2:
#             self.__books.append(book)
#             print(f'Взял книгу - {book}')
#         else:
#             print('у челика много книг нельзя давать')
#
#     def get_books(self):
#         return self.__books
#
#     def return_book(self, book):
#         if book in self.__books:
#             self.__books.remove(book)
#         else:
#             print('у чела нет такой книги')
#
#
# artem = Library('артемка')
# artem.take_book('MaM')
# artem.take_book('LoL')
# print(artem.get_books())
# artem.return_book('LoL')
# artem.take_book('ne ssy')
# print(artem.get_books())
#
# class Matrix:
#     def __init__(self, matrix):
#         if len(matrix) == 0:
#             print('err')
#         else:
#             for line in range(1, len(matrix)):
#                 if len(matrix[0]) == len(matrix[line]):
#                     continue
#                 else:
#                     print('все плохо')
#                     break
#             else:
#                 self.matrix = matrix
#                 self.valid = True
#                 print('все кул')
#
#     def get_matrix(self):
#         print(self.matrix)
#
#     def transpose(self):
#         if self.valid:
#             trans = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
#             return trans
#         else:
#             return 'Error'
#
#
# m = Matrix(
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
# )
#
# m.get_matrix()
# print(m.transpose())

import os


def witch_sys():
    system = os.uname()
    print(f'oперационка - {system.sysname} \nВерсии - {system.version}')
    return system.sysname == 'Linux'


witch_sys()

# def change_in_file(file, to_change, for_change):
#     if file.split('.')[-1] == 'txt' and os.path.isfile(file) and os.path.exists(file):
#         f = open(file)
#         for line in f:
#             if line.__contains__(to_change):
#                 new_line = line.replace(to_change, for_change)
#                 f = open(file, 'w')
#                 f.write(new_line)
#     else:
#         print('нипорядок')
#
#
# change_in_file('mama.txt', 'флексиш', 'сосал')
