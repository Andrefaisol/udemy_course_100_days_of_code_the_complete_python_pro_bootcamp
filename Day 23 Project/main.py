import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Maju Mundur Kena")
screen.tracer(0)

user = Player()
cars = Car()
score = ScoreBoard()

screen.listen()
screen.onkey(key="w", fun=user.move_up)
screen.onkey(key="s", fun=user.move_down)

speed_now = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(speed_now)
    cars.move()

    if cars.cars_list[0].xcor() < -360:
        cars.generate_cars()

    for i in range(0, len(cars.cars_list) - 1):
        if (user.distance(cars.cars_list[i]) < 40 and user.ycor() > cars.cars_list[i].ycor() or
                user.distance(cars.cars_list[i]) < 40 and user.ycor() < cars.cars_list[i].ycor() or
                user.distance(cars.cars_list[i]) < 40 and user.xcor() > cars.cars_list[i].xcor() or
                user.distance(cars.cars_list[i]) < 40 and user.xcor() < cars.cars_list[i].xcor()):
            score.game_over()
            game_on = False
    if user.ycor() > 280:
        user.goto(x=0, y=-260)
        score.setup()
        speed_now *= 0.9

screen.exitonclick()
