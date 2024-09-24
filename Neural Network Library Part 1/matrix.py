import os

class Matrix:

    # Constructor
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []

        for i in range(0, rows):
            self.matrix.append([])
            for j in range(0, cols):
                self.matrix[i].append(0)

    def add(self, n):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.matrix[i][j] += n

    def multiply(self, n):
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






