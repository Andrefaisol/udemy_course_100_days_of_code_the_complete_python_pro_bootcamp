from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        self.xspeed = 20
        self.yspeed = 20

    def move(self):
        new_x = self.xcor() + self.xspeed
        new_y = self.ycor() + self.yspeed
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.yspeed *= -1

    def bounce_x(self):
        self.xspeed *= -1

    def reset_pos(self):
        self.bounce_y()
        self.bounce_x()
        self.setpos(x=0, y=0)
