from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.number = 0
        self.speed("fastest")
        self.color("yellow")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.number}", align="center", move=False, font=("Arial", 12, "normal"))

    def adding(self):
        self.number += 1
        self.clear()
        self.write(arg=f"Score: {self.number}", align="center", move=False, font=("Arial", 12, "normal"))

    def game_over(self):
        self.color("red")
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over", align="center", move=False, font=("Arial", 25, "normal"))
