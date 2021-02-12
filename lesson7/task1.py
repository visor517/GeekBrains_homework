# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        result = ""
        for row in self.arr:
            result += f'{" ".join(map(str,row))}\n'
        return result

    def __add__(self, other):
        # готовим шаблон для результата нужных размеров
        y_max = max(len(self.arr), len(self.arr))
        x_max = max(len(self.arr[0]), len(other.arr[0]))
        result = [[0 for x in range(x_max)] for item in range(y_max)]

        # суммирование
        for y in range(len(result)):
            for x in range(len(result[0])):
                try:
                    result[y][x] += self.arr[y][x]
                except IndexError:
                    pass
                try:
                    result[y][x] += other.arr[y][x]
                except IndexError:
                    pass

        return Matrix(result)

a = [[31,22],[37,43],[51,86]]
b = [[3,5,32],[2,4,6],[-1,64,-8]]
c = [[3,5,8,3],[8,3,7,1]]

matrix_a = Matrix(a)
matrix_b = Matrix(b)
matrix_c = Matrix(c)

print(matrix_a + matrix_b + matrix_c)
