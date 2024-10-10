import turtle

WIDTH=800
HEIGHT=800

def turn_on_tracer():
    turtle.tracer(True)
    turtle.speed("fastest")
    # turtle.hideturtle()

def turtle_init(width=None, height=None):

    if width != None and height != None:
        turtle.setup(width, height)
    else:
        turtle.setup(WIDTH, HEIGHT)
    turtle.tracer(False)
    turtle.bgcolor("grey")

def turtle_close():
    turtle.exitonclick()

def turtle_clear():
    turtle.clear()

def line(x1, y1, x2, y2, color="black"):
    turtle.penup()
    start=(x1, y1)
    end=(x2, y2)
    turtle.color(color, color)  # line color, fill color

    turtle.fillcolor(color)

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


def turtle_mainloop():
    turtle.Screen().mainloop()

def turtle_update():
    turtle.Screen().update()

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

