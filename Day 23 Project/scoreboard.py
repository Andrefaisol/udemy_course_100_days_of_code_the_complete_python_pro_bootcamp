from turtle import Turtle

UPLINE = [260, 220, 180, 160, 100, 60, 20, -20, -60, -100, -160, -180, -220, -260]
DOWNLINE = []


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.number = 0
        self.setup()

    def draw(self):
        self.color("white")
        self.penup()
        self.setpos(x=270, y=-260)
        self.setheading(180)
        for x in range(6):
            for i in range(5):
                self.pendown()
                self.forward(100)
                self.penup()
                self.forward(50)
            self.goto(x=270, y=self.ycor() + 100)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg="GAME OVER", move=False, align="center", font=("arial", 24, "normal"))

    def level(self):
        self.number += 1
        self.color("yellow")
        self.goto(x=-240, y=260)
        self.write(arg=f"Level: {self.number}", move=False, align="center", font=("arial", 18, "normal"))

    def setup(self):
        self.clear()
        self.draw()
        self.level()
