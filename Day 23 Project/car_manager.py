from turtle import Turtle
import random

GENY = [240, 200, 160, 120, 80, 40, 0, -40, -80, -120, -160, -200, -240]
COLOR = ["green", "yellow", "blue", "red", "white", "black"]


class Car:
    def __init__(self):
        self.cars_list = []
        self.add_car()

    def car(self):
        bam = Turtle()
        bam.color(COLOR[random.randint(0, 4)])
        bam.penup()
        bam.shapesize(1, 2)
        bam.shape("square")
        bam.setheading(180)
        bam.setpos(x=random.randint(320, 400), y=GENY[random.randint(0, 11)])
        self.cars_list.append(bam)

    def add_car(self):
        for i in range(10):
            self.car()

    def move(self):
        for i in self.cars_list:
            newx = i.xcor() - 20
            i.goto(x=newx, y=i.ycor())

    def generate_cars(self):
        self.cars_list.pop(0)
        self.car()
