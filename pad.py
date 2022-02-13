from turtle import Turtle
class Pad(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(7, 1, 5)
        self.color("white")
        self.penup()
        self.goto(position)


    def up(self):
        ys=self.ycor()+20
        self.goto(self.xcor(),ys)


    def down(self):
        ys = self.ycor() - 20
        self.goto(self.xcor(), ys)




