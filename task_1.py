"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        answer = ''
        if len(self.data) == len(other.data):
            for row_1, row_2 in zip(self.data, other.data):
                if len(row_1) != len(row_2):
                    return 'The matrices are different'

                added_row = [x + y for x, y in zip(row_1, row_2)]
                answer += ' '.join(map(str, added_row)) + '\n'
        else:
            return 'The matrices are different'
        return answer


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[55, 66], [77, 88], [99, 10], [11, 22]])
print(matrix_1)
print(matrix_2)

print(matrix_1 + matrix_2)
