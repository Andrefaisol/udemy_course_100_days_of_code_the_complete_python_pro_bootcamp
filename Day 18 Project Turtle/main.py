import turtle
from turtle import Turtle
from turtle import Screen
from random import choice
import random

maryadi = Turtle()
maryadi.shape('arrow')
turtle.colormode(255)
maryadi.width(2)
# maryadi.up()
# maryadi.backward(200)
# maryadi.down()
maryadi.speed('fastest')


# for _ in range(2):
#     for steps in range(20):
#         maryadi.forward(10)
#         maryadi.up()
#         maryadi.forward(10)
#         maryadi.down()
#     maryadi.right(90)
#     for x in range(6):
#         maryadi.forward(10)
#         maryadi.up()
#         maryadi.forward(10)
#         maryadi.down()
#     maryadi.right(90)

degree = [3, 4, 5, 6, 7, 8, 9, 10]
listing = ['red', 'orange', 'magenta', 'green', 'blue', 'gray', 'purple', 'black']
n = 0


# def draw_shape(deg):
#     for x in range(deg):
#         maryadi.forward(100)
#         maryadi.right(360 / deg)
#
#
# for y in range(len(listing)):
#     maryadi.color(listing[y])
#     draw_shape(degree[y])
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup
#
#
# def random_walk(step):
#     decide = [1, -1]
#     for i in range(step):
#         w_decide = choice(decide)
#         maryadi.pencolor(random_color())
#         maryadi.forward(20)
#         if w_decide == 1:
#             maryadi.right(90)
#         else:
#             maryadi.left(90)
#
#
# random_walk(200)


def draw_circle(deg):
    for x in range(deg):
        maryadi.color(random_color())
        maryadi.circle(100)
        maryadi.right(360 / deg)


draw_circle(36)

screen = Screen()
screen.exitonclick()

