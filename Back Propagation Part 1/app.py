from console import console
from matrix import Matrix
from nn import NeuralNetwork


print ("Welcome to my Neural Network")


def setup():
    nn = NeuralNetwork(2,2,2)

    inputs = [1,0]
    targets = [1, 0]

    # output = nn.feed_forward(input_array)
    # print(output)

    nn.train(inputs, targets)

setup()