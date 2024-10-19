from matrix import Matrix

# m1 = Matrix(2,2)
# m1.randomize()
# m1.print_matrix()
# m1.multiply(2)
# m1.print_matrix()
#
# m2 = Matrix(2,2)
# m2.randomize()
# m2.print_matrix()
#
# m3 = Matrix.my_multiply(m1, m2)
# m3.print_matrix()

a = Matrix(2,3)
a.randomize()
a.print_matrix()

def double_it(x):
    return x * 2

a.map(double_it)
a.print_matrix()

