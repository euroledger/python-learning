import unittest

from console import console
from matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_matrix_multiplication(self):
        a = Matrix(2, 3, [[1,2,3],[4,5,6]])
        b = Matrix(3, 2, [[7,8],[9,10], [11,12]])
        self.assertEqual(a.matrix,[[1,2,3],[4,5,6]] )
        self.assertEqual(b.matrix,[[7,8],[9,10], [11,12]])

        c = a.multiply(b)
        self.assertEqual(c.matrix,[[58,64],[139, 154]] )

    def test_matrix_transpose(self):
        a = Matrix(2, 3, [[1,2,3],[4,5,6]])

        b = a.transpose()
        self.assertEqual(b.matrix,[[1,4],[2,5],[3,6]] )


if __name__ == '__main__':
    unittest.main()
