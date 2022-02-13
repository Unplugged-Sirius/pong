from turtle import *
sc=Screen()
sc.bgcolor("black")
sc.setup(1500,600)

def up():
    ys=pad1.ycor()+20

    pad1.goto(pad1.xcor(),ys)


def down():
    ys = pad1.ycor() - 20

    pad1.goto(pad1.xcor(), ys)


pad1=Turtle()
pad1.shape("square")
pad1.shapesize(7,2,5)
pad1.color ("white")
pad1.penup()
pad1.goto(-750,0)
sc.listen()
sc.onkeypress(up,"Up")
sc.onkeypress(down, "Down")
ball=Turtle()
ball.shape("circle")
ball.penup()
ball.color("white")
x, y = 0, 0
xdir, ydir = 7, 7
xlimit, ylimit = sc.window_width() / 2.1, sc.window_height() / 2.1










def move():
    global x, y, xdir, ydir


    x = x + xdir
    y = y + ydir

    if not -xlimit < x < xlimit:
        xdir = -xdir
    if not -ylimit < y < ylimit:
        ydir = -ydir


    ball.goto(x, y)
    sc.ontimer(move, 5)





sc.ontimer(move, 1)






sc.exitonclick()