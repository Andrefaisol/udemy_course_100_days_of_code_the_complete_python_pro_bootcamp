from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1 = 0
        self.p2 = 0
        self.penup()
        self.speed("fastest")
        self.color("yellow")
        self.hideturtle()
        self.goto(x=0, y=280)
        self.write(arg=f"Score\nPlayer One: {self.p1} | Player Two: {self.p2}", align="center",
                   move=False, font=("Arial", 14, "normal"))

    def p1_goal(self):
        self.p1 += 1
        self.clear()
        self.write(arg=f"Score\nPlayer One: {self.p1} | Player Two: {self.p2}", align="center",
                   move=False, font=("Arial", 14, "normal"))

    def p2_goal(self):
        self.p2 += 1
        self.clear()
        self.write(arg=f"Score\nPlayer One: {self.p1} | Player Two: {self.p2}", align="center",
                   move=False, font=("Arial", 14, "normal"))
