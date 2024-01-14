from turtle import Turtle
import random
gen_y = [260, 220, 180, 140, 100, 60, 20, -20, -60, -100, -140, -180, -220, -260]

class Car(Turtle):
    def __init__(self, color):
        super().__init__()
        self.random_y = gen_y[random.randint(0, 23)]
        self.color(color)
        self.penup()
        self.shapesize(1, 3)
        self.shape("square")
        self.setheading(180)
        self.setpos(x=320, y=self.random_y)
