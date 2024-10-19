from console import console
from matrix import Matrix
from nn import NeuralNetwork


print ("Welcome to my Neural Network")


def setup():
    a = NeuralNetwork(2,2,1)

    input_array = [1,0]
    output = a.feed_forward(input_array)

    print(output)


setup()