from turtle import Turtle, Screen
import random


def random_color(user, other_color):
    if user in other_color:
        other_color.remove(user)
    random_clr = random.choice(other_color)
    other_color.remove(random_clr)
    return random_clr


race = False
screen = Screen()
screen.setup(width=720, height=540)
color = screen.textinput(title="Choose your turtle color", prompt="Which color gonna win?")
colors = ["red", "green", "black", "purple", "blue", "orange", "gray"]

all_turtle = []
pantek = Turtle(shape="turtle")
pantek.color(color)
pantek.penup()
pantek.goto(x=-340, y=0)
all_turtle.append(pantek)
y_list = [-125, -62, 62, 125]
for i in range(0, 4):
    yoga = Turtle(shape="turtle")
    yoga.color(random_color(color, colors))
    yoga.penup()
    yoga.goto(x=-340, y=y_list[i])
    all_turtle.append(yoga)


if color:
    race = True
while race:
    for x in all_turtle:
        step = random.randint(10, 16)
        x.forward(step)
        if x.xcor() > 360:
            race = False


if pantek.xcor() > 360:
    print("You Won")
else:
    print("You Lose")

screen.exitonclick()
