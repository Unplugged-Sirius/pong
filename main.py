from turtle import *
from pad import Pad

sc=Screen()
sc.bgcolor("black")
sc.setup(1500,600)
pad1=Pad((-750,0))
pad2=Pad((750,0))


sc.listen()
sc.onkeypress(pad2.up,"Up")
sc.onkeypress(pad2.down, "Down")
sc.onkeypress(pad1.up,"w")
sc.onkeypress(pad1.down, "s")

ball=Turtle()
ball.shape("circle")
ball.penup()
ball.color("white")
x, y = 0, 0
xdir, ydir = 12, 12
ylimit =  sc.window_height() / 2.1
print(ball.distance(pad2.pos()))










def move():
    global x, y, xdir, ydir


    x = x + xdir
    y = y + ydir
    xdir *= -1
    if ball.distance(pad2)<50 and ball.xcor()>340 or ball.distance(pad1)<20 and ball.xcor()>-340:
         xdir


    if not -ylimit < y < ylimit:
        ydir = -ydir




    print(ball.distance(pad2.pos()))
    ball.goto(x, y)
    sc.ontimer(move, 5)





sc.ontimer(move, 5)






sc.exitonclick()