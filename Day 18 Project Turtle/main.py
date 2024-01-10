import turtle
from turtle import Turtle
from turtle import Screen
from hirst_painting_color import color_tup
import random

maryadi = Turtle()
Screen().setup(width=880, height=880, startx=None, starty=None)
Screen().bgcolor("antiquewhite")
maryadi.shape('arrow')
turtle.colormode(255)
maryadi.width(2)
maryadi.teleport(-483, 380)
maryadi.speed('fastest')


def fill_straight():
    for i in range(0, 11):
        random_color = random.randint(0, 24)
        decide = color_tup[random_color]
        maryadi.color(decide)
        maryadi.fillcolor(decide)
        maryadi.begin_fill()
        maryadi.circle(20)
        maryadi.end_fill()
        maryadi.penup()
        maryadi.forward(80)
        maryadi.pendown()


def turn_right():
    random_color = random.randint(0, 24)
    decide = color_tup[random_color]
    maryadi.color(decide)
    maryadi.fillcolor(decide)
    maryadi.begin_fill()
    maryadi.circle(20)
    maryadi.end_fill()
    maryadi.penup()
    maryadi.right(90)
    maryadi.forward(60)
    maryadi.right(90)
    maryadi.pendown()


def turn_left():
    random_color = random.randint(0, 24)
    decide = color_tup[random_color]
    maryadi.color(decide)
    maryadi.fillcolor(decide)
    maryadi.begin_fill()
    maryadi.circle(20)
    maryadi.end_fill()
    maryadi.penup()
    maryadi.left(90)
    maryadi.forward(140)
    maryadi.left(90)
    maryadi.pendown()


turn = 2
for x in range(0, 9):
    fill_straight()
    if turn % 2 == 0:
        turn_right()
        turn += 1
    elif turn % 2 == 1:
        turn_left()
        turn -= 1


screen = Screen()
screen.exitonclick()


