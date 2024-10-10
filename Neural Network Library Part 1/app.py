from matrix import Matrix
from nn import NeuralNetwork

print ("Welcome to my Neural Network")

def setup():
    brain = NeuralNetwork(3, 3, 1)

    m = Matrix(3, 2)

    m.add(5)

    m.multiply(-3)
    print(m.toStr())


def draw():
    print("hey")

setup()