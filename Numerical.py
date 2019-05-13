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
