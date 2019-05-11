from turtle import Turtle, Screen

class Grapher:


    def __init__(self,width,height):
        self._T = Turtle(visible = False)
        self._T.speed('fastest')
        self.axis(width,1)
        self._T.setheading(90)
        self.axis(height,1)

    def axis(self, distance, tick):
        position = self._T.position()
        self._T.pendown()

        for _ in range(0, distance // 2, tick):
            self._T.forward(tick)
            self._T.dot()

        self._T.setposition(position)

        for _ in range(0, distance // 2, tick):
            self._T.backward(tick)
            self._T.dot()
        self._T.penup()
        self._T.home()
    '''
    def generate(self,f,interval):
        num = []
        start,end,inc = interval
        while start < end:
            num.append((start,f(start)))
            start += inc
        return num
    '''
    def plot(self,region):
        self._T.speed('slowest')
        self._T.penup()
        self._T.pencolor('blue')

        #num = self.generate(f,interval)

        for p in region:
            self._T.goto(p)
            self._T.pendown()

        self._T.penup()
