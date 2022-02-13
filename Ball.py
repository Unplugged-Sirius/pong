from turtle import Turtle,Screen
class ball():
 ball = Turtle()


 sc = Screen()
 ball.shape("circle")
 ball.penup()
 ball.color("white")
 x, y = 0, 0
 xdir, ydir = 7, 7
 xlimit, ylimit = sc.window_width() / 2.1, sc.window_height() / 2.1


 def __init__(self):
     self.x=0
     self.y=0
     self.xdir=7
     self.ydir =7
     self.x = self.x + self.xdir
     self.y = self.y + self.ydir

     self.xlimit=self.sc.window_width() / 2.1
     self.ylimit =  self.sc.window_height() / 2.1

     self. - xlimit =

     if not self.-xlimit < self.x < self.xlimit:
         xdir = -xdir

     if not -ylimit < y < ylimit:
         ydir = -ydir

     ball.goto(x, y)

     sc.ontimer(move, 5)


 sc.ontimer(move, 1)
 sc.exitonclick()