import math

from matrix import Matrix


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


class NeuralNetwork:

    # Constructor
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)

        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)

        self.bias_h.randomize()
        self.bias_o.randomize()

    def feed_forward(self, input_array):
        # Generating the hidden outputs
        inputs = Matrix.from_array(input_array)
        hidden = Matrix.my_multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)

        # activation function
        hidden.map(sigmoid)

        output = Matrix.my_multiply(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map(sigmoid)

        return output.to_array()
