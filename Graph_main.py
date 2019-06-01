from Grapher import *
from turtle import Turtle, Screen
from math import *
from Numerical import *




if __name__ == '__main__':
    #WIDTH, HEIGHT = 10,10
    win = Screen()

    #win.setworldcoordinates(-WIDTH/2 , -HEIGHT/2 , WIDTH//2 , HEIGHT//2)
    Dim = {'X' : {'lower' : -10 , 'upper' : 10} , 'Y' : {'lower' : -10, 'upper':10}}
    D = [Dim['X']['lower'],Dim['Y']['lower'] , Dim['X']['upper'],Dim['Y']['upper']]
   
    win.setworldcoordinates(D[0],D[1],D[2],D[3])

    
    
    G = Grapher(Dim)
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
    r_theta = lambda theta : 3*cos(2*theta)
    interval = {
        'lower' : 0,
        'upper' : 2*pi,
        'increment' : 0.01
    }
    Region3 = PolarEqu_numGen(r_theta,interval)

    win.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)
    win.delay(5)


    G.plot(Region3)

    win.mainloop()
