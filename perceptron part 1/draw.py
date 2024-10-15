import turtle

WIDTH=800
HEIGHT=800

# WIDTH=800
# HEIGHT=700
# WIDTH, HEIGHT = 750, 750
#
# screen = turtle.Screen()
# screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar

# height = 760
# width = 360
# screen = turtle.Screen()
# screen.screensize(width, height)


def size(height, width):
    turtle.setup(width, height)
    turtle.tracer(False)
    turtle.bgcolor("grey")

def turtle_close():
    turtle.exitonclick()

def line(x1, y1, x2, y2):
    turtle.penup()
    start=(x1, y1)
    end=(x2, y2)
    turtle.fillcolor("black")

    turtle.goto(start)
    turtle.pendown()
    turtle.goto(end)
    turtle.penup()

def ellipse(x, y, radius,linecolor, fillcolor):
    turtle.penup()
    turtle.goto(x,y)

    turtle.color(linecolor, fillcolor)  # line color, fill color

    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

def turtle_on_click(callback):
    screen = turtle.Screen()
    screen.onclick(callback)


def mouse_pressed(x, y):
    print("YO DA MAN!")

def turtle_mainloop():
    turtle.Screen().mainloop()


# turtle_init()

# screen = turtle.Screen()
# screen.onclick(mouse_pressed)

# ellipse(100,100, 10, "black")
# ellipse(-100, -100, 10, "white")
#
# ellipse(100,150, 10, "black")
# ellipse(250, 100, 10, "white")
# ellipse(0, 0, 10, "white")

# line(-WIDTH/2,-HEIGHT/20,WIDTH, HEIGHT)
# screen.mainloop()

# turtle_close()

