from turtle import Turtle, Screen

class Grapher:

   def __init__(self,Dim):
      self.T = Turtle(visible = False)
      self.T.speed('fastest')

      self.draw_axis(Dim)

   def axis(self,distance,tick):
      pos = self.T.position()
      self.T.pendown()

      for _ in range(0,abs(distance['upper']),tick):
         self.T.forward(tick)
         self.T.dot()

      self.T.setposition(pos)

      for _ in range(0,abs(distance['lower']),tick):
         self.T.backward(tick)
         self.T.dot()

      self.T.penup()
      

   def draw_axis(self,Dim):
      self.T.penup()
      self.T.home()

      self.axis(Dim['X'],1)
      self.T.penup()
      self.T.home()

      self.T.setheading(90)
      self.axis(Dim['Y'],1)

   def plot(self,region):
        self.T.speed('slowest')
        self.T.penup()
        self.T.pencolor('blue')


        for p in region:
            self.T.goto(p)
            self.T.pendown()

        self.T.penup()
