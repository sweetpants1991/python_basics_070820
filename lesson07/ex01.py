# case01:
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix .
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_1, list_2):
        self.matrix_new = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix_new = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix_new[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_new]))


my_matrix = Matrix([[1, 4, 1],
                    [2, 8, 2],
                    [3, 16, 3]],
                   [[42, 14, 8],
                    [24, 41, 88],
                    [6, 6, 6]])

print(my_matrix.__add__())
