import random
import time

from draw import turtle_init, turtle_close, line, WIDTH, HEIGHT, turtle_on_click, turtle_mainloop, ellipse, \
    turn_on_tracer, turtle_update, turtle_clear
from perceptron import Perceptron
from training import Point, f

list_of_points = []


def setup():
    brain.print_weights()
    inputs = [-1, 0.5, 1]
    guess = brain.guess(inputs)
    print(guess)

    for i in range(0, 100):
        list_of_points.append(Point())

    turtle_init()
    turtle_on_click(greeting)

def train():
    # while True:
    print("TRAINING ITERATION", iter)
    for pt in list_of_points:
        target = pt.label
        inputs = (pt.x, pt.y, pt.bias)
        brain.train(inputs, target)
    draw()
    time.sleep(1)


def greeting(x, y):
    for pt in list_of_points:
        target = pt.label
        inputs = (pt.x, pt.y, pt.bias)
        brain.train(inputs, target)
    draw()

def initial_draw():
    for pt in list_of_points:
        pt.show()

    x1 = -WIDTH / 2
    y1 = f(x1)
    x2 = WIDTH / 2
    y2 = f(x2)
    # line(-WIDTH/2, -HEIGHT/2, WIDTH / 2, HEIGHT / 2 )

    line(x1, y1, x2, y2)
    x1 = -WIDTH / 2
    x1 = int(x1)
    y1 = brain.guess_y(x1)

    x2 = WIDTH/2
    x2 = int(x2)
    y2 = brain.guess_y(x2)

    line(x1, y1, x2, y2)

def draw():
    turtle_clear()
    x1 = -WIDTH / 2
    y1 = f(x1)
    x2 = WIDTH / 2
    y2 = f(x2)

    line(x1, y1, x2, y2)
    for pt in list_of_points:
        target = pt.label
        inputs = (pt.x, pt.y, pt.bias)
        guess = brain.guess(inputs)
        if guess == target:
            fill = "green"
        else:
            if target == 1:
                fill = "white"
            else:
                fill = "black"
        ellipse(pt.x, pt.y, 10, "black", fill)
    # turtle_mainloop()
    # build new dynamic line
    x1 = -WIDTH / 2
    x1 = int(x1)
    y1 = brain.guess_y(x1)

    x2 = WIDTH/2
    x2 = int(x2)
    y2 = brain.guess_y(x2)

    line(x1, y1, x2, y2)

brain = Perceptron(3)
setup()
initial_draw()
time.sleep(1.0)

# draw()
turtle_update()
while True:
    greeting(0,0)
    time.sleep(0.5)
    turtle_update()

turtle_close()

