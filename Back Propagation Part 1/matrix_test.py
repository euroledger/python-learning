import unittest

from console import console
from matrix import Matrix

class TestMatrix(unittest.TestCase):
    def test_matrix_multiplication(self):
        a = Matrix(2, 3, [[1,2,3],[4,5,6]])
        b = Matrix(3, 2, [[7,8],[9,10], [11,12]])
        self.assertEqual(a.data, [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(b.data, [[7, 8], [9, 10], [11, 12]])

        c = Matrix.my_multiply(a, b)
        self.assertEqual(c.data, [[58, 64], [139, 154]])

    def test_matrix_transpose(self):
        a = Matrix(2, 3, [[1,2,3],[4,5,6]])

        b = Matrix.transpose(a)
        self.assertEqual(b.data, [[1, 4], [2, 5], [3, 6]])

    def test_from_array(self):
        a = [1,2,3]

        b = Matrix.from_array(a)
        self.assertEqual(b.data, [[1],[2],[3]])

    def test_matrix_subtract(self):
        a = Matrix(2, 3, [[4,4,4],[4,5,6]])
        b = Matrix(2, 3, [[1,1,2],[2,1,1]])

        c = Matrix.subtract(a,b)
        self.assertEqual(c.data, [[3, 3, 2], [2, 4, 5]])



if __name__ == '__main__':
    unittest.main()
