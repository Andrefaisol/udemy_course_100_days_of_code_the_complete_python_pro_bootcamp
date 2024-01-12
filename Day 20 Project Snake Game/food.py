from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.4, stretch_len=0.4)
        self.color("red")
        self.speed("fastest")
        self.loc()

    def loc(self):
        random_x = random.randint(-280, 260)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)
