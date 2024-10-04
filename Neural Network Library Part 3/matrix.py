import os
from random import randrange

class Matrix:

    # Constructor
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols

        if data is not None:
            self.matrix = data
        else:
            self.matrix = []
            for i in range(0, rows):
                self.matrix.append([])
                for j in range(0, cols):
                    self.matrix[i].append(0)

    def randomize(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.matrix[i][j] = randrange(10)

    def add(self, n):
        if type(n) is Matrix:
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.matrix[i][j] += n.matrix[i][j]
            return

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.matrix[i][j] += n

    def transpose(self):
        result = Matrix(self.cols, self.rows)

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                result.matrix[j][i] += self.matrix[i][j]

        return result

    def multiply(self, n):
        if type(n) is Matrix:
            if self.cols != n.rows:
                print("ERROR: Columns of A must match Rows of B")
                return None
            # matrix product
            a = self
            b = n

            result = Matrix(self.rows, n.cols)
            for i in range(0, result.rows):
                for j in range(0, result.cols):
                    this_sum = 0
                    for k in range(0, a.cols):
                        this_sum += a.matrix[i][k] * b.matrix[k][j]
                    result.matrix[i][j] = this_sum

            return result

        # scalar product
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.matrix[i][j] *= n



    def toStr(self):
        for row in range(0,self.rows):
            for col in range(0, self.cols):
                # d = self.matrix[row][col]
                print("{0:4d}".format(self.matrix[row][col]), end=" ")
            print("")
        return f"""Matrix {{rows: {self.rows} cols: {self.cols}}}"""






