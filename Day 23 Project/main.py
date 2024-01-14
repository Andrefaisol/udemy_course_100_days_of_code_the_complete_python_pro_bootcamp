import time
from turtle import Screen
from player import Player


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
user = Player()

screen.listen()
screen.onkey(key="w", fun=user.move_up)
screen.onkey(key="s", fun=user.move_down)

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
