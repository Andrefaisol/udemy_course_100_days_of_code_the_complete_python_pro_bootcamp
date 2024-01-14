from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.speed("fastest")
        self.color("green")
        self.setpos(x=0, y=-260)


    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(x=self.xcor(), y=new_y)

