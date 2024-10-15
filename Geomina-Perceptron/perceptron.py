import random

def sign(n):
    if n>=0:
        return 1
    else:
        return -1

class Perceptron:
    def __init__(self):
        self.weights=[]
        self.weights.append(random.uniform(-1,1))
        self.weights.append(random.uniform(-1,1))

    def print_weights(self):
        print(self.weights[0])
        print(self.weights[1])

    # def add_weights(self):
    #    self.weights.append(self.weights[0]+self.weights[1])
    #    print(self.weights)

    def guess(self,inputs):
        sum_inputs=0
        for i in range(0, len(self.weights)):
            sum_inputs +=self.weights[i]*inputs[i]
        output = sign(sum_inputs)
        return output




