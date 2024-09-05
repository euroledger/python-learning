from random import randrange

from draw import ellipse, WIDTH, HEIGHT

class Point:
    x = 0.0
    y = 0.0
    label = 0
    def __init__(self, x=None, y=None):
        w=int(WIDTH / 2)
        h=int(HEIGHT / 2)
        if x is None:
            self.x=randrange(-w, w)
        else:
            self.x = x
        if y is None:
            self.y=randrange(-h, h)
        else:
            self.y = y

        if self.x>self.y:
            self.label = 1
        else:
            self.label = -1

    def show(self):
        fill = ""
        if self.label == 1:
            fill = "white"
        else:
            fill = "black"

        # print("label=", self.label)
        ellipse(self.x, self.y, 10, "blue", fill)