import os
import random

from console import console


class Matrix:

    # Constructor
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols

        if data is not None:
            self.data = data
        else:
            self.data = []
            for i in range(0, rows):
                self.data.append([])
                for j in range(0, cols):
                    self.data[i].append(0)

    @staticmethod
    def from_array(arr):
        m = Matrix(len(arr), 1)
        for i in range(0, len(arr)):
            m.data[i][0] = arr[i]
        return m

    @staticmethod
    def subtract(a, b):
        # return a new matrix a-b
        result = Matrix(a.rows, a.cols)

        for i in range(0, result.rows):
            for j in range(0, result.cols):
                result.data[i][j] = a.data[i][j] - b.data[i][j]

        return result

    def to_array(self):
        arr = []
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                arr.append(self.data[i][j])
        return arr

    def randomize(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.data[i][j] = random.uniform(-1, 1)


    def add(self, n):
        if type(n) is Matrix:
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.data[i][j] += n.data[i][j]
            return

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.data[i][j] += n

    @staticmethod
    def transpose(matrix):
        result = Matrix(matrix.cols, matrix.rows)

        for i in range(0, matrix.rows):
            for j in range(0, matrix.cols):
                result.data[j][i] = matrix.data[i][j]

        return result

    @staticmethod
    def my_multiply(a, b):
        if a.cols != b.rows:
            print("ERROR: Columns of A must match Rows of B")
            return None


        # matrix product
        result = Matrix(a.rows, b.cols)
        for i in range(0, result.rows):
            for j in range(0, result.cols):
                this_sum = 0
                for k in range(0, a.cols):
                    this_sum += a.data[i][k] * b.data[k][j]
                result.data[i][j] = this_sum

        return result

    def multiply(self, n):
        # scalar product
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.data[i][j] *= n

    def map(self, func):
        # Apply a function to every element of matrix
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                val = self.data[i][j]
                self.data[i][j] = func(val)

    def toStr(self):
        for row in range(0,self.rows):
            for col in range(0, self.cols):
                print("{0:4d}".format(self.data[row][col]), end=" ")
            print("")
        return f"""Matrix {{rows: {self.rows} cols: {self.cols}}}"""


    def print_matrix(self):
        console.table(self)




