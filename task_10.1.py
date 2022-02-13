import random


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        m = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                m += f'{self.matrix[i][j]} '
            m += "\n"
        return m

    def __add__(self, other):
        result = None
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                result = self.matrix
        return Matrix(result)


row = int(input("Enter a number of rows for matrix: "))
col = int(input("Enter a number of columns for matrix: "))

m_1 = Matrix([[random.randint(0, 100) for x1 in range(row)] for y1 in range(col)])
m_2 = Matrix([[random.randint(0, 100) for x2 in range(row)] for y2 in range(col)])
print(m_1)
print(m_2)
print(m_1 + m_2)
