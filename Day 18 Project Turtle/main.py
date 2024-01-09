from turtle import Turtle
from turtle import Screen

maryadi = Turtle()
maryadi.shape('arrow')
maryadi.up()
maryadi.backward(200)
maryadi.down()
for _ in range(2):
    for steps in range(20):
        maryadi.forward(10)
        maryadi.up()
        maryadi.forward(10)
        maryadi.down()
    maryadi.right(90)
    for x in range(6):
        maryadi.forward(10)
        maryadi.up()
        maryadi.forward(10)
        maryadi.down()
    maryadi.right(90)






screen = Screen()
screen.exitonclick()
