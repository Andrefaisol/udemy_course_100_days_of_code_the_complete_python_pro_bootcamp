from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.number = 0
        with open("legacy_score.txt", mode="r") as past_score:
            self.highscore = int(past_score.read())
        self.speed("fastest")
        self.color("yellow")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.number} | High Score: {self.highscore}", align="center",
                   move=False, font=("Arial", 12, "normal"))

    def adding(self):
        self.number += 1
        self.clear()
        self.write(arg=f"Score: {self.number} | High Score: {self.highscore}",
                   align="center", move=False, font=("Arial", 12, "normal"))

    def game_over(self):
        if self.number > int(self.highscore):
            self.highscore = self.number
            with open("legacy_score.txt", mode="w") as past_score:
                past_score.write(f"{self.highscore}")
        self.color("red")
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over", align="center", move=False, font=("Arial", 25, "normal"))
