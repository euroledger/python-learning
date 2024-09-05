import random

from draw import turtle_init, turtle_close, line, WIDTH, HEIGHT, turtle_on_click, turtle_mainloop, ellipse
from training import Point

list_of_points = []


# The activation function
def sign(n):
    if n >= 0:
        return 1
    else:
        return -1


def setup():
    brain.print_weights()
    inputs = [-1, 0.5]
    guess = brain.guess(inputs)
    print(guess)

    for i in range(0, 100):
        list_of_points.append(Point())
    # list_of_points.append((Point(0, -200)))
    # list_of_points.append((Point(-200, 0)))

    turtle_init()
    turtle_on_click(greeting)


def greeting(x, y):
    print("YOU ARE A GOOD GUY!")

    for pt in list_of_points:
        target = pt.label
        inputs = (pt.x, pt.y)
        brain.train(inputs, target)

    draw()
def draw():
    print("number of points is:", len(list_of_points))
    for pt in list_of_points:
        pt.show()

    line(WIDTH / 2, HEIGHT / 2, -WIDTH/2, -HEIGHT/2)

    for pt in list_of_points:
        target = pt.label
        inputs = (pt.x, pt.y)
        guess = brain.guess(inputs)
        print("guess=", guess, "target=", target)
        if guess == target:
            fill = "green"
            ellipse(pt.x, pt.y, 10, "black", fill)

    turtle_mainloop()


class Perceptron:
    weights = []
    lr = 0.1

    # Constructor
    def __init__(self):
        for i in range(0, 2):
            self.weights.append(random.uniform(-1, 1))

    def print_weights(self):
        print(self.weights)

    def guess(self, inputs):
        sum = 0.0
        for i in range(0, len(self.weights)):
            sum += inputs[i] * self.weights[i]
        output = sign(sum)
        return output

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        # Tune all the weights
        for i in range(0, len(self.weights)):
            self.weights[i] += error * inputs[i] * self.lr

        return guess


brain = Perceptron()
setup()
draw()
turtle_close()
