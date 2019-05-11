from turtle import Screen, Turtle
from math import *


#win = Screen()
WIDTH , HEIGHT = 20, 15
### __ 

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
    turtle.penup()
    turtle.home()

def generate(f,interval):
    num = []
    start,end,inc = interval
    while start < end:
        num.append((start,f(start)))
        start += inc
    return num

def plot(turtle,f,interval):
    turtle.penup()
    turtle.pencolor('blue')

    num = generate(f,interval)

    for p in num:
        turtle.goto(p)
        turtle.pendown()

    turtle.penup()
    


if __name__ == '__main__':
    win = Screen()
    win.setworldcoordinates(-WIDTH/2 , -HEIGHT/2 , WIDTH//2 , HEIGHT//2)
    
    T = Turtle(visible = False)
    T.speed('fastest')

    axis(T,WIDTH,1)
    T.setheading(90)
    axis(T,HEIGHT,1)
    

    f = lambda x : sin(x)

    interval = (0,9,0.1)

    plot(T,f,interval)

    win.exitonclick()

    

    
