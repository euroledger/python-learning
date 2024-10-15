from random import randrange
from draw import ellipse


class Point:
    def __init__(self, width, height):
        self.x = randrange(width)
        self.y = randrange(height)
        if self.x>self.y:
            self.label=1
        else:
            self.label=-1

    def show(self):
        if self.label==1:
            fill="white"
        else:
            fill="black"
        ellipse(self.x, self.y, 10, "blue", fill)





