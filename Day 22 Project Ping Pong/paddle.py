from turtle import Turtle

LENGTH = (5, 1)
POSITION = [(-350, 0), (350, 0)]


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=LENGTH[0], stretch_len=LENGTH[1])
        self.speed("fastest")
        self.goto(pos)

    def moveup(self):
        new_cor = self.ycor() + 40
        self.goto(x=self.xcor(), y=new_cor)

    def movedown(self):
        new_cor = self.ycor() - 40
        self.goto(x=self.xcor(), y=new_cor)
