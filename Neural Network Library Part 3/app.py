from matrix import Matrix
from nn import NeuralNetwork
import pandas as pd

print ("Welcome to my Neural Network")

class console:
    @staticmethod
    def table(m):
        print(pd.DataFrame(m.matrix))
        print("\n")


def setup():
    brain = NeuralNetwork(3, 3, 1)


    m = Matrix(3, 2)
    m.randomize()
    console.table(m)

    n = Matrix(3, 2)
    n.randomize()

    m.add(1)
    console.table(m)

    console.table(n)

    m.add(n)
    console.table(m)

    # m.add(5)
    # m.multiply(-3)
    # # print(m.toStr())
    #
    # console.table(m)
    #
    # print("\n")
    #


setup()