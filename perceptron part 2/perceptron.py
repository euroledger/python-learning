import random

# The activation function
def sign(n):
    if n >= 0:
        return 1
    else:
        return -1

class Perceptron:
    weights = []
    lr = 0.0001

    # Constructor
    def __init__(self, n):
        for i in range(0, n-1):
            self.weights.append(random.uniform(-1, 1))
        self.weights.append(1)
    def print_weights(self):
        print(self.weights)

    def guess(self, inputs):
        sum = 0.0
        for i in range(0, len(self.weights)):
            sum += inputs[i] * self.weights[i]
        output = sign(sum)
        return output

    def guess_y(self, x):
        w0 = self.weights[0]
        w1 = self.weights[1]
        w2 = self.weights[2]

        return -(w2/w1) - (w0/w1) * x

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        # Tune all the weights
        for i in range(0, len(self.weights)):
            self.weights[i] += error * inputs[i] * self.lr

        return guess