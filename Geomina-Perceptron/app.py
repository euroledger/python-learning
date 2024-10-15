from draw import size, turtle_mainloop
from perceptron import Perceptron
from training import Point

list_of_points=[]

p=Perceptron()
p.print_weights()

def setup():
    size(800,800)

    for i in range(0,100):
        list_of_points.append(Point(800,800))


    inputs=[-1,0.5]
    guess=p.guess(inputs)
    print (guess)

def draw():
    for pt in list_of_points:
        pt.show()

    turtle_mainloop()

setup()
draw()
