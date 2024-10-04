from console import console
from matrix import Matrix
from nn import NeuralNetwork


print ("Welcome to my Neural Network")


def setup():
    brain = NeuralNetwork(3, 3, 1)

    a = Matrix(2,3)
    a.randomize()

    console.table(a)

    b = a.transpose()
    console.table(b)

    # b = Matrix (3,2)
    # a.randomize()
    # b.randomize()
    #
    # console.table(a)
    # console.table(b)
    #
    # c = a.multiply(b)
    # console.table(c)


setup()