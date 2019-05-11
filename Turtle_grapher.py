from turtle import Turtle, Screen

WIDTH, HEIGHT = 20, 15  # coordinate system size

def plotter(turtle, x_range):
    turtle.penup()

    for x in x_range:
        y = x / 2 + 3
        ivy.goto(x, y)
        turtle.pendown()

def axis(turtle, distance, tick):
    position = turtle.position()
    turtle.pendown()

    for _ in range(0, distance // 2, tick):
        turtle.forward(tick)
        turtle.dot()

    turtle.setposition(position)

    for _ in range(0, distance // 2, tick):
        turtle.backward(tick)
        turtle.dot()

screen = Screen()
screen.setworldcoordinates(-WIDTH/2, -HEIGHT/2, WIDTH//2, HEIGHT/2)

ivy = Turtle(visible=False)
ivy.speed('fastest')
ivy.penup()
axis(ivy, WIDTH, 1)

ivy.penup()
ivy.home()
ivy.setheading(90)
axis(ivy, HEIGHT, 1)

plotter(ivy, range(-WIDTH//2, WIDTH//2))

screen.exitonclick()
