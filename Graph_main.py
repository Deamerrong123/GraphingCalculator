from grapher import *
from turtle import Turtle, Screen
from math import *


def singlaValueFun_numGen(f, interval):
    num = []
    start, end, inc = interval
    while start < end:
        num.append((start, f(start)))
        start += inc
    return num

def ParametricEqu_numGen(x_t,y_t,interval):
    num = []
    start, end,inc = interval['lower'],interval['upper'],interval['increment']
    while start < end:
        num.append((x_t(start),y_t(start)))
        start += inc

    return num

def PolarEqu_numGen(r_theta,interval):
    num = []
    start ,end ,inc = interval['lower'],interval['upper'],interval['increment']
    while start < end:
        x = cos(start)*r_theta(start)
        y = sin(start) * r_theta(start)
        num.append((x,y))
        start += inc
    return num

if __name__ == '__main__':
    WIDTH, HEIGHT = 10,10
    win = Screen()

    win.setworldcoordinates(-WIDTH/2 , -HEIGHT/2 , WIDTH//2 , HEIGHT//2)
    
    G = Grapher(WIDTH,HEIGHT)
    '''
    f = lambda x : sin(x)
    interval = (0,9,0.1)
    Region1 = singlaValueFun_numGen(f,interval)
    
    x_t = lambda t : cos(t)
    y_t = lambda t: 2*sin(t)
    interval = {
        'lower' : 0,
        'upper' : 2*pi,
        'increment' : 0.1
    }
    Region2 = ParametricEqu_numGen(x_t,y_t,interval)
    '''
    r_theta = lambda theta : 1-cos(theta)
    interval = {
        'lower' : 0,
        'upper' : 2*pi,
        'increment' : 0.1
    }
    Region3 = PolarEqu_numGen(r_theta,interval)

    win.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)
    win.delay(20)


    G.plot(Region3)

    win.mainloop()
