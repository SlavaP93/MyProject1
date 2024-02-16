class Matrix:
    matrix = []

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def data(self,matrix_data):
        self.matrix = matrix_data
        Matrix.matrix = matrix_data
        return matrix_data

    def transport(self):
        new = self.matrix[:]
        new_lst = [j for i in new for j in i]
        revers_lst = [new_lst[:len(new)] if i == 0
                      else new_lst[len(new) * i:len(new) + len(new) * i]
                      for i in range(len(new[0]))]
        return revers_lst

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения.")

        result = [
            [
                int(self.matrix[i][j]) + int(other.matrix[i][j]) for i in range(len(self.matrix))
            ]
            for j in range(len(self.matrix[0]))
        ]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для вычитания.")

        result = [
            [
                int(self.matrix[i][j]) - int(other.matrix[i][j]) for j in range(self.cols)
            ]
            for i in range(self.rows)
        ]
        return result

    def __mul__(self, other):
        result = [
            [
                int(self.matrix[i][j]) * int(other.matrix[i][j]) for j in range(self.cols)
            ]
            for i in range(self.rows)
        ]
        return result

    def __truediv__(self, other):

        result = [
            [
                int(self.matrix[i][j]) / int(other.matrix[i][j]) for j in range(self.cols)
            ]
            for i in range(self.rows)
        ]
        return result

    def __str__(self):
        matrix_str = ''
        for row in self.matrix:
            matrix_str += '  '.join(str(elem) for elem in row) + '\n'
        return matrix_str


m1 = Matrix(2, 3)
m1.data([[1, 2, 3], [4, 5, 6]])

m2 = Matrix(2, 3)
m2.data([[7, 8, 9], [10, 11, 12]])

print(m1)
print(m2)
print(m1.__add__(m2))
print(m1.__sub__(m2))
print(m1.transport())
print(m2.transport())
print(m1.__mul__(m2))
print(m1.__truediv__(m2))